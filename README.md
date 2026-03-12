# Agent Safety Net 🛟

让 AI agent 变得 **更稳、更省、更好懂、对小白更友好**。✨

这是一个从真实用户痛点倒推出来的 AgentSkill。
它不关注“agent 又会了一个新花活”，而是专门解决那些最容易让人崩溃的日常问题：

- 💥 session 越聊越长，越跑越慢
- 🧊 agent 看起来像卡死了一样
- 📦 工具返回一大坨无用数据
- 🧠 跨 session 记忆不连续
- 🛠️ 明明显示安装成功，但就是不能用
- 👀 用户根本看不懂 agent 现在在干嘛

## 这个 skill 是干什么的？

`agent-safety-net` 不是让 agent “更炫”，而是让 agent **更像一个真的能长期合作的产品**。

它给 agent 一套很实用的“防翻车手册”，专门处理 6 类高频问题：

### 1. Context 爆炸 / Session 失控 💣
**问题是什么：**
对话越来越长，越来越慢，越来越贵，甚至开始 compaction 失败。

**这个 skill 会教 agent 做什么：**
- 把当前任务压缩成一份简短交接摘要
- 只保留真正重要的信息
- 用新 session 继续，而不是硬拖着整个历史上下文跑

**它解决的真实问题：**
用户会觉得：
> “怎么越聊越笨，越聊越慢？”

---

### 2. 隐形卡住 / 看起来像死机 🧊
**问题是什么：**
agent 半路停住、像冻结了一样，或者其实是在等权限/输入，但用户根本看不出来。

**这个 skill 会教 agent 做什么：**
- 先判断是不是在等权限、输入、后台任务
- 找到最后一步成功执行到哪里
- 用人话告诉用户现在卡在哪

**它解决的真实问题：**
很多“它坏了”，其实只是“它在等一个你没看到的东西”。

---

### 3. 记忆不连续 / 总要重复说 🧠
**问题是什么：**
用户每次都得重新解释偏好、背景、之前的决定。

**这个 skill 会教 agent 做什么：**
- 把长期记忆和当前任务状态分开
- 只记真正会影响后续执行的东西
- 避免把整段聊天原样塞进记忆里

**它解决的真实问题：**
用户真正想要的是：
> “你记得我是怎么做事的。”
而不是：
> “请再把背景复制一遍。”

---

### 4. 工具输出太吵太啰嗦 📦
**问题是什么：**
MCP、API、脚本经常返回一大堆 JSON、日志、元数据，真正有用的只有一点点。

**这个 skill 会教 agent 做什么：**
- 先压缩工具输出，再交给模型判断
- 只保留下一步决策需要的字段
- 能程序化提取的，就别整段复制进去

**它解决的真实问题：**
这会直接改善：
- token 花费 💸
- 推理速度 ⚡
- 回答质量 ✅

---

### 5. 装好了但还是不能用 🛠️
**问题是什么：**
CLI 装好了、包也在、命令也有，但一跑还是报错。

**这个 skill 会教 agent 做什么：**
- 检查整条链路，而不只看“安装成功”
- 验证 env、cookie、登录、浏览器依赖、MCP endpoint、权限
- 只有真能跑通一个样例动作，才算 setup 完成

**它解决的真实问题：**
很多用户理解里的“安装成功”=“我现在就能用”。
这个 skill 就是在补那条最烦人的最后一公里。🚶

---

### 6. 用户看不懂 agent 在干嘛 👀
**问题是什么：**
用户不知道：
- 现在在做什么
- 为什么停了
- 下一步要干嘛

**这个 skill 会教 agent 做什么：**
- 默认输出短状态：当前阶段 / 卡点 / 下一步
- 优先说人话，而不是扔一大段技术日志

**它解决的真实问题：**
好的 observability 会让 agent 看起来是“靠谱”，而不是“神秘”。

## 适合谁用？

如果你是下面这些人，这个 skill 会很有用：

- 🤖 在做 AI agent 产品的人
- 🧪 在跑 OpenClaw / Codex / Claude Code / AutoGen 工作流的人
- 🔧 经常调试长 session、长任务的人
- 🙋 想让 agent 对非技术用户更友好的人
- 🧭 想做“更好用的 agent UX”，而不只是“更多工具”的人

