<img align="right" width="96" height="96" src="assets/sancheck-pixel.png" alt="A pixel investigator adapted from my avatar: tall hat, golden hair, tiny cloak">

### >_ San_Check’s save point

Building Agents, connecting knowledge, occasionally duelling bugs.<br>
`GraphRAG` `Agent` `RL` · [简体中文 ↗](README.md)

**`$ ls ~/playground`**　Pick a quest. Have a look around ↓

<p>
  <a href="https://github.com/redai-studio/Relax"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/relax-en-dark.svg">
    <img src="assets/relax-en-light.svg" width="360" height="88" alt="Relax — Reinforcement learning · Training engine">
  </picture></a>
  <a href="https://github.com/HKUDS/nanobot"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/nanobot-en-dark.svg">
    <img src="assets/nanobot-en-light.svg" width="360" height="88" alt="nanobot — Tool use · Long-term memory">
  </picture></a>
  <a href="https://github.com/qxcnm/Codex-Manager"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/codex-manager-en-dark.svg">
    <img src="assets/codex-manager-en-light.svg" width="360" height="88" alt="Codex-Manager — Account management · Request routing">
  </picture></a>
  <a href="https://github.com/Ontos-AI/knowhere"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/knowhere-en-dark.svg">
    <img src="assets/knowhere-en-light.svg" width="360" height="88" alt="Knowhere — Document parsing · Knowledge extraction">
  </picture></a>
  <a href="https://github.com/xcosmosbox/Cairn"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/cairn-en-dark.svg">
    <img src="assets/cairn-en-light.svg" width="360" height="88" alt="Cairn — Graph retrieval · Versioned knowledge">
  </picture></a>
  <a href="https://github.com/xcosmosbox/xcosmosbox/issues/new?template=hello.yml"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/party-en-dark.svg">
    <img src="assets/party-en-light.svg" width="360" height="88" alt="Find a new party member — Swap ideas · Leave a little note">
  </picture></a>
</p>

Code at your own pace. Make a friend along the way. [Drop by](https://github.com/xcosmosbox/xcosmosbox/issues/new?template=hello.yml) — peace & love ✌️

<details>
<summary>🎲 Spot Hidden: is that a note on the back of this README?</summary>

#### Save 00 · The unspeakable legacy code

You pick up a note. It contains a single line:

```python
# TODO: Do not touch. The reason is beyond human comprehension.
```

**Choose your investigation:**

<details>
<summary>🔎 Investigate → git blame</summary>

```diff
- Author: an unspeakable Great Old One
+ Author: me, three months ago
```

**Sanity −1. Experience +1.** The eldritch horror was me all along.

</details>

<details>
<summary>🎲 Try your luck → run the tests</summary>

```console
$ pytest -q
100 passed
$ git diff --stat
0 files changed
```

**Ending: critical success.** Nothing changed. The bug vanished. Today, you decide to leave the mysteries of the universe alone.

</details>

<details>
<summary>🍵 Willpower → save, then make tea</summary>

```python
sanity += 1
party.add("you, passing by")
quest.pause(reason="tea is best enjoyed warm")
```

Loot: **hot tea × 1 · new party member × 1**. The code can be saved tomorrow. Live a little today.

</details>

<sub>The name is a nod to Call of Cthulhu: Sanity Check + 1D100. This is a tiny choose-your-path adventure. For an actual roll, bring dice—or borrow this one.</sub>

```python
from random import randint
print(f"SAN CHECK · 1D100 = {randint(1, 100):02d}")
```

</details>
