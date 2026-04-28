# Codex Open Scholar Skills

Codex / Code X adaptation of the Open Scholar Skill workflow.

This project rewrites the academic workflow logic of `joshzyj/open-scholar-skill` into a Codex-friendly skill project. It keeps the strongest parts of the original idea: modular research skills, researcher-in-the-loop control, source integrity, citation verification, data-safety classification, process logs, verification loops, journal preparation, replication packaging, and review response.

## What is included

The project generates 32 Codex skills and 19 review/verification agent role cards.

### Core research pipeline

- scholar-init
- scholar-idea
- scholar-brainstorm
- scholar-lit-review
- scholar-lit-review-hypothesis
- scholar-hypothesis
- scholar-design
- scholar-causal
- scholar-data
- scholar-eda
- scholar-analyze
- scholar-compute
- scholar-qual
- scholar-ling
- scholar-write
- scholar-citation
- scholar-verify
- scholar-polish
- scholar-journal
- scholar-open
- scholar-replication
- scholar-code-review
- scholar-respond

### Extended research management

- scholar-knowledge
- scholar-monitor
- scholar-collaborate
- scholar-conceptual
- scholar-openai
- scholar-ethics
- scholar-safety
- scholar-auto-improve
- sync-docs

## Build the expanded project

```bash
cd codex-open-scholar-skills
python build_project.py
```

This creates:

```text
codex-open-scholar-skills/
├── skills/
│   ├── scholar-lit-review/SKILL.md
│   ├── scholar-conceptual/SKILL.md
│   └── ... 32 skills total
├── shared/
├── agents/
├── examples/
├── templates/
├── install.sh
├── LICENSE
└── UPSTREAM_NOTICE.md
```

## Install into Codex / Code X

Default install target:

```bash
bash install.sh
```

Custom target:

```bash
CODEX_SKILLS_DIR="/path/to/your/codex/skills" bash install.sh
```

## Recommended workflow

```text
/scholar-init
/scholar-idea 基于环境感知的智能座舱设计
/scholar-lit-review targeted 基于车内乘员状态感知的智能座舱交互设计
/scholar-conceptual diagram 构建“乘员状态感知—系统判断—座舱自适应—体验改善”的机制模型
/scholar-write 开题报告研究现状部分
/scholar-citation audit GB/T 7714
/scholar-verify full output/drafts/opening-report.md
```

## Data safety principle

Before reading any dataset, transcript, interview, medical record, private email, contract, or participant-level file, classify it as one of:

- CLEARED
- LOCAL_MODE
- ANONYMIZED
- OVERRIDE
- HALTED

When uncertain, fail closed and use LOCAL_MODE or HALTED.

## Citation principle

Never invent citations. If a source cannot be verified, mark it as `[CITATION NEEDED]`. If the source exists but the exact claim has not been checked, mark it as `[CLAIM UNVERIFIED]`.

## License and attribution

This is an academic / educational / non-commercial adaptation. See `UPSTREAM_NOTICE.md` and `LICENSE`.
