---
name: web-demo-video-maker
description: Record a local web demo and turn it into a clean promo video using Playwright and ffmpeg only. Use when the user has a local HTML file, localhost demo, prototype, or web app and wants a demo video, walkthrough video, promo clip, screen capture, or edited showcase without using external video APIs.
metadata:
  author: OpenAI
  version: "0.1.0"
  tags: local-video, playwright, ffmpeg, demo-video, prototype, screen-recording, codex, no-api
---

# Web Demo Video Maker

Create a polished walkthrough video for a web demo using only local tools.

This skill is for cases where the user already has a prototype or demo page and wants a presentable video quickly.

## Goals

- work fully locally
- avoid external model APIs
- produce repeatable, scripted recordings
- keep output consistent across revisions

## Required tools

- Node.js 20+
- ffmpeg available in PATH
- Playwright Chromium installed locally

## Repository files

- `scripts/record-scenes.mjs` — records scene clips with Playwright video capture
- `scripts/render-promo.mjs` — trims, normalizes, fades, concatenates, and optionally mixes background music
- `templates/scenario.example.json` — scene and interaction template
- `templates/render.example.json` — rendering template

## When to use this skill

Use this skill when the user says things like:

- make a showcase video for my local html demo
- record my prototype into a presentation clip
- make a clean walkthrough video from my web app
- help me automate clicks and export a demo video

## Inputs expected

### 1. Scenario file

A scenario file describes the demo location and each scene to record.

Minimum fields:

```json
{
  "projectName": "demo-video",
  "baseUrl": "file:///D:/demo/index.html",
  "viewport": { "width": 1440, "height": 900 },
  "outputDir": "./output",
  "scenes": [
    {
      "id": "home",
      "title": "Home overview",
      "startUrl": "file:///D:/demo/index.html",
      "leadInMs": 400,
      "tailMs": 500,
      "steps": [
        { "type": "wait", "ms": 800 },
        { "type": "click", "selector": "button.start" },
        { "type": "wait", "ms": 1200 }
      ]
    }
  ]
}
```

### 2. Render file

A render file controls trimming and final output.

```json
{
  "projectName": "demo-video",
  "inputDir": "./output/raw",
  "outputDir": "./output/final",
  "clipDir": "./output/clips",
  "finalName": "demo-promo.mp4",
  "width": 1920,
  "height": 1080,
  "fps": 30,
  "trimStartSec": 0.2,
  "trimEndSec": 0.2,
  "fadeInSec": 0.25,
  "fadeOutSec": 0.25,
  "bgm": {
    "enabled": false,
    "path": "",
    "volume": 0.12
  }
}
```

## Workflow

### Step 1. Inspect the demo

- identify the main user story worth showing
- reduce the walkthrough to 3 to 6 scenes
- keep each scene purposeful and visually different
- prefer clean pauses over frantic cursor movement

### Step 2. Write or update the scenario

Build a deterministic scenario that records well.

Preferred rhythm:
- short pause before each action
- one primary interaction per beat
- one or two seconds of settling time after motion-heavy changes

### Step 3. Record scenes

Run:

```bash
node scripts/record-scenes.mjs --scenario ./templates/scenario.example.json
```

What the recorder does:
- launches Chromium through Playwright
- opens a fresh browser context per scene
- records a local browser video for that scene
- saves raw webm files under `output/raw`
- writes a metadata file listing all captured clips

### Step 4. Render the final promo

Run:

```bash
node scripts/render-promo.mjs --config ./templates/render.example.json
```

What the renderer does:
- trims scene heads and tails
- scales and pads to a consistent resolution
- adds quick fade in and fade out
- concatenates all scenes in order
- optionally mixes background music
- writes the final mp4

## Agent behavior rules

When using this skill:

1. Keep the story concise.
2. Prefer visible, readable interactions over fast cursor travel.
3. Avoid showing loading states longer than necessary.
4. Keep each clip stable for at least 500 ms after a major transition.
5. If the user provides only a local html file, use it directly through a `file:///` URL or a local server.
6. If the page requires a dev server, tell the user to start it first, then point the scenario to localhost.
7. Do not invent remote APIs or cloud video tools.
8. Do not claim the workflow can generate cinematic footage from scratch. It records and edits the actual demo.

## Good scene structure

A strong demo usually follows this arc:

1. entry state
2. key feature activation
3. feature result
4. secondary interaction
5. final summary view

## Example prompt for the agent

Use the `web-demo-video-maker` skill on my local demo.

- demo path: `file:///D:/projects/demo/index.html`
- goal: create a 20 to 30 second clean showcase video
- style: minimal, product-demo, no flashy moves
- include scenes for home, key interaction, result screen, and settings
- record the clips locally and render a final mp4

## Troubleshooting

### ffmpeg not found

Install ffmpeg and make sure it is available in PATH.

### Playwright browser missing

Run:

```bash
npx playwright install chromium
```

### file:/// page blocks local assets

Serve the project through a local dev server and change `baseUrl` to localhost.

### Click target is flaky

Add a wait before the click, or use a more stable selector.

### Output is letterboxed

Adjust viewport and render size to match the aspect ratio you want.

## Deliverables

At the end of a run, present:

- the final video path
- the list of raw recorded scenes
- any selectors or waits that were adjusted for stability
