# -*- coding: utf-8 -*-
"""
v3_html.py
Generates the semantic HTML body for 远处 ELSEWHERE · 深空科学策展馆.
"""

def get_html(b64):
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>远处 · 深空科学策展馆 — 探索更辽阔的世界</title>
<meta name="description" content="一座运行于浏览器端的美术馆级深空天文学展馆。沉浸探索太阳系行星、冰下海洋卫星、恒星生命史、韦布多波段星云、M87*超大质量黑洞与引力透镜、系外宜居行星及人类深空探测舰队。">
<style>
/* CSS will be injected here */
</style>
</head>
<body>

<canvas id="starCanvas"></canvas>
<a class="skip-link" href="#solar">跳至主要展览</a>
<div class="scroll-progress" id="scrollProgress" aria-hidden="true"></div>

<!-- SITE HEADER WITH LIVE TELEMETRY HUD -->
<header class="site-header">
  <div class="hud-bar">
    <div class="hud-items">
      <span class="hud-item"><span class="dot"></span> 实时遥测链路正常</span>
      <span class="hud-item" id="hudCoords">天球坐标 RA 17h 45m 40s · DEC -29°00′28″</span>
      <span class="hud-item" id="hudWind">太阳风速 438 km/s</span>
      <span class="hud-item">日地 L2 延迟 5.1s</span>
    </div>
    <div class="hud-clock" id="hudUtc">2026.10.28 07:28:00 UTC</div>
  </div>

  <div class="shell nav-bar">
    <div class="brand-wrap">
      <a class="brand" href="#">远处 ELSEWHERE</a>
      <span class="brand-sub">深空策展馆</span>
    </div>

    <nav class="nav-links" aria-label="主展区导航">
      <a href="#solar">01 行星</a>
      <a href="#moons">02 卫星</a>
      <a href="#stars">03 恒星</a>
      <a href="#nebula">04 星云</a>
      <a href="#blackhole">05 黑洞</a>
      <a href="#exoplanet">06 系外</a>
      <a href="#distance">07 尺度</a>
      <a href="#observe">08 观星</a>
    </nav>

    <div class="header-controls">
      <button class="ctrl-btn" id="audioToggle" aria-label="切换氛围音效">🔊 氛围原声: 关</button>
      <button class="ctrl-btn" id="motionToggle" aria-label="切换动效设置">动效: 开</button>
      <a class="nav-action" href="#quiz">直觉测验 ↗</a>
    </div>
  </div>
</header>

