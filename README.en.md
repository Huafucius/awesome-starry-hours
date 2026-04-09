# Awesome Personalized Skills

<div align="center">

### 人类群星闪耀时

> 你是万千星辰中的一颗，于某个 Ta 而言却是整个世界。
>
> *You are one star among countless others; to someone, you are an entire world.*

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](./CONTRIBUTING.md)
[![Awesome](https://img.shields.io/badge/awesome-list-fc60a8?style=flat-square)](#)

**English** • [简体中文](README.md)

A repository that now does two things: curates external skills and incubates in-repo skill-factory prototypes.

[Repository Structure](#-repository-structure) • [Figures](#-figures) • [Books](#-books) • [Brands](#-brands) • [Contributing](#-contributing)

</div>

---

This repository now has two tracks:

1. **Awesome index**: a curated list of real, public skill repositories that clearly trace back to a specific **figure**, **book**, or **brand**.
2. **Skill factory prototypes**: in-repo skills under `skills/` that generate new distilled skills, starting with public-information figure skills.

We reject generic role-playing and empty hodgepodges, focusing entirely on extracting truly reusable **thinking frameworks** and **business logic**.

## Contents

- [🌟 Featured](#-featured)
- [🧪 Repository Structure](#-repository-structure)
- [👤 Figures](#-figures)
- [📚 Books](#-books)
- [🏪 Brands](#-brands)
- [📏 Selection Criteria](#-selection-criteria)
- [🤝 Contributing](#-contributing)

## 🧪 Repository Structure

### Part 1: Awesome index

- `README.md` / `README.en.md`
- Continuously curates external `xx.skill` repositories

### Part 2: In-repo skill factory

- `skills/create-figure-skill/`
  - A prototype skill whose job is to create new public-information figure skills
  - Uses a `source -> research -> distilled -> SKILL.md` pipeline
- `skills/luxun-perspective/`
  - A Lu Xun demo skill generated as the first end-to-end verification artifact

The current prototype only supports **figures**. Book and brand generators come later.

## 🌟 Featured

Repositories that clearly demonstrate a solid `source -> skill` distillation path:

- [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) — Distills problem-solving methods from Mao Zedong's works.
- [slavingia/skills](https://github.com/slavingia/skills) — Deconstructs a book into a set of callable commands, showcasing the `book -> skill` path.
- [JinGuYuan/jinguyuan-dumpling-skill](https://github.com/JinGuYuan/jinguyuan-dumpling-skill) — Turns a real-world restaurant into an MCP skill, demonstrating how physical brands enter the AI agent ecosystem.

---

## 👤 Figures

> Extracting the mental models or working methods of specific figures into callable skills.

### Thinkers

| Repo | Name | Description |
|------|------|-------------|
| [RoundTable02/socrates-skill](https://github.com/RoundTable02/socrates-skill) | Socrates | Distills the Socratic method into a teaching skill that helps users discover answers through disciplined questioning. |
| [alchaincyf/feynman-skill](https://github.com/alchaincyf/feynman-skill) | Richard Feynman | Turns Feynman's cognitive operating system into a runnable skill focused on first-principles checking, clear explanation, and self-correction. |
| [alchaincyf/taleb-skill](https://github.com/alchaincyf/taleb-skill) | Nassim Nicholas Taleb | Distills Taleb's frameworks for antifragility, risk exposure, and asymmetric payoff into a callable judgment skill. |

### Politicians

| Repo | Name | Description |
|------|------|-------------|
| [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | Mao Zedong | Distills one general principle and nine methodological tools from Mao-related works for real-world problem-solving. |
| [leezythu/maoxuan-skill](https://github.com/leezythu/maoxuan-skill) | Mao Zedong | Reworks the thinking frameworks, decision heuristics, and expression patterns of *Selected Works of Mao* into a figure-bound analytical skill. |
| [alchaincyf/trump-skill](https://github.com/alchaincyf/trump-skill) | Donald Trump | Distills Trump's negotiation instincts, power framing, and agenda-control style into a high-pressure strategic skill. |

### Entrepreneurs

| Repo | Name | Description |
|------|------|-------------|
| [EveryInc/charlie-cfo-skill](https://github.com/EveryInc/charlie-cfo-skill) | Charlie Munger | Uses Charlie Munger as the cognitive anchor for a bootstrap CFO skill covering capital discipline, unit economics, and cash management. |
| [alchaincyf/munger-skill](https://github.com/alchaincyf/munger-skill) | Charlie Munger | Distills Munger's multidisciplinary thinking, inversion, and anti-stupidity principles into a general business skill. |
| [will2025btc/buffett-perspective](https://github.com/will2025btc/buffett-perspective) | Warren Buffett | Converts Buffett's long-termism, circle-of-competence logic, and capital allocation style into an investable judgment skill. |
| [derrickgong87/duan-yongping-skill](https://github.com/derrickgong87/duan-yongping-skill) | Duan Yongping | Distills Duan Yongping's Chinese value-investing framework and long-term business judgment into a runnable thinking system. |
| [alchaincyf/steve-jobs-skill](https://github.com/alchaincyf/steve-jobs-skill) | Steve Jobs | Distills Steve Jobs's cognitive operating system around product taste, ruthless focus, and persuasive storytelling. |
| [alchaincyf/elon-musk-skill](https://github.com/alchaincyf/elon-musk-skill) | Elon Musk | Turns Musk's first-principles reasoning, engineering constraints, and cost focus into a high-intensity execution skill. |
| [alchaincyf/zhang-yiming-skill](https://github.com/alchaincyf/zhang-yiming-skill) | Zhang Yiming | Captures Zhang Yiming's judgments around information distribution, organizational efficiency, and long-term business competitiveness. |
| [alchaincyf/paul-graham-skill](https://github.com/alchaincyf/paul-graham-skill) | Paul Graham | Distills Paul Graham's startup, writing, and product judgment into a callable founder-mentor skill. |
| [alchaincyf/naval-skill](https://github.com/alchaincyf/naval-skill) | Naval Ravikant | Turns Naval's frameworks for wealth, leverage, and life decisions into a cognitive operating system that spans business and philosophy. |
| [AytuncYildizli/legends-mcp](https://github.com/AytuncYildizli/legends-mcp) | Elon Musk, Steve Jobs, Jeff Bezos, Warren Buffett, Charlie Munger, Paul Graham, Naval Ravikant | A multi-person bundle built around legendary founders and investors, enabling debate-style analysis directly inside Claude. |

### Technical Leaders

| Repo | Name | Description |
|------|------|-------------|
| [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | Andrej Karpathy | Packages Karpathy's observations on LLM coding mistakes and workflow discipline into directly usable Claude Code principles. |
| [alchaincyf/karpathy-skill](https://github.com/alchaincyf/karpathy-skill) | Andrej Karpathy | Distills Karpathy's own cognitive operating system into a runnable skill focused on model intuition, engineering simplification, and explanation quality. |
| [alchaincyf/ilya-sutskever-skill](https://github.com/alchaincyf/ilya-sutskever-skill) | Ilya Sutskever | Extracts Ilya's thinking about scaling, research taste, and AI safety boundaries into a technical judgment skill. |
| [rjs/shaping-skills](https://github.com/rjs/shaping-skills) | Ryan Singer | Breaks Ryan Singer's Shape Up / shaping methods into executable skills for framing problems and roughing out solution spaces. |
| [Atypical-Consulting/claude-legends-review](https://github.com/Atypical-Consulting/claude-legends-review) | Elon Musk, Steve Jobs, Linus Torvalds | Centers code review on disagreement between three famous technical figures until their perspectives converge into a shared verdict. |

### Public Figures

| Repo | Name | Description |
|------|------|-------------|
| [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | Zhang Xuefeng | Distills Zhang Xuefeng's realist frameworks for education choice, graduate exams, and career judgment into a callable consulting skill. |
| [YixiaJack/luo-xiang-skill](https://github.com/YixiaJack/luo-xiang-skill) | Luo Xiang | Lets the AI analyze questions with Luo Xiang's legal reasoning and humanistic concern, emphasizing justice, boundaries, and institutions. |
| [alchaincyf/mrbeast-skill](https://github.com/alchaincyf/mrbeast-skill) | MrBeast | Distills MrBeast's content-production system, hook strategy, and pacing logic into a creator-focused growth skill. |
| [hotcoffeeshake/tong-jincheng-skill](https://github.com/hotcoffeeshake/tong-jincheng-skill) | Tong Jincheng | Distills Tong Jincheng's relationship judgment and blunt interpersonal style into a people-reading skill. |
| [Janlaywss/hu-chenfeng-skill](https://github.com/Janlaywss/hu-chenfeng-skill) | Hu Chenfeng | Uses Hu Chenfeng's consumer realism and life-choice perspective to analyze spending, settling down, and everyday decisions. |
| [rottenpen/fengge-wangmingtianya-perspective](https://github.com/rottenpen/fengge-wangmingtianya-perspective) | Fengge Wangming Tianya | Distills Fengge Wangming Tianya's disillusioned realism and wandering-storytelling style into a Chinese persona skill. |

## 📚 Books

> Distilling core architectures, methodologies, or rules from classic books into skills.

| Repo | Title | Description |
|------|-------|-------------|
| [slavingia/skills](https://github.com/slavingia/skills) | The Minimalist Entrepreneur | Extracts methodologies from Sahil Lavingia's book, mapping each chapter to an independent slash command. |
| [obra/the-elements-of-style](https://github.com/obra/the-elements-of-style) | The Elements of Style | Translates William Strunk Jr.'s 7 rules of usage and 11 principles of composition into AI style constraints. |
| [luoling8192/software-design-philosophy-skill](https://github.com/luoling8192/software-design-philosophy-skill) | A Philosophy of Software Design | Distills software design principles from John Ousterhout's book for code review, architecture, and refactoring. |

## 🏪 Brands

> Converting physical brands into AI-callable information interfaces.

| Repo | Brand Name | Description |
|------|------------|-------------|
| [JinGuYuan/jinguyuan-dumpling-skill](https://github.com/JinGuYuan/jinguyuan-dumpling-skill) | JinGuYuan Dumpling | A dumpling restaurant next to Beijing University of Posts and Telecommunications, providing an MCP Skill for personal AI assistants. |

## 📏 Selection Criteria

- **Real & Open**: Repositories must exist and be publicly accessible.
- **Clear Origin**: Entries must clearly correspond to **one or more specific people**, a **specific book**, or a **specific brand**.
- **Focus on Distillation**: The core value must be extracting frameworks and logic, not merely imitating tone or role-playing.
- We do not include generic targets (e.g., "Any Real Person") or broad skill packs that merely borrow a name; however, tightly scoped multi-person bundles are allowed when they enumerate a recognizable set of notable figures.

## 🤝 Contributing

PRs are welcome. Please ensure:

1. The repository is publicly accessible.
2. It falls under one of the three categories: Figures, Books, or Brands.
3. The name column contains **only exact names**; for multi-person bundles, list the most recognizable named figures explicitly.
4. The description clearly states what specific content was distilled, based on the repository's own README.

## License

[MIT](LICENSE)

---

<p align="center">
  <i>「一个人的命运，当然要靠自我奋斗，但也要考虑到历史的进程。」</i>
  <br/>
  <sub>现在，把历史的进程装进你的终端。</sub>
</p>
