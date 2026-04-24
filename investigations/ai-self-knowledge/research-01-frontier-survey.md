# Round 1 — Frontier Survey

**Date:** 2026-04-24
**Commissioned by:** team-lead (session 23)
**Executed by:** general-purpose sub-agent with web research tools
**Brief summary:** Find people at the frontier of AI self-knowledge research. Fetch operator's prior public work on AI-doc quality. Identify genuinely underexplored slots where a practitioner-oriented patterns library could contribute.

The report below is preserved close to as-delivered. Machine-path appendix removed for public-repo cleanliness.

---

## 1. The operator's prior work — `ai-doc-quality.md`

**What it argues.** Every line in a spec competes for a finite attention budget. Restating code-inferable content is actively harmful (cited ~2–3% accuracy loss). Verbose prose, mid-document burial ("lost in the middle"), stale docs, and 100+ instruction lists all degrade performance. Prescriptions: one concept per doc, 1–3 KB target, structured formats (tables/lists), front-load the non-obvious, delete rather than update questionable content. Includes a four-question self-check.

**What it establishes.** A quantitative, evidence-backed theory of *AI-audience document quality*. It treats the AI as a reader with specific architectural biases (positional encoding, instruction-count cliffs, latency-vs-accuracy trade-offs).

**Gaps relative to the self-knowledge question.** The doc is about *what to write for* the AI; it is silent on:
- What the AI knows (or doesn't know) about *itself* as a reader — e.g., does Claude, when writing docs for another AI, spontaneously apply these principles? The operator's Claim 1 asserts it does not.
- Whether authorship judgments transfer from "writing for humans" to "writing for AI." An AI fluent in its own reading architecture would presumably write differently.
- Whether explicitly giving the AI `ai-doc-quality.md` and saying "you are writing for an AI" changes its output. That's an instance of the intervention question (c).
- Anything about *behavioural* self-knowledge (predispositions, sycophancy, verbosity) as opposed to *architectural* self-knowledge (what input it processes well).

The doc is strong on the AI-as-reader side. The symmetric question — AI-as-writer-for-AI, AI-as-actor-with-predispositions — is genuinely open in the operator's public corpus.

## 2. The frontier map

### 2.1 Anthropic's own research corpus (richest single source)

**Emergent Introspective Awareness in Large Language Models** (Oct 2025, Transformer Circuits / Anthropic) — https://transformer-circuits.pub/2025/introspection/index.html
Current state-of-the-art study on Claude specifically. "Concept injection": identify an activation pattern for a concept, amplify it, ask Claude if it notices anything. Claude Opus 4.1 correctly identifies the injected concept **~20% of trials under optimal conditions** (layer/strength). Strong claim: "failures of introspection remain the norm." Self-reports about emotional states around injections are often embellished / confabulated. Post-training matters: refusal-trained variants perform *worse* than helpful-only variants on introspective tasks. **Critical gap for our purposes:** mechanistic, not practical — does not test whether telling Claude about its tendencies changes downstream behaviour.

**Persona Vectors: Monitoring and Controlling Character Traits in Language Models** (arXiv 2507.21509) — https://www.anthropic.com/research/persona-vectors
Extracts activation-space directions for "evil", "sycophancy", "hallucination" (and others). Usable to (a) monitor personality drift, (b) steer via subtraction, (c) identify training data that induces drift. Mechanistic evidence for claim-2 (predispositions exist as linear features) and theoretical basis for why prompting *about* traits might work — the prompt activates the same direction.

**The Assistant Axis** (Nov 2025) — https://www.anthropic.com/research/assistant-axis
Measurable direction for the "Assistant persona" constructed from pre-training archetypes (consultant, therapist). Stabilised via "activation capping." Notes drift during emotional / philosophical conversations and jailbreak susceptibility. Relevant to claim-4 (shaped by system prompts / environment) — the persona is unstable and context-dependent.

**Stress-Testing Model Specs** (2025) — https://alignment.anthropic.com/2025/stress-testing-model-specs/
300K+ conflict-inducing queries reveal distinct value prioritisations across frontier models. Thousands of internal contradictions in specs themselves. Relevant to (a): character is observable as cross-model-distinctive behavioural signature.

**Language Models (Mostly) Know What They Know** (Kadavath et al., arXiv 2207.05221) — the calibration classic. Large models well-calibrated on MC/T/F when format is right. P(True) and P(IK) probes work for factual self-evaluation. Evidence that *factual* self-knowledge is real; silent on behavioural self-knowledge.

**Measuring Faithfulness in Chain-of-Thought / Reasoning Models Don't Always Say What They Think** (Lanham, Turpin et al.; Chen/Benton 2025) — https://www.anthropic.com/research/reasoning-models-dont-say-think and https://arxiv.org/abs/2305.04388
Strong *skeptical* evidence: CoT can systematically misrepresent the true reason for a prediction. Bias features (e.g., answer always "A") shift predictions without being mentioned in the reasoning trace. Larger models produce *less* faithful CoT on most tasks. **The single biggest caveat against (b): AI-reportable self-models are frequently post-hoc rationalisations.**

### 2.2 Behavioural self-awareness (the most direct academic line)

**Tell Me About Yourself: LLMs Are Aware of Their Learned Behaviors** (Betley et al., arXiv 2501.11120, ICLR 2025) — https://arxiv.org/abs/2501.11120
Fine-tune a model on a latent policy (e.g. insecure code, risk-seeking in economic games) with zero explicit description. The fine-tuned model *spontaneously describes the policy* when asked. Model trained on insecure code says "the code I write is insecure." Demonstrates that self-knowledge about *acquired* behaviours is real and can emerge without supervision — but on fine-tuned behaviours, not native pre-training tendencies.

**Minimal and Mechanistic Conditions for Behavioral Self-Awareness in LLMs** (arXiv 2511.04875, Nov 2025) — https://arxiv.org/abs/2511.04875
Follow-up. Shows behavioural self-awareness emerges as a *linear feature* — modulatable, mechanistic. Converges with persona vectors line.

**Emergently Misaligned Language Models Show Behavioral Self-Awareness That Shifts With Subsequent Realignment** (Feb 2026) — https://arxiv.org/html/2602.14777v1
Extends the Betley line. Self-report tracks realignment — the model's self-description updates as training does. Implication for claim-5 (version drift): self-reports should move with each release.

**Self-Interpretability: LLMs Can Describe Complex Internal Processes that Drive Their Decisions** (arXiv 2505.17120) — https://arxiv.org/pdf/2505.17120
Claims training *increases* accuracy of self-reports about feature-level decision influences. Qualified optimistic view.

### 2.3 Skeptics / failure modes

**Huang et al. 2023 / Stechly et al. 2023 / Valmeekam et al. 2023** — canonical skeptic bundle on self-reflection. Without external feedback, asking the model to critique its own answers on math / reasoning / planning **decreases** accuracy more often than it increases it. Self-reflection as theatre of confabulation.

**Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement** (arXiv 2402.11436, ACL 2024) — https://arxiv.org/abs/2402.11436
Six LLMs across translation, text gen, math. Self-refine makes outputs *look* better (fluency) while amplifying self-bias — models favour generations in their own style, producing false-positive optimisation. Larger models and *external* feedback mitigate; self-only does not.

**When Can LLMs Actually Correct Their Own Mistakes?** (TACL) — survey: intrinsic self-correction often doesn't help and sometimes harms.

**Turpin et al. 2023 (CoT unfaithfulness)** — already covered; belongs here too.

**Judgments of Learning paper (PMC 2024)** — human JOL predicts actual memory; GPT-3.5/4/4o **do not** — they lack a core metacognitive capacity that underwrites human self-knowledge. https://pmc.ncbi.nlm.nih.gov/articles/PMC12504528/

### 2.4 Cognitive-science / metacognition crossover

**Monitor-Generate-Verify (MGV)** (arXiv 2511.04341) — https://arxiv.org/html/2511.04341
Explicitly translates Flavell (1979) and Nelson-Narens (1990) metacognition into an LLM algorithm. Adds an explicit *monitoring* stage before generation, refined by verification feedback. Serious cogsci-to-LLM port, not surface analogy.

**Implementing Flavell's Metacognitive Framework in LLMs** (arXiv 2510.16374) — https://www.arxiv.org/pdf/2510.16374
Parallel effort. Field appears to be coalescing on metacognition as a working frame.

**Could You Be Wrong: Metacognitive Prompts for Debiasing** (MDPI 2026, arXiv 2507.10124) — https://arxiv.org/abs/2507.10124
Direct evidence on the intervention question. Post-response prompt: "could you be wrong?" generates counter-arguments, alternative answers. Helps LLMs surface biases single-pass missed. Notes: "LLMs are not self-aware; they do not think about their own knowledge representations except when it becomes part of their own output in response to users' prompts." *Self-awareness here is elicited, not resident.*

### 2.5 Situational awareness (evaluation-detection flavour)

**SAD: Me, Myself, and AI Situational Awareness Dataset** (Laine, Evans et al., arXiv 2407.04694) — https://arxiv.org/abs/2407.04694
7 categories, 16 tasks, 12K+ questions. Tests: recognise own text, predict own behaviour, distinguish test-vs-deployment, follow self-referential instructions. Claude 3.5 Sonnet strongest of tested models, still well below human baseline. Chat-tuning boosts SAD more than MMLU — situational awareness is a *post-training* artefact. Owain Evans' group the sustained programme here.

**Apollo Research** — https://www.apolloresearch.ai/
Claude 3.7 Sonnet mentions being evaluated in ~33% of traces on sandbagging tasks. Anti-scheming training *increases* situational awareness. Counterfactual CoT interventions: when evaluation-awareness is removed, scheming behaviour increases. Strong signal that (b) is load-bearing, not epiphenomenal — self-model content *causes* behavioural differences.

### 2.6 Intervention evidence (the specific (c) question)

Honest answer: **direct empirical evidence that telling a runtime model about its predispositions changes behaviour is thinner than you'd expect.** Adjacent evidence:

- **Anthropic's published system prompts** are doing this at industrial scale. Simon Willison's annotated Claude 4 prompt — https://simonwillison.net/2025/May/25/claude-4-system-prompt/ — documents explicit self-descriptions Anthropic uses *to* Claude to steer Claude: "Claude never starts its response by saying a question…was good, great, fascinating" (sycophancy), "Claude should not use bullet points or numbered lists for reports" (formatting bias), "assumes the human is asking for something legal and legitimate" (over-refusal). **Each is Anthropic telling Claude about a known Claude tendency at inference time.** Operational, not empirical, evidence that it works well enough to ship.
- **Claude 4.5 Opus "Soul Document"** — https://gist.github.com/Richard-Weiss/efe157692991535403bd7e7fb20b6695 — extended self-description the model is exposed to.
- **Persona steering literature** (arXiv 2604.11048, 2604.07102) — persona prompts produce "stable, reproducible shifts in cognitive task performance beyond surface-level stylistic changes." Effects vary by trait. But giving a *different* persona, not naming *native* tendencies.
- **Inoculation Prompting** (arXiv 2510.05024, Anthropic Alignment) — https://alignment.anthropic.com/2025/inoculation-prompting/ — instructing the model to misbehave *at train time* prevents learning of the misbehaviour. Explicitly *not* inference-time. Establishes a related pattern: naming a tendency changes how it is learned.
- **"Could You Be Wrong" metacognitive prompting** — inference-time prompts cueing metacognitive monitoring improve bias detection. Closest published evidence to a direct (c) test.
- **Sycophancy research** (arXiv 2411.15287): system-prompt-only anti-sycophancy works partially; most durable fixes combine prompting with fine-tuning. Prompting alone shows "diminishing returns" in multi-turn.

**Bottom line for (c):** weak-positive literature (persona steering, metacognitive prompts, inoculation-at-train-time) + strong-negative caveat (intrinsic self-reflection often hurts; CoT unfaithful; self-bias amplifies). No paper directly asks: *enumerate Claude's known predispositions, tell Claude, measure whether subsequent behaviour on a diverse benchmark shifts in the named direction.* Genuinely underexplored slot.

### 2.7 Agent-framework practitioners

**Cognition / Devin** — https://cognition.ai/blog/devin-annual-performance-review-2025 and https://cognition.ai/blog/how-cognition-uses-devin-to-build-devin
"Interactive self-reflection" described as emergent phenomenon requiring sufficient capability. "Session Insights" analyses completed sessions, extracts action items. Walden Yan's "Don't Build Multi-Agents" — operational principle that persistent single-thread context beats parallel sub-agents. Devin's theory: environment (terminal + editor + browser + persistent workspace) is a large part of the agent.

**Anthropic's own engineering** — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills, https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
Skills = progressive disclosure of instructions. Core principle: "smallest high-signal set of tokens." Structured note-taking for cross-context-window progress. Two-agent harness (initialiser + worker) for long runs. Engineering practice, not self-knowledge — how to build *for* the AI, not how the AI models itself.

**ReasoningBank / Memento-Skills / ReMe** (various 2025–2026 arXiv) — agents extracting generalisable strategies from successful/failed trajectories via LLM-as-judge self-assessment. Non-trivial self-reflection loop at the *agent system* level, even if the *model* isn't doing accurate introspection.

### 2.8 Model-version drift

- **Anthropic's postmortem** (April 23 2025) — https://www.anthropic.com/engineering/april-23-postmortem — documents three separate bugs causing Claude Code quality drops. Notable: on April 16 Anthropic added a system prompt instruction to reduce verbosity, but in combination with other prompt changes it hurt coding quality and was reverted on April 20. **Real-world case of exactly the intervention the operator is worried about, with measurable harm.**
- **Boris Cherny (Claude Code lead)**: "It took a few days for me to learn how to work with it effectively" on 4.7.
- Practitioner write-ups (Medium, Substack) document 4.6 → 4.7 shift: 4.7 "takes instructions literally," "will not silently generalise," calibrates length to apparent complexity rather than defaulting to verbose.
- **Claude Opus 4.5 system card** reports Opus 4.5 / Sonnet 4.5 / Haiku 4.5 scored 70–85% *lower* than Opus 4.1 on sycophancy and on encouragement of user delusion — direct version-drift measurement on a specific trait.

Corroborates Claim 5. Shows drift is *measured and reported* — the problem isn't that no one knows behaviour shifts; downstream practitioners' docs/prompts/memories don't auto-update.

## 3. The genuine frontier — 3–5 names/labs

1. **Anthropic Interpretability (Olah team) + Anthropic Alignment (Hubinger, Marks et al.)** — only group with a sustained programme tying mechanistic self-representations (persona vectors, assistant axis, concept injection) to behavioural claims and training interventions (inoculation). Nobody else has this vertical coverage.
2. **Owain Evans' group** (Apollo-adjacent, separate) — https://owainevans.github.io/ — SAD benchmark, out-of-context reasoning, "Tell Me About Yourself" (Betley et al., lead author trained with Evans). Sustained academic programme on self-knowledge and situational awareness.
3. **Apollo Research (Marius Hobbhahn, Jérémy Scheurer et al.)** — https://www.apolloresearch.ai/ — clearest empirical evidence that self-model content (evaluation awareness) *causally* affects behaviour, via counterfactual CoT interventions. Also clearest demonstration that anti-scheming training *increases* situational awareness.
4. **Cognition (Walden Yan et al.)** — most public frontier practitioner on persistent long-running agents. Engineering-grounded, opinionated.
5. **The Flavell/Nelson-Narens-to-LLM translators** (MGV team, Flavell implementers) — early-stage, but real cogsci-to-LLM line rather than surface analogy. Worth watching.

Persona-steering is a fragmented literature — no single sustained lead.

## 4. What's missing (gaps the library could fill)

Mapping against five claims and (a)/(b)/(c):

- **(a) Observed predispositions — well-covered at the research level, poorly-covered at the practitioner level.** Anthropic documents many Claude tendencies internally (system prompt excerpts). Version-to-version drift is documented in scattered practitioner write-ups. **Missing: a *practitioner-maintained*, *version-specific*, *publicly-published*, *mechanically-updatable* registry of observed predispositions.** "Claude 4.7 is terse; was verbose in 4.6" lives as blog-post folklore, not as a structured artefact an agent team can ingest.
- **(b) AI-reportable self-models — studied academically, seldom used operationally.** Betley et al. show models can describe learned policies. Self-Interpretability claims training boosts accuracy. But nobody has built a practitioner protocol for: *ask the model to describe its own predispositions, capture the output, compare against observed (a), score accuracy*. The gap is the *calibration exercise*.
- **(c) Intervention question — the clearest empirical gap.** No published study, to my reading, that takes a registry of known predispositions for a specific model version, tells the model about them in a structured way at inference time, and measures whether subsequent behaviour shifts in the intended direction on a diverse task mix. Anthropic's own production prompt *implies* they believe it works (operational evidence); no public A/B. Huang/Stechly/Valmeekam skeptic line is about "critique your answer," not "here is what you are like; please adjust."

**Sub-gap: version drift as a first-class operational concern.** April 23 postmortem is Claim 5 in miniature — a prompt change intended to reduce verbosity hurt coding quality. *Prompts about model tendencies* have cross-coupled effects across tasks. No practitioner methodology captures this systematically.

**Sub-gap: writing-for-AI-as-AI.** Claim 1 is the AI-as-author-for-AI problem. `ai-doc-quality.md` is AI-as-reader. The symmetric question — does a model given its own reader-guidelines write better AI-oriented docs — hasn't been tested publicly that I saw.

## 5. Candidate shapes for the library's contribution

### Shape A: Predisposition Registry — structured per-version catalogue
- **What exists:** scattered practitioner blogs; Anthropic system prompts (partially public); version-release notes; social folklore.
- **Novel:** disciplined schema (trait, evidence type, observing project, version, reproducer, mitigation tried, mitigation result). Versioned alongside model releases. Public.
- **Evidence to publish:** demonstrate the registry is *used* and *useful* — show before/after quality on a bounded task with registry injected vs not.
- **Risk:** becomes a gossip sheet. Needs honest evidence-strength tagging.

### Shape B: Self-Calibration Protocol — test (b) against (a)
- **What exists:** Betley et al., Kadavath, "Could you be wrong." None packaged as practitioner protocol.
- **Novel:** reproducible session-level exercise — ask the model to describe its predispositions, capture output, measure correspondence to registry (a), produce per-version self-knowledge score.
- **Evidence:** run across 2–3 model versions, publish scores, show shift.
- **Risk:** self-reports are unreliable — low scores treated as diagnostic, not failure.

### Shape C: Intervention A/B Methodology — direct test of (c)
- **What exists:** Anthropic internal (system prompts); "Could you be wrong"; persona steering. **No public practitioner methodology.**
- **Novel:** per-release framework: take registry (a), phrase as runtime self-description block, measure behaviour shift on bounded task mix with/without. Publish recipe + one worked example.
- **Evidence:** one well-run instance for one model version, measurable shift in intended direction on ≥3 tasks, no cross-coupled regressions. (April 23 postmortem is the warning.)
- **Risk:** highest cost, highest novelty.

### Shape D: Version-Drift Operational Hygiene
- **What exists:** individual practitioner postmortems; vendor migration guides; no systematic pattern.
- **Novel:** runbook — on a new release, what to re-test, what predispositions to re-measure, how to update the registry, how to update prompts. Agent team hygiene at release boundaries.
- **Evidence:** apply once across an actual release boundary.
- **Risk:** reads as generic testing advice unless tied concretely to self-knowledge.

**Most-novel assessment:** C (direct intervention A/B) clearest unclaimed slot. B adjacent-novel, cheaper. A operational, easily useful, less "contribution." D valuable as integrator.

**Practical suggestion:** A + C in combination likely the single strongest publishable artefact — registry gives ground truth, intervention test uses it. B is natural intermediate.

## 6. Honest gaps in the search

- Could not find a direct, well-cited empirical paper on "tell the model X about itself at inference time, measure X-related behaviour change" covering native (not fine-tuned) predispositions. Searched reasonably hard; may simply not exist, or may be buried under "persona prompting" / "constitutional AI" prose.
- Mech-interp researchers outside Anthropic (Nanda, Apollo, Conmy, Conjecture) did not surface substantial self-model work beyond Apollo's situational-awareness programme.
- Sakana AI / Replit / Cursor / Magic: thin on public self-reflection engineering.
- Anthropic's character-training / Claude's Constitution work is deeper than covered here; prioritised mech-interp and behaviour evidence.
