# Codex Demo Video Skill

A local-first demo video generation skill for Codex / Code X workflows.

这个 skill 用于把已经可以运行的网页 Demo、HTML 原型、前端交互页面或产品功能 Demo，整理成适合作品集、课程汇报、比赛提交和产品说明的视频展示内容。

## Keywords

codex skill, code x skill, demo video skill, local video generation, playwright video recording, puppeteer automation, ffmpeg video export, html demo recorder, web prototype video, portfolio demo video, design presentation automation

## What it does

This skill helps Codex analyze an existing local demo and generate a clearer video presentation plan. It focuses on:

- identifying important screens, states, and interaction nodes
- turning loose user operation into a structured video flow
- using browser automation to open pages, click, scroll, pause, and switch states
- recording or capturing key moments from a web-based demo
- exporting video clips or organized material for further editing

## Best use cases

- HTML / web prototype recording
- product concept demo presentation
- interaction design portfolio video
- competition submission video
- course project demonstration
- front-end project walkthrough
- UI flow explanation

## Typical workflow

```text
1. Provide a local HTML file or localhost URL.
2. Tell Codex the video goal, duration, and core functions.
3. The skill extracts key scenes and creates a shot plan.
4. Browser automation records the planned flow.
5. FFmpeg exports or assembles the final video material.
```

## Suggested tech stack

```text
Node.js
TypeScript
Playwright or Puppeteer
FFmpeg
```

## Example prompt

```text
Use the Codex Demo Video Skill to create a 40-second portfolio demo video for my local HTML prototype. The page is at http://localhost:3000. Focus on the onboarding screen, the main interaction flow, the feedback animation, and the result summary page. Keep the rhythm clean and suitable for a design portfolio.
```

## Positioning

This is a local-first showcase automation skill. It does not depend on third-party AI video generation APIs. It is designed for users who already have a working demo and need to package it into a clearer, more watchable video sequence.
