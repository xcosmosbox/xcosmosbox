<img align="right" width="96" height="96" src="assets/sancheck-pixel.png" alt="从原头像走出来的像素调查员：高帽、金发、小披风">

### >_ San_Check 的存档点

写点 Agent，连点知识，偶尔跟 bug 对线。<br>
`GraphRAG` `Agent` `RL` · [English ↗](README.en.md)

**`$ ls ~/playground`**　挑个副本，随便逛逛 ↓

<p>
  <a href="https://github.com/redai-studio/Relax"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/relax-zh-dark.svg">
    <img src="assets/relax-zh-light.svg" width="360" height="88" alt="Relax — 强化学习 · 训练引擎">
  </picture></a>
  <a href="https://github.com/HKUDS/nanobot"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/nanobot-zh-dark.svg">
    <img src="assets/nanobot-zh-light.svg" width="360" height="88" alt="nanobot — 工具调用 · 长期记忆">
  </picture></a>
  <a href="https://github.com/qxcnm/Codex-Manager"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/codex-manager-zh-dark.svg">
    <img src="assets/codex-manager-zh-light.svg" width="360" height="88" alt="Codex-Manager — 账号管理 · 请求路由">
  </picture></a>
  <a href="https://github.com/Ontos-AI/knowhere"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/knowhere-zh-dark.svg">
    <img src="assets/knowhere-zh-light.svg" width="360" height="88" alt="Knowhere — 文档解析 · 知识提取">
  </picture></a>
  <a href="https://github.com/xcosmosbox/Cairn"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/cairn-zh-dark.svg">
    <img src="assets/cairn-zh-light.svg" width="360" height="88" alt="Cairn — 图谱检索 · 版本化知识">
  </picture></a>
  <a href="https://github.com/xcosmosbox/xcosmosbox/issues/new?template=hello.yml"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/party-zh-dark.svg">
    <img src="assets/party-zh-light.svg" width="360" height="88" alt="邀请一位新队友 — 聊个想法 · 留个脚印">
  </picture></a>
</p>

代码慢慢写，朋友慢慢交。[来串个门](https://github.com/xcosmosbox/xcosmosbox/issues/new?template=hello.yml)，peace & love ✌️

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

<sub>名字里的梗是 COC 的 Sanity Check + 1D100。这里是一个选路线的小模组；真实检定请自备骰子，也可以借下面这颗。</sub>

```python
from random import randint
print(f"SAN CHECK · 1D100 = {randint(1, 100):02d}")
```

</details>
