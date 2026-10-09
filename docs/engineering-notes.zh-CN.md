# 工程笔记

[← 返回首页](../README.zh-CN.md) · [English](engineering-notes.md)

记录公开工作里的三个具体取舍。实现、测试和讨论都在对应的仓库与 PR 中。

## 让知识可以持续维护

**问题。** Skill 文档会变。一次性抽取出图谱，还没有解决人工修正如何保留、更新如何安全交给 Agent 的问题。

**[Cairn](https://github.com/xcosmosbox/Cairn) 的设计。** 将需要 LLM 的构建端与只读查询端分开；通过结构化 Markdown 块和 sidecar 保留可编辑知识。人工修改保留来源标记，之后的 LLM 更新不会覆盖它。图谱打包成不可变 Bundle，消费端校验摘要后原子热切换，历史版本可以回滚。

**边界。** 图谱有结构，不等于回答就更准确。查询行为和抽取质量仍需评测。检索实验区分召回变化与回答正确率，也明确记录 SQLite FTS5 默认分词对中文的限制。

[架构与设计](https://github.com/xcosmosbox/Cairn) · [检索评测](https://github.com/xcosmosbox/Cairn/tree/main/e2e/quality)

## 让请求日志离开转发热路径

**问题。** 记录请求内容可能与请求转发争抢数据库连接和 I/O。清空又带来并发问题：旧的排队任务不能在清空后重新出现，新写入的数据也不能被误删。

**我在 Codex-Manager 的改动。** [#496](https://github.com/qxcnm/Codex-Manager/pull/496) 把捕获改为共享字节并进入有界内存流水线，预处理、组提交和磁盘溢出交给后台线程。重试、重启与丢弃原因有明确观测入口；开启脱敏时，数据先脱敏再溢出到磁盘。

[#498](https://github.com/qxcnm/Codex-Manager/pull/498) 用清理代次替代时间边界。SQLite 可能在同一秒内复用 row ID；代次能区分一行数据是在清空前还是清空后写入，不依赖时间戳精度。回归测试直接复现了同秒复用场景。

**边界。** 有界流水线不能承诺无限保留。磁盘压力和线程故障需要明确的处理方式与计数。PR 记录了这些边界，也区分实际执行和未执行的测试。

## 把强化学习算法的实现边界写清楚

**问题。** 支持一种训练算法，需要 baseline、loss 分发、归约、配置校验与诊断指标共同保持一致。

**我在 [Relax #205](https://github.com/redai-studio/Relax/pull/205) 的贡献。** 实现同步 RLOO 支持，包括 leave-one-out baseline、非裁剪 policy loss、Megatron 集成、分布式测试和 recipe。参数校验限制支持的同步拓扑；测试覆盖生产 reducer 与实际 loss 分发路径。

**边界。** 当前实现采用全局有效 token 归一化。逐元素 REINFORCE 项与所述公式一致，但不把最终标量归约宣称为与论文的 sequence-level estimator 逐值相同。PR 解释了尺度差异与支持的配置。

---

[返回首页 →](../README.zh-CN.md)
