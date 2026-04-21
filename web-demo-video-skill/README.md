# Web Demo Video Skill

A local-only skill scaffold for turning a web demo into a clean presentation video.

This project is designed for skill-enabled agents such as Codex, OpenClaw, Claude Code, Cursor, or similar environments that can read a `SKILL.md` file and execute local commands.

## What it does

- opens a local or hosted web demo with Playwright
- performs scripted interactions scene by scene
- records each scene as a browser video locally
- trims and normalizes the clips with ffmpeg
- joins the clips into a final promo video
- optionally mixes in background music

## What it does not need

- no remote text-to-video API
- no external vision API
- no SaaS video generator

## Local dependencies

- Node.js 20+
- ffmpeg
- Playwright Chromium browser

## Install

```bash
npm install
npm run install:browsers
```

## Basic workflow

1. Edit `templates/scenario.example.json` to describe the demo URL and the step-by-step interactions.
2. Edit `templates/render.example.json` to control output size, trim amount, fades, and music.
3. Record the scenes.
4. Render the final video.

```bash
node scripts/record-scenes.mjs --scenario ./templates/scenario.example.json
node scripts/render-promo.mjs --config ./templates/render.example.json
```

## Supported demo targets

- `http://localhost:3000`
- `http://127.0.0.1:5500`
- `file:///D:/path/to/demo.html`

## Step types supported in scenario

- `goto`
- `wait`
- `click`
- `dblclick`
- `fill`
- `press`
- `hover`
- `scroll`
- `evaluate`
- `screenshot`

## Output layout

```text
output/
├── raw/
│   ├── 01-home.webm
│   └── 02-feature.webm
├── clips/
│   ├── 01-home.mp4
│   └── 02-feature.mp4
└── final/
    └── demo-promo.mp4
```

## Notes

- Playwright records videos in webm first. The render step converts them to mp4.
- If your demo needs a local dev server, start it first.
- If your demo is a static html file, use a `file:///` URL or a simple local server.
- If your demo uses system audio, this scaffold currently focuses on video-first output. Background music can be mixed in from a local audio file.

## Windows example

```bash
npm install
npx playwright install chromium
node scripts/record-scenes.mjs --scenario .\templates\scenario.example.json
node scripts/render-promo.mjs --config .\templates\render.example.json
```
