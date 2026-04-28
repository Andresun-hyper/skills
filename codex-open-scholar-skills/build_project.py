#!/usr/bin/env python3
from pathlib import Path
import os,json
S={
'scholar-init':'project initialization, standard folders, safety sidecar, process logs',
'scholar-idea':'turn broad topics into researchable questions and thesis directions',
'scholar-brainstorm':'rank research ideas from data, papers, codebooks, and design briefs',
'scholar-lit-review':'systematic or targeted literature review with search log and gap map',
'scholar-lit-review-hypothesis':'integrated literature review, theory logic, and hypotheses',
'scholar-hypothesis':'constructs, variables, indicators, propositions, and test matrices',
'scholar-design':'methodology for experiments, surveys, interviews, usability studies, and mixed methods',
'scholar-causal':'causal question, DAG, identification strategy, assumptions, and robustness',
'scholar-data':'dataset search, data feasibility, survey/interview/observation instruments',
'scholar-eda':'exploratory data analysis, missingness, cleaning, descriptive summaries',
'scholar-analyze':'statistical/computational analysis plans, scripts, tables, figures, interpretation',
'scholar-compute':'NLP, ML, networks, vision, LLM workflow, geospatial, audio, simulation',
'scholar-qual':'qualitative coding, thematic analysis, codebooks, reliability, design implications',
'scholar-ling':'linguistic, corpus, discourse, sociolinguistic, phonetic analysis',
'scholar-write':'academic drafting with outline, evidence, citations, and claim control',
'scholar-citation':'citation insertion, audit, conversion, verification, export, and risk report',
'scholar-verify':'verify claims, numbers, tables, figures, citations, logic, completeness',
'scholar-polish':'clarity, concision, structure, paragraph flow, and venue voice polishing',
'scholar-journal':'journal fit, formatting, cover letter, declarations, submission checklist',
'scholar-open':'preregistration, open data/code, reproducibility, open-access planning',
'scholar-replication':'replication package, artifact registry, run order, documentation',
'scholar-code-review':'research code correctness, robustness, statistics, reproducibility, style, data handling',
'scholar-respond':'reviewer simulation, response letter, revision plan, resubmission framing',
'scholar-knowledge':'cross-project knowledge base for papers, theories, methods, mechanisms, findings',
'scholar-monitor':'literature monitoring, preprint/journal digest, deduplication, relevance ranking',
'scholar-collaborate':'CRediT roles, task division, review cycles, collaboration risks',
'scholar-conceptual':'theoretical frameworks, mechanism diagrams, typologies, process models',
'scholar-openai':'external-style multi-lens second-opinion audit workflow',
'scholar-ethics':'AI disclosure, privacy, authorship, COI, IRB-like ethics audit',
'scholar-safety':'file privacy scan, PII/restricted data classification, safe processing mode',
'scholar-auto-improve':'audit and improve skills, prompts, workflow, and recurring quality issues',
'sync-docs':'sync manuscripts, slides, scripts, posters, boards, claims, numbers, citations'}
A={
'peer-reviewer-quant':'quantitative methods and robustness','peer-reviewer-theory':'theory and contribution','peer-reviewer-computational':'NLP ML network simulation LLM workflow','peer-reviewer-qual':'qualitative design and evidence','peer-reviewer-ling':'language and discourse methods','peer-reviewer-demographics':'population representativeness','peer-reviewer-mixed-methods':'mixed-methods integration','peer-reviewer-ethics':'ethics privacy AI disclosure','peer-reviewer-senior':'editorial significance and fit','verify-numerics':'numeric consistency','verify-figures':'figure consistency','verify-logic':'claim logic','verify-completeness':'artifact completeness','review-code-correctness':'code correctness','review-code-robustness':'edge cases','review-code-statistics':'statistical fidelity','review-code-reproducibility':'reproducibility','review-code-style':'style maintainability','review-code-data-handling':'data handling'}
README='''# Codex Open Scholar Skills\n\nCodex / Code X adaptation of the Open Scholar Skill workflow. It preserves the original essence: modular skills, researcher-in-the-loop control, source integrity, citation verification, data safety, process logs, verification loops, journal preparation, replication packaging, and reviewer response.\n\nRun:\n\n```bash\npython build_project.py\nbash install.sh\n```\n'''
UP='''# Upstream Notice\n\nInspired by https://github.com/joshzyj/open-scholar-skill. Original project: Open Scholar Skill — Academic Paper Writing for Claude Code. Original license: Academic Use. This Codex version rewrites operational instructions and layout for academic, educational, non-commercial research use.\n'''
LIC='''Open Scholar Skill License (Academic Use)\n\nCopyright (c) 2025-2026 Open Scholar Skill Contributors. Academic, educational, and non-commercial research use is permitted with this notice. Commercial use requires separate written permission from the upstream author. Provided AS IS.\n'''
INSTALL='''#!/usr/bin/env bash\nset -euo pipefail\nD="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"\nT="${CODEX_SKILLS_DIR:-$HOME/.codex/skills}"\nmkdir -p "$T"\nfor p in "$D"/skills/*; do [ -d "$p" ]||continue; n="$(basename "$p")"; rm -rf "$T/$n"; cp -R "$p" "$T/$n"; echo "Installed: $n"; done\nmkdir -p "$T/_open-scholar-shared"; cp -R "$D/shared/." "$T/_open-scholar-shared/"\necho Done\n'''
def w(p,t,m=None):
 p.parent.mkdir(parents=True,exist_ok=True); p.write_text(t,encoding='utf-8');
 if m: os.chmod(p,m)