<main>
  <!-- HALL 00: HERO COVER SHOWCASE -->
  <section class="hero" id="top">
    <div class="shell hero-grid">
      <div class="hero-intro">
        <div class="hero-badge">00 · 策展总引 / ISSUE 03</div>
        <h1 class="hero-title">宇宙，<br>超出想象。</h1>
        <p class="hero-lead">
          有冰下的海洋，有正在诞生的太阳。<br>
          还有一束光，走了很久才遇见你。<br>
          从这里，认识一个更大的世界。
        </p>
        <div class="hero-actions">
          <a class="btn-primary" href="#solar">开启探索 ↗</a>
          <a class="btn-secondary" href="#blackhole">黑洞特展 ↓</a>
        </div>
        <div class="hero-caption">
          标本 01 · 土星 (Saturn) · 卡西尼号探测器 自然色真实合成影像<br>
          NASA / JPL-Caltech / Space Science Institute
        </div>
      </div>

      <div class="hero-stage">
        <div class="hero-celestial">
          <img src="{b64['saturn']}" alt="卡西尼号拍摄的真实土星与壮丽光环" loading="eager" fetchpriority="high">
        </div>
      </div>
    </div>
  </section>

  <!-- FAST EXHIBITION DOCK -->
  <div class="tour-route">
    <div class="shell">
      <div class="route-list">
        <a class="route-item" href="#solar">
          <span class="route-idx">01 / SOLAR</span>
          <strong class="route-name">太阳系行星展台</strong>
          <span class="route-sub">8 颗行星 · 探测足迹</span>
        </a>
        <a class="route-item" href="#moons">
          <span class="route-idx">02 / MOONS</span>
          <strong class="route-name">卫星与地下海洋</strong>
          <span class="route-sub">5 颗卫星 · 月相明暗</span>
        </a>
        <a class="route-item" href="#stars">
          <span class="route-idx">03 / STARS</span>
          <strong class="route-name">恒星演化与光谱</strong>
          <span class="route-sub">核聚变史 · 光谱型态</span>
        </a>
        <a class="route-item" href="#nebula">
          <span class="route-idx">04 / NEBULA</span>
          <strong class="route-name">宇宙悬崖与多波段</strong>
          <span class="route-sub">船底座星云 · 红外观测</span>
        </a>
        <a class="route-item" href="#blackhole">
          <span class="route-idx">05 / BLACK HOLE</span>
          <strong class="route-name">黑洞与引力透镜</strong>
          <span class="route-sub">M87* 视界 · 光线弯曲</span>
        </a>
        <a class="route-item" href="#exoplanet">
          <span class="route-idx">06 / EXOPLANET</span>
          <strong class="route-name">系外行星与宜居带</strong>
          <span class="route-sub">TRAPPIST-1 · 凌星光变</span>
        </a>
        <a class="route-item" href="#distance">
          <span class="route-idx">07 / SCALE</span>
          <strong class="route-name">宇宙尺度与深空舰队</strong>
          <span class="route-sub">光程延迟 · 旅行者谱系</span>
        </a>
        <a class="route-item" href="#observe">
          <span class="route-idx">08 / GUIDE</span>
          <strong class="route-name">暗空模拟与观星便笺</strong>
          <span class="route-sub">波特尔等级 · 灵感导出</span>
        </a>
      </div>
    </div>
  </div>

  <!-- HALL 01: SOLAR SYSTEM PLANETS EXHIBIT -->
  <section class="chapter planet-exhibit" id="solar">
    <div class="shell">
      <div class="section-head">
        <div>
          <div class="section-badge">01 · 太阳系标本展台</div>
          <h2 class="section-title">同一个太阳。<br>八种截然不同的世界。</h2>
        </div>
        <p class="section-desc">
          先不记距离与排名。选一颗行星，看看它最让人意外的地方。<br>你会发现，“行星”从来不是同一种风景。
        </p>
      </div>

      <!-- Horizontal Switcher Rail -->
      <div class="planet-rail" id="planetRail" role="tablist" aria-label="选择行星标本">
        <button class="planet-tab" data-idx="0" role="tab" aria-selected="false" aria-pressed="false"><span class="num">01</span> 水星</button>
        <button class="planet-tab" data-idx="1" role="tab" aria-selected="false" aria-pressed="false"><span class="num">02</span> 金星</button>
        <button class="planet-tab" data-idx="2" role="tab" aria-selected="true" aria-pressed="true"><span class="num">03</span> 地球</button>
        <button class="planet-tab" data-idx="3" role="tab" aria-selected="false" aria-pressed="false"><span class="num">04</span> 火星</button>
        <button class="planet-tab" data-idx="4" role="tab" aria-selected="false" aria-pressed="false"><span class="num">05</span> 木星</button>
        <button class="planet-tab" data-idx="5" role="tab" aria-selected="false" aria-pressed="false"><span class="num">06</span> 土星</button>
        <button class="planet-tab" data-idx="6" role="tab" aria-selected="false" aria-pressed="false"><span class="num">07</span> 天王星</button>
        <button class="planet-tab" data-idx="7" role="tab" aria-selected="false" aria-pressed="false"><span class="num">08</span> 海王星</button>
      </div>

      <!-- Plinth Showcase Stage -->
      <div class="plinth-stage">
        <div class="plinth-visual">
          <div class="orbit-accent" aria-hidden="true"></div>
          <div class="planet-disc-wrap">
            <img id="planetImg" src="{b64['earth']}" alt="真实地球全景照片" loading="lazy">
          </div>
          <div class="specimen-tag" id="planetSpecimenTag">SPECIMEN · 03 EARTH</div>
        </div>

        <div class="plinth-dossier" aria-live="polite">
          <div class="dossier-header">
            <div class="planet-en" id="planetEn">03 / EARTH</div>
            <h3 class="planet-name" id="planetName">地球</h3>
          </div>
          <p class="planet-intro" id="planetText">
            液态海洋、活跃地壳与富氧大气共同构成了我们的家。薄薄一层脆弱的大气，庇护着已知宇宙中唯一的繁盛生命。
          </p>

          <div class="planet-metadata-grid">
            <div class="meta-box">
              <span>绕太阳公转一周</span>
              <strong id="planetYear">365 天</strong>
            </div>
            <div class="meta-box">
              <span>天体类型</span>
              <strong id="planetType">岩质行星</strong>
            </div>
            <div class="meta-box">
              <span>平均表面温度</span>
              <strong id="planetTemp">约 15°C</strong>
            </div>
            <div class="meta-box">
              <span>大气主要成分</span>
              <div class="atmosphere-tags" id="planetAtmos">
                <span class="atmos-tag">N₂ 78%</span>
                <span class="atmos-tag">O₂ 21%</span>
                <span class="atmos-tag">Ar 0.9%</span>
              </div>
            </div>
          </div>

          <div class="planet-wonder" id="planetWonder">
            从太空看，国界并不是刻在地表的线。薄薄的大气层包裹着脆弱的生命，这是目前已知唯一存在生命的星球。
          </div>

          <div class="dossier-footer">
            <span id="planetProbe">历史印记：阿波罗 17 号“蓝色弹珠”摄影</span>
            <a id="planetSource" href="https://solarsystem.nasa.gov/planets/earth/overview/" target="_blank" rel="noopener">继续阅读 NASA 原始档案 ↗</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- HALL 02: MOONS CABINET (#moons) -->
  <section class="chapter moons-cabinet" id="moons">
    <div class="shell">
      <div class="section-head">
        <div>
          <div class="section-badge">02 · 卫星群与冰下海洋</div>
          <h2 class="section-title">别小看<br>行星身边的小世界。</h2>
        </div>
        <p class="section-desc">
          有的火山喷发不息，有的冰壳下藏着比地球还深的海洋，有的表面流淌着液态甲烷。<br>
          这组标本展示了它们真实的大小比例与截然不同的地质性格。
        </p>
      </div>

      <!-- Scaled Specimen Cabinet -->
      <div class="collection-tray" id="moonChoices" role="group" aria-label="选择卫星收藏标本"></div>

      <!-- Curatorial Dossier -->
      <div class="moon-dossier" aria-live="polite">
        <div class="dossier-left">
          <div class="moon-en" id="moonEn">THE MOON · LUNA</div>
          <h3 id="moonTag">离我们最近的另一个世界</h3>
          <div class="dossier-stats" id="moonStats">母行星：地球 · 公转周期：27.3 天 · 直径：3,474 km</div>
        </div>
        <div class="dossier-right">
          <p id="moonText">月面上的暗色区域，许多是古老熔岩形成的平原。它并非永远只有一面被照亮；只是自转与公转同步，让大致相同的一面始终朝向地球。</p>
          <div class="dossier-footer">
            <span id="moonSpecial">地质特质：被潮汐锁定的静止邻居</span>
            <a id="moonSource" href="https://moon.nasa.gov" target="_blank" rel="noopener">NASA 月球任务档案 ↗</a>
          </div>
        </div>
      </div>

      <!-- Lunar Phase Lab -->
      <div class="phase-lab">
        <div class="phase-lab-grid">
          <div class="phase-viewport">
            <img class="phase-base-img" src="{b64['moon']}" alt="月球正面真实高分辨率摄影">
            <canvas id="phaseCanvas" width="220" height="220"></canvas>
          </div>

          <div class="phase-controls">
            <div class="phase-tag">TRY IT · 观测实验室</div>
            <h3 id="phaseName">满月 (望)</h3>
            <p id="phaseFraction">第 14.8 天 · 受光面 100% 朝向地球</p>
            <p>
              太阳几乎始终照亮月球的一半。我们看到的“残缺”，纯粹来自地月相对位置造成的视角变化。拖动游标，观察光影交界线的推移：
            </p>

            <div class="phase-slider-wrap">
              <label for="phaseRange">
                <span>从新月到满月的一个朔望月周期</span>
                <span id="dayIndicator">14.8 天</span>
              </label>
              <input class="phase-slider" id="phaseRange" type="range" min="0" max="29.53" step="0.1" value="14.8" aria-label="调整月相天数">
            </div>

            <div class="phase-presets" id="phasePresets" role="group" aria-label="快捷月相预设">
              <button class="preset-btn" data-day="0" aria-pressed="false">新月 (0d)</button>
              <button class="preset-btn" data-day="7.38" aria-pressed="false">上弦月 (7.4d)</button>
              <button class="preset-btn" data-day="14.77" aria-pressed="true">满月 (14.8d)</button>
              <button class="preset-btn" data-day="22.15" aria-pressed="false">下弦月 (22.1d)</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- HALL 03: STARS LIFECYCLE & SPECTRAL TYPES (#stars) -->
  <section class="chapter stars-chapter" id="stars">
    <div class="shell">
      <div class="section-head">
        <div>
          <div class="section-badge">03 · 恒星生命史与光谱</div>
          <h2 class="section-title">星星，<br>也有一生。</h2>
        </div>
        <p class="section-desc">
          抬头看到的恒星，并不是永恒不变的光点。<br>
          它们收拢于星云，在漫长岁月里燃烧核心，并在晚期把物质归还给宇宙。
        </p>
      </div>

      <!-- Chronological Timeline -->
      <div class="stellar-storyline">
        <div class="stellar-steps" id="lifeTrack" role="group" aria-label="选择恒星演化阶段">
          <button class="step-node" data-idx="0" aria-pressed="true">
            <span class="step-num">01 / STAGE</span>
            <span class="step-name">恒星诞生</span>
          </button>
          <button class="step-node" data-idx="1" aria-pressed="false">
            <span class="step-num">02 / STAGE</span>
            <span class="step-name">主序星</span>
          </button>
          <button class="step-node" data-idx="2" aria-pressed="false">
            <span class="step-num">03 / STAGE</span>
            <span class="step-name">红巨星</span>
          </button>
          <button class="step-node" data-idx="3" aria-pressed="false">
            <span class="step-num">04 / STAGE</span>
            <span class="step-name">超新星爆发</span>
          </button>
          <button class="step-node" data-idx="4" aria-pressed="false">
            <span class="step-num">05 / STAGE</span>
            <span class="step-name">致密残骸</span>
          </button>
        </div>
      </div>

      <!-- Morphing Visual Well -->
      <div class="stellar-stage-box">
        <div class="stellar-visual-well">
          <div class="star-morph star-state-0" id="starVisual"></div>
        </div>

        <div class="stellar-narrative" aria-live="polite">
          <div class="stage-tag" id="lifeLabel">01 / BIRTH · 诞生</div>
          <h3 id="lifeTitle">从云里，收拢出一颗星。</h3>
          <p class="story-text" id="lifeStory">
            气体与尘埃云的一部分在引力作用下收缩。物质越聚越多，核心逐渐升温。直到核心能持续进行氢聚变，一颗恒星才真正诞生。
          </p>
          <div class="stellar-fact" id="lifeFact">
            星云不只是背景装饰，它是孕育恒星与行星系统的真正摇篮。
          </div>
        </div>
      </div>

      <!-- Harvard Spectral Class Selector -->
      <div class="spectral-lab">
        <div class="spectral-head">
          <h3>哈佛恒星光谱型分类模拟器 (OBAFGKM)</h3>
          <span>表面温度越高，恒星颜色越偏蓝白</span>
        </div>

        <div class="spectral-buttons" id="spectralBtns" role="group" aria-label="选择恒星光谱型">
          <button class="spec-btn" data-spec="O" aria-pressed="false"><strong>O 型</strong><span>35,000K 蓝巨星</span></button>
          <button class="spec-btn" data-spec="B" aria-pressed="false"><strong>B 型</strong><span>20,000K 蓝白星</span></button>
          <button class="spec-btn" data-spec="A" aria-pressed="false"><strong>A 型</strong><span>9,000K 织女星</span></button>
          <button class="spec-btn" data-spec="F" aria-pressed="false"><strong>F 型</strong><span>7,000K 黄白星</span></button>
          <button class="spec-btn" data-spec="G" aria-pressed="true"><strong>G 型</strong><span>5,800K 太阳</span></button>
          <button class="spec-btn" data-spec="K" aria-pressed="false"><strong>K 型</strong><span>4,500K 橙巨星</span></button>
          <button class="spec-btn" data-spec="M" aria-pressed="false"><strong>M 型</strong><span>3,200K 红矮星</span></button>
        </div>

        <div class="spec-info-box" id="specInfo">
          <div><span>光谱类型</span><strong id="specType">G2V 主序黄矮星</strong></div>
          <div><span>有效温度</span><strong id="specTemp">约 5,778 K</strong></div>
          <div><span>代表天体</span><strong id="specStar">太阳 (Sun) · 寿命约 100 亿年</strong></div>
        </div>
      </div>
    </div>
  </section>

  <!-- HALL 04: NEBULA & MULTI-WAVELENGTH EXHIBIT (#nebula) -->
  <section class="chapter nebula-exhibit" id="nebula">
    <div class="shell">
      <div class="section-head">
        <div>
          <div class="section-badge">04 · 星云专属展厅</div>
          <h2 class="section-title">看起来像山。<br>其实，新的太阳<br>正在这里诞生。</h2>
        </div>
        <p class="section-desc">
          韦布空间望远镜 · 船底座星云 NGC 3324。<br>“宇宙悬崖”近红外合成影像，点击观察点探索细节。
        </p>
      </div>

      <!-- Panoramic Museum Plate -->
      <div class="panoramic-frame">
        <img class="panoramic-img" id="nebulaImg" src="{b64['cliffs']}" alt="韦布近红外相机拍摄的 NGC 3324 宇宙悬崖宽幅全景" loading="lazy">
        <button class="hotspot-pin pin-1" data-hot="0" aria-label="观察点 1：气体与尘埃边缘" aria-pressed="true">01</button>
        <button class="hotspot-pin pin-2" data-hot="1" aria-label="观察点 2：隐藏的新生恒星群" aria-pressed="false">02</button>
        <button class="hotspot-pin pin-3" data-hot="2" aria-label="观察点 3：原恒星外流喷流" aria-pressed="false">03</button>
      </div>

      <!-- Hotspot Analysis Plaque -->
      <div class="nebula-analysis" aria-live="polite">
        <div class="analysis-meta">
          <div class="ana-idx" id="hotLabel">01 / CLOUDS · 分子云边缘</div>
          <h3 id="hotTitle">“悬崖”不是岩石。</h3>
          <div class="ana-guide" id="hotGuide">试着看：图像下方起伏的金色云雾，实际上是分子气体与尘埃的界面。</div>
        </div>
        <div class="analysis-content">
          <p id="hotText">这道轮廓是恒星形成区内气体与尘埃云的边缘。附近年轻大质量恒星的强烈紫外辐射和高速恒星风，正在不断侵蚀并雕刻这片云壁。</p>
        </div>
      </div>

      <!-- Multi-Wavelength Spectrum Explorer -->
      <div class="wavelength-console">
        <div class="wavelength-head">
          <h3>多波段宇宙观测窗 (Multi-Wavelength Spectrum)</h3>
          <span>切换不同电磁波段，揭示被尘埃掩盖的物理结构</span>
        </div>
        <div class="wave-nav" id="waveNav" role="group" aria-label="切换观测波段">
          <button class="wave-btn" data-wave="vis" aria-pressed="false">可见光 (Visible / Hubble)</button>
          <button class="wave-btn" data-wave="nir" aria-pressed="true">近红外 (Near-IR / JWST NIRCam)</button>
          <button class="wave-btn" data-wave="mir" aria-pressed="false">中红外 (Mid-IR / JWST MIRI)</button>
          <button class="wave-btn" data-wave="xray" aria-pressed="false">X 射线 (X-Ray / Chandra)</button>
        </div>
        <div class="wave-explainer" id="waveExplainer">
          近红外（0.6 ~ 5 微米）：红外波长能穿透致密的不透明尘埃，暴露出隐藏在云深处的上千颗新生原恒星与胚胎恒星。
        </div>
      </div>
    </div>
  </section>

  <!-- HALL 05: BLACK HOLES & GRAVITATIONAL LENSING (#blackhole - BRAND NEW) -->
  <section class="chapter blackhole-chapter" id="blackhole">
    <div class="shell">
      <div class="section-head">
        <div>
          <div class="section-badge cyan">05 · 极端引力特展</div>
          <h2 class="section-title">光线折返之处：<br>黑洞与时空弯曲。</h2>
        </div>
        <p class="section-desc">
          事件视界望远镜 (EHT) 拍摄的人类首张超大质量黑洞真实影像。<br>
          质量集中在极小尺度时，引力将时空弯曲到光也无法逃逸的边界。
        </p>
      </div>

      <!-- EHT Black Hole Showcase -->
      <div class="bh-grid">
        <div class="bh-image-box">
          <img src="{b64['blackhole']}" alt="事件视界望远镜拍摄的 M87* 超大质量黑洞真实吸积环" loading="lazy">
          <div class="bh-caption">
            M87* 超大质量黑洞 · 质量为太阳的 65 亿倍 · 距离地球 5,500 万光年<br>
            Event Horizon Telescope Collaboration
          </div>
        </div>

        <div class="bh-dossier">
          <h3>看见不可见。</h3>
          <p>
            中心黑色的区域并不是黑洞本身，而是 <strong>事件视界的引力阴影</strong>。周围耀眼的橙金光环，是气体在以接近光速绕黑洞盘旋时、被极端摩擦加热到数十亿度产生的辐射。
          </p>
          <div class="physics-cards">
            <div class="phys-card">
              <div class="formula">R_s = 2GM / c²</div>
              <span>施瓦西半径：决定事件视界物理大小的临界方程。</span>
            </div>
            <div class="phys-card">
              <div class="formula">相对论性多普勒增亮</div>
              <span>光环下方更明亮，因为发光物质正朝向地球飞奔而来。</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Gravitational Lensing Interactive Simulator -->
      <div class="lensing-lab">
        <div class="lensing-head">
          <h3>交互模拟：引力透镜与爱因斯坦环 (Gravitational Lensing)</h3>
          <span>在下方画布上移动鼠标或手指，观察大质量黑洞如何弯曲背景星系光线</span>
        </div>
        <div class="lensing-canvas-wrap" id="lensCanvasWrap">
          <canvas id="lensCanvas" width="1140" height="380"></canvas>
          <div class="lens-instructions">拖动黑洞视界 · 观察爱因斯坦环变形</div>
        </div>
      </div>
    </div>
  </section>

  <!-- HALL 06: EXOPLANETS & TRANSIT LAB (#exoplanet - BRAND NEW) -->
  <section class="chapter exoplanet-chapter" id="exoplanet">
    <div class="shell">
      <div class="section-head">
        <div>
          <div class="section-badge violet">06 · 宜居地平线</div>
          <h2 class="section-title">跨越恒星的寻觅：<br>寻找第二个地球。</h2>
        </div>
        <p class="section-desc">
          TRAPPIST-1 行星系统全景。在一颗距离我们 40 光年的超冷红矮星周围，<br>
          紧密环绕着 7 颗岩质地球大小的行星，其中 3 颗位于液态水可存在的宜居带。
        </p>
      </div>

      <!-- TRAPPIST-1 Lineup Banner -->
      <div class="trappist-banner">
        <img src="{b64['trappist']}" alt="NASA 绘制的 TRAPPIST-1 7颗岩质系外行星真实比例对比图" loading="lazy">
      </div>

      <!-- Transit Light Curve Lab -->
      <div class="transit-lab">
        <div class="transit-grid">
          <div class="transit-visual-box">
            <div class="transit-stage">
              <div class="host-star"></div>
              <div class="transit-planet"></div>
            </div>
            <div class="transit-curve-box">
              <canvas id="curveCanvas" width="460" height="120"></canvas>
            </div>
          </div>

          <div class="transit-details">
            <h3>凌星法与大气透射光谱</h3>
            <p>
              当行星从宿主恒星前方横截而过时，恒星亮度会发生微小下跌（通常仅 0.1% ~ 1%）。通过分析穿过行星稀薄大气的微弱恒星光谱线，天文学家得以检测遥远世界的大气成分：
            </p>
            <div class="spectral-bars">
              <div class="spec-bar-item">
                <div class="spec-bar-label"><span>水蒸气 (H₂O) 吸收峰</span><strong>78% 置信度</strong></div>
                <div class="spec-bar-track"><div class="spec-bar-fill h2o"></div></div>
              </div>
              <div class="spec-bar-item">
                <div class="spec-bar-label"><span>甲烷 (CH₄) 生物标志物候选</span><strong>52% 置信度</strong></div>
                <div class="spec-bar-track"><div class="spec-bar-fill ch4"></div></div>
              </div>
              <div class="spec-bar-item">
                <div class="spec-bar-label"><span>二氧化碳 (CO₂) 温室气体</span><strong>92% 置信度</strong></div>
                <div class="spec-bar-track"><div class="spec-bar-fill co2"></div></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- HALL 07: SCALE & DEEP SPACE FLEET (#distance) -->
  <section class="chapter distance-chapter" id="distance">
    <div class="shell">
      <div class="section-head">
        <div>
          <div class="section-badge">07 · 距离、光程与深空舰队</div>
          <h2 class="section-title">你看到的光，<br>从什么时候出发？</h2>
        </div>
        <p class="section-desc">
          光的速度是每秒三十万千米。<br>
          在浩瀚的宇宙中，即便是光也需要漫长的旅程。望向远方，就是望向过去。
        </p>
      </div>

      <!-- Immense Typographic Scale Console -->
      <div class="scale-console">
        <div class="dest-buttons" id="destChoices" role="group" aria-label="选择目的地光程">
          <button class="dest-btn" data-idx="0" aria-pressed="true">月球 (38.4 万千米)</button>
          <button class="dest-btn" data-idx="1" aria-pressed="false">太阳 (1.5 亿千米)</button>
          <button class="dest-btn" data-idx="2" aria-pressed="false">旅行者 1 号 (244 亿千米)</button>
          <button class="dest-btn" data-idx="3" aria-pressed="false">仙女座星系 (250 万光年)</button>
          <button class="dest-btn" data-idx="4" aria-pressed="false">早期宇宙 GN-z11 (134 亿光年)</button>
        </div>

        <div class="scale-readout">
          <div class="time-monument">
            <span class="time-number" id="timeNum">1.3</span>
            <span class="time-unit" id="timeUnit">秒</span>
          </div>

          <div class="dest-details" aria-live="polite">
            <h3 id="destTitle">近到一秒多，<br>远到三十多万千米。</h3>
            <p id="destText">月球反射的太阳光离开月面后，大约走 1.3 秒才抵达地球。我们平时觉得“立刻看见”，只是因为这段延迟在人类感知里极短。</p>
          </div>
        </div>

        <!-- Light Journey Line -->
        <div class="light-journey-line" aria-hidden="true">
          <div class="photon-beam"></div>
        </div>
      </div>

      <!-- Deep Space Fleet Timeline -->
      <div class="fleet-section">
        <div class="fleet-head">
          <h3>人类深空探测舰队谱系 (Human Deep Space Fleet)</h3>
          <span>飞出摇篮的信使与望远镜</span>
        </div>

        <div class="fleet-tabs" id="fleetTabs" role="group" aria-label="选择深空探测器">
          <button class="fleet-tab" data-idx="0" aria-pressed="true">旅行者 1 号 / 2 号</button>
          <button class="fleet-tab" data-idx="1" aria-pressed="false">新视野号 (New Horizons)</button>
          <button class="fleet-tab" data-idx="2" aria-pressed="false">韦布空间望远镜 (JWST)</button>
          <button class="fleet-tab" data-idx="3" aria-pressed="false">帕克太阳探测器 (Parker)</button>
          <button class="fleet-tab" data-idx="4" aria-pressed="false">嫦娥与天问工程</button>
        </div>

        <div class="fleet-dossier-box" aria-live="polite">
          <div class="fleet-img-wrap">
            <img id="fleetImg" src="{b64['voyager']}" alt="旅行者号探测器在星际空间示意图">
          </div>
          <div class="fleet-content">
            <h4 id="fleetName">旅行者 1 号 (Voyager 1) · 1977 年发射</h4>
            <p id="fleetDesc" style="margin: 12px 0; font-size: 14.5px; line-height: 1.85;">
              人类飞得最远的造造物体。2012 年穿越日球层顶进入星际空间，携带着镀金铜质唱片，录制着地球的声音、音乐与人类问候。即使跨越近五十年光阴，微弱的信号仍穿越 240 多亿公里抵达地球。
            </p>
            <div class="meta-box" style="margin-top: 16px;">
              <span>当前距离与状态</span>
              <strong id="fleetStatus">距地球约 244 亿千米 · 正在星际等离子体中前行</strong>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- HALL 08: STARGAZING, BORTLE SIMULATOR & FIELD NOTES (#observe) -->
  <section class="chapter observe-chapter" id="observe">
    <div class="shell">
      <div class="section-head">
        <div>
          <div class="section-badge">08 · 观星实操与便笺</div>
          <h2 class="section-title">用肉眼与好奇，<br>开始今晚的观察。</h2>
        </div>
        <p class="section-desc">
          观星不需要昂贵的设备。关掉刺眼的强光，给瞳孔二十分钟适应黑暗。<br>
          天空永远向清醒的人敞开。
        </p>
      </div>

      <!-- Bortle Dark Sky Simulator -->
      <div class="bortle-lab">
        <div class="bortle-head">
          <h3>波特尔暗空等级模拟器 (Bortle Scale 1 ~ 9)</h3>
          <span>拖动滑块查看不同光污染环境下的夜空可见度</span>
        </div>
        <div class="bortle-viewport">
          <canvas id="bortleCanvas" width="1140" height="220"></canvas>
        </div>
        <div class="bortle-slider-wrap">
          <label for="bortleRange">
            <span id="bortleClassLabel">第 4 级：乡村与郊区过渡带</span>
            <span id="bortleMag">极限星等：约 6.2 等</span>
          </label>
          <input class="phase-slider" id="bortleRange" type="range" min="1" max="9" step="1" value="4" aria-label="调整波特尔暗空等级">
        </div>
        <div class="bortle-desc-box" id="bortleDesc">
          银河清晰可见，能在地平线上方展现出复杂的尘埃暗带；只有城市方向有轻微的光穹顶。适合开展深入的天文双筒镜观测。
        </div>
      </div>

      <!-- Prep Checklist & Notes Desk -->
      <div class="prep-grid">
        <div class="checklist-panel">
          <h3>观星前简易准备清单</h3>
          <label class="check-item">
            <input type="checkbox" id="task1">
            <div>
              <strong>避开强光源与满月之夜</strong>
              <span>选择开阔、无直射路灯的开阔地，避开农历十五前后月光冲刷。</span>
            </div>
          </label>
          <label class="check-item">
            <input type="checkbox" id="task2">
            <div>
              <strong>给双眼 20 分钟适应暗视</strong>
              <span>视网膜视紫红质合成需要时间；期间严禁直视刺眼的手机白光，推荐使用微弱红光手电。</span>
            </div>
          </label>
          <label class="check-item">
            <input type="checkbox" id="task3">
            <div>
              <strong>认出第一颗亮星与四季标志</strong>
              <span>夏季大三角（织女、牛郎、天津四）或冬季大三角（猎户参宿四、天狼星、南河三）。</span>
            </div>
          </label>
          <label class="check-item">
            <input type="checkbox" id="task4">
            <div>
              <strong>备好保暖衣物与折叠椅</strong>
              <span>夜间静坐体温散失极快，舒适平躺才能长时间从容凝望天顶。</span>
            </div>
          </label>
        </div>

        <div class="notes-panel">
          <h3>我的深空观察便笺</h3>
          <p id="taskProgress" style="font-size: 13px; color: var(--fg-muted); margin-bottom: 12px;">已完成 0 / 4 项准备 · 记录将在本地保存</p>
          <textarea class="note-textarea" id="skyNote" placeholder="写下今晚观察到的天象、天气，或者一个你想继续探究的问题..."></textarea>
          <div class="note-actions">
            <button class="btn-primary" id="saveNote">保存便笺</button>
            <button class="btn-secondary" id="downloadNote">导出便笺 (.txt)</button>
            <span class="note-status" id="noteStatus">准备就绪</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- HALL 09: SCIENTIFIC INTUITION LAB (#quiz) -->
  <section class="chapter quiz-chapter" id="quiz">
    <div class="shell">
      <div class="section-head">
        <div>
          <div class="section-badge">09 · 科学直觉实验室</div>
          <h2 class="section-title">测测你的<br>天文直觉。</h2>
        </div>
        <p class="section-desc">
          宇宙经常挑战人类在地面上培养出来的日常直觉。<br>
          选一个选项，看看物理原理怎么说。
        </p>
      </div>

      <div class="quiz-box">
        <div class="quiz-header">
          <span class="quiz-meta" id="quizProgress">QUESTION 01 / 08</span>
          <span class="quiz-meta" id="quizScore">正确直觉：0</span>
        </div>

        <h3 class="quiz-question" id="quizQuestion">哪颗行星的表面平均温度最高？</h3>

        <div class="quiz-options" id="quizOptions"></div>

        <div class="quiz-feedback" id="quizFeedback" style="display: none;" aria-live="polite"></div>

        <div class="quiz-footer">
          <button class="btn-secondary" id="prevQuizBtn">上一题</button>
          <button class="btn-primary" id="nextQuizBtn">下一题</button>
        </div>
      </div>
    </div>
  </section>
</main>

<!-- SITE FOOTER -->
<footer class="site-footer">
  <div class="shell">
    <div class="footer-grid">
      <div class="footer-brand">
        <h4>远处 ELSEWHERE · 深空科学策展馆</h4>
        <p>
          一个致力于将现代前沿天文学科研数据转化为美术馆级体验的数字策展项目。
          致敬所有仰望星空、探索未知的人类探测器与先驱者。
        </p>
      </div>
      <div class="footer-col">
        <h5>科学影像与数据来源</h5>
        <ul>
          <li><a href="https://photojournal.jpl.nasa.gov" target="_blank" rel="noopener">NASA / JPL Photojournal</a></li>
          <li><a href="https://webbtelescope.org" target="_blank" rel="noopener">James Webb Space Telescope</a></li>
          <li><a href="https://hubblesite.org" target="_blank" rel="noopener">Hubble Space Telescope</a></li>
          <li><a href="https://eventhorizontelescope.org" target="_blank" rel="noopener">Event Horizon Telescope</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>展厅快速索引</h5>
        <ul>
          <li><a href="#solar">太阳系八大行星</a></li>
          <li><a href="#moons">卫星与冰下海洋</a></li>
          <li><a href="#blackhole">M87* 黑洞与引力透镜</a></li>
          <li><a href="#exoplanet">TRAPPIST-1 系外行星</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <span>ELSEWHERE OBSERVATORY · VER 3.0 CURATORIAL EDITION</span>
      <span>所有真实摄影底片由 NASA, ESA, JPL-Caltech 与 EHT 科学合作组织提供</span>
    </div>
  </div>
</footer>

<script>
/* JS logic will be injected here */
</script>
</body>
</html>
"""
