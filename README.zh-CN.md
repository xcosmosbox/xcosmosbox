<picture><source media="(prefers-reduced-motion: reduce)" srcset="assets/quantum-pier-still.png"><img align="right" width="360" height="101" src="assets/quantum-pier.gif" alt="像素调查员在霓虹渔村遇见量子古神：先 Debug，再一起饮茶。"></picture>

### >_ San_Check 的存档点

写点 Agent，连点知识，偶尔跟 bug 对线。<br>
`GraphRAG` `Agent` `RL` · [English ↗](README.en.md)

**`$ ls ~/playground`**　挑个副本，随便逛逛 ↓

<p>
  <a href="https://github.com/redai-studio/Relax"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/relax-zh-dark.svg"><img src="assets/relax-zh-light.svg" width="360" height="88" alt="Relax — 强化学习 · 训练引擎"></picture></a>
  <a href="https://github.com/HKUDS/nanobot"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/nanobot-zh-dark.svg"><img src="assets/nanobot-zh-light.svg" width="360" height="88" alt="nanobot — 工具调用 · 长期记忆"></picture></a>
  <a href="https://github.com/qxcnm/Codex-Manager"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/codex-manager-zh-dark.svg"><img src="assets/codex-manager-zh-light.svg" width="360" height="88" alt="Codex-Manager — 账号管理 · 请求路由"></picture></a>
  <a href="https://github.com/Ontos-AI/knowhere"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/knowhere-zh-dark.svg"><img src="assets/knowhere-zh-light.svg" width="360" height="88" alt="Knowhere — 文档解析 · 知识提取"></picture></a>
  <a href="https://github.com/xcosmosbox/Cairn"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cairn-zh-dark.svg"><img src="assets/cairn-zh-light.svg" width="360" height="88" alt="Cairn — 图谱检索 · 版本化知识"></picture></a>
  <a href="https://github.com/xcosmosbox/xcosmosbox/issues/new?template=hello.yml"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/party-zh-dark.svg"><img src="assets/party-zh-light.svg" width="360" height="88" alt="邀请一位新队友 — 聊个想法 · 留个脚印"></picture></a>
</p>

代码慢慢写，朋友慢慢交。[来串个门](https://github.com/xcosmosbox/xcosmosbox/issues/new?template=hello.yml)，peace & love ✌️ · 饮茶先啦 🍵

<details>
<summary>🎲 侦查检定：README 背面好像有张纸条……</summary>

#### 存档 00 · 不可名状的旧代码

你捡起纸条，上面只有一行：

```python
# TODO: 这里千万别动。原因已经不可名状。
```

**选择你的调查路线：**

<details>
<summary>🔎 侦查 → git blame</summary>

```diff
- 作者：不可名状的旧日支配者
+ 作者：三个月前的我
```

**理智 −1，经验 +1。** 原来古神竟是我自己。

</details>

<details>
<summary>🎲 幸运 → 先跑一下测试</summary>

```console
$ pytest -q
100 passed
$ git diff --stat
0 files changed
```

**结局 · 大成功。** 什么都没改，bug 自己消失了。你决定今天先不追究宇宙的真相。

</details>

<details>
<summary>🍵 意志 → 存档，先去泡茶</summary>

```python
sanity += 1
party.add("路过的你")
quest.pause(reason="茶要趁热")
```

获得 **热茶 × 1 · 新队友 × 1**。明天再拯救代码，今天先好好生活。

</details>

纸条背面还粘着一枚赛博骰子。终端低声说：

> **「调查员，把它掷出去。看看是你先找到 bug，还是 bug 先找到你。」**

```python
from random import randint

san, d100 = 60, randint(1, 100)
print(f"🎲 SAN {san} · 1D100 = {d100:02d}")
if d100 == 1:
    print("大成功。古神看了眼你的代码，决定帮你修。")
elif d100 == 100:
    print("大失败。git blame 指向了你的前世。")
elif d100 <= san:
    print("检定成功。古神也说：饮茶先啦 🍵")
else:
    print(f"SAN -{randint(1, 6)}。你在栈底听见了自己的名字。")
```

<sub>连接已断开。海面上，多亮起了一扇窗。</sub>

</details>