def skill(n,d):
 return f'''---\nname: {n}\ndescription: "{d}"\n---\n\n# {n}\n\nUse this skill for {d}.\n\n## Core principles\n\n- Keep the researcher in the loop.\n- Do not fabricate sources, citations, data, findings, or methods.\n- Check data safety before reading private or participant-level files.\n- Mark unverifiable citations as [CITATION NEEDED].\n- Mark unchecked source claims as [CLAIM UNVERIFIED].\n- Create process logs for complex work.\n\n## Workflow\n\n1. Parse the user goal, discipline, output type, language, and constraints.\n2. Identify source/data safety requirements.\n3. Build a structured plan before producing polished text or artifacts.\n4. Produce reusable output under output/ when useful.\n5. Add a verification note: sources checked, citation gaps, assumptions, risks, next skill.\n\n## Output standard\n\nReturn a concise result plus structured artifacts fit for papers, theses, reports, presentations, or design boards.\n'''
def main():
 r=Path(__file__).resolve().parent
 w(r/'README.md',README); w(r/'UPSTREAM_NOTICE.md',UP); w(r/'LICENSE',LIC); w(r/'install.sh',INSTALL,0o755)
 shared={'source-integrity.md':'Never fabricate references. Use [CITATION NEEDED] and [CLAIM UNVERIFIED]. Verify title, author, year, venue, DOI, claim direction, method, population, and limitation.','data-handling-policy.md':'Statuses: CLEARED, LOCAL_MODE, ANONYMIZED, OVERRIDE, HALTED. Treat interviews, health data, private messages, IDs, location, proprietary and participant-level files as high risk.','process-logger.md':'Create output/logs/process-log-[skill]-[date].md. Log request, files, searches, assumptions, decisions, outputs, risks, and checks.','citation-rules.md':'Default Chinese thesis style: GB/T 7714 sequential numeric citations. Never invent references.','output-contract.md':'Use output/lit-review, theory, methods, analysis, drafts, citations, figures, reviews, journal, replication, logs.'}
 for k,v in shared.items(): w(r/'shared'/k,'# '+k+'\n\n'+v+'\n')
 w(r/'examples'/'EXAMPLE_PROMPTS.md','/scholar-lit-review targeted 基于车内乘员状态感知的智能座舱交互设计\n/scholar-conceptual diagram 构建乘员状态感知—系统判断—座舱自适应—体验改善机制模型\n/scholar-citation audit GB/T 7714\n')
 w(r/'templates'/'research-project-template.md','# Research Project Template\n\ndata/raw, data/interim, data/processed, materials, output, scripts, docs, .codex/safety-status.json\n')
 for n,d in S.items(): w(r/'skills'/n/'SKILL.md',skill(n,d))
 w(r/'skills-registry.json',json.dumps({'skills':[{'name':k,'description':v} for k,v in S.items()]},ensure_ascii=False,indent=2))
 am='# Agents Overview\n\nReusable review lenses.\n\n'
 for n,d in A.items(): w(r/'agents'/(n+'.md'),f'# {n}\n\n{d}. Identify high-risk issues first and provide concrete repair suggestions.\n'); am+=f'## {n}\n\n{d}\n\n'
 w(r/'agents'/'README.md',am); w(r/'agents-registry.json',json.dumps(A,ensure_ascii=False,indent=2))
 print('Built',len(S),'skills and',len(A),'agents')
if __name__=='__main__': main()
