# -*- coding: utf-8 -*-
"""
v3_css.py
Defines the cutting-edge aesthetic stylesheet for 远处 ELSEWHERE · 深空科学策展馆.
"""

CSS = """
/* ==========================================================================
   CSS VARIABLES & DESIGN TOKENS
   ========================================================================== */
:root {
  --bg-deep: #030407;
  --bg-card: rgba(14, 18, 27, 0.72);
  --bg-card-hover: rgba(22, 28, 42, 0.85);
  --bg-surface: #0a0d14;
  --line: rgba(255, 255, 255, 0.08);
  --line-strong: rgba(255, 255, 255, 0.18);
  --line-glow: rgba(255, 255, 255, 0.32);
  
  --fg-white: #f5f4ef;
  --fg-soft: #c8ceda;
  --fg-muted: #788194;
  --fg-subtle: #4d5464;
  
  --accent: #e26d40;
  --accent-soft: rgba(226, 109, 64, 0.12);
  --accent-glow: rgba(226, 109, 64, 0.3);
  
  --cyan: #38bdf8;
  --cyan-soft: rgba(56, 189, 248, 0.12);
  --cyan-glow: rgba(56, 189, 248, 0.28);
  
  --violet: #a78bfa;
  --violet-soft: rgba(167, 139, 250, 0.12);
  
  --font-serif: "New York", "Songti SC", "Source Han Serif CN", Georgia, serif;
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
  --font-mono: "SF Mono", ui-monospace, Menlo, Consolas, monospace;
  
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --glass-blur: blur(20px);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  background-color: var(--bg-deep);
  color: var(--fg-soft);
  font-family: var(--font-sans);
  font-size: 15px;
  line-height: 1.85;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  position: relative;
  background: transparent;
  overflow-x: hidden;
  min-height: 100vh;
}

/* Background Living Cosmos Canvas */
#starCanvas {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: -1;
  pointer-events: none;
  background: radial-gradient(circle at 50% 30%, #080b14 0%, #030407 85%);
}

/* Container Shell */
.shell {
  width: 100%;
  max-width: 1220px;
  margin: 0 auto;
  padding: 0 32px;
}

@media (max-width: 768px) {
  .shell {
    padding: 0 20px;
  }
}

/* Typography Foundation */
h1, h2, h3, h4 {
  color: var(--fg-white);
  font-weight: 380;
  letter-spacing: -0.015em;
  text-wrap: balance;
  overflow-wrap: break-word;
}

p {
  text-wrap: pretty;
  overflow-wrap: break-word;
}

a {
  color: inherit;
  text-decoration: none;
}

button {
  font-family: inherit;
  color: inherit;
  background: none;
  border: none;
  cursor: pointer;
}

/* Skip link */
.skip-link {
  position: absolute;
  top: -100px;
  left: 20px;
  padding: 8px 16px;
  background: var(--accent);
  color: #fff;
  z-index: 9999;
  border-radius: 4px;
}
.skip-link:focus {
  top: 20px;
}

/* Scroll progress */
.scroll-progress {
  position: fixed;
  top: 0;
  left: 0;
  height: 2px;
  width: 0%;
  background: linear-gradient(90deg, var(--accent), var(--cyan));
  z-index: 1000;
  transition: width 0.08s linear;
}

/* ==========================================================================
   SITE HEADER & LIVE TELEMETRY HUD
   ========================================================================== */
header.site-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(3, 4, 7, 0.82);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border-bottom: 1px solid var(--line);
}

.hud-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 5px 32px;
  background: rgba(0, 0, 0, 0.45);
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
  font-family: var(--font-mono);
  font-size: 10.5px;
  color: var(--fg-muted);
  letter-spacing: 0.06em;
}

.hud-items {
  display: flex;
  align-items: center;
  gap: 20px;
}

.hud-item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.hud-item .dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 6px #10b981;
  animation: pulseGreen 2.5s infinite;
}

@keyframes pulseGreen {
  0%, 100% { opacity: 0.6; }
  50% { opacity: 1; filter: drop-shadow(0 0 4px #10b981); }
}

.nav-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 60px;
}

.brand-wrap {
  display: flex;
  align-items: baseline;
  gap: 10px;
}
.brand {
  font-size: 17px;
  font-weight: 420;
  color: var(--fg-white);
  letter-spacing: 0.1em;
}
.brand-sub {
  font-size: 10.5px;
  font-family: var(--font-mono);
  color: var(--fg-muted);
  letter-spacing: 0.16em;
}

.nav-links {
  display: flex;
  gap: 22px;
}
.nav-links a {
  font-size: 13px;
  color: var(--fg-muted);
  transition: color 0.2s;
  letter-spacing: 0.02em;
}
.nav-links a:hover {
  color: var(--fg-white);
}

.header-controls {
  display: flex;
  align-items: center;
  gap: 10px;
}

.ctrl-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 5px 12px;
  border-radius: 99px;
  border: 1px solid var(--line-strong);
  font-size: 11.5px;
  font-family: var(--font-mono);
  color: var(--fg-soft);
  transition: all 0.2s;
  white-space: nowrap;
}
.ctrl-btn:hover {
  border-color: var(--accent);
  color: var(--fg-white);
  background: var(--accent-soft);
}
.ctrl-btn.active {
  border-color: var(--cyan);
  color: var(--cyan);
  background: var(--cyan-soft);
}

.nav-action {
  padding: 6px 14px;
  border-radius: 99px;
  border: 1px solid var(--line-strong);
  font-size: 12px;
  color: var(--fg-white);
  transition: all 0.2s;
  white-space: nowrap;
}
.nav-action:hover {
  border-color: var(--accent);
  background: var(--accent-soft);
}

@media (max-width: 900px) {
  .hud-bar {
    display: none;
  }
  .nav-links {
    display: none;
  }
  .brand-sub {
    display: none;
  }
}

/* ==========================================================================
   HALL 00: HERO COVER SHOWCASE
   ========================================================================== */
.hero {
  position: relative;
  min-height: 82vh;
  display: flex;
  align-items: center;
  padding: 64px 0 52px;
  border-bottom: 1px solid var(--line);
}

.hero-grid {
  display: grid;
  grid-template-columns: 1fr 1.15fr;
  gap: 64px;
  align-items: center;
}

.hero-intro {
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 4px 10px;
  border: 1px solid rgba(226, 109, 64, 0.35);
  background: rgba(226, 109, 64, 0.08);
  color: var(--accent);
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.12em;
  border-radius: 4px;
  width: fit-content;
}

.hero-title {
  font-size: 46px;
  line-height: 1.25;
  font-weight: 380;
  color: var(--fg-white);
}

.hero-lead {
  font-size: 16px;
  line-height: 1.9;
  color: var(--fg-soft);
  max-width: 520px;
}

.hero-actions {
  display: flex;
  gap: 14px;
  margin-top: 6px;
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 11px 24px;
  border-radius: 99px;
  background: var(--accent);
  color: #fff;
  font-size: 13.5px;
  font-weight: 450;
  letter-spacing: 0.03em;
  transition: all 0.25s var(--ease-out);
  box-shadow: 0 4px 20px var(--accent-glow);
}
.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 26px rgba(226, 109, 64, 0.45);
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 11px 24px;
  border-radius: 99px;
  border: 1px solid var(--line-strong);
  color: var(--fg-soft);
  font-size: 13.5px;
  letter-spacing: 0.03em;
  transition: all 0.2s;
  background: rgba(255, 255, 255, 0.02);
}
.btn-secondary:hover {
  border-color: var(--fg-white);
  color: var(--fg-white);
  background: rgba(255, 255, 255, 0.06);
}

.hero-caption {
  font-size: 11px;
  font-family: var(--font-mono);
  color: var(--fg-muted);
  line-height: 1.7;
  border-left: 1px solid var(--line-strong);
  padding-left: 12px;
  margin-top: 10px;
}

.hero-stage {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-celestial {
  width: 100%;
  max-width: 540px;
  aspect-ratio: 4 / 3;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero-celestial img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  filter: drop-shadow(0 0 60px rgba(210, 185, 140, 0.16));
  animation: heroDrift 28s ease-in-out infinite alternate;
}

@keyframes heroDrift {
  0% { transform: translateY(0px) rotate(0deg); }
  100% { transform: translateY(-10px) rotate(-1.5deg); }
}

/* Fast Exhibition Jump Dock */
.tour-route {
  border-bottom: 1px solid var(--line);
  background: #06080d;
  padding: 18px 0;
}
.route-list {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}
.route-item {
  display: flex;
  flex-direction: column;
  padding: 12px 16px;
  border-radius: 8px;
  border: 1px solid var(--line);
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  transition: all 0.2s var(--ease-out);
}
.route-item:hover {
  border-color: var(--accent);
  background: var(--bg-card-hover);
  transform: translateY(-2px);
}
.route-idx {
  font-size: 10px;
  font-family: var(--font-mono);
  color: var(--accent);
  letter-spacing: 0.14em;
  margin-bottom: 4px;
}
.route-name {
  font-size: 14px;
  color: var(--fg-white);
  font-weight: 420;
}
.route-sub {
  font-size: 11.5px;
  color: var(--fg-muted);
}

@media (max-width: 900px) {
  .hero-grid {
    grid-template-columns: 1fr;
    gap: 36px;
  }
  .hero-stage {
    order: -1;
  }
  .hero-celestial {
    max-width: 380px;
    margin: 0 auto;
  }
  .hero-title {
    font-size: 34px;
  }
  .route-list {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (max-width: 520px) {
  .route-list {
    grid-template-columns: 1fr;
  }
}

/* ==========================================================================
   CHAPTER COMMON STYLES
   ========================================================================== */
.chapter {
  padding: 96px 0;
  border-bottom: 1px solid var(--line);
  position: relative;
}

.section-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 48px;
  gap: 32px;
}

.section-badge {
  font-size: 11px;
  font-family: var(--font-mono);
  color: var(--accent);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  margin-bottom: 12px;
}
.section-badge.cyan {
  color: var(--cyan);
}
.section-badge.violet {
  color: var(--violet);
}

.section-title {
  font-size: 32px;
  line-height: 1.35;
  font-weight: 380;
  color: var(--fg-white);
}

.section-desc {
  max-width: 480px;
  font-size: 14.5px;
  line-height: 1.85;
  color: var(--fg-muted);
}

@media (max-width: 800px) {
  .section-head {
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
    margin-bottom: 32px;
  }
  .section-title {
    font-size: 26px;
  }
}

/* ==========================================================================
   HALL 01: PLANETS EXHIBIT (#solar - SPECIMEN PLINTH)
   ========================================================================== */
.planet-exhibit {
  background: #05070c;
}

.planet-rail {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding-bottom: 12px;
  margin-bottom: 36px;
  scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
}
.planet-rail::-webkit-scrollbar {
  display: none;
}

.planet-tab {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border-radius: 99px;
  border: 1px solid var(--line);
  background: var(--bg-card);
  color: var(--fg-muted);
  font-size: 13px;
  letter-spacing: 0.02em;
  transition: all 0.2s var(--ease-out);
}
.planet-tab span.num {
  font-family: var(--font-mono);
  font-size: 10px;
  color: var(--fg-subtle);
}
.planet-tab:hover {
  border-color: var(--line-strong);
  color: var(--fg-white);
}
.planet-tab[aria-pressed="true"] {
  border-color: var(--accent);
  background: var(--accent);
  color: #fff;
}
.planet-tab[aria-pressed="true"] span.num {
  color: rgba(255, 255, 255, 0.8);
}

.plinth-stage {
  display: grid;
  grid-template-columns: 1.15fr 1fr;
  gap: 48px;
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 48px;
  align-items: center;
}

.plinth-visual {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 420px;
}

.orbit-accent {
  position: absolute;
  width: 90%;
  aspect-ratio: 1 / 1;
  border: 1px dashed rgba(255, 255, 255, 0.09);
  border-radius: 50%;
  pointer-events: none;
  animation: orbitRotate 90s linear infinite;
}

@keyframes orbitRotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.planet-disc-wrap {
  position: relative;
  width: 320px;
  aspect-ratio: 1 / 1;
  display: flex;
  align-items: center;
  justify-content: center;
}
.planet-disc-wrap img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  transition: opacity 0.35s ease, transform 0.35s ease;
  filter: drop-shadow(0 0 45px rgba(255, 255, 255, 0.12));
}

.specimen-tag {
  position: absolute;
  bottom: 12px;
  left: 20px;
  font-family: var(--font-mono);
  font-size: 10px;
  color: var(--fg-muted);
  letter-spacing: 0.16em;
  background: rgba(0, 0, 0, 0.6);
  padding: 3px 8px;
  border-radius: 3px;
  border: 1px solid var(--line);
}

.plinth-dossier {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.dossier-header .planet-en {
  font-size: 11px;
  font-family: var(--font-mono);
  color: var(--accent);
  letter-spacing: 0.16em;
  margin-bottom: 4px;
}
.dossier-header .planet-name {
  font-size: 34px;
  font-weight: 380;
  color: var(--fg-white);
}

.planet-intro {
  font-size: 15px;
  line-height: 1.85;
  color: var(--fg-soft);
}

.planet-metadata-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  padding: 16px 0;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
}

.meta-box {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.meta-box span {
  font-size: 11px;
  font-family: var(--font-mono);
  color: var(--fg-muted);
}
.meta-box strong {
  font-size: 16px;
  font-weight: 420;
  color: var(--fg-white);
}

.atmosphere-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 4px;
}
.atmos-tag {
  font-size: 10.5px;
  font-family: var(--font-mono);
  padding: 2px 7px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--line);
  border-radius: 3px;
  color: var(--fg-soft);
}

.planet-wonder {
  background: rgba(255, 255, 255, 0.02);
  border-left: 2px solid var(--accent);
  padding: 14px 18px;
  border-radius: 0 6px 6px 0;
  font-size: 13.5px;
  line-height: 1.8;
  color: var(--fg-soft);
}

.dossier-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
  color: var(--fg-muted);
}
.dossier-footer a {
  color: var(--fg-soft);
  border-bottom: 1px solid var(--line-strong);
  padding-bottom: 2px;
  transition: color 0.2s, border-color 0.2s;
}
.dossier-footer a:hover {
  color: var(--accent);
  border-color: var(--accent);
}

@media (max-width: 900px) {
  .plinth-stage {
    grid-template-columns: 1fr;
    padding: 24px;
    gap: 32px;
  }
  .plinth-visual {
    min-height: 280px;
  }
  .planet-disc-wrap {
    width: 240px;
  }
}

/* ==========================================================================
   HALL 02: MOONS CABINET (#moons - COLLECTION TRAY)
   ========================================================================== */
.moons-cabinet {
  background: #040508;
}

.collection-tray {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 16px;
  margin-bottom: 36px;
}

.specimen-card {
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 24px 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  text-align: center;
  cursor: pointer;
  transition: all 0.25s var(--ease-out);
  position: relative;
}
.specimen-card:hover {
  border-color: var(--line-strong);
  background: var(--bg-card-hover);
  transform: translateY(-2px);
}
.specimen-card[aria-pressed="true"] {
  border-color: var(--accent);
  background: rgba(226, 109, 64, 0.05);
}
.specimen-card[aria-pressed="true"]::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 20%;
  right: 20%;
  height: 2px;
  background: var(--accent);
}

.specimen-sphere {
  width: 100px;
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}
.specimen-sphere img {
  border-radius: 50%;
  object-fit: cover;
  filter: drop-shadow(0 0 16px rgba(255, 255, 255, 0.1));
}

.specimen-info strong {
  font-size: 15px;
  color: var(--fg-white);
  font-weight: 420;
}
.specimen-info span {
  font-size: 11px;
  font-family: var(--font-mono);
  color: var(--fg-muted);
}

.moon-dossier {
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 32px;
  display: grid;
  grid-template-columns: 1fr 1.6fr;
  gap: 36px;
  align-items: center;
  margin-bottom: 40px;
}
.dossier-left .moon-en {
  font-size: 11px;
  font-family: var(--font-mono);
  color: var(--accent);
  letter-spacing: 0.16em;
  margin-bottom: 6px;
}
.dossier-left h3 {
  font-size: 24px;
  font-weight: 380;
  margin-bottom: 10px;
}
.dossier-stats {
  font-size: 12px;
  font-family: var(--font-mono);
  color: var(--fg-muted);
}

.dossier-right p {
  font-size: 14.5px;
  line-height: 1.85;
  color: var(--fg-soft);
  margin-bottom: 12px;
}

/* Lunar Phase Lab */
.phase-lab {
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 40px;
}
.phase-lab-grid {
  display: grid;
  grid-template-columns: 240px 1fr;
  gap: 48px;
  align-items: center;
}

.phase-viewport {
  position: relative;
  width: 220px;
  height: 220px;
  margin: 0 auto;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 0 35px rgba(255, 255, 255, 0.08);
}
.phase-base-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
#phaseCanvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.phase-controls {
  display: flex;
  flex-direction: column;
  gap: 18px;
}
.phase-tag {
  font-size: 11px;
  font-family: var(--font-mono);
  color: var(--accent);
  letter-spacing: 0.16em;
}
.phase-controls h3 {
  font-size: 24px;
  font-weight: 380;
}
.phase-controls p {
  font-size: 14px;
  color: var(--fg-muted);
  line-height: 1.8;
}

.phase-slider-wrap {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 16px 0;
}
.phase-slider-wrap label {
  display: flex;
  justify-content: space-between;
  font-size: 12.5px;
  font-family: var(--font-mono);
  color: var(--fg-soft);
}
.phase-slider {
  width: 100%;
  height: 6px;
  background: var(--line-strong);
  border-radius: 99px;
  outline: none;
  -webkit-appearance: none;
  cursor: pointer;
}
.phase-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 10px var(--accent-glow);
  cursor: pointer;
  transition: transform 0.15s;
}
.phase-slider::-webkit-slider-thumb:hover {
  transform: scale(1.25);
}

.phase-presets {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}
.preset-btn {
  padding: 6px 14px;
  border-radius: 99px;
  border: 1px solid var(--line);
  background: rgba(255, 255, 255, 0.02);
  font-size: 12px;
  color: var(--fg-muted);
  transition: all 0.2s;
}
.preset-btn:hover {
  border-color: var(--line-strong);
  color: var(--fg-white);
}
.preset-btn[aria-pressed="true"] {
  border-color: var(--accent);
  background: var(--accent);
  color: #fff;
}

@media (max-width: 860px) {
  .collection-tray {
    display: flex;
    gap: 12px;
    overflow-x: auto;
    padding-bottom: 12px;
    scrollbar-width: none;
  }
  .specimen-card {
    flex: 0 0 140px;
  }
  .moon-dossier {
    grid-template-columns: 1fr;
    padding: 24px;
  }
  .phase-lab-grid {
    grid-template-columns: 1fr;
    gap: 32px;
  }
}

/* ==========================================================================
   HALL 03: STARS LIFECYCLE & SPECTRAL TYPES (#stars)
   ========================================================================== */
.stars-chapter {
  background: #06080e;
}

.stellar-storyline {
  display: flex;
  position: relative;
  margin-bottom: 36px;
}
.stellar-storyline::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 5%;
  right: 5%;
  height: 1px;
  background: var(--line-strong);
  z-index: 1;
}

.stellar-steps {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 12px;
  width: 100%;
  position: relative;
  z-index: 2;
}

.step-node {
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 16px 14px;
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 4px;
  transition: all 0.25s var(--ease-out);
}
.step-node:hover {
  border-color: var(--line-strong);
  background: var(--bg-card-hover);
  transform: translateY(-2px);
}
.step-node[aria-pressed="true"] {
  border-color: var(--accent);
  background: rgba(226, 109, 64, 0.08);
}
.step-num {
  font-size: 10px;
  font-family: var(--font-mono);
  color: var(--accent);
  letter-spacing: 0.12em;
}
.step-name {
  font-size: 13.5px;
  color: var(--fg-white);
  font-weight: 420;
}

.stellar-stage-box {
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 48px;
  display: grid;
  grid-template-columns: 1fr 1.25fr;
  gap: 48px;
  align-items: center;
  margin-bottom: 40px;
}

.stellar-visual-well {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 280px;
}

.star-morph {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  transition: all 0.6s var(--ease-out);
  position: relative;
}

/* State 0: Birth Cloud */
.star-state-0 {
  width: 180px;
  height: 180px;
  background: radial-gradient(circle, #e26d40 0%, #85371b 45%, rgba(60, 20, 10, 0.2) 70%, transparent 100%);
  filter: blur(14px);
  animation: starPulse 6s ease-in-out infinite;
}
/* State 1: Main Sequence */
.star-state-1 {
  width: 140px;
  height: 140px;
  background: radial-gradient(circle, #ffffff 0%, #ffdf9e 40%, #e27d3b 75%, transparent 100%);
  box-shadow: 0 0 70px rgba(255, 200, 120, 0.6), 0 0 120px rgba(226, 125, 59, 0.3);
  animation: starFlicker 3s ease-in-out infinite alternate;
}
/* State 2: Red Giant */
.star-state-2 {
  width: 220px;
  height: 220px;
  background: radial-gradient(circle, #ff9b71 0%, #d83a1e 50%, #751406 80%, transparent 100%);
  box-shadow: 0 0 85px rgba(216, 58, 30, 0.5), 0 0 140px rgba(117, 20, 6, 0.35);
  animation: giantBreathe 7s ease-in-out infinite alternate;
}
/* State 3: Supernova / Planetary */
.star-state-3 {
  width: 210px;
  height: 210px;
  background: radial-gradient(circle, #ffffff 0%, #38bdf8 30%, #a78bfa 60%, rgba(226, 109, 64, 0.4) 85%, transparent 100%);
  box-shadow: 0 0 90px rgba(56, 189, 248, 0.6), 0 0 150px rgba(167, 139, 250, 0.4);
  animation: novaGlow 4s ease-in-out infinite alternate;
}
/* State 4: White Dwarf / Neutron Star */
.star-state-4 {
  width: 48px;
  height: 48px;
  background: #ffffff;
  box-shadow: 0 0 35px #ffffff, 0 0 80px rgba(56, 189, 248, 0.9), 0 0 140px rgba(167, 139, 250, 0.5);
  animation: dwarfBeaming 2s ease-in-out infinite alternate;
}

@keyframes starPulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.08); } }
@keyframes starFlicker { 0% { transform: scale(1); } 100% { transform: scale(1.03); } }
@keyframes giantBreathe { 0% { transform: scale(1); } 100% { transform: scale(1.06); } }
@keyframes novaGlow { 0% { transform: scale(0.96); filter: hue-rotate(0deg); } 100% { transform: scale(1.05); filter: hue-rotate(25deg); } }
@keyframes dwarfBeaming { 0% { transform: scale(1); box-shadow: 0 0 30px #fff; } 100% { transform: scale(1.15); box-shadow: 0 0 60px #38bdf8; } }

.stellar-narrative {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.stage-tag {
  font-size: 11px;
  font-family: var(--font-mono);
  color: var(--accent);
  letter-spacing: 0.16em;
}
.stellar-narrative h3 {
  font-size: 28px;
  font-weight: 380;
}
.story-text {
  font-size: 15px;
  line-height: 1.9;
  color: var(--fg-soft);
}
.stellar-fact {
  background: rgba(255, 255, 255, 0.02);
  border-left: 2px solid var(--accent);
  padding: 12px 18px;
  border-radius: 0 6px 6px 0;
  font-size: 13.5px;
  line-height: 1.8;
  color: var(--fg-soft);
}

/* Harvard Spectral Class Interactive Selector */
.spectral-lab {
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 36px;
}
.spectral-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 24px;
}
.spectral-head h3 {
  font-size: 20px;
  font-weight: 380;
}
.spectral-head span {
  font-size: 11.5px;
  font-family: var(--font-mono);
  color: var(--fg-muted);
}

.spectral-buttons {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 8px;
  margin-bottom: 24px;
}
.spec-btn {
  padding: 10px 4px;
  border-radius: 6px;
  border: 1px solid var(--line);
  background: rgba(255, 255, 255, 0.02);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  transition: all 0.2s;
}
.spec-btn strong {
  font-size: 18px;
  font-family: var(--font-mono);
}
.spec-btn span {
  font-size: 10px;
  font-family: var(--font-mono);
  color: var(--fg-muted);
}
.spec-btn:hover {
  border-color: var(--line-strong);
  background: rgba(255, 255, 255, 0.06);
}
.spec-btn[aria-pressed="true"] {
  border-color: var(--cyan);
  background: rgba(56, 189, 248, 0.1);
  color: #fff;
}

.spec-info-box {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  padding: 16px;
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid var(--line);
  border-radius: 8px;
}

@media (max-width: 860px) {
  .stellar-steps {
    grid-template-columns: repeat(2, 1fr);
  }
  .stellar-storyline::before {
    display: none;
  }
  .stellar-stage-box {
    grid-template-columns: 1fr;
    padding: 24px;
    gap: 32px;
  }
  .spectral-buttons {
    grid-template-columns: repeat(4, 1fr);
  }
  .spec-info-box {
    grid-template-columns: 1fr;
  }
}

/* ==========================================================================
   HALL 04: NEBULA & MULTI-WAVELENGTH EXHIBIT (#nebula)
   ========================================================================== */
.nebula-exhibit {
  background: #05060b;
}

.panoramic-frame {
  position: relative;
  width: 100%;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid var(--line);
  background: #020306;
  margin-bottom: 24px;
}
.panoramic-img {
  width: 100%;
  height: auto;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  display: block;
  transition: filter 0.5s ease;
}

.hotspot-pin {
  position: absolute;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: rgba(5, 6, 8, 0.82);
  border: 1.5px solid var(--accent);
  color: var(--accent);
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transform: translate(-50%, -50%);
  transition: all 0.2s var(--ease-out);
  box-shadow: 0 0 14px rgba(226, 109, 64, 0.45);
}
.hotspot-pin:hover, .hotspot-pin[aria-pressed="true"] {
  transform: translate(-50%, -50%) scale(1.2);
  background: var(--accent);
  color: #fff;
  box-shadow: 0 0 24px rgba(226, 109, 64, 0.85);
}

.pin-1 { top: 62%; left: 34%; }
.pin-2 { top: 48%; left: 65%; }
.pin-3 { top: 74%; left: 76%; }

.nebula-analysis {
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 32px;
  display: grid;
  grid-template-columns: 1fr 1.6fr;
  gap: 36px;
  align-items: center;
  margin-bottom: 36px;
}
.analysis-meta .ana-idx {
  font-size: 11px;
  font-family: var(--font-mono);
  color: var(--accent);
  letter-spacing: 0.16em;
  margin-bottom: 4px;
}
.analysis-meta h3 {
  font-size: 26px;
  font-weight: 380;
}
.ana-guide {
  font-size: 12px;
  font-family: var(--font-mono);
  color: var(--cyan);
  margin-top: 10px;
}
.analysis-content p {
  font-size: 15px;
  line-height: 1.9;
  color: var(--fg-soft);
}

/* Multi-Wavelength Spectrum Explorer */
.wavelength-console {
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 32px;
}
.wavelength-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 20px;
}
.wavelength-head h3 {
  font-size: 20px;
  font-weight: 380;
}
.wave-nav {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 20px;
}
.wave-btn {
  padding: 8px 16px;
  border-radius: 99px;
  border: 1px solid var(--line);
  background: rgba(255, 255, 255, 0.02);
  font-size: 12.5px;
  color: var(--fg-muted);
  transition: all 0.2s;
}
.wave-btn:hover {
  border-color: var(--line-strong);
  color: var(--fg-white);
}
.wave-btn[aria-pressed="true"] {
  border-color: var(--cyan);
  background: var(--cyan-soft);
  color: var(--cyan);
}
.wave-explainer {
  font-size: 14px;
  color: var(--fg-soft);
  line-height: 1.85;
  padding: 16px;
  background: rgba(0, 0, 0, 0.35);
  border-radius: 6px;
  border-left: 2px solid var(--cyan);
}

@media (max-width: 800px) {
  .nebula-analysis {
    grid-template-columns: 1fr;
    padding: 24px;
  }
}

/* ==========================================================================
   HALL 05: BLACK HOLES & GRAVITATIONAL LENSING (#blackhole - BRAND NEW)
   ========================================================================== */
.blackhole-chapter {
  background: #020306;
}

.bh-grid {
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  gap: 48px;
  align-items: center;
  margin-bottom: 48px;
}

.bh-image-box {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid var(--line);
  background: #000;
  box-shadow: 0 0 50px rgba(226, 109, 64, 0.15);
}
.bh-image-box img {
  width: 100%;
  height: auto;
  display: block;
}
.bh-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(180deg, transparent, rgba(0, 0, 0, 0.85));
  padding: 16px 20px;
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--fg-muted);
}

.bh-dossier {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.bh-dossier h3 {
  font-size: 28px;
  font-weight: 380;
}
.bh-dossier p {
  font-size: 15px;
  line-height: 1.85;
  color: var(--fg-soft);
}

.physics-cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}
.phys-card {
  background: var(--bg-card);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 16px;
}
.phys-card .formula {
  font-family: var(--font-mono);
  font-size: 13.5px;
  color: var(--cyan);
  margin-bottom: 4px;
}
.phys-card span {
  font-size: 12px;
  color: var(--fg-muted);
  line-height: 1.6;
  display: block;
}

/* Gravitational Lensing Interactive Simulator */
.lensing-lab {
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 40px;
}
.lensing-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 20px;
}
.lensing-head h3 {
  font-size: 22px;
  font-weight: 380;
}
.lensing-canvas-wrap {
  position: relative;
  width: 100%;
  height: 380px;
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid var(--line-strong);
  background: #010204;
  cursor: crosshair;
}
#lensCanvas {
  width: 100%;
  height: 100%;
  display: block;
}
.lens-instructions {
  position: absolute;
  top: 16px;
  left: 16px;
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--cyan);
  background: rgba(3, 4, 7, 0.75);
  padding: 4px 10px;
  border-radius: 4px;
  border: 1px solid var(--line);
  pointer-events: none;
}

@media (max-width: 860px) {
  .bh-grid {
    grid-template-columns: 1fr;
    gap: 32px;
  }
  .physics-cards {
    grid-template-columns: 1fr;
  }
  .lensing-canvas-wrap {
    height: 280px;
  }
}

/* ==========================================================================
   HALL 06: EXOPLANETS & TRANSIT LAB (#exoplanet - BRAND NEW)
   ========================================================================== */
.exoplanet-chapter {
  background: #05070d;
}

.trappist-banner {
  position: relative;
  width: 100%;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid var(--line);
  margin-bottom: 36px;
}
.trappist-banner img {
  width: 100%;
  height: auto;
  display: block;
}

.transit-lab {
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 40px;
}
.transit-grid {
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  gap: 40px;
  align-items: center;
}

.transit-visual-box {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.transit-stage {
  position: relative;
  width: 100%;
  height: 180px;
  background: #010205;
  border-radius: 8px;
  border: 1px solid var(--line);
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.host-star {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: radial-gradient(circle, #fff 0%, #ff8b54 60%, #9e2b0e 90%);
  box-shadow: 0 0 50px rgba(255, 139, 84, 0.7);
}

.transit-planet {
  position: absolute;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: #000;
  border: 1px solid rgba(255, 255, 255, 0.2);
  top: calc(50% - 11px);
  animation: transitPass 6s linear infinite;
}

@keyframes transitPass {
  0% { left: -30px; }
  100% { left: 100%; }
}

.transit-curve-box {
  position: relative;
  width: 100%;
  height: 120px;
  background: rgba(0, 0, 0, 0.4);
  border-radius: 8px;
  border: 1px solid var(--line);
}
#curveCanvas {
  width: 100%;
  height: 100%;
  display: block;
}

.transit-details {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.transit-details h3 {
  font-size: 26px;
  font-weight: 380;
}
.transit-details p {
  font-size: 14.5px;
  line-height: 1.85;
  color: var(--fg-soft);
}

.spectral-bars {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 8px;
}
.spec-bar-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.spec-bar-label {
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  font-family: var(--font-mono);
  color: var(--fg-muted);
}
.spec-bar-track {
  width: 100%;
  height: 6px;
  background: var(--line-strong);
  border-radius: 99px;
  overflow: hidden;
}
.spec-bar-fill {
  height: 100%;
  border-radius: 99px;
}
.spec-bar-fill.h2o { width: 78%; background: var(--cyan); }
.spec-bar-fill.ch4 { width: 52%; background: var(--accent); }
.spec-bar-fill.co2 { width: 92%; background: var(--violet); }

@media (max-width: 860px) {
  .transit-grid {
    grid-template-columns: 1fr;
    gap: 32px;
  }
}

/* ==========================================================================
   HALL 07: SCALE & DEEP SPACE FLEET (#distance)
   ========================================================================== */
.distance-chapter {
  background: #030408;
}

.scale-console {
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 48px;
  margin-bottom: 48px;
}

.dest-buttons {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 40px;
}

.dest-btn {
  padding: 8px 18px;
  border-radius: 99px;
  border: 1px solid var(--line);
  background: rgba(255, 255, 255, 0.02);
  color: var(--fg-muted);
  font-size: 13px;
  transition: all 0.2s var(--ease-out);
}
.dest-btn:hover {
  border-color: var(--line-strong);
  color: var(--fg-white);
}
.dest-btn[aria-pressed="true"] {
  border-color: var(--accent);
  background: var(--accent-soft);
  color: var(--accent);
}

.scale-readout {
  display: grid;
  grid-template-columns: 1fr 1.6fr;
  gap: 48px;
  align-items: center;
  margin-bottom: 40px;
}

.time-monument {
  display: flex;
  align-items: baseline;
  gap: 8px;
}
.time-number {
  font-size: 80px;
  line-height: 1;
  font-weight: 280;
  color: var(--fg-white);
  font-family: var(--font-mono);
  letter-spacing: -0.04em;
}
.time-unit {
  font-size: 24px;
  color: var(--accent);
  font-family: var(--font-mono);
}

.dest-details h3 {
  font-size: 26px;
  font-weight: 380;
  margin-bottom: 12px;
}
.dest-details p {
  font-size: 15px;
  line-height: 1.85;
  color: var(--fg-soft);
}

/* Light Journey Tracker Line */
.light-journey-line {
  position: relative;
  width: 100%;
  height: 1px;
  background: var(--line-strong);
  margin-top: 24px;
}
.photon-beam {
  position: absolute;
  top: -2px;
  left: 0;
  width: 6px;
  height: 5px;
  border-radius: 50%;
  background: #ffffff;
  box-shadow: 0 0 10px var(--accent), 0 0 20px #fff;
  animation: photonTravel 7s linear infinite;
}

@keyframes photonTravel {
  0% { left: 0%; opacity: 0; }
  10% { opacity: 1; }
  90% { opacity: 1; }
  100% { left: 100%; opacity: 0; }
}

/* Deep Space Fleet Timeline */
.fleet-section {
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 40px;
}
.fleet-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 24px;
}
.fleet-head h3 {
  font-size: 22px;
  font-weight: 380;
}
.fleet-tabs {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding-bottom: 8px;
  margin-bottom: 28px;
  scrollbar-width: none;
}
.fleet-tab {
  padding: 7px 16px;
  border-radius: 99px;
  border: 1px solid var(--line);
  background: rgba(255, 255, 255, 0.02);
  font-size: 12px;
  font-family: var(--font-mono);
  color: var(--fg-muted);
  white-space: nowrap;
  transition: all 0.2s;
}
.fleet-tab:hover {
  border-color: var(--line-strong);
  color: var(--fg-white);
}
.fleet-tab[aria-pressed="true"] {
  border-color: var(--cyan);
  background: var(--cyan-soft);
  color: var(--cyan);
}

.fleet-dossier-box {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 36px;
  align-items: center;
}
.fleet-img-wrap {
  width: 100%;
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid var(--line);
}
.fleet-img-wrap img {
  width: 100%;
  height: auto;
  display: block;
}

@media (max-width: 860px) {
  .scale-readout {
    grid-template-columns: 1fr;
    gap: 24px;
  }
  .time-number {
    font-size: 56px;
  }
  .fleet-dossier-box {
    grid-template-columns: 1fr;
  }
}

/* ==========================================================================
   HALL 08: STARGAZING, BORTLE SIMULATOR & FIELD NOTES (#observe)
   ========================================================================== */
.observe-chapter {
  background: #05060a;
}

.bortle-lab {
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 40px;
  margin-bottom: 40px;
}
.bortle-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 20px;
}
.bortle-head h3 {
  font-size: 22px;
  font-weight: 380;
}
.bortle-viewport {
  position: relative;
  width: 100%;
  height: 220px;
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid var(--line);
  background: #0a0d16;
  margin-bottom: 20px;
}
#bortleCanvas {
  width: 100%;
  height: 100%;
  display: block;
}

.bortle-slider-wrap {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 16px;
}
.bortle-slider-wrap label {
  display: flex;
  justify-content: space-between;
  font-family: var(--font-mono);
  font-size: 13px;
  color: var(--fg-soft);
}

.bortle-desc-box {
  background: rgba(0, 0, 0, 0.4);
  padding: 16px 20px;
  border-radius: 6px;
  border-left: 2px solid var(--accent);
  font-size: 13.5px;
  line-height: 1.8;
  color: var(--fg-soft);
}

.prep-grid {
  display: grid;
  grid-template-columns: 1fr 1.3fr;
  gap: 40px;
  margin-bottom: 48px;
}

.checklist-panel, .notes-panel {
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 36px;
}

.checklist-panel h3, .notes-panel h3 {
  font-size: 20px;
  font-weight: 380;
  margin-bottom: 20px;
}

.check-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 12px 0;
  border-bottom: 1px solid var(--line);
  cursor: pointer;
}
.check-item input[type="checkbox"] {
  margin-top: 5px;
  accent-color: var(--accent);
  width: 16px;
  height: 16px;
  cursor: pointer;
}
.check-item strong {
  display: block;
  font-size: 14.5px;
  color: var(--fg-white);
  font-weight: 420;
}
.check-item span {
  font-size: 12.5px;
  color: var(--fg-muted);
  line-height: 1.6;
}

.note-textarea {
  width: 100%;
  min-height: 160px;
  background: rgba(0, 0, 0, 0.5);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 16px;
  color: var(--fg-white);
  font-family: inherit;
  font-size: 14px;
  line-height: 1.8;
  resize: vertical;
  margin-bottom: 16px;
  outline: none;
  transition: border-color 0.2s;
}
.note-textarea:focus {
  border-color: var(--accent);
}

.note-actions {
  display: flex;
  gap: 10px;
  align-items: center;
  flex-wrap: wrap;
}
.note-status {
  font-size: 11.5px;
  font-family: var(--font-mono);
  color: var(--cyan);
}

@media (max-width: 860px) {
  .prep-grid {
    grid-template-columns: 1fr;
  }
}

/* ==========================================================================
   HALL 09: SCIENTIFIC INTUITION LAB (#quiz)
   ========================================================================== */
.quiz-chapter {
  background: #030509;
}

.quiz-box {
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 48px;
  max-width: 860px;
  margin: 0 auto;
}

.quiz-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  border-bottom: 1px solid var(--line);
  padding-bottom: 16px;
  margin-bottom: 28px;
}
.quiz-meta {
  font-size: 12px;
  font-family: var(--font-mono);
  color: var(--accent);
  letter-spacing: 0.1em;
}

.quiz-question {
  font-size: 22px;
  font-weight: 380;
  color: var(--fg-white);
  margin-bottom: 28px;
}

.quiz-options {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 28px;
}

.quiz-opt-btn {
  text-align: left;
  padding: 14px 20px;
  border-radius: 8px;
  border: 1px solid var(--line);
  background: rgba(0, 0, 0, 0.4);
  color: var(--fg-soft);
  font-size: 14.5px;
  transition: all 0.2s;
}
.quiz-opt-btn:hover {
  border-color: var(--line-strong);
  background: rgba(255, 255, 255, 0.03);
}
.quiz-opt-btn[aria-pressed="true"] {
  border-color: var(--accent);
  background: rgba(226, 109, 64, 0.08);
  color: var(--fg-white);
}

.quiz-feedback {
  background: rgba(255, 255, 255, 0.02);
  border-left: 2px solid var(--accent);
  padding: 16px 20px;
  border-radius: 0 8px 8px 0;
  font-size: 14px;
  line-height: 1.85;
  color: #dfdcd5;
  margin-bottom: 28px;
}

.quiz-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

@media (max-width: 600px) {
  .quiz-box {
    padding: 24px;
  }
}

/* ==========================================================================
   SITE FOOTER
   ========================================================================== */
footer.site-footer {
  padding: 64px 0;
  border-top: 1px solid var(--line);
  background: #020306;
  font-size: 12.5px;
  color: var(--fg-muted);
}
.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr;
  gap: 40px;
  margin-bottom: 40px;
}
.footer-brand h4 {
  font-size: 16px;
  color: var(--fg-white);
  margin-bottom: 8px;
}
.footer-brand p {
  font-size: 13px;
  line-height: 1.8;
  max-width: 420px;
}
.footer-col h5 {
  font-size: 11px;
  font-family: var(--font-mono);
  color: var(--accent);
  letter-spacing: 0.16em;
  margin-bottom: 12px;
  text-transform: uppercase;
}
.footer-col ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.footer-col a:hover {
  color: var(--fg-white);
}
.footer-bottom {
  display: flex;
  justify-content: space-between;
  padding-top: 24px;
  border-top: 1px solid var(--line);
  font-family: var(--font-mono);
  font-size: 11px;
}

@media (max-width: 768px) {
  .footer-grid {
    grid-template-columns: 1fr;
    gap: 28px;
  }
  .footer-bottom {
    flex-direction: column;
    gap: 12px;
  }
}

/* ==========================================================================
   REDUCED MOTION SUPPORT
   ========================================================================== */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.001ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.001ms !important;
  }
}

html.reduced-motion *,
html.reduced-motion *::before,
html.reduced-motion *::after {
  animation-duration: 0.001ms !important;
  animation-iteration-count: 1 !important;
  transition-duration: 0.001ms !important;
}
"""
