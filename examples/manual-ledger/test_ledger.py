import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('ledger', HERE / 'ledger.py')
ledger = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ledger)


class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.data = json.loads((HERE / 'plan.json').read_text())
        (self.root / 'contract.md').write_text('Original acceptance contract')
        (self.root / 'evidence.md').write_text('Evidence for this attempt')

    def result(self, task, state='submitted'):
        task['state'] = state
        task['result'] = dict(attempt='attempt-1', artifact_version='fixture-v1',
                              contract='contract.md', evidence='evidence.md',
                              finding='No direction change', residual='Only fixture checked')
        if state == 'accepted':
            task['decision'] = dict(by='test-reviewer', authority='fixture policy',
                                    reason='Fixture accepted', artifact_version='fixture-v1')

    def check(self):
        return ledger.validate(self.data, self.root)

    def test_dependency_waits_for_acceptance_not_submission(self):
        first, second = self.data['tasks']
        self.assertEqual(ledger.select(self.check())['id'], first['id'])
        self.result(first)
        self.assertIsNone(ledger.select(self.check()))
        self.result(first, 'accepted')
        self.assertEqual(ledger.select(self.check())['id'], second['id'])

    def test_invalid_top_level_shapes_fail_closed(self):
        for data in ([], None, {}, {'version': True},
                     {'version': 1, 'workstreams': [], 'tasks': []},
                     {'version': 1, 'workstreams': {'W': {'outcome': 'x'}}, 'tasks': {}}):
            with self.subTest(data=data), self.assertRaises(ValueError):
                ledger.validate(data, self.root)

    def test_missing_dependency_duplicate_id_and_cycle_fail(self):
        original = copy.deepcopy(self.data)
        for mutation in ('missing', 'duplicate', 'cycle'):
            with self.subTest(mutation=mutation):
                self.data = copy.deepcopy(original)
                first, second = self.data['tasks']
                if mutation == 'missing':
                    first['depends_on'] = ['absent']
                elif mutation == 'duplicate':
                    second['id'] = first['id']
                else:
                    first['depends_on'] = [second['id']]
                with self.assertRaises(ValueError):
                    self.check()

    def test_missing_evidence_and_version_mismatch_fail(self):
        task = self.data['tasks'][0]
        self.result(task, 'accepted')
        task['decision']['artifact_version'] = 'other-version'
        with self.assertRaises(ValueError):
            self.check()
        task['decision']['artifact_version'] = 'fixture-v1'
        (self.root / 'evidence.md').unlink()
        with self.assertRaises(ValueError):
            self.check()

    def test_evidence_cannot_escape_by_parent_absolute_or_symlink(self):
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside) / 'secret.md'
            target.write_text('not a public fixture')
            (self.root / 'link.md').symlink_to(target)
            for name in ('../secret.md', str(target), 'link.md'):
                with self.subTest(name=name), self.assertRaises(ValueError):
                    ledger.local_file(self.root, name)

    def test_interruption_requires_reconciliation(self):
        self.data['tasks'][0]['state'] = 'active'
        with self.assertRaisesRegex(ValueError, 'reconcile'):
            ledger.select(self.check())

    def test_deferred_and_blocked_need_wake_and_are_not_selected(self):
        for state in ('blocked', 'deferred'):
            with self.subTest(state=state):
                first = self.data['tasks'][0]
                first['state'] = state
                with self.assertRaises(ValueError):
                    self.check()
                first['wake'] = 'Consumer specification becomes available'
                self.assertIsNone(ledger.select(self.check()))
                del first['wake']

    def test_unknown_state_and_boolean_priority_fail(self):
        first = self.data['tasks'][0]
        first['state'] = 'finished-ish'
        with self.assertRaises(ValueError):
            self.check()
        first['state'], first['priority'] = 'ready', True
        with self.assertRaises(ValueError):
            self.check()

    def test_packet_reports_findings_and_residual_without_accepting(self):
        first = self.data['tasks'][0]
        self.result(first)
        before = copy.deepcopy(self.data)
        output = ledger.packet(self.check())
        self.assertIn('Only fixture checked', output)
        self.assertIn('No direction change', output)
        self.assertIn('fixture-v1', output)
        self.assertEqual(before, self.data)

    def test_acceptance_does_not_remove_findings_from_packet(self):
        first = self.data['tasks'][0]
        self.result(first, 'accepted')
        output = ledger.packet(self.check())
        self.assertIn('Only fixture checked', output)
        self.assertIn('No direction change', output)
        self.assertIn('Accepted by: test-reviewer', output)
        self.assertIn('Finding delivery/acknowledgment: not tracked', output)
        self.assertEqual(first['state'], 'accepted')

    def test_cli_is_read_only_and_fails_on_invalid_json(self):
        path = self.root / 'plan.json'
        path.write_text(json.dumps(self.data))
        before = path.read_bytes()
        for command in ('check', 'next', 'packet'):
            run = subprocess.run([sys.executable, str(HERE / 'ledger.py'), command, str(path)],
                                 capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual(path.read_bytes(), before)
        path.write_text('{broken')
        run = subprocess.run([sys.executable, str(HERE / 'ledger.py'), 'next', str(path)],
                             capture_output=True, text=True)
        self.assertEqual(run.returncode, 2)
        self.assertFalse(json.loads(run.stderr)['ok'])


if __name__ == '__main__':
    unittest.main()
