# Engineering notes

[← Profile](../README.md) · [简体中文](engineering-notes.zh-CN.md)

Three decisions from my public work. The linked repositories and PRs contain the implementation, tests and discussion.

## Knowledge that can be maintained

**The problem.** Skill documents change. Extracting a graph once does not solve how to preserve a person's corrections or safely deliver updates to agents.

**The design in [Cairn](https://github.com/xcosmosbox/Cairn).** Separate the LLM-assisted build side from a read-only query service. Keep editable knowledge in structured Markdown blocks and sidecars. Human-curated edits retain their provenance and are protected from later LLM overwrites. Package the graph into immutable, digest-verified bundles, then atomically switch the consuming service to a new version.

**The boundary.** A graph structure is not proof of better answers. Query behavior and extraction quality still need evaluation. Cairn's retrieval experiments distinguish recall changes from answer correctness, including the limitations of SQLite FTS5's default Chinese tokenization.

[Architecture and design](https://github.com/xcosmosbox/Cairn) · [Retrieval evaluation](https://github.com/xcosmosbox/Cairn/tree/main/e2e/quality)

## Keeping request logging off the forwarding path

**The problem.** Capturing request payloads can compete with request forwarding for database connections and I/O. Cleanup introduces another challenge: an old queued item must not reappear after a clear, and a newly written item must survive it.

**My changes to Codex-Manager.** In [#496](https://github.com/qxcnm/Codex-Manager/pull/496), capture enqueues shared bytes into a bounded in-memory pipeline. Background workers handle preprocessing, grouped writes and disk spill. The implementation makes retry, restart and drop reasons observable, and redacts data before spill when redaction is enabled.

In [#498](https://github.com/qxcnm/Codex-Manager/pull/498), I replaced time-based cleanup boundaries with generations. SQLite can reuse row IDs within the same second; a generation identifies which side of the clear a row belongs to without depending on timestamp resolution. A regression test reproduces that same-second reuse.

**The boundary.** A bounded pipeline cannot promise unlimited retention. Disk pressure and worker failures need explicit behavior and visible counters. The PR records those limits and the tests that were actually run.

## Making an RL algorithm explicit

**The problem.** Adding an algorithm name is only one part of supporting a training method. Baseline computation, loss dispatch, reduction, configuration validation and diagnostics have to agree.

**My contribution to [Relax #205](https://github.com/redai-studio/Relax/pull/205).** I implemented synchronous RLOO support, including the leave-one-out baseline, unclipped policy loss, Megatron integration, distributed tests and recipes. Configuration guards constrain it to the supported synchronous topology. Tests exercise production reducers and loss dispatch.

**The boundary.** The implementation uses global valid-token normalization. The element-wise REINFORCE terms match the stated formulation; the final scalar reduction is not claimed to be numerically identical to the paper's sequence-level estimator. The PR explains the scale difference and the supported settings.

---

[Back to the profile →](../README.md)