## 仓库里有什么？

- `SKILL.md` — skill 触发说明 + 使用流程
- `references/` — 每类痛点的解释和解决思路
- `scripts/make_active_task.py` — 生成任务交接摘要
- `scripts/reduce_tool_output.py` — 压缩大 JSON / 工具输出

## 典型使用场景 ✨

- “这个 session 太大了，帮我整理后继续。”
- “agent 看起来卡住了，帮我判断到底卡在哪。”
- “这个 MCP 返回太啰嗦了，先压缩一下再分析。”
- “明明说安装成功了，为什么还是不能用？帮我排查整条链路。”
- “帮我把 agent 产品做得更稳一点，小白也能上手。”

## 为什么做这个 repo？

大多数 agent demo 都在展示：
> agent **能做什么**

这个 skill 更关心的是：
> agent **为什么在真实使用里经常不好用**，以及**怎么把它补好**

所以它特别适合这些方向：
- agent reliability
- agent UX
- token efficiency
- session maintenance
- operator confidence
- beginner-friendly automation

---

# Agent Safety Net 🛟

Make AI agents feel **stable, cheaper, easier to understand, and easier for beginners to use**. ✨

This is an AgentSkill inspired by real user pain from public agent tools and framework discussions.
It focuses on the unglamorous problems that make agents frustrating in real work:

- 💥 sessions getting longer and worse over time
- 🧊 agents freezing or looking stuck
- 📦 tools returning giant noisy payloads
- 🧠 memory across sessions being weak
- 🛠️ installs that look finished but still do not work
- 👀 users not knowing what the agent is doing right now

## What this skill actually does

`agent-safety-net` helps an AI agent improve **operational reliability**, not just output quality.

It gives the agent a practical playbook for six common failures:

### 1. Context explosion 💣
**Problem:** the session gets too long, too slow, too expensive, or starts failing compaction.

**What this skill teaches:**
- shrink the current task into a compact handoff
- preserve only the important state
- continue in a clean session instead of dragging the whole history forward

### 2. Hidden stalls and reliability failures 🧊
**Problem:** the agent looks frozen, stops in the middle, or silently waits for approval.

**What this skill teaches:**
- check whether the agent is actually blocked on permission/input
- identify the last successful step
- tell the user the blocker in plain language

### 3. Weak memory continuity 🧠
**Problem:** users repeat preferences and prior decisions again and again.

**What this skill teaches:**
- separate durable memory from current-task state
- store only the parts that help future execution
- avoid dumping entire conversations into memory

### 4. Noisy tool output 📦
**Problem:** tools return giant JSON blobs, repeated metadata, and long logs that waste context.

**What this skill teaches:**
- reduce tool payloads before handing them back to the model
- keep only the fields needed for the next decision
- use deterministic extraction where possible

### 5. Setup gap: installed but not usable 🛠️
**Problem:** something is “installed” but still fails in real use.

**What this skill teaches:**
- verify the whole chain, not just package presence
- check auth, browser dependencies, env vars, MCP endpoints, cookies, and permissions
- treat setup as done only when a real action works

### 6. Poor observability 👀
**Problem:** the user cannot tell what the agent is doing, why it stopped, or what happens next.

**What this skill teaches:**
- give short status updates with stage, blocker, and next action
- prefer human-readable status over dense raw traces

## Who this is for

This skill is useful if you are:
- building an AI agent product
- running OpenClaw / Codex / Claude Code / AutoGen style workflows
- debugging long-running agent sessions
- trying to make agents easier for non-technical users
- designing a better “agent UX” instead of only adding more tools

## Files

- `SKILL.md` — trigger description + operating workflow
- `references/` — beginner-friendly explanations for each pain point and solution area
- `scripts/make_active_task.py` — generate a compact handoff summary for session rollover
- `scripts/reduce_tool_output.py` — reduce large JSON/tool payloads

## Example use cases

- “This session is getting huge. Help me keep it usable.”
- “The agent looks stuck. Figure out whether it is actually blocked.”
- “This MCP output is too verbose. Reduce it before reasoning.”
- “The install says success, but the tool still does not work. Check the whole chain.”
- “Help me make my agent product feel more stable for beginners.”
