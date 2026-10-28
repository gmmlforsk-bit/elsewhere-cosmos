# -*- coding: utf-8 -*-
"""
v3_js.py
Complete client-side interactivity, audio synthesizer, and canvas simulators for 远处 ELSEWHERE.
"""

JS = """
const $ = id => document.getElementById(id);

/* ==========================================================================
   1. SOUND SYNTHESIZER (WEB AUDIO API - 100% SELF-CONTAINED CODE)
   ========================================================================== */
class CosmicAudio {
  constructor() {
    this.ctx = null;
    this.enabled = false;
    this.droneGain = null;
    this.osc1 = null;
    this.osc2 = null;
  }

  init() {
    if (this.ctx) return;
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    this.ctx = new AudioContext();

    // Ambient Sub-Bass Drone (55Hz + 110Hz)
    this.droneGain = this.ctx.createGain();
    this.droneGain.gain.setValueAtTime(0.0001, this.ctx.currentTime);
    this.droneGain.connect(this.ctx.destination);

    this.osc1 = this.ctx.createOscillator();
    this.osc1.type = 'sine';
    this.osc1.frequency.setValueAtTime(55, this.ctx.currentTime);

    this.osc2 = this.ctx.createOscillator();
    this.osc2.type = 'sine';
    this.osc2.frequency.setValueAtTime(110.2, this.ctx.currentTime);

    // Subtle low-pass filter
    const filter = this.ctx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(140, this.ctx.currentTime);

    this.osc1.connect(filter);
    this.osc2.connect(filter);
    filter.connect(this.droneGain);

    this.osc1.start();
    this.osc2.start();
  }

  toggle() {
    if (!this.ctx) this.init();
    if (this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
    this.enabled = !this.enabled;
    const target = this.enabled ? 0.08 : 0.0001;
    this.droneGain.gain.setTargetAtTime(target, this.ctx.currentTime, 0.5);
    return this.enabled;
  }

  clickSound(freq = 900) {
    if (!this.enabled || !this.ctx) return;
    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(300, this.ctx.currentTime + 0.035);
      gain.gain.setValueAtTime(0.05, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.035);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.04);
    } catch(e) {}
  }
}

const audio = new CosmicAudio();
const audioBtn = $('audioToggle');
audioBtn.onclick = () => {
  const on = audio.toggle();
  audioBtn.textContent = on ? '🔊 氛围原声: 开' : '🔊 氛围原声: 关';
  audioBtn.classList.toggle('active', on);
  if (on) audio.clickSound(1100);
};

/* ==========================================================================
   2. GLOBAL LIVING STARFIELD BACKGROUND
   ========================================================================== */
const starCanvas = $('starCanvas');
const starCtx = starCanvas.getContext('2d');
let stars = [];
let mouseX = 0, mouseY = 0;
let targetMouseX = 0, targetMouseY = 0;

function resizeStarCanvas() {
  starCanvas.width = window.innerWidth;
  starCanvas.height = window.innerHeight;
  initStars();
}
window.addEventListener('resize', resizeStarCanvas);

function initStars() {
  stars = [];
  const count = Math.min(140, Math.floor((window.innerWidth * window.innerHeight) / 9000));
  for (let i = 0; i < count; i++) {
    stars.push({
      x: Math.random() * starCanvas.width,
      y: Math.random() * starCanvas.height,
      radius: Math.random() * 1.4 + 0.3,
      alpha: Math.random() * 0.7 + 0.2,
      speed: Math.random() * 0.015 + 0.005,
      phase: Math.random() * Math.PI * 2,
      layer: Math.random() * 2 + 1,
      color: Math.random() > 0.85 ? '#93c5fd' : (Math.random() > 0.7 ? '#fed7aa' : '#ffffff')
    });
  }
}
resizeStarCanvas();

window.addEventListener('mousemove', e => {
  targetMouseX = (e.clientX - window.innerWidth / 2) * 0.03;
  targetMouseY = (e.clientY - window.innerHeight / 2) * 0.03;

  // Live HUD Coordinates Calculation
  const raH = Math.floor((e.clientX / window.innerWidth) * 24);
  const raM = Math.floor(((e.clientX / window.innerWidth) * 1440) % 60);
  const decD = Math.floor((e.clientY / window.innerHeight) * 90 - 45);
  $('hudCoords').textContent = `天球坐标 RA ${String(raH).padStart(2, '0')}h ${String(raM).padStart(2, '0')}m · DEC ${decD >= 0 ? '+' : ''}${decD}°`;
});

function animateStars() {
  mouseX += (targetMouseX - mouseX) * 0.05;
  mouseY += (targetMouseY - mouseY) * 0.05;

  starCtx.clearRect(0, 0, starCanvas.width, starCanvas.height);

  for (let s of stars) {
    s.phase += s.speed;
    const flicker = Math.sin(s.phase) * 0.35 + 0.65;
    const px = s.x + mouseX * s.layer;
    const py = s.y + mouseY * s.layer;

    starCtx.beginPath();
    starCtx.arc(px, py, s.radius, 0, Math.PI * 2);
    starCtx.fillStyle = s.color;
    starCtx.globalAlpha = s.alpha * flicker;
    starCtx.fill();
  }
  starCtx.globalAlpha = 1.0;

  if (!document.documentElement.classList.contains('reduced-motion')) {
    requestAnimationFrame(animateStars);
  }
}
animateStars();

// Live UTC Clock
function updateUtc() {
  const d = new Date();
  const y = d.getUTCFullYear();
  const m = String(d.getUTCMonth() + 1).padStart(2, '0');
  const day = String(d.getUTCDate()).padStart(2, '0');
  const h = String(d.getUTCHours()).padStart(2, '0');
  const min = String(d.getUTCMinutes()).padStart(2, '0');
  const s = String(d.getUTCSeconds()).padStart(2, '0');
  $('hudUtc').textContent = `${y}.${m}.${day} ${h}:${min}:${s} UTC`;
}
setInterval(updateUtc, 1000);
updateUtc();

// Scroll Progress
window.addEventListener('scroll', () => {
  const max = document.documentElement.scrollHeight - window.innerHeight;
  const pct = max > 0 ? (window.scrollY / max) * 100 : 0;
  $('scrollProgress').style.width = pct + '%';
}, { passive: true });

/* ==========================================================================
   3. HALL 01: PLANETS EXHIBIT DATA & SWITCHER
   ========================================================================== */
const planets = [
  {
    name: '水星', en: '01 / MERCURY', tag: 'SPECIMEN · 01 MERCURY',
    text: '最靠近太阳的岩石世界，昼夜温差超过 500°C。没有浓厚大气保温，阳光直射处如熔炉，背阳面则陷入极寒。',
    year: '88 天', type: '岩质行星', temp: '-180°C ~ 430°C',
    atmos: ['极微弱散逸层', 'Na', 'He', 'O₂'],
    probe: '历史印记：信使号 (MESSENGER) 轨道探测器',
    wonder: '虽然距离太阳最近，但由于自转与公转周期呈 3:2 潮汐共振，在水星上过一天比过一年还要漫长。',
    url: 'https://solarsystem.nasa.gov/planets/mercury/overview/'
  },
  {
    name: '金星', en: '02 / VENUS', tag: 'SPECIMEN · 02 VENUS',
    text: '被厚重的二氧化碳与浓硫酸云层完全包裹。失控的极端温室效应使地表常年保持在 465°C 左右，是全太阳系最炎热的行星。',
    year: '225 天', type: '岩质行星', temp: '常年约 465°C',
    atmos: ['CO₂ 96.5%', 'N₂ 3.5%', 'SO₂ 云雾'],
    probe: '历史印记：麦哲伦号雷达绘图仪 / 金星快车',
    wonder: '地表气压高达地球的 90 多倍，相当于地球一千米深的海底压力。同时它还是自东向西逆向自转的叛逆者。',
    url: 'https://solarsystem.nasa.gov/planets/venus/overview/'
  },
  {
    name: '地球', en: '03 / EARTH', tag: 'SPECIMEN · 03 EARTH',
    text: '液态海洋、活跃地壳与富氧大气共同构成了我们的家。薄薄一层脆弱的大气，庇护着已知宇宙中唯一的繁盛生命。',
    year: '365 天', type: '岩质行星', temp: '平均约 15°C',
    atmos: ['N₂ 78%', 'O₂ 21%', 'Ar 0.9%'],
    probe: '历史印记：阿波罗 17 号“蓝色弹珠”全景摄影',
    wonder: '从太空看，国界并不是刻在地表的线。薄薄的大气层包裹着脆弱的生命，这是目前已知唯一存在生命的星球。',
    url: 'https://solarsystem.nasa.gov/planets/earth/overview/'
  },
  {
    name: '火星', en: '04 / MARS', tag: 'SPECIMEN · 04 MARS',
    text: '富含氧化铁的地表泛着锈红色。拥有全太阳系最高的奥林匹斯火山与横跨大陆的水手号大峡谷，地表曾流淌着远古液态水。',
    year: '687 天', type: '岩质行星', temp: '-140°C ~ 20°C',
    atmos: ['CO₂ 95%', 'N₂ 2.6%', 'Ar 1.9%'],
    probe: '历史印记：好奇号与毅力号漫游车实地钻探',
    wonder: '火星上的一天约为 24 小时 37 分钟，与地球极为相近；但稀薄的大气已无法阻止水分永久逃逸入太空。',
    url: 'https://solarsystem.nasa.gov/planets/mars/overview/'
  },
  {
    name: '木星', en: '05 / JUPITER', tag: 'SPECIMEN · 05 JUPITER',
    text: '太阳系最大行星，质量是其余所有行星总和的两倍半。巨大的大红斑风暴已肆虐数百年，拥有极其强烈的偶极磁场。',
    year: '11.9 年', type: '气态巨行星', temp: '云顶约 -110°C',
    atmos: ['H₂ 90%', 'He 10%', 'CH₄ / NH₃'],
    probe: '历史印记：伽利略号 / 朱诺号 (Juno) 极轨观测',
    wonder: '木星就像太阳系内部的引力护盾，其庞大的引力场不断清理内太阳系的彗星与流星碎片，保护了地球的演化。',
    url: 'https://solarsystem.nasa.gov/planets/jupiter/overview/'
  },
  {
    name: '土星', en: '06 / SATURN', tag: 'SPECIMEN · 06 SATURN',
    text: '拥有太阳系中最宏伟复杂的光环系统。光环主要由数十亿块冰晶与岩石颗粒组成，整体密度甚至比水还要轻。',
    year: '29.4 年', type: '气态巨行星', temp: '云顶约 -140°C',
    atmos: ['H₂ 96%', 'He 3%', 'CH₄ 微量'],
    probe: '历史印记：卡西尼-惠更斯号十三载深空探秘',
    wonder: '虽然光环直径跨越数十万千米，但平均厚度仅有数十米。若按比例缩小为一张纸，光环比纸页还要纤薄千倍。',
    url: 'https://solarsystem.nasa.gov/planets/saturn/overview/'
  },
  {
    name: '天王星', en: '07 / URANUS', tag: 'SPECIMEN · 07 URANUS',
    text: '青绿色的冰巨星，大气中的甲烷吸收了红光。拥有高达 98 度的自转轴倾角，几乎是“侧躺”在公转轨道上打滚前行。',
    year: '84 年', type: '冰巨行星', temp: '低至 -224°C',
    atmos: ['H₂ 83%', 'He 15%', 'CH₄ 2%'],
    probe: '历史印记：旅行者 2 号 1986 年历史性飞掠',
    wonder: '极端的侧躺自转导致极昼与极夜各持续 42 年之久；其磁场轴与自转轴发生了惊人的 59 度巨大偏转。',
    url: 'https://solarsystem.nasa.gov/planets/uranus/overview/'
  },
  {
    name: '海王星', en: '08 / NEPTUNE', tag: 'SPECIMEN · 08 NEPTUNE',
    text: '深邃幽蓝的最外侧行星，太阳系风速之冠，超音速强风时速突破 2,100 千米。距离太阳过于遥远，太阳在那里只是一颗刺目星点。',
    year: '165 年', type: '冰巨行星', temp: '约 -214°C',
    atmos: ['H₂ 80%', 'He 19%', 'CH₄ 1.5%'],
    probe: '历史印记：旅行者 2 号 1989 年深空飞掠',
    wonder: '海王星是人类历史上第一个完全通过牛顿天体力学数学计算、预测其坐标后才在望远镜中被找到的行星。',
    url: 'https://solarsystem.nasa.gov/planets/neptune/overview/'
  }
];

const planetRail = $('planetRail');
const planetImg = $('planetImg');
const planetTabs = planetRail.querySelectorAll('.planet-tab');

function selectPlanet(idx) {
  planetTabs.forEach((tab, i) => {
    const active = i === idx;
    tab.setAttribute('aria-selected', String(active));
    tab.setAttribute('aria-pressed', String(active));
  });

  const p = planets[idx];
  audio.clickSound(700 + idx * 60);

  planetImg.style.opacity = '0';
  planetImg.style.transform = 'scale(0.92)';

  setTimeout(() => {
    planetImg.src = window.b64Assets[idx === 0 ? 'mercury' : idx === 1 ? 'venus' : idx === 2 ? 'earth' : idx === 3 ? 'mars' : idx === 4 ? 'jupiter' : idx === 5 ? 'saturn' : idx === 6 ? 'uranus' : 'neptune'];
    planetImg.alt = `真实${p.name}照片`;
    planetImg.style.opacity = '1';
    planetImg.style.transform = 'scale(1)';
  }, 180);

  $('planetSpecimenTag').textContent = p.tag;
  $('planetEn').textContent = p.en;
  $('planetName').textContent = p.name;
  $('planetText').textContent = p.text;
  $('planetYear').textContent = p.year;
  $('planetType').textContent = p.type;
  $('planetTemp').textContent = p.temp;
  $('planetWonder').textContent = p.wonder;
  $('planetProbe').textContent = p.probe;
  $('planetSource').href = p.url;

  const atmosWrap = $('planetAtmos');
  atmosWrap.innerHTML = p.atmos.map(a => `<span class="atmos-tag">${a}</span>`).join('');
}

planetTabs.forEach((tab, i) => {
  tab.onclick = () => selectPlanet(i);
});

/* ==========================================================================
   4. HALL 02: MOONS CABINET & LUNAR PHASE LAB
   ========================================================================== */
const moons = [
  {
    name: '泰坦', en: 'TITAN · SATURN VI', dia: '5,150 km', parent: '土星', period: '15.9 天',
    tag: '拥有浓厚大气与液态甲烷海洋',
    desc: '太阳系第二大卫星，也是唯一拥有浓厚大气层与地表稳定液态河流湖泊的天体，但流淌的不是水，而是零下 180°C 的液态甲烷与乙烷。',
    special: '地质特质：富含有机分子的冰封冰冻史前地球模型',
    url: 'https://solarsystem.nasa.gov/moons/saturn-moons/titan/overview/',
    key: 'titan', scale: 88
  },
  {
    name: '伊奥', en: 'IO · JUPITER I', dia: '3,642 km', parent: '木星', period: '1.77 天',
    tag: '太阳系中火山活动最剧烈的天体',
    desc: '深陷木星与其他伽利略卫星的潮汐引力拉扯，内部剧烈潮汐摩擦加热使得地表分布着数百座活火山，持续喷射硫黄与二氧化硫羽流。',
    special: '地质特质：熔岩湖泊覆盖的无水重金属火山世界',
    url: 'https://solarsystem.nasa.gov/moons/jupiter-moons/io/overview/',
    key: 'io', scale: 64
  },
  {
    name: '露娜', en: 'THE MOON · LUNA', dia: '3,474 km', parent: '地球', period: '27.3 天',
    tag: '离我们最近的另一个完整世界',
    desc: '月面上的暗色区域是古老熔岩冷却形成的玄武岩平原。它被地球潮汐锁定，自转与公转周期完全同步，让同一面始终朝向地球。',
    special: '地质特质：被潮汐锁定的静止邻居',
    url: 'https://moon.nasa.gov',
    key: 'moon', scale: 62
  },
  {
    name: '欧罗巴', en: 'EUROPA · JUPITER II', dia: '3,122 km', parent: '木星', period: '3.6 天',
    tag: '光滑冰壳下藏着比地球还深的海洋',
    desc: '地表覆盖着交错纵横的褐色裂纹冰壳。在数十公里厚的冰层下方，蕴藏着深达百公里的全球性液态咸水海洋，水量甚至超过地球全部海洋之和。',
    special: '地质特质：地热喷口与地外生命最具希望的温床',
    url: 'https://solarsystem.nasa.gov/moons/jupiter-moons/europa/overview/',
    key: 'europa', scale: 56
  },
  {
    name: '恩克拉多斯', en: 'ENCELADUS · SATURN II', dia: '504 km', parent: '土星', period: '1.37 天',
    tag: '南极冰缝中持续喷涌的冰羽',
    desc: '太阳系中最洁白反光的天体。卡西尼号飞入其南极“虎条纹”裂隙喷出的冰喷泉中，检测到了水蒸气、有机分子、盐分与二氧化硅微粒。',
    special: '地质特质：喷入太空直接造就了土星外侧 E 环',
    url: 'https://solarsystem.nasa.gov/moons/saturn-moons/enceladus/overview/',
    key: 'enceladus', scale: 24
  }
];

const moonChoices = $('moonChoices');
moonChoices.innerHTML = moons.map((m, i) => `
  <div class="specimen-card" data-idx="${i}" role="button" tabindex="0" aria-pressed="${i === 2}">
    <div class="specimen-sphere">
      <img src="${window.b64Assets[m.key]}" alt="${m.name}" style="width: ${m.scale}px; height: ${m.scale}px;">
    </div>
    <div class="specimen-info">
      <strong>${m.name}</strong>
      <span>${m.dia}</span>
    </div>
  </div>
`).join('');

function selectMoon(idx) {
  moonChoices.querySelectorAll('.specimen-card').forEach((card, i) => {
    card.setAttribute('aria-pressed', String(i === idx));
  });
  const m = moons[idx];
  audio.clickSound(850 + idx * 50);

  $('moonEn').textContent = m.en;
  $('moonTag').textContent = m.tag;
  $('moonStats').textContent = `母行星：${m.parent} · 公转周期：${m.period} · 直径：${m.dia}`;
  $('moonText').textContent = m.desc;
  $('moonSpecial').textContent = m.special;
  $('moonSource').href = m.url;
}

moonChoices.querySelectorAll('.specimen-card').forEach((c, i) => {
  c.onclick = () => selectMoon(i);
  c.onkeydown = e => { if (e.key === 'Enter' || e.key === ' ') selectMoon(i); };
});

/* Lunar Phase Terminator Renderer */
const phaseCanvas = $('phaseCanvas');
const phaseCtx = phaseCanvas.getContext('2d');
const phaseRange = $('phaseRange');

function updateLunarPhase() {
  const day = parseFloat(phaseRange.value);
  $('dayIndicator').textContent = `${day.toFixed(1)} 天`;

  const frac = day / 29.53059;
  let phaseText = '新月';
  const eps = 0.02;

  if (frac < eps || frac > 1 - eps) {
    phaseText = '新月 (朔)';
  } else if (Math.abs(frac - 0.25) < eps) {
    phaseText = '上弦月';
  } else if (Math.abs(frac - 0.5) < eps) {
    phaseText = '满月 (望)';
  } else if (Math.abs(frac - 0.75) < eps) {
    phaseText = '下弦月';
  } else if (frac < 0.25) {
    phaseText = '蛾眉月';
  } else if (frac < 0.5) {
    phaseText = '盈凸月';
  } else if (frac < 0.75) {
    phaseText = '亏凸月';
  } else {
    phaseText = '残月';
  }

  $('phaseName').textContent = phaseText;
  const illuminated = Math.round((1 - Math.cos(frac * 2 * Math.PI)) / 2 * 100);
  $('phaseFraction').textContent = `第 ${day.toFixed(1)} 天 · 受光面 ${illuminated}% 朝向地球`;

  const w = phaseCanvas.width, h = phaseCanvas.height, r = w / 2;
  phaseCtx.clearRect(0, 0, w, h);

  phaseCtx.save();
  phaseCtx.beginPath();
  phaseCtx.arc(r, r, r, 0, Math.PI * 2);
  phaseCtx.clip();

  phaseCtx.fillStyle = 'rgba(3, 4, 7, 0.88)';
  if (frac <= 0.5) {
    const norm = frac * 2;
    phaseCtx.fillRect(0, 0, r, h);
    phaseCtx.beginPath();
    const xR = Math.abs(r * (1 - 2 * norm));
    phaseCtx.ellipse(r, r, xR, r, 0, 0, Math.PI * 2);
    if (norm < 0.5) {
      phaseCtx.fill();
    } else {
      phaseCtx.globalCompositeOperation = 'destination-out';
      phaseCtx.fill();
    }
  } else {
    const norm = (frac - 0.5) * 2;
    phaseCtx.fillRect(r, 0, r, h);
    phaseCtx.beginPath();
    const xR = Math.abs(r * (1 - 2 * norm));
    phaseCtx.ellipse(r, r, xR, r, 0, 0, Math.PI * 2);
    if (norm < 0.5) {
      phaseCtx.fill();
    } else {
      phaseCtx.globalCompositeOperation = 'destination-out';
      phaseCtx.fill();
    }
  }
  phaseCtx.restore();
}

phaseRange.addEventListener('input', () => {
  updateLunarPhase();
  audio.clickSound(1100);
});
updateLunarPhase();

$('phasePresets').querySelectorAll('.preset-btn').forEach(btn => {
  btn.onclick = () => {
    $('phasePresets').querySelectorAll('.preset-btn').forEach(b => b.setAttribute('aria-pressed', 'false'));
    btn.setAttribute('aria-pressed', 'true');
    phaseRange.value = btn.dataset.day;
    updateLunarPhase();
    audio.clickSound(900);
  };
});

/* ==========================================================================
   5. HALL 03: STARS LIFECYCLE & HARVARD SPECTRAL LAB
   ========================================================================== */
const lifeData = [
  {
    tag: '01 / BIRTH · 诞生', title: '从云里，收拢出一颗星。',
    story: '气体与尘埃云的一部分在引力作用下收缩。物质越聚越多，核心逐渐升温。直到温度达到一千万度、持续进行稳定的氢核聚变，一颗真正的恒星才宣告诞生。',
    fact: '星云不只是深空的背景装饰，它是孕育恒星与行星系统的真正母体。'
  },
  {
    tag: '02 / MAIN SEQUENCE · 壮年', title: '在漫长岁月中，平衡引力与核火。',
    story: '恒星生命中最稳定的漫长时期。核心氢聚变为氦释放出的向外巨大辐射压力，与恒星自身不可思议的引力向内坍缩达到精妙流体静力学平衡。我们的太阳正处于这黄金十年中的第五十亿年。',
    fact: '太阳每秒钟将大约六亿吨氢转化为氦，这微小的质量亏损转化成了照亮地球的无尽光辉。'
  },
  {
    tag: '03 / RED GIANT · 晚期', title: '核心氢耗尽，外壳巨大膨胀。',
    story: '核心的氢燃料耗尽后，失去核压支撑的核心在引力下坍缩升温，点燃外层剩余氢壳层。恒星外壳在剧烈辐射下膨胀上百倍，表面温度降低而变红，成为一颗庞大的红巨星。',
    fact: '大约五十亿年后，膨胀的红巨星太阳将吞噬水星与金星，地表海洋将彻底汽化。'
  },
  {
    tag: '04 / SUPERNOVA · 爆发', title: '宇宙中熔铸黄金的剧烈终局。',
    story: '大于八倍太阳质量的大质量恒星，在聚变出铁核后无法继续释放能量而瞬时向心坍缩，引发剧烈绝伦的超新星大爆炸。其亮度在瞬间甚至能超越整个宿主星系百亿颗恒星的总和。',
    fact: '我们血液中的铁、骨骼中的钙以及佩戴的金银首饰，全部来自古老超新星爆发核合成的抛射物。我们皆是星尘。'
  },
  {
    tag: '05 / REMNANT · 终局', title: '致密残骸：白矮星、中子星与黑洞。',
    story: '类太阳恒星遗留下由电子简并压支撑的地球大小致密白矮星；超大恒星则压缩为由中子简并压支撑的城市大小中子星（脉冲星），或者彻底超越极限坍缩为无底深渊——恒星级黑洞。',
    fact: '一茶匙中子星物质在地球重力场下的重量超过十亿吨。'
  }
];

const lifeTrack = $('lifeTrack');
const starVisual = $('starVisual');
lifeTrack.querySelectorAll('.step-node').forEach((node, i) => {
  node.onclick = () => {
    lifeTrack.querySelectorAll('.step-node').forEach((n, j) => n.setAttribute('aria-pressed', String(i === j)));
    audio.clickSound(800 + i * 80);

    starVisual.className = `star-morph star-state-${i}`;
    const d = lifeData[i];
    $('lifeLabel').textContent = d.tag;
    $('lifeTitle').textContent = d.title;
    $('lifeStory').textContent = d.story;
    $('lifeFact').textContent = d.fact;
  };
});

// Harvard Spectral Types
const spectralData = {
  O: { type: 'O 型 蓝超巨星', temp: '30,000 ~ 50,000 K', star: '参宿一 (Alnitak) · 辐射极强、寿命极短' },
  B: { type: 'B 型 蓝白大质量星', temp: '10,000 ~ 30,000 K', star: '参宿七 (Rigel) · 猎户座右膝' },
  A: { type: 'A 型 纯白主序星', temp: '7,500 ~ 10,000 K', star: '织女星 (Vega) / 天狼星 (Sirius)' },
  F: { type: 'F 型 黄白主序星', temp: '6,000 ~ 7,500 K', star: '南河三 (Procyon) · 小犬座主星' },
  G: { type: 'G 型 黄矮主序星', temp: '5,200 ~ 6,000 K', star: '太阳 (Sun) · G2V 恒星' },
  K: { type: 'K 型 橙色次巨/矮星', temp: '3,700 ~ 5,200 K', star: '大角星 (Arcturus) / 毕宿五' },
  M: { type: 'M 型 红矮星 / 红超巨星', temp: '2,400 ~ 3,700 K', star: '比邻星 (Proxima) / 参宿四 (Betelgeuse)' }
};

$('spectralBtns').querySelectorAll('.spec-btn').forEach(btn => {
  btn.onclick = () => {
    $('spectralBtns').querySelectorAll('.spec-btn').forEach(b => b.setAttribute('aria-pressed', 'false'));
    btn.setAttribute('aria-pressed', 'true');
    const s = btn.dataset.spec;
    audio.clickSound(600 + ['O','B','A','F','G','K','M'].indexOf(s) * 70);

    const d = spectralData[s];
    $('specType').textContent = d.type;
    $('specTemp').textContent = d.temp;
    $('specStar').textContent = d.star;
  };
});

/* ==========================================================================
   6. HALL 04: NEBULA & MULTI-WAVELENGTH FILTERS
   ========================================================================== */
const hotData = [
  {
    label: '01 / CLOUDS · 分子云边缘',
    title: '“悬崖”不是岩石。',
    guide: '试着看：图像下方起伏的金色云雾，实际上是分子气体与尘埃的界面。',
    text: '这道轮廓是恒星形成区内气体与尘埃云的边缘。附近年轻大质量恒星的强烈紫外辐射和高速恒星风，正在不断侵蚀并雕刻这片云壁。'
  },
  {
    label: '02 / INFRARED · 新生星群',
    title: '红外线看穿尘埃。',
    guide: '试着看：云层后方点缀的大量微小亮红光点，是刚刚诞生的原恒星。',
    text: '在可见光下，厚厚的尘埃会遮挡内部的一切。韦布望远镜通过穿透力极强的近红外光，直接观测到了被尘埃密实包裹的新生恒星胚胎。'
  },
  {
    label: '03 / PROTOSTAR · 外流喷流',
    title: '原恒星的喷流痕迹。',
    guide: '试着看：右侧尘埃柱顶端延伸出的细微红色流光，是原恒星喷流的痕迹。',
    text: '正在吸积质量的原恒星会从磁极向外高速喷射双向气体喷流，猛烈撞击周围分子云，在红外波段留下标志性的明亮激波条纹。'
  }
];

document.querySelectorAll('.hotspot-pin').forEach(pin => {
  pin.onclick = () => {
    document.querySelectorAll('.hotspot-pin').forEach(p => p.setAttribute('aria-pressed', 'false'));
    pin.setAttribute('aria-pressed', 'true');
    const idx = parseInt(pin.dataset.hot, 10);
    audio.clickSound(1200 + idx * 100);

    const d = hotData[idx];
    $('hotLabel').textContent = d.label;
    $('hotTitle').textContent = d.title;
    $('hotGuide').textContent = d.guide;
    $('hotText').textContent = d.text;
  };
});

const waveExplains = {
  vis: '可见光波段（0.4 ~ 0.7 微米）：哈勃经典视角。致密的分子云表现为几乎不透光的黑暗幕布，只能看到云层表面的反射辉光。',
  nir: '近红外波段（0.6 ~ 5 微米）：JWST NIRCam 视角。红外光穿透微米级尘埃颗粒，暴露出尘埃背后的成百上千颗新生原恒星。',
  mir: '中红外波段（5 ~ 28 微米）：JWST MIRI 视角。炽热尘埃颗粒本身发出强烈热辐射，高分子多环芳烃 (PAHs) 发光如发丝般精细交织。',
  xray: 'X 射线波段（0.1 ~ 10 keV）：钱德拉 X 射线天文台视角。揭示被磁场加速的高温等离子体激波以及大质量恒星炽热外冕的剧烈活动。'
};

const waveFilters = {
  vis: 'contrast(1.2) brightness(0.9) saturate(1.3)',
  nir: 'none',
  mir: 'hue-rotate(45deg) saturate(1.8) contrast(1.1)',
  xray: 'invert(0.9) hue-rotate(180deg) saturate(2)'
};

$('waveNav').querySelectorAll('.wave-btn').forEach(btn => {
  btn.onclick = () => {
    $('waveNav').querySelectorAll('.wave-btn').forEach(b => b.setAttribute('aria-pressed', 'false'));
    btn.setAttribute('aria-pressed', 'true');
    const w = btn.dataset.wave;
    audio.clickSound(950);

    $('nebulaImg').style.filter = waveFilters[w];
    $('waveExplainer').textContent = waveExplains[w];
  };
});

/* ==========================================================================
   7. HALL 05: GRAVITATIONAL LENSING CANVAS SIMULATOR
   ========================================================================== */
const lensCanvas = $('lensCanvas');
const lensCtx = lensCanvas.getContext('2d');
let bhX = 400, bhY = 190;
let targetBhX = 400, targetBhY = 190;
const galaxyImg = new Image();
galaxyImg.src = window.b64Assets['galaxy'];

function resizeLensCanvas() {
  const rect = lensCanvas.parentElement.getBoundingClientRect();
  lensCanvas.width = rect.width;
  lensCanvas.height = rect.height;
}
window.addEventListener('resize', resizeLensCanvas);
resizeLensCanvas();

lensCanvas.parentElement.addEventListener('mousemove', e => {
  const rect = lensCanvas.getBoundingClientRect();
  targetBhX = e.clientX - rect.left;
  targetBhY = e.clientY - rect.top;
});
lensCanvas.parentElement.addEventListener('touchmove', e => {
  if (e.touches.length > 0) {
    const rect = lensCanvas.getBoundingClientRect();
    targetBhX = e.touches[0].clientX - rect.left;
    targetBhY = e.touches[0].clientY - rect.top;
  }
}, { passive: true });

function drawLensing() {
  bhX += (targetBhX - bhX) * 0.1;
  bhY += (targetBhY - bhY) * 0.1;

  const w = lensCanvas.width, h = lensCanvas.height;
  lensCtx.fillStyle = '#03050a';
  lensCtx.fillRect(0, 0, w, h);

  // Background galaxy
  if (galaxyImg.complete && galaxyImg.naturalWidth > 0) {
    lensCtx.save();
    lensCtx.globalAlpha = 0.55;
    const gSize = Math.min(w, h) * 0.85;
    lensCtx.drawImage(galaxyImg, w * 0.5 - gSize / 2, h * 0.5 - gSize / 2, gSize, gSize);
    lensCtx.restore();
  }

  // Background star grid warped by gravity
  lensCtx.fillStyle = 'rgba(255, 255, 255, 0.7)';
  const gridStep = 45;
  const einsteinR = 65; // Einstein ring radius

  for (let x = 20; x < w; x += gridStep) {
    for (let y = 20; y < h; y += gridStep) {
      const dx = x - bhX;
      const dy = y - bhY;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < 10) continue;

      // Schwarzschild lensing deflection angle ~ 4GM / (c^2 * r)
      const deflection = (einsteinR * einsteinR) / dist;
      const factor = (dist + deflection) / dist;
      const warpedX = bhX + dx * factor;
      const warpedY = bhY + dy * factor;

      lensCtx.beginPath();
      lensCtx.arc(warpedX, warpedY, 1.2, 0, Math.PI * 2);
      lensCtx.fill();
    }
  }

  // Draw Einstein Ring & Accretion Glow
  lensCtx.save();
  lensCtx.beginPath();
  lensCtx.arc(bhX, bhY, einsteinR, 0, Math.PI * 2);
  lensCtx.strokeStyle = 'rgba(226, 109, 64, 0.45)';
  lensCtx.lineWidth = 4;
  lensCtx.stroke();

  // Accretion disk glow
  const glow = lensCtx.createRadialGradient(bhX, bhY, einsteinR * 0.5, bhX, bhY, einsteinR * 1.4);
  glow.addColorStop(0, 'rgba(226, 109, 64, 0.8)');
  glow.addColorStop(0.5, 'rgba(245, 158, 11, 0.3)');
  glow.addColorStop(1, 'transparent');
  lensCtx.fillStyle = glow;
  lensCtx.beginPath();
  lensCtx.arc(bhX, bhY, einsteinR * 1.4, 0, Math.PI * 2);
  lensCtx.fill();

  // Black Hole Event Horizon Shadow
  lensCtx.beginPath();
  lensCtx.arc(bhX, bhY, einsteinR * 0.65, 0, Math.PI * 2);
  lensCtx.fillStyle = '#000000';
  lensCtx.fill();
  lensCtx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
  lensCtx.lineWidth = 1;
  lensCtx.stroke();
  lensCtx.restore();

  if (!document.documentElement.classList.contains('reduced-motion')) {
    requestAnimationFrame(drawLensing);
  }
}
drawLensing();

/* ==========================================================================
   8. HALL 06: EXOPLANET TRANSIT LIGHT CURVE SIMULATOR
   ========================================================================== */
const curveCanvas = $('curveCanvas');
const curveCtx = curveCanvas.getContext('2d');
let transitT = 0;

function drawTransitCurve() {
  transitT = (transitT + 0.008) % 1.0;
  const w = curveCanvas.width, h = curveCanvas.height;
  curveCtx.clearRect(0, 0, w, h);

  // Axes lines
  curveCtx.strokeStyle = 'rgba(255, 255, 255, 0.12)';
  curveCtx.lineWidth = 1;
  curveCtx.beginPath();
  curveCtx.moveTo(40, 20);
  curveCtx.lineTo(w - 20, 20);
  curveCtx.moveTo(40, 20);
  curveCtx.lineTo(40, h - 25);
  curveCtx.stroke();

  curveCtx.fillStyle = 'rgba(255, 255, 255, 0.45)';
  curveCtx.font = '10px monospace';
  curveCtx.fillText('1.000 (100% 相对亮度)', 48, 16);
  curveCtx.fillText('0.992 (凌星光陷 -0.8%)', 48, h - 30);

  // Plot light curve
  curveCtx.strokeStyle = '#38bdf8';
  curveCtx.lineWidth = 2;
  curveCtx.beginPath();

  const startX = 40, endX = w - 20;
  for (let x = startX; x <= endX; x++) {
    const prog = (x - startX) / (endX - startX);
    // U-shaped dip around prog = 0.5
    let dip = 0;
    const distFromCenter = Math.abs(prog - 0.5);
    if (distFromCenter < 0.12) {
      dip = Math.cos((distFromCenter / 0.12) * (Math.PI / 2)) * (h - 60);
    }
    const py = 25 + dip;
    if (x === startX) curveCtx.moveTo(x, py);
    else curveCtx.lineTo(x, py);
  }
  curveCtx.stroke();

  // Current transit cursor dot
  const curX = startX + transitT * (endX - startX);
  let curDip = 0;
  const curDist = Math.abs(transitT - 0.5);
  if (curDist < 0.12) {
    curDip = Math.cos((curDist / 0.12) * (Math.PI / 2)) * (h - 60);
  }
  const curY = 25 + curDip;

  curveCtx.beginPath();
  curveCtx.arc(curX, curY, 4, 0, Math.PI * 2);
  curveCtx.fillStyle = '#e26d40';
  curveCtx.fill();
  curveCtx.shadowColor = '#e26d40';
  curveCtx.shadowBlur = 8;
  curveCtx.shadowBlur = 0;

  if (!document.documentElement.classList.contains('reduced-motion')) {
    requestAnimationFrame(drawTransitCurve);
  }
}
drawTransitCurve();

/* ==========================================================================
   9. HALL 07: SCALE & DEEP SPACE FLEET
   ========================================================================== */
const distances = [
  {
    num: '1.3', unit: '秒',
    title: '近到一秒多，<br>远到三十多万千米。',
    text: '月球反射的太阳光离开月面后，大约走 1.3 秒才抵达地球。我们平时觉得“立刻看见”，只是因为这段延迟在人类感知里极短。'
  },
  {
    num: '8.3', unit: '分钟',
    title: '八分钟前的阳光。',
    text: '地球距离太阳大约 1.5 亿千米。此刻照在身上的日光，是 8 分 20 秒前从太阳光球层出发的。我们看到的永远是 8 分钟前的太阳。'
  },
  {
    num: '22.5', unit: '小时',
    title: '人类足迹的最远边缘。',
    text: '1977 年发射的旅行者 1 号探测器已飞出日球层顶，距离地球超过 244 亿千米。即便以光速传递无线电指令，单程也需要 22 小时 30 分钟。'
  },
  {
    num: '250', unit: '万年',
    title: '银河外的星光，<br>来自人类旧石器时代。',
    text: '仙女座星系是肉眼可见的最遥远天体。当它的光线今晚落在你的视网膜上时，那束光其实是在 250 万年前、早期人类甚至尚未学会生火时出发的。'
  },
  {
    num: '134', unit: '亿年',
    title: '穿透大爆炸余烬，<br>触及宇宙第一缕曙光。',
    text: '韦布望远镜捕捉到了大爆炸仅三亿年后诞生的极早期星系 GN-z11。这束红移极大的微弱红外光穿越了整个可观测宇宙的漫长岁月才来到镜片前。'
  }
];

const destChoices = $('destChoices');
destChoices.querySelectorAll('.dest-btn').forEach((btn, i) => {
  btn.onclick = () => {
    destChoices.querySelectorAll('.dest-btn').forEach((b, j) => b.setAttribute('aria-pressed', String(i === j)));
    const d = distances[i];
    audio.clickSound(750 + i * 80);

    $('timeNum').textContent = d.num;
    $('timeUnit').textContent = d.unit;
    $('destTitle').innerHTML = d.title;
    $('destText').textContent = d.text;
  };
});

// Fleet tabs
const fleetData = [
  {
    name: '旅行者 1 号 / 2 号 (Voyager) · 1977 年发射',
    desc: '人类飞得最远的造造物体。2012 年穿越日球层顶进入星际空间，携带着镀金铜质唱片，录制着地球的声音、音乐与人类问候。即使跨越近五十年光阴，微弱的信号仍穿越 240 多亿公里抵达地球。',
    status: '距地球约 244 亿千米 · 正在星际等离子体中前行'
  },
  {
    name: '新视野号 (New Horizons) · 2006 年发射',
    desc: '人类历史上速度最快的深空探测器之一。2015 年首次掠过冥王星系统，拍摄下标志性的“冥王星之心”氮冰平原；2019 年探访柯伊伯带天体“阿罗科斯 (Arrokoth)”，揭开太阳系原始星子拼合之谜。',
    status: '距地球约 85 亿千米 · 正在柯伊伯带边缘巡航'
  },
  {
    name: '詹姆斯·韦布空间望远镜 (JWST) · 2021 年发射',
    desc: '人类有史以来最强大的太空望远镜。配备 6.5 米镀金铍镜与网球场大小的五层遮阳罩，驻留于距地球 150 万公里的第二拉格朗日点 (L2)，以史无前例的高分辨率近红外视界洞穿深空尘埃。',
    status: '日地 L2 晕轮轨道 · 持续运行并向全人类公开科学数据'
  },
  {
    name: '帕克太阳探测器 (Parker Solar Probe) · 2018 年发射',
    desc: '人类历史上第一艘真正“触摸太阳”的飞船。配备先进碳复合热防护盾，在近日点时速高达每小时 70 万千米，直接飞入太阳日冕层采集高能粒子与磁场重联的一手物理证据。',
    status: '近日点距离日表仅 690 万千米 · 经受 1,400°C 炽热烈焰考验'
  },
  {
    name: '中国嫦娥工程与天问一号 · 2013-2024 年',
    desc: '嫦娥四号实现人类探测器首次月球背面软着陆，嫦娥六号完成了人类首次月球背面采样返回；天问一号一步实现火星“绕、着、巡”，祝融号漫游车在乌托邦平原开展了漫长科学巡视。',
    status: '月球科研站规划中 · 持续拓展地外天体采样与深空探索边界'
  }
];

$('fleetTabs').querySelectorAll('.fleet-tab').forEach((tab, i) => {
  tab.onclick = () => {
    $('fleetTabs').querySelectorAll('.fleet-tab').forEach((t, j) => t.setAttribute('aria-pressed', String(i === j)));
    audio.clickSound(880 + i * 50);

    const f = fleetData[i];
    $('fleetName').textContent = f.name;
    $('fleetDesc').textContent = f.desc;
    $('fleetStatus').textContent = f.status;
  };
});

/* ==========================================================================
   10. HALL 08: BORTLE SIMULATOR, CHECKLIST & FIELD NOTES
   ========================================================================== */
const bortleCanvas = $('bortleCanvas');
const bortleCtx = bortleCanvas.getContext('2d');
const bortleRange = $('bortleRange');

const bortleData = {
  1: { title: '第 1 级：极致纯净的完全黑暗天空', mag: '极限星等：约 7.6 ~ 8.0 等', desc: '黄道光、对日照与气辉肉眼可见；银河核心细节繁复至极，甚至在地面投下微弱黑影。真正的荒野秘境。' },
  2: { title: '第 2 级：典型的纯净暗夜乡村', mag: '极限星等：约 7.1 ~ 7.5 等', desc: '银河高度结构化且明亮如浮云；地平线几乎没有任何城市光穹顶干扰。绝佳天文摄影圣地。' },
  3: { title: '第 3 级：乡村天空', mag: '极限星等：约 6.6 ~ 7.0 等', desc: '地平线上有一两处微弱光污染源；头顶银河依然复杂震撼，M31 仙女座星系肉眼清晰可辨。' },
  4: { title: '第 4 级：乡村与郊区过渡带', mag: '极限星等：约 6.2 ~ 6.5 等', desc: '银河清晰可见，能在地平线上方展现出复杂的尘埃暗带；只有城市方向有轻微的光穹顶。适合双筒镜观测。' },
  5: { title: '第 5 级：典型郊区天空', mag: '极限星等：约 5.6 ~ 6.0 等', desc: '银河在地平线附近完全隐没，只有在头顶附近依稀可见浅淡发白光带；大部分光污染方向有明显光幕。' },
  6: { title: '第 6 级：明亮郊区天空', mag: '极限星等：约 5.1 ~ 5.5 等', desc: '银河即便在天顶也几乎不可见；地平线以上 35 度以内的天空都呈现灰白发亮。' },
  7: { title: '第 7 级：郊区与城市过渡带', mag: '极限星等：约 4.6 ~ 5.0 等', desc: '整个天空呈现浅灰白色光晕；只有最明亮的恒星和主要星座轮廓肉眼勉强可认。' },
  8: { title: '第 8 级：典型城市中心天空', mag: '极限星等：约 4.1 ~ 4.5 等', desc: '天空发白甚至泛黄；肉眼只能认出北斗七星或猎户座主星，天文学深空天体完全绝迹。' },
  9: { title: '第 9 级：大都市繁华中心天空', mag: '极限星等：约 3.0 ~ 4.0 等', desc: '强烈的霓虹与路灯泛光将天幕照得如同薄雾；肉眼只能辨认月亮、金星与木星。' }
};

function drawBortleSky() {
  const level = parseInt(bortleRange.value, 10);
  const w = bortleCanvas.width, h = bortleCanvas.height;

  // Sky background gradient according to light pollution
  const skyGrad = bortleCtx.createLinearGradient(0, 0, 0, h);
  const baseAlpha = (level - 1) / 8;
  const skyTop = `rgb(${Math.round(4 + baseAlpha * 40)}, ${Math.round(6 + baseAlpha * 40)}, ${Math.round(12 + baseAlpha * 45)})`;
  const skyBottom = `rgb(${Math.round(8 + baseAlpha * 75)}, ${Math.round(10 + baseAlpha * 65)}, ${Math.round(18 + baseAlpha * 55)})`;
  skyGrad.addColorStop(0, skyTop);
  skyGrad.addColorStop(1, skyBottom);

  bortleCtx.fillStyle = skyGrad;
  bortleCtx.fillRect(0, 0, w, h);

  // Milky Way band (visible only in low Bortle levels)
  if (level <= 5) {
    bortleCtx.save();
    const mwAlpha = (6 - level) * 0.16;
    const mwGrad = bortleCtx.createRadialGradient(w * 0.5, h * 0.4, 20, w * 0.5, h * 0.4, w * 0.6);
    mwGrad.addColorStop(0, `rgba(230, 235, 255, ${mwAlpha})`);
    mwGrad.addColorStop(0.5, `rgba(180, 195, 230, ${mwAlpha * 0.5})`);
    mwGrad.addColorStop(1, 'transparent');
    bortleCtx.fillStyle = mwGrad;
    bortleCtx.fillRect(0, 0, w, h);
    bortleCtx.restore();
  }

  // Star count inversely proportional to Bortle
  const starCounts = { 1: 300, 2: 240, 3: 180, 4: 120, 5: 75, 6: 45, 7: 28, 8: 16, 9: 7 };
  const numStars = starCounts[level];

  // Pseudo-random deterministic stars based on fixed seed
  for (let i = 0; i < numStars; i++) {
    const sx = ((i * 137.5) % (w - 20)) + 10;
    const sy = ((i * 263.3) % (h - 20)) + 10;
    const br = ((i * 47) % 100) / 100;
    const r = br > 0.85 ? 1.6 : (br > 0.5 ? 1.1 : 0.7);

    bortleCtx.beginPath();
    bortleCtx.arc(sx, sy, r, 0, Math.PI * 2);
    bortleCtx.fillStyle = '#ffffff';
    bortleCtx.globalAlpha = Math.max(0.2, br * (1 - (level - 1) * 0.08));
    bortleCtx.fill();
  }
  bortleCtx.globalAlpha = 1.0;
}

bortleRange.addEventListener('input', () => {
  const lvl = bortleRange.value;
  const d = bortleData[lvl];
  $('bortleClassLabel').textContent = d.title;
  $('bortleMag').textContent = d.mag;
  $('bortleDesc').textContent = d.desc;
  drawBortleSky();
  audio.clickSound(700 + lvl * 50);
});
drawBortleSky();

// Checklist progress
const tasks = [1, 2, 3, 4].map(i => $('task' + i));
function updateChecklist() {
  const done = tasks.filter(t => t.checked).length;
  $('taskProgress').textContent = `已完成 ${done} / 4 项准备 · 记录将在本地保存`;
}
tasks.forEach(t => t.addEventListener('change', () => {
  updateChecklist();
  audio.clickSound(1000);
}));

// Field Notes LocalStorage & Export
try {
  const saved = JSON.parse(localStorage.getItem('elsewhere-observation-v3') || 'null');
  if (saved) {
    if (saved.note) $('skyNote').value = saved.note;
    if (saved.tasks) {
      saved.tasks.forEach((val, i) => { if (tasks[i]) tasks[i].checked = val; });
      updateChecklist();
    }
  }
} catch(e) {}

$('saveNote').onclick = () => {
  try {
    const data = {
      note: $('skyNote').value,
      tasks: tasks.map(t => t.checked),
      timestamp: new Date().toISOString()
    };
    localStorage.setItem('elsewhere-observation-v3', JSON.stringify(data));
    $('noteStatus').textContent = '已保存到本地浏览器。';
    audio.clickSound(1200);
    setTimeout(() => { $('noteStatus').textContent = '准备就绪'; }, 2500);
  } catch(e) {}
};

$('downloadNote').onclick = () => {
  audio.clickSound(1300);
  const taskStatus = tasks.map((t, i) => `[${t.checked ? 'X' : ' '}] 准备步骤 0${i + 1}`).join(String.fromCharCode(10));
  const text = `远处 ELSEWHERE · 观星观察便笺
=================================
记录时间：${new Date().toLocaleString()}

准备核对清单：
${taskStatus}

我的深空观察记录与问题：
${$('skyNote').value || '（未记录心得）'}

=================================
远处 ELSEWHERE · 探索更辽阔的世界`;

  const blob = new Blob([text], { type: 'text/plain;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `远处-观星便笺-${new Date().toISOString().slice(0, 10)}.txt`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
};

/* ==========================================================================
   11. HALL 09: SCIENTIFIC INTUITION LAB (8 QUESTIONS)
   ========================================================================== */
const quizQuestions = [
  {
    q: '太阳系中表面平均温度最高的是哪颗行星？',
    opts: ['离太阳最近的水星', '被失控温室效应包裹的金星', '拥有巨大热核风暴的木星'],
    ans: 1,
    exp: '金星。虽然水星离太阳最近，但由于没有大气保温，背阳面极冷。金星拥有 96.5% 的致密二氧化碳大气，引发失控温室效应，地表常年保持在 465°C 左右。'
  },
  {
    q: '我们看到月球经常缺了一块，物理原因通常是因为……',
    opts: ['地球的巨大影子遮挡了月球表面', '月球只有朝向太阳的一半被照亮，且我们从地球观察角度不同', '月球自身发光受到月球地核活动控制'],
    ans: 1,
    exp: '视角变化。太阳几乎始终照亮月球的大约一半，但随着月球绕地球公转，我们在地球上看到的月球受光面比例不断改变。地球影子遮挡造成的现象是月食而非日常月相。'
  },
  {
    q: '天文学上说一个星系距离我们 100 光年，意思是……',
    opts: ['这个星系诞生于 100 年前', '光线从那里穿过太空到达地球需要约 100 年', '必须使用放大 100 倍的望远镜才能看见它'],
    ans: 1,
    exp: '光年是绝对的距离单位（约 9.46 万亿千米）。说距离 100 光年意味着此刻进入望远镜的光子是 100 年前出发的，不能据此推断天体本身的诞生年龄。'
  },
  {
    q: '我们的太阳在几十亿年后老去，最终会变成黑洞吗？',
    opts: ['会，所有恒星在燃料耗尽后都会变成黑洞', '不会，太阳的质量不足以在引力坍缩下形成黑洞', '只要吞噬周围八大行星就会变黑洞'],
    ans: 1,
    exp: '不会。太阳在经过红巨星阶段后会抛去外壳形成行星状星云，中心残留一颗由电子简并压力支撑的碳氧白矮星。只有质量大于太阳约 20 倍以上的恒星才会在超新星爆发后坍缩为黑洞。'
  },
  {
    q: '在木卫二（欧罗巴）冰壳下证实存在全球性液态海洋，科学意义在于……',
    opts: ['人类已经直接发现了外星鱼类或复杂智慧生命', '确认了太阳系内部存在极具科研价值的潜在宜居水热环境', '那里的水质完全不需要过滤就可以直接饮用'],
    ans: 1,
    exp: '确认了地外液态水与能量热源共存的宜居环境。液态水与深海热泉被认为是生命诞生的关键要素，但发现宜居环境本身不能直接等同于已发现生命。'
  },
  {
    q: '深空星云照片中瑰丽的色彩，等于肉眼贴在望远镜目镜上看到的原貌吗？',
    opts: ['完全一样，现代科研相机拍摄的就是真实原貌', '不一定，极微弱光线经长曝光累积，且科学家将特定红外/紫外窄波段映射为代表色', '完全是美术画师凭空手绘的纯粹科幻画'],
    ans: 1,
    exp: '不一定。深空天体光线极其微弱且大多位于人眼不可见的红外或电磁波段。天文影像通过数小时长曝光捕获微弱光子，并遵循严格物理数据将特定元素吸收发射波段映射为红、绿、蓝三种代表色。'
  },
  {
    q: '如果一艘宇宙飞船以 99% 的光速飞往 4 光年外的比邻星，在宇航员自己的手表上看：',
    opts: ['经过了大约 4 年时间', '经过了远少于 4 年的时间（狭义相对论钟慢效应）', '手表会因为超光速直接倒着走'],
    ans: 1,
    exp: '远少于 4 年。根据爱因斯坦狭义相对论时间膨胀效应，在接近光速运动的高速参考系中，时间流逝显著变慢。在地球观察者看来飞船飞了 4 年多，但在飞船上的宇航员看来可能只过了半年多。'
  },
  {
    q: '在 TRAPPIST-1 拥有 7 颗地球大小行星的系统中，行星之间的天空景观是……',
    opts: ['因为距离遥远，在彼此天空中只是不起眼的暗淡针尖星点', '因为轨道极紧凑，邻近行星在天空中看起来比地球上看满月还要大数倍', '行星之间有引力轨道钢索连接'],
    ans: 1,
    exp: '比满月还要大数倍。TRAPPIST-1 系统极其紧凑，整个系统的七颗行星轨道全部位于水星轨道以内。如果你站在其中一颗行星表面仰望，邻近的兄弟行星就像悬挂在空中的庞大月亮，甚至能用肉眼看清其上的大陆与云系。'
  }
];

let currentQ = 0;
let userScore = 0;
let answered = new Array(quizQuestions.length).fill(false);

function renderQuiz() {
  const q = quizQuestions[currentQ];
  $('quizProgress').textContent = `QUESTION 0${currentQ + 1} / 0${quizQuestions.length}`;
  $('quizScore').textContent = `正确直觉：${userScore}`;
  $('quizQuestion').textContent = q.q;

  const optWrap = $('quizOptions');
  optWrap.innerHTML = q.opts.map((opt, i) => `
    <button class="quiz-opt-btn" data-opt="${i}" role="radio" aria-pressed="false">${opt}</button>
  `).join('');

  const feedback = $('quizFeedback');
  feedback.style.display = 'none';
  feedback.textContent = '';

  optWrap.querySelectorAll('.quiz-opt-btn').forEach(btn => {
    btn.onclick = () => {
      if (answered[currentQ]) return;
      answered[currentQ] = true;
      const chosen = parseInt(btn.dataset.opt, 10);
      btn.setAttribute('aria-pressed', 'true');

      const isCorrect = chosen === q.ans;
      if (isCorrect) userScore++;
      audio.clickSound(isCorrect ? 1400 : 450);

      feedback.style.display = 'block';
      feedback.innerHTML = `<strong>${isCorrect ? '✓ 直觉敏锐！' : '✕ 直觉受到挑战：'}</strong> ${q.exp}`;
      $('quizScore').textContent = `正确直觉：${userScore}`;
    };
  });
}

$('nextQuizBtn').onclick = () => {
  currentQ = (currentQ + 1) % quizQuestions.length;
  renderQuiz();
  audio.clickSound(900);
};
$('prevQuizBtn').onclick = () => {
  currentQ = (currentQ - 1 + quizQuestions.length) % quizQuestions.length;
  renderQuiz();
  audio.clickSound(800);
};
renderQuiz();

/* ==========================================================================
   12. REDUCED MOTION TOGGLE
   ========================================================================== */
const motionBtn = $('motionToggle');
const savedMotion = localStorage.getItem('cosmos_reduce_motion_v3');
if (savedMotion === 'true') {
  document.documentElement.classList.add('reduced-motion');
  motionBtn.textContent = '动效: 关';
}

motionBtn.onclick = () => {
  const isReduced = document.documentElement.classList.toggle('reduced-motion');
  motionBtn.textContent = isReduced ? '动效: 关' : '动效: 开';
  localStorage.setItem('cosmos_reduce_motion_v3', isReduced);
  audio.clickSound(950);
  if (!isReduced) {
    animateStars();
    drawLensing();
    drawTransitCurve();
  }
};
"""
