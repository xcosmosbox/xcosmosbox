<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg">
  <img alt="San_Check — Knowledge into action. Agent systems, GraphRAG and infrastructure." src="assets/hero-light.svg" width="100%">
</picture>

<p align="center">
  <b>English</b> · <a href="README.zh-CN.md">简体中文</a>
  <br>
  <a href="#selected-work">Selected work</a> · <a href="#upstream-contributions">Contributions</a> · <a href="docs/engineering-notes.md">Engineering notes</a> · <a href="#lets-build">Let's build</a>
</p>

Hi, I'm **San_Check** (`xcosmosbox`). I build knowledge systems for AI agents, work on the infrastructure around them, and turn everyday problems into usable software.

My work spans **GraphRAG & MCP**, **agent infrastructure**, and **reinforcement-learning engineering**. I'm currently exploring how to evaluate and improve reusable agent skills.

## Selected work

<a href="https://github.com/xcosmosbox/Cairn">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/cairn-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/cairn-light.svg">
    <img alt="Cairn — Versioned knowledge for agents. Skill documents → knowledge graph → MCP." src="assets/cairn-light.svg" width="100%">
  </picture>
</a>

**[Cairn](https://github.com/xcosmosbox/Cairn)** turns scattered skill documents into an editable knowledge graph and serves it to agents over MCP. I built a system for incrementally updating the graph, preserving human edits, and distributing versioned bundles with hot swaps and rollback.

`Go` `SQLite / FTS5` `MCP` `React / TypeScript`

[Explore the architecture →](https://github.com/xcosmosbox/Cairn#架构) · [See the correctness work →](https://github.com/xcosmosbox/Cairn/blob/main/CORRECTNESS.md)

<a href="https://github.com/xcosmosbox/campus-jobs-2027">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/campus-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/campus-light.svg">
    <img alt="Campus Jobs 2027 — From finding an opportunity to tracking an application. Filter, verify and keep your progress." src="assets/campus-light.svg" width="100%">
  </picture>
</a>

**[Campus Jobs 2027 · 27届秋招筛选站](https://github.com/xcosmosbox/campus-jobs-2027)** brings job discovery, source verification, application tracking and deadlines into one workspace. It supports guest access, recovery codes, data export and Docker self-hosting—a full product built around a real job-search workflow.

`TypeScript` `SQLite / D1` `Docker`

[Try the public app →](https://autumn27-screening.ottofeng00.chatgpt.site) · [Self-host it →](https://github.com/xcosmosbox/campus-jobs-2027/blob/main/docs/self-hosting.md)

## Upstream contributions

I also contribute to tools I use. These are **my merged changes in upstream projects**; the projects belong to their respective maintainers.

| Project | What I contributed | Read the code & discussion |
| :-- | :-- | :-- |
| **[nanobot](https://github.com/HKUDS/nanobot)** | Background gateway controls and systemd / launchd service integration. | [#1854](https://github.com/HKUDS/nanobot/pull/1854) |
| **[Relax](https://github.com/redai-studio/Relax)** | Synchronous RLOO training support: advantage estimation, policy loss, validation and distributed tests. | [#205](https://github.com/redai-studio/Relax/pull/205) |
| **[Codex-Manager](https://github.com/qxcnm/Codex-Manager)** | Bounded background payload writes and generation-based cleanup to protect newly written data. | [#496](https://github.com/qxcnm/Codex-Manager/pull/496) · [#498](https://github.com/qxcnm/Codex-Manager/pull/498) |
| **[Knowhere](https://github.com/Ontos-AI/knowhere)** | An HTML document adapter that reuses the existing structured parsing pipeline. | [#181](https://github.com/Ontos-AI/knowhere/pull/181) |

[Browse my merged public PRs →](https://github.com/pulls?q=is%3Apr+author%3Axcosmosbox+is%3Amerged+is%3Apublic+-user%3Axcosmosbox)

## How I approach engineering

- **Make knowledge maintainable.** Preserve human edits and provenance; version what an agent consumes. [Cairn design →](https://github.com/xcosmosbox/Cairn#核心设计)
- **Follow the failure paths.** Think through bounded memory, backpressure, restart recovery and concurrent cleanup. [Request-log case study →](docs/engineering-notes.md#keeping-request-logging-off-the-forwarding-path)
- **Make evaluation honest.** State supported configurations and test the production path. [RLOO implementation notes →](docs/engineering-notes.md#making-an-rl-algorithm-explicit)

## Earlier builds

| Project | What I explored |
| :-- | :-- |
| [wechaty-PaimonBot](https://github.com/xcosmosbox/wechaty-PaimonBot) | A TypeScript chat bot with modular Python tools—an early step toward tool-using assistants. |
| [TinyJSON](https://github.com/xcosmosbox/TinyJSON) | JSON parsing in C++. |
| [Ukkonen · BWT · LZ77](https://github.com/xcosmosbox/Ukkonen_BWT_LZ77) | Suffix trees, string matching and compression in Python. |

## Let's build

Interested in **agent systems, knowledge infrastructure, or turning an idea into a working product**? [Start a conversation →](https://github.com/xcosmosbox/xcosmosbox/issues/new?template=hello.yml)

<sub>This profile highlights selected public work. Project details and implementation boundaries live in the linked repositories and pull requests.</sub>
