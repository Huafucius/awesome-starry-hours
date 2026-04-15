# 群星 · Starry Hours

<div align="center">

### 人类群星闪耀时

> 你是万千星辰中的一颗，于某个 Ta 而言却是整个世界。
>
> *You are one star among countless others; to someone, you are an entire world.*

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](./CONTRIBUTING.md)
[![Awesome](https://img.shields.io/badge/awesome-list-fc60a8?style=flat-square)](#)

[English](README.en.md) • **简体中文**

一份外部 skill 的精选索引；也是一座「做 skill 的 skill」的工厂。

[仓库结构](#-仓库结构--repository-structure) • [人物](#-人物--figures) • [书籍](#-书籍--books) • [品牌](#-品牌--brands) • [贡献](#-贡献--contributing)

</div>

---

这个仓库把三类对象蒸馏成 Claude Code 可调用的 Skill：历史与当代里值得学的**人物**、**书籍**、**品牌**。

不收泛泛的角色扮演，不收空洞的大杂烩——只蒸馏**思维框架**与**业务逻辑**。

## 目录 / Contents

- [🌟 精选 / Featured](#-精选--featured)
- [🧪 仓库结构 / Repository Structure](#-仓库结构--repository-structure)
- [👤 人物 / Figures](#-人物--figures)
- [📚 书籍 / Books](#-书籍--books)
- [🏪 品牌 / Brands](#-品牌--brands)
- [📏 收录标准 / Selection Criteria](#-收录标准--selection-criteria)
- [🤝 贡献 / Contributing](#-贡献--contributing)

## 🧪 仓库结构 / Repository Structure

### Part 1: 索引

- `README.md` / `README.en.md`
- 持续收录外部 `xx.skill` 仓库

### Part 2: Skill 工厂

- `skills/create-figure-skill/` — 一个做「人物 skill」的 skill；流程 `source → research → distilled → SKILL.md`

工厂现在只做**人物**，书籍和品牌以后再说。

## 🌟 精选 / Featured

三个最能看出 `源对象 → Skill` 蒸馏路径的样本：

- [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) — 从《毛选》提炼问题拆解方法，中文个性化 skill 赛道的代表样本之一。
- [slavingia/skills](https://github.com/slavingia/skills) — 将一本书拆解为一组命令，展示了 `book -> skill` 的实现路径。
- [JinGuYuan/jinguyuan-dumpling-skill](https://github.com/JinGuYuan/jinguyuan-dumpling-skill) — 将现实餐馆做成 MCP skill，展示品牌进入 agent 生态的直观方式。

---

## 👤 人物 / Figures

> 把一个人的思维方式或工作方法，做成可调用的 Skill。

### 思想家

| Repo | 人名 | 简介 |
|------|------|------|
| [RoundTable02/socrates-skill](https://github.com/RoundTable02/socrates-skill) | 苏格拉底 | 将苏格拉底式提问法提炼成教学 Skill，通过连续追问引导用户自行发现答案。 |
| [alchaincyf/feynman-skill](https://github.com/alchaincyf/feynman-skill) | 理查德·费曼 | 将费曼的认知操作系统蒸馏为可运行的 Skill，强调第一性检验、清晰解释与自我纠错。 |
| [alchaincyf/taleb-skill](https://github.com/alchaincyf/taleb-skill) | 纳西姆·塔勒布 | 提炼 Taleb 的反脆弱、风险暴露与非对称收益框架，用于判断复杂系统中的真实脆弱点。 |

### 政治家

| Repo | 人名 | 简介 |
|------|------|------|
| [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | 毛泽东 | 从教员相关著作中提炼出一条总原则和九大方法论工具，系统性地武装 AI 的大脑，用于现实问题拆解。 |
| [leezythu/maoxuan-skill](https://github.com/leezythu/maoxuan-skill) | 毛泽东 | 将《毛选》中的思维框架、决策启发式与表达结构整理为人物强绑定的分析 Skill。 |
| [alchaincyf/trump-skill](https://github.com/alchaincyf/trump-skill) | Donald Trump | 提炼 Trump 在谈判、表达与议题设置上的方式，形成一套强表达型的沟通 Skill。 |

### 企业家

| Repo | 人名 | 简介 |
|------|------|------|
| [EveryInc/charlie-cfo-skill](https://github.com/EveryInc/charlie-cfo-skill) | Charlie Munger | 以 Charlie Munger 为认知原型，把资本纪律、单位经济和现金管理封装成 bootstrap CFO Skill。 |
| [alchaincyf/munger-skill](https://github.com/alchaincyf/munger-skill) | Charlie Munger | 将芒格的多学科思维、逆向思考与避免愚蠢原则蒸馏为通用商业判断 Skill。 |
| [will2025btc/buffett-perspective](https://github.com/will2025btc/buffett-perspective) | Warren Buffett | 将 Buffett 的长期主义、能力圈与资本配置框架转成可调用的投资认知 Skill。 |
| [derrickgong87/duan-yongping-skill](https://github.com/derrickgong87/duan-yongping-skill) | 段永平 | 将段永平的中国价值投资与长期商业判断提炼为可运行的思维操作系统。 |
| [alchaincyf/steve-jobs-skill](https://github.com/alchaincyf/steve-jobs-skill) | Steve Jobs | 提炼 Steve Jobs 在产品审美、聚焦取舍与叙事表达上的认知操作系统。 |
| [alchaincyf/elon-musk-skill](https://github.com/alchaincyf/elon-musk-skill) | Elon Musk | 将 Musk 的第一性原理、工程约束与成本思维蒸馏为高压执行型 Skill。 |
| [alchaincyf/zhang-yiming-skill](https://github.com/alchaincyf/zhang-yiming-skill) | 张一鸣 | 围绕张一鸣在信息分发、组织效率与长期竞争力上的判断方式，整理为企业经营 Skill。 |
| [alchaincyf/paul-graham-skill](https://github.com/alchaincyf/paul-graham-skill) | Paul Graham | 提炼 Paul Graham 在写作、创业与产品判断上的认知框架，形成可调用的创业导师型 Skill。 |
| [alchaincyf/naval-skill](https://github.com/alchaincyf/naval-skill) | Naval Ravikant | 将 Naval 的财富、杠杆与人生决策框架蒸馏为兼具商业与人生哲学的认知操作系统。 |
| [AytuncYildizli/legends-mcp](https://github.com/AytuncYildizli/legends-mcp) | Elon Musk、Steve Jobs、Jeff Bezos、Warren Buffett、Charlie Munger、Paul Graham、Naval Ravikant | 一个围绕传奇创业者与投资人构建的多人 bundle，可在 Claude 中直接发起多名人辩论式分析。 |

### 技术领袖

| Repo | 人名 | 简介 |
|------|------|------|
| [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | Andrej Karpathy | 将 Karpathy 对 LLM 编程失误与工作流的观察整理为 Claude Code 可直接采用的技术原则。 |
| [alchaincyf/karpathy-skill](https://github.com/alchaincyf/karpathy-skill) | Andrej Karpathy | 将 Karpathy 本人的认知操作系统蒸馏为可运行 Skill，强调模型直觉、工程简化与解释能力。 |
| [alchaincyf/ilya-sutskever-skill](https://github.com/alchaincyf/ilya-sutskever-skill) | Ilya Sutskever | 围绕 Ilya 在 scaling、研究品味与 AI 安全边界上的思考，提炼成技术判断 Skill。 |
| [rjs/shaping-skills](https://github.com/rjs/shaping-skills) | Ryan Singer | 将 Ryan Singer 的 Shape Up / shaping 方法拆成可执行技能，用于问题塑形与方案粗建模。 |
| [Atypical-Consulting/claude-legends-review](https://github.com/Atypical-Consulting/claude-legends-review) | Elon Musk、Steve Jobs、Linus Torvalds | 以三位技术名人的分歧式审查为核心，让代码在争辩中收敛到共识评审意见。 |

### 公众人物

| Repo | 人名 | 简介 |
|------|------|------|
| [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | 张雪峰 | 将张雪峰在升学、考研与职业判断上的现实主义框架提炼为可直接调用的咨询 Skill。 |
| [YixiaJack/luo-xiang-skill](https://github.com/YixiaJack/luo-xiang-skill) | 罗翔 | 让 AI 以罗翔的法学思维与人文关怀分析问题，强调正义、边界与制度理解。 |
| [alchaincyf/mrbeast-skill](https://github.com/alchaincyf/mrbeast-skill) | MrBeast | 将 MrBeast 的内容制作、标题策略与传播节奏提炼为面向创作者的内容增长 Skill。 |

## 📚 书籍 / Books

> 把一本书里的架构、方法或规则，做成可调用的 Skill。

| Repo | 书名 | 简介 |
|------|------|------|
| [slavingia/skills](https://github.com/slavingia/skills) | The Minimalist Entrepreneur | 提取 Sahil Lavingia 原书方法论，每章对应一个独立的 slash command 供实际调用。 |
| [obra/the-elements-of-style](https://github.com/obra/the-elements-of-style) | The Elements of Style | 将 William Strunk Jr. 原著中的 7 条基本用法和 11 条写作原则转成面向 AI 的风格约束规则。 |
| [luoling8192/software-design-philosophy-skill](https://github.com/luoling8192/software-design-philosophy-skill) | A Philosophy of Software Design | 基于 John Ousterhout 的著作提炼软件设计原则，用于代码评审、架构讨论与重构实现。 |

## 🏪 品牌 / Brands

> 把一个实体品牌，做成 AI 能调用的接口。万物皆可 CLI 化。

| Repo | 品牌名 | 简介 |
|------|--------|------|
| [JinGuYuan/jinguyuan-dumpling-skill](https://github.com/JinGuYuan/jinguyuan-dumpling-skill) | 金谷园饺子馆 | 北京邮电大学旁的饺子馆，面向顾客私人 AI 助理的 MCP Skill。 |

## 📏 收录标准 / Selection Criteria

- **真实开源**：仓库必须真实存在、可访问。
- **明确溯源**：必须对应到**一个或多个具体人物**、**一本具体的书**或**一个具体品牌**。
- **重在蒸馏**：提取的是框架和逻辑，不是模仿语气或扮演角色。
- 不收泛指对象（比如“任意真实人物”），不收只是借名号的大杂烩；但围绕**一组能点名的知名人物**构建的多人 bundle 可以收。

## 🤝 贡献 / Contributing

欢迎 PR。请确保：

1. 仓库公开可访问。
2. 属于人物、书籍、品牌三类之一。
3. 名字列**只写明确的名字**；多人 bundle 请列出最具识别度的几位。
4. 描述基于该仓库自己的 README 写，说清楚它蒸馏了什么。

## 许可证 / License

[MIT](LICENSE)

---

<p align="center">
  <i>「一个人的命运，当然要靠自我奋斗，但也要考虑到历史的进程。」</i>
  <br/>
  <sub>现在，把历史的进程装进你的终端。</sub>
</p>
