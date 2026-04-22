#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import { chromium } from 'playwright';

function parseArgs(argv) {
  const args = {};
  for (let i = 2; i < argv.length; i += 1) {
    const token = argv[i];
    if (token.startsWith('--')) {
      const key = token.slice(2);
      const next = argv[i + 1];
      if (!next || next.startsWith('--')) {
        args[key] = true;
      } else {
        args[key] = next;
        i += 1;
      }
    }
  }
  return args;
}

function sanitizeName(value) {
  return String(value)
    .toLowerCase()
    .replace(/[^a-z0-9-_]+/gi, '-')
    .replace(/^-+|-+$/g, '') || 'scene';
}

async function ensureDir(dir) {
  await fs.mkdir(dir, { recursive: true });
}

async function exists(target) {
  try {
    await fs.access(target);
    return true;
  } catch {
    return false;
  }
}

async function readJson(filePath) {
  const content = await fs.readFile(filePath, 'utf8');
  return JSON.parse(content);
}

async function resolveUrl(baseUrl, startUrl) {
  if (!startUrl) return baseUrl;
  if (/^(https?:|file:)/.test(startUrl)) return startUrl;
  if (!baseUrl) throw new Error(`Relative startUrl requires baseUrl. Got: ${startUrl}`);
  return new URL(startUrl, baseUrl).toString();
}

async function runStep(page, step) {
  switch (step.type) {
    case 'goto': {
      if (!step.url) throw new Error('goto step requires url');
      await page.goto(step.url, { waitUntil: step.waitUntil ?? 'load' });
      break;
    }
    case 'wait': {
      await page.waitForTimeout(step.ms ?? 500);
      break;
    }
    case 'click': {
      await page.locator(step.selector).click({ timeout: step.timeout ?? 10000 });
      break;
    }
    case 'dblclick': {
      await page.locator(step.selector).dblclick({ timeout: step.timeout ?? 10000 });
      break;
    }
    case 'fill': {
      await page.locator(step.selector).fill(step.value ?? '', { timeout: step.timeout ?? 10000 });
      break;
    }
    case 'press': {
      if (step.selector) {
        await page.locator(step.selector).press(step.key, { timeout: step.timeout ?? 10000 });
      } else {
        await page.keyboard.press(step.key);
      }
      break;
    }
    case 'hover': {
      await page.locator(step.selector).hover({ timeout: step.timeout ?? 10000 });
      break;
    }
    case 'scroll': {
      const x = step.x ?? 0;
      const y = step.y ?? 400;
      await page.mouse.wheel(x, y);
      break;
    }
    case 'evaluate': {
      if (!step.script) throw new Error('evaluate step requires script');
      await page.evaluate(step.script);
      break;
    }
    case 'screenshot': {
      if (!step.path) throw new Error('screenshot step requires path');
      await ensureDir(path.dirname(step.path));
      await page.screenshot({ path: step.path, fullPage: step.fullPage ?? false });
      break;
    }
    default:
      throw new Error(`Unsupported step type: ${step.type}`);
  }
}

async function moveFileSafe(fromPath, toPath) {
  if (fromPath === toPath) return;
  await ensureDir(path.dirname(toPath));
  try {
    await fs.rename(fromPath, toPath);
  } catch {
    await fs.copyFile(fromPath, toPath);
    await fs.unlink(fromPath);
  }
}

async function main() {
  const args = parseArgs(process.argv);
  const scenarioPath = path.resolve(args.scenario ?? './templates/scenario.example.json');
  const scenario = await readJson(scenarioPath);

  const outputDir = path.resolve(path.dirname(scenarioPath), scenario.outputDir ?? './output');
  const rawDir = path.join(outputDir, 'raw');
  const shotsDir = path.join(outputDir, 'shots');
  await ensureDir(rawDir);
  await ensureDir(shotsDir);

  const viewport = scenario.viewport ?? { width: 1440, height: 900 };
  const launchOptions = {
    headless: scenario.headless ?? true,
    slowMo: scenario.slowMoMs ?? 0,
  };

  const browser = await chromium.launch(launchOptions);
  const manifest = {
    projectName: scenario.projectName ?? 'demo-video',
    generatedAt: new Date().toISOString(),
    viewport,
    clips: [],
  };

  try {
    for (let i = 0; i < (scenario.scenes ?? []).length; i += 1) {
      const scene = scenario.scenes[i];
      const index = String(i + 1).padStart(2, '0');
      const id = sanitizeName(scene.id ?? scene.title ?? `scene-${index}`);
      const clipBaseName = `${index}-${id}`;
      const startUrl = await resolveUrl(scenario.baseUrl, scene.startUrl ?? scenario.baseUrl);

      const context = await browser.newContext({
        viewport,
        recordVideo: {
          dir: rawDir,
          size: { width: viewport.width, height: viewport.height },
        },
      });

      const page = await context.newPage();
      if (startUrl) {
        await page.goto(startUrl, { waitUntil: scene.waitUntil ?? 'load' });
      }

      if (scene.leadInMs) await page.waitForTimeout(scene.leadInMs);

      for (const step of scene.steps ?? []) {
        const stepCopy = { ...step };
        if (stepCopy.type === 'goto' && stepCopy.url) {
          stepCopy.url = await resolveUrl(scenario.baseUrl, stepCopy.url);
        }
        if (stepCopy.type === 'screenshot' && stepCopy.path) {
          stepCopy.path = path.resolve(shotsDir, stepCopy.path);
        }
        await runStep(page, stepCopy);
      }

      if (scene.tailMs) await page.waitForTimeout(scene.tailMs);

      const video = page.video();
      await context.close();
      const recordedPath = await video.path();
      const finalRawPath = path.join(rawDir, `${clipBaseName}.webm`);
      if (!(await exists(finalRawPath))) {
        await moveFileSafe(recordedPath, finalRawPath);
      }

      manifest.clips.push({
        index: i + 1,
        id,
        title: scene.title ?? id,
        rawPath: finalRawPath,
        startUrl,
        steps: scene.steps?.length ?? 0,
      });

      console.log(`Recorded ${clipBaseName}: ${finalRawPath}`);
    }
  } finally {
    await browser.close();
  }

  const manifestPath = path.join(outputDir, 'record-manifest.json');
  await fs.writeFile(manifestPath, JSON.stringify(manifest, null, 2), 'utf8');
  console.log(`Saved manifest: ${manifestPath}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
