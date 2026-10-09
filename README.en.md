<picture><source media="(prefers-reduced-motion: reduce)" srcset="assets/quantum-pier-still.png"><img align="right" width="360" height="101" src="assets/quantum-pier.gif" alt="A pixel investigator meets a quantum bug in a neon fishing village: debug, then tea."></picture>

### >_ San_Check’s save point

Building Agents, connecting knowledge, occasionally duelling bugs.<br>
`GraphRAG` `Agent` `RL` · [简体中文 ↗](README.md)

**`$ ls ~/playground`**　Pick a quest. Have a look around ↓

<p>
  <a href="https://github.com/redai-studio/Relax"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/relax-en-dark.svg"><img src="assets/relax-en-light.svg" width="360" height="88" alt="Relax — Reinforcement learning · Training engine"></picture></a>
  <a href="https://github.com/HKUDS/nanobot"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/nanobot-en-dark.svg"><img src="assets/nanobot-en-light.svg" width="360" height="88" alt="nanobot — Tool use · Long-term memory"></picture></a>
  <a href="https://github.com/qxcnm/Codex-Manager"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/codex-manager-en-dark.svg"><img src="assets/codex-manager-en-light.svg" width="360" height="88" alt="Codex-Manager — Account management · Request routing"></picture></a>
  <a href="https://github.com/Ontos-AI/knowhere"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/knowhere-en-dark.svg"><img src="assets/knowhere-en-light.svg" width="360" height="88" alt="Knowhere — Document parsing · Knowledge extraction"></picture></a>
  <a href="https://github.com/xcosmosbox/Cairn"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cairn-en-dark.svg"><img src="assets/cairn-en-light.svg" width="360" height="88" alt="Cairn — Graph retrieval · Versioned knowledge"></picture></a>
  <a href="https://github.com/xcosmosbox/xcosmosbox/issues/new?template=hello.yml"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/party-en-dark.svg"><img src="assets/party-en-light.svg" width="360" height="88" alt="Find a new party member — Swap ideas · Leave a little note"></picture></a>
</p>

Code at your own pace. Make a friend along the way. [Drop by](https://github.com/xcosmosbox/xcosmosbox/issues/new?template=hello.yml) — peace & love ✌️ · tea first 🍵

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

<details>
<summary>🗝️ Before closing the case… turn the note over</summary>

A cybernetic die is taped to the back of the note. The terminal whispers:

> **“Roll it, investigator. Let’s see whether you find the bug—or the bug finds you.”**

```python
from random import randint

san, d100 = 60, randint(1, 100)
print(f"🎲 SAN {san} · 1D100 = {d100:02d}")
if d100 == 1:
    print("Critical success. The Old One offers to fix your code.")
elif d100 == 100:
    print("Fumble. git blame points to your previous life.")
elif d100 <= san:
    print("Check passed. Even the Old One says: tea first 🍵")
else:
    print(f"SAN -{randint(1, 6)}. Your name echoes from the stack.")
```

<sub>Connection closed. One more window lights up across the water.</sub>

</details>

</details>
