from pathlib import Path
import html, json, re

ROOT = Path(__file__).resolve().parent

SITE_NAME = '共同等候｜Quaker Meeting 研究与实践'
TAGLINE = '研究贵格会 Meeting 如何通过静默、共同聆听与群体明辨，让尚未被任何个人完全拥有的真实，有机会出现。'

NAV = [
    ('index.html','首页'),
    ('meeting.html','Meeting'),
    ('worship.html','静默敬拜'),
    ('practice.html','开始实践'),
    ('business.html','共同明辨'),
    ('clearness.html','澄心会'),
    ('learning.html','共学'),
    ('history.html','历史'),
    ('comparisons.html','比较'),
    ('glossary.html','术语'),
    ('research.html','研究室'),
]


def icon(name):
    icons = {
        'light':'<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="5"/><circle cx="24" cy="24" r="12" fill="none"/><circle cx="24" cy="24" r="20" fill="none" opacity=".45"/></svg>',
        'silence':'<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M8 24h32M14 17h20M14 31h20" fill="none"/></svg>',
        'group':'<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="15" r="5"/><circle cx="13" cy="28" r="4"/><circle cx="35" cy="28" r="4"/><path d="M16 38c2-6 14-6 16 0M7 39c1-4 8-5 11-2M30 37c3-3 10-2 11 2" fill="none"/></svg>',
        'question':'<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M17 17c1-7 14-8 16 0 1 5-3 7-7 9-2 1-2 3-2 5" fill="none"/><circle cx="24" cy="38" r="2"/></svg>',
        'book':'<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M8 10c8-2 13 0 16 3 3-3 8-5 16-3v26c-8-2-13 0-16 3-3-3-8-5-16-3z" fill="none"/><path d="M24 13v26" fill="none"/></svg>',
        'path':'<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M8 40c10-6 6-14 16-20s8-10 16-12" fill="none"/><circle cx="9" cy="39" r="3"/><circle cx="39" cy="9" r="3"/></svg>',
    }
    return icons.get(name, icons['light'])


def circle_visual():
    seats = []
    pts = [(50,12),(74,20),(88,42),(82,69),(61,86),(34,86),(15,67),(12,39),(28,19)]
    for x,y in pts:
        seats.append(f'<g class="seat"><circle cx="{x}" cy="{y}" r="4.6" fill="#d8ddd8"/><path d="M{x-7} {y+9}q7-5 14 0" fill="none" stroke="#aab5ad" stroke-width="1.4" stroke-linecap="round"/></g>')
    return f'''<div class="circle-visual" aria-label="围坐的 Meeting 示意图">
    <svg viewBox="0 0 100 100" role="img">
      <defs><radialGradient id="halo"><stop offset="0" stop-color="#d7b76a" stop-opacity=".72"/><stop offset="1" stop-color="#d7b76a" stop-opacity="0"/></radialGradient></defs>
      <circle class="halo h1" cx="50" cy="50" r="10" fill="url(#halo)"/>
      <circle class="halo h2" cx="50" cy="50" r="18" fill="none"/>
      <circle class="halo h3" cx="50" cy="50" r="27" fill="none"/>
      {''.join(seats)}
      <circle cx="50" cy="50" r="2.3" class="center-dot" fill="#b49a5c"/>
    </svg>
    <p>圆心没有讲台，也不属于任何一个人。</p>
    </div>'''


def layer_visual():
    labels = [('Center','Light / Truth'),('Inward','settling · waiting'),('Between','listening · ministry'),('Corporate','unity · discernment'),('Outward','concern · action')]
    circles=''
    rs=[20,35,50,65,80]
    for i,(a,b) in enumerate(labels):
        circles += f'<circle cx="100" cy="100" r="{rs[i]}" class="layer l{i+1}"/>'
    return f'''<div class="layer-diagram"><svg viewBox="0 0 200 200" role="img" aria-label="Meeting 五层模型">{circles}<circle cx="100" cy="100" r="4" class="core"/></svg>
      <div class="layer-legend">{''.join(f'<div><b>{i+1:02d}</b><span><strong>{a}</strong><small>{b}</small></span></div>' for i,(a,b) in enumerate(labels))}</div></div>'''


def triad_visual():
    return '''<div class="triad-visual" aria-label="Meeting for Learning 的三方关系">
      <svg viewBox="0 0 560 360" role="img">
        <path d="M120 270 L280 75 L440 270 Z" class="triad-line"/>
        <circle cx="120" cy="270" r="48"/><circle cx="440" cy="270" r="48"/><circle cx="280" cy="75" r="55" class="third"/>
        <text x="120" y="266">人</text><text x="120" y="288" class="sub">Person</text>
        <text x="440" y="266">人</text><text x="440" y="288" class="sub">Person</text>
        <text x="280" y="69">第三物</text><text x="280" y="92" class="sub">Third Thing</text>
        <text x="280" y="225" class="center-label">Truth emerges in relation</text>
      </svg>
    </div>'''


def decision_visual():
    return '''<div class="decision-visual"><div class="decision-track">
      <span>议题进入</span><i>→</i><span>事实与处境</span><i>→</i><span>静默</span><i>→</i><span>听取贡献</span><i>→</i><span>再次静默</span><i>→</i><span>Clerk 试写 minute</span><i>→</i><span>Meeting 检验</span><i>→</i><strong>行动 / 等待</strong>
    </div><p>重点不是“更快表决”，而是辨认群体是否真的清楚到可以行动。</p></div>'''


def source_box(items):
    lis=''.join(f'<li><b>{html.escape(t)}</b><span>{html.escape(d)}</span></li>' for t,d in items)
    return f'<aside class="sources"><div class="source-head">{icon("book")}<div><span>本页主要依据</span><strong>Primary sources</strong></div></div><ul>{lis}</ul><a href="research.html" class="text-link">进入研究室 →</a></aside>'


def callout(title, body, tone='light'):
    return f'<div class="callout {tone}"><strong>{title}</strong><div>{body}</div></div>'


def query_cards(qs):
    return '<div class="query-grid">' + ''.join(f'<article class="query-card"><span>QUERY {i+1:02d}</span><p>{q}</p></article>' for i,q in enumerate(qs)) + '</div>'


def smart_heading(text):
    """Prefer semantic/punctuation break opportunities without forcing a line break."""
    safe = html.escape(text)
    for token in ['，', '：', '；', '？', '。', '——', '｜', ' / ', ' · ']:
        safe = safe.replace(token, token + '<wbr>')
    return safe


def enhance_plain_headings(doc):
    """Add semantic break opportunities to plain-text h1/h2/h3 left in hand-authored blocks."""
    pattern = re.compile(r'<(h[1-3])([^>]*)>([^<]+)</\1>')
    def repl(match):
        tag, attrs, text_only = match.groups()
        return f'<{tag}{attrs}>{smart_heading(html.unescape(text_only))}</{tag}>'
    return pattern.sub(repl, doc)


def research_note(title, body, label='研究札记'):
    return f'''<aside class="research-card"><span>{label}</span><h3>{smart_heading(title)}</h3><div>{body}</div></aside>'''


def epistemology_visual():
    return '''<figure class="concept-figure"><svg viewBox="0 0 760 420" role="img" aria-label="Meeting 的三重检验：个人经验、共同体、历史传统">
      <defs><filter id="soft"><feGaussianBlur stdDeviation="18"/></filter></defs>
      <circle cx="300" cy="190" r="118" class="field a"/><circle cx="460" cy="190" r="118" class="field b"/><circle cx="380" cy="300" r="118" class="field c"/>
      <circle cx="380" cy="225" r="48" class="center-glow"/>
      <text x="245" y="155">个人经验</text><text x="514" y="155">共同体检验</text><text x="380" y="360">历史与实践传统</text>
      <text x="380" y="218" class="figure-main">Discernment</text><text x="380" y="243" class="figure-sub">不是任何单一来源说了算</text>
    </svg><figcaption><b>一种“共同体认识论”</b><span>经验被认真对待，却不被绝对化；群体提供检验，却不取代良知；传统提供语言与记忆，却不停止新的发现。</span></figcaption></figure>'''


def discernment_visual():
    return '''<figure class="concept-figure compact"><svg viewBox="0 0 760 360" role="img" aria-label="Leadings 的四重检验">
      <path d="M380 70V290M180 180H580" class="axis"/>
      <circle cx="380" cy="180" r="56" class="center-glow"/>
      <circle cx="380" cy="70" r="34" class="node"/><circle cx="580" cy="180" r="34" class="node"/><circle cx="380" cy="290" r="34" class="node"/><circle cx="180" cy="180" r="34" class="node"/>
      <text x="380" y="76">时间</text><text x="580" y="186">果实</text><text x="380" y="296">共同体</text><text x="180" y="186">持续性</text>
      <text x="380" y="175" class="figure-main">Leading?</text><text x="380" y="199" class="figure-sub">让冲动接受检验</text>
    </svg><figcaption><b>辨识不是一次“直觉确认”</b><span>Patricia Loring 强调，重要引领需要等待、观察其果实，并放入可信任的共同体中检验；急迫感本身不等于真实性。</span></figcaption></figure>'''


def silence_visual():
    return '''<figure class="concept-figure compact"><svg viewBox="0 0 760 330" role="img" aria-label="从噪声到静默等候，再回到行动">
      <path d="M95 165 C210 70 270 70 350 165 S510 260 665 165" class="wave"/>
      <path d="M95 165 C205 230 275 225 350 165 S515 105 665 165" class="wave faint"/>
      <circle cx="350" cy="165" r="68" class="center-glow"/><circle cx="350" cy="165" r="8" class="core-dot"/>
      <text x="125" y="285">纷杂 / 反应</text><text x="350" y="285">等待 / 可被触动</text><text x="615" y="285">清晰 / 行动</text>
    </svg><figcaption><b>静默不是“关掉自己”</b><span>更像把注意从自动反应中松开，使某些原本被噪声盖住的关系、责任或方向逐渐可见。</span></figcaption></figure>'''


def section(title, body, eyebrow=None, cls=''):
    ey=f'<div class="section-eyebrow">{eyebrow}</div>' if eyebrow else ''
    return f'<section class="content-section {cls}">{ey}<h2>{smart_heading(title)}</h2>{body}</section>'


def page_shell(filename, title, intro, body, label='研究与实践', extra_js=''):
    nav = ''.join(f'<a href="{u}" class="{"active" if filename==u else ""}">{t}</a>' for u,t in NAV)
    hero_html = '' if filename == 'index.html' else f'''<section class="page-hero"><div class="hero-copy"><span class="kicker">{label}</span><h1>{smart_heading(title)}</h1><p>{intro}</p><div class="hero-line"></div></div></section>'''
    doc_title = SITE_NAME if filename == 'index.html' else f'{title}｜{SITE_NAME}'
    return f'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{html.escape(doc_title)}</title>
<meta name="description" content="{html.escape(intro[:155])}"/>
<meta name="theme-color" content="#1f2723"/>
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml"/>
<link rel="stylesheet" href="assets/style.css"/>
</head>
<body data-page="{filename}">
<a class="skip-link" href="#main">跳到正文</a>
<header class="site-header">
  <a class="brand" href="index.html"><span class="brand-mark"><i></i><i></i><i></i></span><span><b>共同等候</b><small>Quaker Meeting Lab</small></span></a>
  <button class="nav-toggle" aria-label="打开导航">☰</button>
  <nav class="main-nav">{nav}</nav>
</header>
<main id="main">
{hero_html}
{body}
</main>
<footer class="site-footer"><div><b>共同等候｜Quaker Meeting 研究与实践</b><p>这是一个中文研究与实践项目，不代表任何贵格会年会或官方机构。</p></div><div class="footer-links"><a href="research.html">来源与研究方法</a><a href="glossary.html">术语表</a><a href="practice.html">开始一次练习</a></div><p class="footer-note">Designed for slow reading, careful listening, and lived practice.</p></footer>
<script src="assets/app.js"></script>{extra_js}
</body></html>'''

# --- Home page ---
index_body = f'''
<section class="home-hero"><div class="home-copy"><span class="kicker">QUAKER MEETING · 研究 × 实践</span><h1>{smart_heading('在静默中，共同聆听。')}</h1><p>{TAGLINE}</p><div class="cta-row"><a class="btn primary" href="practice.html">体验一次 12 分钟 Meeting</a><a class="btn ghost" href="meeting.html">先理解 Meeting 是什么</a></div><div class="hero-note"><span></span>不是冥想 App，也不是宗教百科；这是一个把 Meeting 当作“共同聆听、共同检验与共同明辨的方法”来研究的网站。</div></div>{circle_visual()}</section>
<section class="home-intro"><div class="big-question"><span>THE QUESTION</span><h2>{smart_heading('如果一群人暂时不争着表达立场，会不会有一些东西，反而更容易被听见？')}</h2></div><div class="intro-copy"><p>贵格会 Meeting 最令人着迷的地方，不只是“安静”。真正独特的是：一群人共同停下来，不把某个人、某套理论或某种程序放在中心，而是通过等待、聆听、说与不说，让一个更深的共同辨识逐渐出现。</p><p>Howard Brinton 把 Quakerism 描述为一种以经验为基础的 <em>method</em>，并把它称为一种 <em>group mysticism</em>：内在经验不是终点，必须进入群体、历史与行动。Parker Palmer 又把 “meeting” 这一精神延伸到学习，使它成为一种关于“我们怎样共同认识真实”的实践。</p></div></section>
<section class="home-depth"><div class="section-head"><span>WHY IT MATTERS</span><h2>{smart_heading('Meeting 不只是安静下来，而是在练习“如何共同认识”')}</h2><p>它既涉及灵性，也涉及认识论、群体动力、组织治理与伦理行动。</p></div>{epistemology_visual()}<div class="depth-grid"><article><span>01</span><h3>经验，不等于任性</h3><p>个人经验被认真对待，但重要的 leading 需要时间、共同体与生活后果的检验。</p></article><article><span>02</span><h3>群体，不等于多数</h3><p>Meeting 重视 corporate discernment，却不把人数优势当作 Truth 的替代品。</p></article><article><span>03</span><h3>静默，不等于退避</h3><p>Thomas Kelly 与 Brinton 都把 inward life 指向 outward action：内在聆听若有生命，会进入关系、决定与公共见证。</p></article></div></section>
<section class="home-map"><div class="section-head"><span>ONE MAP</span><h2>一张图，理解 Meeting 的五个层次</h2><p>从“我里面发生什么”，到“我们如何一起行动”。</p></div>{layer_visual()}<div class="map-links"><a href="worship.html"><b>01</b><span>静默与等候<small>Silence / Waiting</small></span></a><a href="ministry.html"><b>02</b><span>说与不说<small>Vocal Ministry</small></span></a><a href="gathered.html"><b>03</b><span>被聚集的时刻<small>Gathered Meeting</small></span></a><a href="business.html"><b>04</b><span>共同明辨<small>Sense of the Meeting</small></span></a><a href="toolkit.html"><b>05</b><span>进入日常<small>Practice & Action</small></span></a></div></section>
<section class="meeting-family"><div class="section-head"><span>MEETING FAMILY</span><h2>Meeting 不是只有一种</h2></div><div class="family-grid">
<a href="worship.html"><span>01</span><h3>Meeting for Worship</h3><p>共同静默、等候、聆听；必要时出现受感分享。</p></a>
<a href="business.html"><span>02</span><h3>Meeting for Worship for Business</h3><p>不以投票决定，而在敬拜精神中辨认群体是否形成清晰。</p></a>
<a href="clearness.html"><span>03</span><h3>Clearness Committee</h3><p>以开放问题、静默和保密，帮助一个人更清楚地听见自己的引领。</p></a>
<a href="learning.html"><span>04</span><h3>Meeting for Learning</h3><p>让人、人和“第三物”真正相遇，把学习从信息摄取变成共同探寻。</p></a>
</div></section>
<section class="practice-banner"><div><span>不要只读。</span><h2>Meeting 最终只能通过 Meeting 来理解。</h2><p>先做一次 12 分钟练习。没有指导语轰炸，也没有“放松成功”的要求。</p></div><a class="btn inverted" href="practice.html">进入实践 →</a></section>
<section class="reading-path"><div class="section-head"><span>TWO PATHS</span><h2>你可以这样进入</h2></div><div class="path-grid"><article><span>第一次接触</span><ol><li><a href="meeting.html">Meeting 到底是什么？</a></li><li><a href="worship.html">静默不是空白</a></li><li><a href="practice.html">12 分钟体验</a></li><li><a href="ministry.html">什么时候该说话？</a></li><li><a href="business.html">为什么不投票？</a></li></ol></article><article><span>想刨根究底</span><ol><li><a href="history.html">从 Seekers 到现代</a></li><li><a href="gathered.html">Gathered Meeting</a></li><li><a href="research.html">原典与研究书目</a></li><li><a href="comparisons.html">与其他方法比较</a></li><li><a href="glossary.html">建立术语坐标</a></li></ol></article></div></section>
'''

pages = {}
pages['index.html'] = page_shell('index.html','共同等候',TAGLINE,index_body,label='QUAKER MEETING LAB')

# --- Meeting overview ---
meeting_body = f'''
<div class="article-grid"><article class="article-main">
{section('Meeting：不是“会议”的同义词','''<p>在贵格会语境里，<strong>Meeting</strong> 同时指一次聚集、一个持续存在的共同体，也指一种特殊的共同实践。把它全部翻成“会议”，会让最重要的东西消失。</p><p>在 Meeting 中，中心并不预先被一个讲者、主持人、教义或议程占据。人们首先做的，是让自己安顿下来，进入一种共同的等待：不急着制造结果，也不假装什么都没有发生。</p>''','01 · DEFINITION')}
{callout('一个抓手','<p><strong>Meeting 可以理解为：一群人共同为“尚未完全显现的真实”腾出空间。</strong></p><p>这不是严格定义，却是理解 Worship、Business、Clearness 和 Learning 的共同钥匙。</p>')}
{section('为什么 Brinton 说 Quakerism 首先是一种 method？','''<p>Howard Brinton 的一个关键判断是：要理解贵格会，不能只列出“它相信什么”，还要看<strong>它如何抵达、检验和修正这些相信</strong>。因此他把 Quakerism 比作一种方法：它不像科学那样测量外部对象，而是面向内在生命、道德要求、宗教洞见与群体经验。</p><p>这使 Meeting 变成一种持续的认识实践。经验很重要，但经验不是“我感觉如此，所以就是真理”；它需要在时间、历史、共同体与行动后果中不断被检验。也正因为如此，Brinton 所说的 <em>group mysticism</em> 不是一群人各自拥有神秘体验，而是个人经验在共同体中被承接、修正并获得社会形态。</p>'''+research_note('把“体验”变成“可检验的实践”','''<p>如果只强调 inward experience，Meeting 很容易滑向私人灵性消费；如果只强调组织规则，它又会失去直接经验的生命。贵格会长期存在的张力，正是在两者之间保持开放：既不把权威外包给制度，也不把权威收回到个人情绪。</p>'''), '02 · METHOD')}
{section('它与“大家一起静坐”有什么不同？','''<div class="compare-mini"><div><b>一起静坐</b><p>重点可能在个体专注、觉察、放松或禅修。</p></div><div><b>Quaker Meeting</b><p>个人内在安顿很重要，但始终处在一个群体场域中：我在听自己，也在听这个房间、这个共同体，以及可能超越个人意志的引领。</p></div></div><p>Jim Pym 早年把 Meeting 误以为 meditation group，后来才意识到它并不是佛教意义上的冥想团体。这种误解今天依然非常普遍。</p>''','02 · NOT JUST MEDITATION')}
{section('五个层次同时发生','''<p>一个成熟的 Meeting 往往同时有五个层次。它们不是五步流程，而是五种可以被观察的维度。</p>'''+layer_visual()+'''<div class="definition-list"><dl><dt>Center</dt><dd>这个圆圈最终忠于什么？早期 Friends 会说 God、Christ、Truth、Light；现代不同传统的 Friends 会使用不同语言。</dd><dt>Inward</dt><dd>我是否从惯性反应、紧张和自我表演中稍微退开，变得可听？</dd><dt>Between</dt><dd>我如何听别人？一句 spoken ministry 如何被整个房间接住，而不是立刻讨论？</dd><dt>Corporate</dt><dd>群体有没有出现一种任何单个人都无法制造的清晰、深度或 unity？</dd><dt>Outward</dt><dd>这份清晰最后如何进入决定、关系、工作与社会行动？</dd></dl></div>'''+epistemology_visual(), '03 · FIVE LAYERS')}
{section('Inner Light 不是“我的感觉就是对的”','''<p>“内在之光”最容易在现代语境里被误读成直觉主义：只要我内在有强烈感觉，就应该忠于它。Michael Marsh 对这一点提出了有价值的哲学追问：<strong>Light 是一个隐喻，它让原本隐藏的关系变得可见；但“看见”本身不自动保证客观正确。</strong></p><p>Patricia Loring 也从实践面提醒：我们内部同时存在愿望、恐惧、自我意志、父母和文化留下的声音。所谓 discernment，恰恰是学习分辨这些声音，而不是把“来自内在”当作免检标签。</p>'''+research_note('专业性来自“允许复杂性存在”','''<p>一个成熟的 Meeting 不急着把 Light 心理学化，也不急着把所有体验神学化。它更像一套长期实践：经验出现——停下来——交给时间——交给共同体——观察果实——再决定是否行动。</p>'''), '04 · INNER LIGHT')}
{section('最常见的七个误解','''<div class="myth-grid"><article><b>“就是沉默一小时”</b><p>沉默只是外在形式；核心是 expectant waiting。</p></article><article><b>“每个人做自己的内观”</b><p>Meeting 是群体实践，不是并排进行的私人练习。</p></article><article><b>“想说就说”</b><p>传统上 spoken ministry 需要经过内在辨识。</p></article><article><b>“没有领导者”</b><p>不是没有角色，而是角色不拥有 Truth。Clerk、elders 等都服务于共同体。</p></article><article><b>“没有教义，所以什么都可以”</b><p>贵格会长期以 experience、testimony、community testing 形成非常严肃的纪律。</p></article><article><b>“不投票就是共识决策”</b><p>Sense of the Meeting 与现代 consensus 有重叠，但目标与精神基础并不相同。</p></article><article><b>“安静一定会让人平静”</b><p>真正的聆听也可能让人面对不愿承认的冲突、责任或召唤。</p></article></div>''','05 · MISUNDERSTANDINGS')}
{section('一个极简观察框架','''<div class="process-row"><span>Arrive</span><i>→</i><span>Settle</span><i>→</i><span>Wait</span><i>→</i><span>Listen</span><i>→</i><span>Speak / Remain Silent</span><i>→</i><span>Return</span></div><p class="fineprint">注意：这不是“Quaker Meeting 六步法”。它只是本站为了帮助初学者观察内部动态而做的一张地图。</p>''','05 · OBSERVE')}
{section('带着这些问题继续','''<p>贵格会传统喜欢用 Queries 而不是“标准答案”结束学习。你也可以从这几个问题继续。</p>'''+query_cards(['当我安静下来时，我最先遇到的通常是什么：焦躁、计划、疲惫，还是别的东西？','我能否分辨“我很想表达”与“这句话真的需要被这个圆圈听见”之间的差别？','如果一个群体迟迟没有形成清晰，我是否愿意把“暂不决定”也看作一种成熟的结果？']))}
</article>{source_box([('Howard H. Brinton, Friends for 300 Years','重点参见第4章 The Meeting for Worship、第5章 Vocal Ministry、第6章 Reaching Decisions。'),('Jim Pym, Listening to the Light','“The Source—the Quaker meeting for worship” 与 “A New Way of Working”。'),('Parker J. Palmer, Meeting for Learning','以 Meeting 作为教育与共同探寻的核心隐喻。')])}</div>
'''
pages['meeting.html'] = page_shell('meeting.html','Meeting 到底是什么？','它不是“会议”的简单翻译，也不只是多人静坐。理解 Meeting，要同时看到内在、关系、群体与行动四个方向。',meeting_body)

# --- worship ---
worship_body = f'''
<div class="article-grid"><article class="article-main">
{section('静默不是空白','''<p>贵格会 Meeting 的静默常常被误解为“清空头脑”。但传统中的 waiting 更接近<strong>带着期待的开放</strong>：人不必把念头清掉，也不急着跟随每个念头，而是让注意力逐渐从惯性反应中松开。</p><p>Brinton 在讨论 worship 时强调，与其说要消灭纷乱思想，不如说要“活在那超越它们的地方”。这使静默不是一种对心智的暴力控制，而是一种重新排序注意力的方式。</p>''','01 · SILENCE')}
{section('Silence → Waiting → Worship','''<div class="three-stage"><article><span>01</span><h3>Silence</h3><p>外在声音减少，身体和注意力开始有空间。</p></article><article><span>02</span><h3>Waiting</h3><p>不只是没有讲话，而是期待某种尚未被制造出来的清晰。</p></article><article><span>03</span><h3>Worship</h3><p>等待带有关系性：我把自己置于 Light / Truth / God 的可能引领之下。</p></article></div>''','02 · THREE DEPTHS')}
{silence_visual()}
{callout('重要区别','<p><strong>静默是外在条件；waiting 是内在姿态；worship 是关系与方向。</strong></p>','dark')}
{section('“等候”为什么不是一种注意力技巧？','''<p>如果只从心理训练看，waiting 很容易被理解成“延迟反应”或“保持开放”。这些描述有帮助，却还没有触到传统语境的全部。对早期 Friends 而言，等候之所以有方向，是因为他们相信 Divine Presence 并非缺席；人不是在制造启示，而是在学习停止遮蔽、停止抢先。</p><p>这也是为什么 Brinton 会说，Quaker worship 把“God reveals himself directly”这一信念推到实践层面：如果启示并非只属于过去，那么 worship 的基本动作就不是不断填充语言，而是 reverent waiting 与 listening。</p>'''+research_note('历史语言与当代语言之间，需要保持张力','''<p>今天一些 liberal Friends 会更多使用 Truth、Light、Life、Love 或 inward guidance；另一些 Friends 仍明确以 Christ、Scripture 与 Holy Spirit 为中心。把所有这些语言强行统一，会失去传统内部真实存在的差异。本站会尽量标注语境，而不是把某一支当成全部。</p>'''), '03 · THEOLOGICAL DIRECTION')}
{section('进入 Meeting 时，具体可以怎么做？','''<div class="practice-steps"><article><b>先允许自己还没有安静</b><p>注意身体接触椅子、脚底、呼吸和房间里的声音。不要把“马上进入状态”变成新任务。</p></article><article><b>不追赶每一个念头</b><p>你可以知道它在，却不必完成它。计划、回忆、情绪都可以经过。</p></article><article><b>从“我要做什么”转向“有什么值得被听见”</b><p>不是逼自己找答案，而是让问题在空间里待一会儿。</p></article><article><b>同时听房间</b><p>Meeting 不是私人练习。感受其他人的存在，不必想象他们在做什么。</p></article><article><b>有人说话后，不立即回应</b><p>让话语重新落回静默。它可能不是讨论的开端，而是共同聆听的一部分。</p></article></div>''','03 · HOW TO ENTER')}
{section('杂念怎么办？','''<p>最容易把初学者带偏的问题，就是：“怎样才能没有杂念？” Meeting 并不要求达到某种纯净意识状态。一个更实用的观察方式是：</p><div class="ladder"><div><span>念头出现</span><p>我注意到了。</p></div><div><span>自动跟随</span><p>我已经在心里写完三封邮件。</p></div><div><span>重新回来</span><p>不责备，重新感到身体、房间、等待。</p></div><div><span>渐渐变深</span><p>某些念头退到背景，某些问题反而显出重量。</p></div></div>''','04 · DISTRACTION')}
{section('什么时候结束？','''<p>正式 Meeting 的结束方式因群体而异，常见做法是 designated Friends 握手，其他人随之握手，表示 worship 已结束。本站的练习采用轻微提示音，只是数字环境中的替代。</p><p>更重要的是：结束不意味着把静默留在房间。Thomas Kelly 的一个核心关切，正是让内在注意逐渐进入日常行动，使“内在圣所”成为工作日也可返回的参照。</p>''','05 · RETURN')}
{section('从 inward life 到 workaday life','''<p>Thomas Kelly 反复强调，内在生命若只发生在固定的安静时段，仍然是不完整的。他所描述的是一种“同时生活在两层”的能力：表层继续工作、说话、做决定；更深一层保持对 Light 的注意。</p><p>这使 Meeting 的价值不在于把人从生活中抽离，而在于训练一种能够回到市场、办公室、家庭与公共事务中的注意方式。外在见证不是附加的“公益活动”，而是 inward attention 结出的果实。</p>'''+research_note('一个可观察的检验','''<p>一次 Meeting 是否“有效”，不只看当场是否平静、感动或深刻。更值得问的是：离开以后，我是否更诚实？更能承担关系？更少被自我防卫驱动？更愿意做一件代价真实、但更忠实的事？</p>'''), '06 · EVERYDAY LIGHT')}
{section('试着这样观察下一次静默', query_cards(['我是在等“某件事发生”，还是在练习不预设会发生什么？','沉默里最难放下的是什么：控制、效率、表现、解释，还是被看见的需要？','如果我把今天一个真实处境带入 Light 中重新看，它的意义有没有发生一点变化？']) + '<div class="cta-inline"><a class="btn primary" href="practice.html">开始 12 分钟体验</a><a class="btn ghost" href="ministry.html">继续：什么时候该说话？</a></div>', '07 · PRACTICE')}
</article>{source_box([('Howard H. Brinton, Friends for 300 Years','第4章 The Meeting for Worship，尤其关于 waiting、silence、unity 与 worship 的讨论。'),('Thomas R. Kelly, The Light Within','关于持续的 inward orientation，以及把内在之光带入日常行动。')])}</div>
'''
pages['worship.html'] = page_shell('worship.html','静默，不是什么都不做','从 Silence 到 Waiting，再到 Worship：贵格会静默的关键不是“脑中无念”，而是从立即反应中退开，进入共同等候。',worship_body)

# --- practice ---
practice_body = f'''
<section class="practice-intro"><div><span class="kicker">12 MINUTES · BEGINNER PRACTICE</span><h2>一次尽量少指导的 Meeting 体验</h2><p>这不是正式 Meeting for Worship 的替代品，而是一段帮助初学者理解“共同等候”内部质感的数字练习。最好把手机调静音，坐直但不僵硬，允许自己不进入任何特殊状态。</p></div><div class="practice-rules"><span>不追求放松</span><span>不强迫清空</span><span>不解释体验</span><span>不急着得答案</span></div></section>
<section class="timer-shell"><div class="timer-top"><div><span id="stageIndex">准备</span><h2 id="stageTitle">坐下来，让自己到达这里。</h2><p id="stagePrompt">注意身体、房间和此刻的状态。不需要马上安静。</p></div><div class="timer-circle"><svg viewBox="0 0 120 120"><circle class="timer-bg" cx="60" cy="60" r="52"/><circle id="timerProgress" class="timer-progress" cx="60" cy="60" r="52"/></svg><strong id="timeDisplay">12:00</strong></div></div><div class="timer-controls"><button class="btn primary" id="startTimer">开始</button><button class="btn ghost" id="pauseTimer">暂停</button><button class="btn ghost" id="resetTimer">重置</button></div><div class="stage-track" id="stageTrack"></div></section>
<section class="after-practice"><div class="section-head"><span>AFTER</span><h2>结束后，不急着评价“做得好不好”</h2><p>只记录一点事实。记录会保存在当前浏览器中，不会上传。</p></div><div class="reflection-grid"><label>刚才什么最明显？<textarea id="r1" placeholder="例如：很躁、听到空调、某个问题一直回来……"></textarea></label><label>有没有什么变得稍微清楚？<textarea id="r2" placeholder="不必是答案，也可以只是一个感觉或方向。"></textarea></label><label>我现在想带走什么？<textarea id="r3" placeholder="一个问题、一句提醒、一件准备去做或暂时不做的事。"></textarea></label></div><div class="reflection-actions"><button class="btn primary" id="saveReflection">保存到本机</button><button class="btn ghost" id="clearReflection">清空</button><span id="saveStatus"></span></div></section>
<section class="content-section"><div class="section-head"><span>NEXT</span><h2>这 12 分钟里，你其实在练习什么？</h2></div><div class="skill-grid"><article>{icon('silence')}<h3>Settling</h3><p>从外部刺激与内部惯性中慢慢收回注意。</p></article><article>{icon('light')}<h3>Waiting</h3><p>不预设答案，却保持可被触动的状态。</p></article><article>{icon('group')}<h3>Corporate attention</h3><p>即使不说话，也把自己理解为群体的一部分。</p></article><article>{icon('question')}<h3>Discernment</h3><p>分辨“很多声音”里，哪些值得继续等待和检验。</p></article></div>{callout('下一步','<p>真正的 Meeting 需要人与人同处。数字练习只能帮你熟悉一些内在动作。下一步最好是参加真实 Meeting，或与 3–8 位伙伴举行一次 30–45 分钟的简化实践。</p>')}</section>
<section class="content-section"><div class="section-head"><span>FROM SOLO TO CORPORATE</span><h2>不要把 12 分钟练习误当成 Meeting 的缩小版</h2><p>个人练习只能帮助你熟悉 settling 与 waiting。真正独特的部分，要等到“别人也在场”以后才开始出现。</p></div><div class="practice-ladder-v2"><article><span>01 · SOLO</span><h3>12 分钟个人练习</h3><p>认识自己的自动反应：急于找答案、追念头、追求特殊状态。</p></article><article><span>02 · SMALL GROUP</span><h3>30–45 分钟共同静默</h3><p>开始练习 corporate attention：别人存在，却不需要被我分析、照顾或回应。</p></article><article><span>03 · MINISTRY</span><h3>学习“说与不说”</h3><p>让 insight 经历等待；区分“我想表达”与“这个 Meeting 需要听见”。</p></article><article><span>04 · DISCERNMENT</span><h3>把真实议题带进群体</h3><p>当群体具有足够信任与纪律，再进入 clearness、business 与共同辨识。</p></article></div></section>
'''
pages['practice.html'] = page_shell('practice.html','开始实践','少一点引导，留多一点空间。用 12 分钟亲自体验 settling、waiting 与 listening，而不是把 Meeting 只理解成概念。',practice_body,label='PRACTICE')

# --- ministry ---
ministry_body = f'''
<div class="article-grid"><article class="article-main">
{section('Vocal Ministry：不是“自由发言”','''<p>在 unprogrammed Meeting 中，任何人都有可能站起来说话，但这并不意味着“想到什么就分享什么”。传统中的 ministry 是经过等待、辨识，并感到这句话可能不仅属于“我”，也可能服务于整个 Meeting 的发言。</p><p>Brinton 明确指出：vocal ministry 很重要，却不是 Meeting 的必要元素。一次全程静默的 Meeting 完全可以是完整的；相反，没有真正来源的发言，反而可能削弱 worship。</p>''','01 · MINISTRY')}
{research_note('Ministry 的问题不是“我有没有表达欲”，而是“这句话是否属于这个共同体”','''<p>现代文化容易把真诚等同于即时表达；Quaker discipline 恰好相反：真诚还要接受等待。一个强烈、感人、聪明的念头，也可能只是“属于我”的材料，而不是 spoken ministry。成熟不是压抑表达，而是让表达承担关系责任。</p>''')}
{section('一句话从出现到说出，中间可以有一段路','''<div class="ministry-flow"><span>一个念头出现</span><i>↓</i><span>先不急着说</span><i>↓</i><span>它是否持续？</span><i>↓</i><span>它是否需要这个房间？</span><i>↓</i><span>我愿不愿意承担说出它的风险？</span><i>↓</i><strong>说 / 继续沉默</strong></div>''','02 · TESTING')}
{section('五个辨识问题','''<p>下面不是“规定”，而是一组帮助初学者减慢冲动的测试问题。点击你此刻真实的答案。</p><div class="discern-box" id="ministryTest"><label><input type="checkbox"/> 这句话已经在我里面停留了一会儿，而不是刚刚闪过。</label><label><input type="checkbox"/> 如果没人回应、没人称赞，我仍然觉得它值得说。</label><label><input type="checkbox"/> 它不是为了纠正上一位、展示知识或把讨论拉回我的主题。</label><label><input type="checkbox"/> 我感到它可能服务于整个房间，而不只是释放自己的情绪。</label><label><input type="checkbox"/> 我也愿意接受：真正忠于它的方式可能是继续不说。</label><button class="btn primary" id="evaluateMinistry">看看提醒</button><p id="ministryResult" class="result-note"></p></div>''','03 · INTERACTIVE')}
{callout('一个反直觉的事实','<p>在 Meeting 中，<strong>“没有说出来”并不等于“没有参与”</strong>。一个人可以忠实地承接一个 insight，却不把它变成 spoken ministry。</p>','dark')}
{section('别人说完之后，为什么不立即接话？','''<p>因为 ministry 不是讨论串。它说完之后，Meeting 通常重新回到静默，让话语进入整个群体，而不是马上被赞同、反驳、解释或延伸。</p><p>这会创造一种很少见的听法：<strong>听完，不马上占有。</strong>有些话会沉下去，有些会消失，有些可能与十分钟后另一个人的话形成意外联系。</p>''','04 · AFTER WORDS')}
{section('一句 ministry 的“权威”从哪里来？','''<p>它不来自说话者的身份，也不来自音量、知识、情绪强度或个人魅力。传统上，ministry 的分量最终要由 Meeting 自己来承接和检验：它是否深化了共同等待？是否把人带向更清楚、更真实、更有责任的地方？还是把注意重新拉回说话者本人？</p><p>这也是 equality testimony 在 worship 中的一个具体表现：任何人可能被使用，任何人也可能判断错误。没有人因为“经常有感动”就获得永久属灵特权。</p>''', '05 · AUTHORITY')}
{section('常见偏差','''<div class="myth-grid"><article><b>讲小型演说</b><p>准备完整观点，上台输出；这更接近 sermon，而非 unprogrammed ministry。</p></article><article><b>接力回应</b><p>“刚才那位让我想到……”很容易把 Meeting 变成 discussion。</p></article><article><b>知识展示</b><p>引用越多并不意味着越有分量。</p></article><article><b>情绪卸载</b><p>真诚很重要，但“我需要说出来”与“这个 Meeting 需要听见”不是同一个判断。</p></article></div>''','06 · PITFALLS')}
{section('Queries', query_cards(['我最常在什么时刻产生“必须说点什么”的冲动？','如果我把自己的 insight 留在静默里，它会变得更深，还是只是消失？','我能否在别人发言后，不立刻判断“赞成/不同意”，而先让它在我里面停留？']), '07 · QUERIES')}
</article>{source_box([('Howard H. Brinton, Friends for 300 Years','第5章 Vocal Ministry：完整静默与 spoken ministry 的关系。'),('Patricia Loring, Spiritual Discernment','关于分辨真正的 leading 与“想分享、想教导、想纠正别人”的冲动。')])}</div>
'''
pages['ministry.html'] = page_shell('ministry.html','什么时候该说话？','Vocal Ministry 不是“想说就说”。真正困难的，往往不是鼓起勇气表达，而是分辨这句话究竟来自哪里、是否属于这个 Meeting。',ministry_body)

# --- gathered ---
gathered_body = f'''
<div class="article-grid"><article class="article-main">
{section('Gathered Meeting：当圆圈变成“一个整体”','''<p>贵格会传统用 <strong>gathered meeting</strong> 描述一种并非每次都会发生、也无法靠技巧强行制造的群体经验：房间仍然是那些人，但注意力、沉默与关系突然有了一种共同的深度。</p><p>它不要求大家拥有相同思想。Brinton 强调，真正的 “together” 并不等于 intellectual agreement，而更接近一种深层、内在的 unity。</p>''','01 · GATHEREDNESS')}
{circle_visual()}
{section('你可能怎样识别它？','''<div class="signal-grid"><article><b>时间感改变</b><p>不是“终于熬完一小时”，而是很少去看时间。</p></article><article><b>沉默有质地</b><p>安静不再像空档，而像房间里有某种共同注意。</p></article><article><b>个人中心感减弱</b><p>仍有个人经验，却不再需要把它全部表达。</p></article><article><b>话语变少但更有重量</b><p>一句简单的话可能被整个群体“听进去”。</p></article><article><b>差异没有消失</b><p>却暂时不再把人推成阵营。</p></article><article><b>离开后仍有余波</b><p>清晰、责任、柔软或行动方向在之后继续发酵。</p></article></div>''','02 · SIGNALS')}
{callout('不要把它变成KPI','<p>Gatheredness 不是每次 Meeting 都必须达到的“高峰体验”。越想制造它，越容易让人表演深刻。传统更强调忠实地准备、等待，并接受一次平淡的 Meeting 也可能是完整的。</p>')}
{section('为什么群体会比个人多出一些东西？','''<p>Brinton 用“多支蜡烛放在一起，光变得更强”来说明 group worship 的群体性。现代语言可以把它理解为：每个人都不是封闭系统；注意力、身体节奏、说话方式、沉默承载力会相互影响。</p><p>但贵格会自己的解释不只停在社会心理学层面。对传统 Friends 而言，这个“多出来的东西”与 Divine Presence、Spirit、Light 和 Truth 的共同临在相关。</p>''','03 · WHY GROUP')}
{section('Group mysticism：既不是“集体情绪”，也不是“大家想法一样”','''<p>Brinton 用 <em>group mysticism</em> 来强调 Quakerism 的一个罕见特征：它不是“独自的人面对神”的简单复制，而是把垂直维度——人与 Divine / Truth 的关系——和水平维度——人与人的关系——放进同一个 worship 事件。</p><p>因此 gatheredness 不能被简化为氛围感。群体可能非常感动，却仍然彼此投射；也可能没有明显情绪高潮，却出现更深的共同清晰。判断标准不是“房间很有能量”，而是注意、关系与行动是否出现更深的整合。</p>'''+research_note('保留双重解释，而不是急着二选一','''<p>心理学可以帮助解释共同节奏、注意同步、社会调节等现象；Quaker 传统则用 Spirit、Presence、Light 等语言理解其来源。专业的研究不需要仓促把其中一方“证明”为另一方，而是清楚区分解释层次。</p>'''), '04 · GROUP MYSTICISM')}
{section('Practice：练习感受“群体”而不是只听自己','''<div class="practice-card"><span>20–30 分钟 · 3–8 人</span><ol><li>围成圆形，不放桌子或只放一个很小的中心物。</li><li>开始前只说明：这是共同静默，不要求分享。</li><li>前 3 分钟感受身体和房间。</li><li>接下来不再给指导；同时留意“我”与“我们”的注意如何变化。</li><li>结束后每人只用一句话回答：“刚才房间里，有什么是我一个人做不出来的？”</li><li>不互相评论。</li></ol></div>''','05 · PRACTICE')}
{section('Queries', query_cards(['我有没有把“群体经验”浪漫化，以至于害怕普通、干燥、没有感觉的 Meeting？','当别人和我意见不同，我是否仍有可能体验到一种不等于认同的 unity？','什么样的空间、节奏与规则，会帮助一群人少一点表演，多一点共同注意？']), '06 · QUERIES')}
</article>{source_box([('Howard H. Brinton, Friends for 300 Years','第4章关于 collective silent worship、unity 与 group meditation 的讨论。'),('Patricia Loring, Spiritual Discernment','Gathered meeting 与 corporate discernment / unity 的关系。')])}</div>
'''
pages['gathered.html'] = page_shell('gathered.html','当 Meeting 被“聚集”','有些 Meeting 只是很多人一起安静；有些时刻，圆圈会出现一种难以归属于任何个人的共同深度。贵格会称之为 gathered meeting。',gathered_body)

# --- business ---
business_body = f'''
<div class="article-grid"><article class="article-main">
{section('为什么一个宗教群体发展出一种独特的决策法？','''<p>17世纪的 Friends 很快就遇到现实问题：救济受迫害者、婚姻、教育、旅行传道、财务、纪律与公共行动都需要组织。但一个强调“内在引领”的群体，怎样避免又建立一个由外部权威支配的制度？</p><p>由此逐渐形成 <strong>Meeting for Worship for Business</strong>：议事不是从 worship 中抽离出来的世俗事务，而是在同一种共同聆听与明辨中处理具体事项。</p>''','01 · ORIGIN')}
{decision_visual()}
{section('Voting、Consensus、Sense of the Meeting','''<div class="compare-table"><div class="row head"><span>机制</span><span>核心问题</span><span>结束条件</span><span>风险</span></div><div class="row"><b>多数表决</b><span>哪个选项票更多？</span><span>达到规则票数</span><span>少数意见被合法压过</span></div><div class="row"><b>Consensus</b><span>我们能接受什么？</span><span>达到足够一致</span><span>可能滑向最低共同点或谈判</span></div><div class="row accent"><b>Sense of the Meeting</b><span>此刻什么方向最忠于 Truth / leading？</span><span>Meeting 形成可被辨认的 unity / clearness</span><span>若缺少敬拜精神，也可能只是假装的“无投票共识”</span></div></div><p>Patricia Loring 特别强调，Quaker unity 不是 agreement、consensus、compromise 或最低共同点。不同意见仍可能存在，但群体可能对“现在应该怎样前进”出现更深的共同清晰。</p>''','02 · THREE MODELS')}
{research_note('为什么“没有反对意见”仍然可能不是 unity？','''<p>沉默可能来自清晰，也可能来自权力差异、疲惫、害怕冲突或对 Clerk 的顺从。因此严肃的 Meeting for Business 会主动听取关键保留意见，尤其当议题重大时。真正的 unity 不是把分歧消音，而是让分歧在共同敬拜中获得足够空间，直到它被理解、转化，或被承认仍然存在。</p>''')}
{section('Clerk：不是主席','''<div class="role-grid"><article><b>Chairperson</b><p>通常负责控制议程、分配发言、维持程序，必要时推动表决。</p></article><article class="accent"><b>Clerk</b><p>准备议程并照看秩序，但关键任务是<strong>听整个 Meeting</strong>：辨认何时接近清晰，并尝试把 emerging sense 写成 minute，交回群体检验。</p></article></div><p>因此 Clerk 的权威不是“我决定”，而是“我试着说出我听见这个 Meeting 正在形成的东西”。如果群体认为措辞不对，minute 就继续修改，甚至整个议题被推迟。</p>''','03 · CLERK')}
{section('互动案例：12个人要不要搬迁社区空间？','''<div class="case-lab" id="caseLab"><div class="case-story"><p><strong>情境</strong>：租约即将到期。新空间更大、更便宜，但离原社区 4 公里。12位核心成员中，7人赞成、3人反对、2人不确定。</p><p>你会怎么处理？</p></div><div class="case-options"><button data-case="vote">A · 现在投票</button><button data-case="consensus">B · 继续协商到大家都能接受</button><button data-case="sense">C · 进入 Meeting for Business 的明辨过程</button></div><div id="caseResult" class="case-result">选择一种路径，看它真正优化的是什么。</div></div>''','04 · CASE LAB')}
{section('什么时候“不决定”反而更成熟？','''<p>Brinton 记录，Friends 在重大议题上可能长时间等待 unity。这个传统很容易被现代组织理解成低效率，但它提醒我们：<strong>“做出决定”与“真正清楚”不是同一件事。</strong></p><p>当然，现实并非所有事项都能无限等待。成熟实践需要区分：哪些只是执行层面的 routine business，哪些会伤及共同体、使命或重大价值，需要更多时间。</p>''','05 · WAITING')}
{section('Minute：不是会后整理，而是现场检验','''<p>Quaker business 中的 minute 常常在现场形成。Clerk 尝试把自己听见的 emerging sense 写成一句或几句清楚的文字，再读回给 Meeting。这个动作非常重要，因为“感觉差不多了”会被迫转化为具体语言。</p><p>文字一旦不准确，隐藏的分歧就会显现出来。于是 minute 既是记录，也是检验工具：群体是在认可同一个方向，还是只是在各自脑中认可不同的东西？</p>'''+research_note('Clerk 的艺术：既不能过早总结，也不能永远不总结','''<p>过早 minute 会把活的明辨压成结论；过晚 minute 又可能让 Meeting 在重复意见中失去方向。Clerk 需要同时听内容、情绪、沉默与群体能量，却不能把个人偏好偷偷写成“Meeting 的声音”。</p>'''), '06 · MINUTE')}
{section('一场 90 分钟 Meeting for Business 的简化模板','''<div class="agenda"><div><b>00–10</b><span>共同静默，重新记住“为何在这里”</span></div><div><b>10–20</b><span>事实澄清：只说已知信息，不抢着立场辩论</span></div><div><b>20–50</b><span>围绕议题贡献，Clerk 保护节奏与静默</span></div><div><b>50–60</b><span>更长静默；让意见从“我的方案”退回共同中心</span></div><div><b>60–75</b><span>Clerk 尝试陈述 emerging sense / draft minute</span></div><div><b>75–85</b><span>Meeting 检验措辞；必要时承认尚未形成 clearness</span></div><div><b>85–90</b><span>静默结束，确认后续责任</span></div></div><p class="fineprint">这是现代学习用模板，不是贵格会统一规定。</p>''','07 · PRACTICAL TEMPLATE')}
</article>{source_box([('Howard H. Brinton, Friends for 300 Years','第6章 Reaching Decisions：无投票、clerk、sense of meeting 与 unity 的历史及方法。'),('Jim Pym, Listening to the Light','“A New Way of Working—the Quaker business method”。'),('Patricia Loring, Spiritual Discernment','关于 meeting for business 中 unity 与 corporate guidance 的解释。')])}</div>
'''
pages['business.html'] = page_shell('business.html','不投票，怎么做决定？','Meeting for Worship for Business 把“议事”重新放回共同聆听：不以多数压倒少数，也不把妥协当成终点，而是辨认群体是否真的清楚。',business_body)

# --- clearness ---
clearness_body = f'''
<div class="article-grid"><article class="article-main">
{section('澄心会不是“大家帮你出主意”','''<p>Clearness Committee 的独特之处，在于它把一个人的重要问题放进一个被保护的群体空间。成员的任务不是诊断、鼓励、说服或给建议，而是通过<strong>开放问题、静默、耐心与保密</strong>，帮助 focal person 更清楚地听见自己的处境与引领。</p><p>本站沿用“<strong>澄心会</strong>”这一中文名称，以避免“委员会”过于行政化。</p>''','01 · CLEARNESS')}
{section('一场澄心会的核心结构','''<div class="clearness-flow"><article><b>带着真实问题进入</b><p>不是“帮我证明已经决定的答案”，而是仍存在真实未知。</p></article><article><b>圆圈承诺保密</b><p>让焦点人不用为之后的社交后果自我审查。</p></article><article><b>只问真问题</b><p>问题不是建议换一个问号。</p></article><article><b>允许大量静默</b><p>问题问完后，不急着补充解释。</p></article><article><b>焦点人拥有自己的辨识</b><p>群体不替他决定。</p></article><article><b>结束后让经验继续发酵</b><p>清晰未必在两小时内完成。</p></article></div>''','02 · STRUCTURE')}
{section('Discernment：真正要分辨的，是“这个声音从哪里来”','''<p>Patricia Loring 把 discernment 看作 Quaker spirituality 的核心实践之一。问题并不是“我有没有强烈感觉”，而是：这个冲动是否持续？它的果实是什么？它是否越来越把我带向诚实、爱、责任与更大的生命？可信任的他人是否也能感到其中有某种一致性？</p><p>她特别提醒，人的内部同时有自我意志、恐惧、角色期待、父母与文化留下的声音。一个冲动越急迫，并不表示越“属灵”；相反，真正的 leading 往往经得起等待。</p>'''+discernment_visual(), '03 · DISCERNMENT')}
{section('互动：这是开放问题，还是伪装建议？','''<div class="question-lab" id="questionLab"><div class="question-example" id="questionExample">“你有没有想过，其实你应该先休息一段时间？”</div><div class="question-actions"><button data-q="advice">这是伪装建议</button><button data-q="open">这是开放问题</button><button id="nextQuestion">换一道</button></div><div class="question-feedback" id="questionFeedback">先判断，再看为什么。</div></div>''','03 · QUESTION LAB')}
{section('怎样把“建议”改写成真正的问题？','''<div class="rewrite-list"><article><small>建议式</small><p>“你为什么不先辞职再说？”</p><b>→ 当你分别想象“留下”和“离开”时，身体和情绪有什么不同？</b></article><article><small>建议式</small><p>“是不是因为你太在意父母看法？”</p><b>→ 在这件事上，哪些声音最容易盖过你自己的声音？</b></article><article><small>建议式</small><p>“你不是一直想做更有意义的事吗？”</p><b>→ 对你来说，“有意义”具体意味着什么？它现在怎样在你的生活里出现？</b></article></div>''','04 · REWRITE')}
{research_note('开放问题不是“更高级的提问术”','''<p>如果提问者只是把建议藏得更漂亮，澄心会仍然会变成操控。真正的 discipline 是放弃“我来帮你看清”的优越位置，相信焦点人能够在被尊重、被挑战、又不被接管的空间里，逐步遇见自己的 truth。</p><p>Loring 把这种克制称为一种反文化实践：我们习惯把“帮助”等同于给方案，而澄心会练习的是不给方案也能深度陪伴。</p>''')}
{section('一个 120 分钟的实践模板','''<div class="agenda"><div><b>0–10</b><span>静默、保密约定、说明角色</span></div><div><b>10–25</b><span>焦点人陈述问题与背景；其他人只听</span></div><div><b>25–95</b><span>开放问题 + 充分停顿；必要时重新回到静默</span></div><div><b>95–105</b><span>较长静默，让焦点人自行整理</span></div><div><b>105–115</b><span>焦点人可以说“我现在知道了什么 / 仍不知道什么”</span></div><div><b>115–120</b><span>静默结束；不做集体总结</span></div></div><p class="fineprint">具体时长可调整。Loring 提醒，过度结构化会把 discernment 变成机械清单。</p>''','05 · TEMPLATE')}
{section('什么时候不适合用澄心会？','''<div class="boundary-grid"><article><b>需要专业诊断或治疗</b><p>严重抑郁、自伤风险、创伤反应、精神病性症状等，不应由澄心会承担。</p></article><article><b>权力关系无法被保护</b><p>当委员会成员掌握焦点人的职位、资源或评价权，保密和自由表达可能只是表面。</p></article><article><b>问题其实已经决定</b><p>如果目标只是获得背书，澄心会很容易变成仪式化认可。</p></article><article><b>委员会成员无法克制</b><p>若成员习惯给建议、诊断和说服，即使善意，也会破坏辨识空间。</p></article></div>''', '06 · BOUNDARIES')}
{callout('边界','<p>澄心会不是心理治疗，也不是危机干预。涉及严重心理危机、安全风险、创伤处理或需要专业诊断时，应寻求合适专业支持。</p>')}
{section('Queries', query_cards(['我提出的问题，是真的不知道答案，还是其实想把自己的答案放进对方嘴里？','当焦点人沉默很久时，我能不能不急着“帮忙”？','我是否相信一个人可能需要的不是更多观点，而是一个不被替他决定的空间？']), '07 · QUERIES')}
</article>{source_box([('Patricia Loring, Spiritual Discernment','澄心会作为 spiritual discernment 的语境、community testing、silence 与 open questions。'),('Jim Pym, Listening to the Light','Meetings for Clearness 的用途、保密、倾听与结束方式。')])}</div>
'''
pages['clearness.html'] = page_shell('clearness.html','澄心会：不替你决定','用开放问题、静默和保密，帮助一个人把自己的处境与选择慢慢理清。群体提供的不是答案，而是条件。',clearness_body)

# --- learning ---
learning_body = f'''
<div class="article-grid"><article class="article-main">
{section('如果学习也被当作 Meeting，会发生什么？','''<p>Parker J. Palmer 观察到，Friends 用 “meeting” 描述 Worship、Business、婚礼、纪念等不同场合并非偶然：这些场合都可以在同一种 search for truth 的精神中举行。于是他进一步提出 <strong>Meeting for Learning</strong>。</p><p>这并不是给课堂加几分钟静默，而是重新理解学习：知识不是老师“装进”学生头脑里，而是在<strong>人—人—第三物</strong>的关系中出现。</p>''','01 · MEETING FOR LEARNING')}
{triad_visual()}
{section('第三物为什么如此重要？','''<p>如果只有“我和你”，对话很容易滑向互相分析、讨好、辩论或交换主观感受。第三物——一首诗、一段电影、一个数据集、一则案例、一幅画——让关系有一个共同中心。</p><p>Palmer 认为第三物有自己的现实性，它可以打破两个人之间的封闭，让双方同时聆听一个“不是你，也不是我”的东西。</p>''','02 · THIRD THING')}
{section('Meeting for Learning 背后，其实是一种知识观','''<p>Palmer 的激进之处，不只是课堂设计。他认为学习发生在关系里：个人经验重要，却要公开地放到群体中接受检验；群体重要，却不能成为新的权威；文本重要，却不能因为“写在书里”就免于追问。</p><p>因此学习不是把知识从一个已经拥有者搬运给另一个空容器，而是让人、他人和对象彼此校正。真正要信任的，最终不是老师、群体或技巧，而是一个超出我们控制的 Truth。</p>'''+research_note('为什么静默是认识论的一部分？','''<p>Palmer 说，Meeting for Learning 要知道什么时候停止追逐答案。静默不是课堂气氛工具，而是在承认：有些知识需要沉淀，有些对象带着 mystery；我们可以解决问题，却不能把所有真实都压缩成“可立即说清”的结论。</p>'''), '03 · EPISTEMOLOGY')}
{section('Meeting for Learning 的五条纪律','''<div class="practice-steps"><article><b>经验优先于权威</b><p>文本值得尊重，但不能仅因“书上这样写”就终止探寻。</p></article><article><b>只认领自己真正知道的部分</b><p>允许说“不知道”，让疑惑重新成为学习动力。</p></article><article><b>角色可以移动</b><p>老师拥有专业资源，但不垄断 insight；学生也可能成为下一刻的“老师”。</p></article><article><b>信任群体，但不迷信群体</b><p>个人 insight 需要放到群体中检验，却不等于服从多数。</p></article><article><b>知道什么时候停止追赶答案</b><p>有些时刻需要停止讲话，让 insight 沉淀；学习不只有 problems to solve，也有 mysteries to ponder。</p></article></div>''','03 · DISCIPLINES')}
{section('一场 90 分钟共读，如何从“读书会”变成 Meeting for Learning？','''<div class="agenda"><div><b>0–8</b><span>静默到场；不急着签到聊天</span></div><div><b>8–20</b><span>第三物进入：共同阅读一段短文本</span></div><div><b>20–32</b><span>个人圈画 + 自由书写：“哪里让我停住？”</span></div><div><b>32–50</b><span>两人聆听：只说“我在文本里遇到什么”</span></div><div><b>50–58</b><span>静默</span></div><div><b>58–78</b><span>大组：围绕文本，不互相诊断、不抢总结</span></div><div><b>78–85</b><span>再次静默，让学习落回自己</span></div><div><b>85–90</b><span>每人一句：“这段文本现在怎样继续跟着我？”</span></div></div>''','04 · 90-MINUTE DESIGN')}
{section('教师 / 带领者的角色反而更难','''<p>Palmer 并没有因为“群体平等”而削弱教师。相反，教师既要有内容专业，也要有能力照看一个可以被成员信任的群体。角色从“可见的控制”转向“更不显眼、更微妙的托住条件”。</p><p>这与普通 facilitation 有相似处，但 Meeting for Learning 的重点不只是提高参与度，而是让每个人都对 Truth 保持可被纠正的开放。</p>''','05 · FACILITATOR')}
{section('怎样判断一次共学是否真的“发生了学习”？','''<div class="signal-grid"><article><b>问题变得更好</b><p>大家不只是收集答案，而是发现原先问题过于简单。</p></article><article><b>经验被具体化</b><p>成员开始区分“我听说过”与“我真正知道”。</p></article><article><b>文本重新有陌生感</b><p>第三物不再只是支持观点的素材，而能反过来挑战参与者。</p></article><article><b>沉默不再尴尬</b><p>群体可以停止生产语言，让 insight 有时间成形。</p></article><article><b>角色开始流动</b><p>专业者仍然有专业，但 insight 不再只从固定位置出现。</p></article><article><b>学习进入生活</b><p>离开后，参与者愿意调整行为、关系或下一步实践。</p></article></div>''', '06 · EVIDENCE OF LEARNING')}
{section('Queries', query_cards(['我在带领学习时，是更关心“大家有没有听懂我”，还是“这个文本有没有真正进入房间”？','我能否在教学中坦然说“这里我也不知道”？','一次学习如果没有立刻产出可测量结果，我是否仍能辨认它正在发生？']), '07 · QUERIES')}
</article>{source_box([('Parker J. Palmer, Meeting for Learning','关于 meeting、third thing、experience、group trust、silence 与 teacher role 的核心文本。'),('Howard H. Brinton, Friends for 300 Years','作为背景：Meeting 如何从 worship 延伸到 corporate life。')])}</div>
'''
pages['learning.html'] = page_shell('learning.html','Meeting for Learning','如果学习不是“一个人把知识交给另一个人”，而是一群人围绕第三物共同等待真实显现，会发生什么？',learning_body)

# --- community ---
community_body = f'''
<div class="article-grid"><article class="article-main">
{section('Meeting 既是一场聚集，也是一个共同体','''<p>贵格会语境里，Meeting 既可以指今天上午十点开始的一场 worship，也可以指一个长期存在的地方共同体。这个双重含义很重要：一次深刻静默如果没有进入关系、照顾、责任与共同生活，很容易变成个人体验消费。</p>''','01 · COMMUNITY')}
{section('从圆圈到组织，但不让组织吞掉圆圈','''<p>早期 Friends 很快建立 local / monthly 等层级来处理照顾、婚姻、旅行 ministry、财务与公共见证。组织不是为了制造权威中心，而是为了让共同体能承担持续责任。</p><div class="org-map"><div><b>Local worship</b><small>一起敬拜</small></div><i>→</i><div><b>Local / Area Meeting</b><small>照顾与事务</small></div><i>→</i><div><b>Yearly Meeting</b><small>更大范围的共同体与见证</small></div></div><p class="fineprint">不同国家和分支的组织名称、层级与制度并不完全相同；此图只表达功能关系。</p>''','02 · ORGANIZATION')}
{section('一个 Meeting Community 需要照顾什么？','''<div class="care-grid"><article><h3>Worship</h3><p>共同体的源头是否仍有真实生命，而不是只剩例行程序？</p></article><article><h3>Hospitality</h3><p>新人进入时是否被欢迎，又不会被拉拢或传教？</p></article><article><h3>Pastoral care</h3><p>成员遭遇疾病、丧亲、关系或生活危机时，谁来照看？</p></article><article><h3>Conflict</h3><p>差异是否只能在礼貌下压住，还是能进入共同辨识？</p></article><article><h3>Children & learning</h3><p>下一代是否只有“活动”，还是能进入一种活的实践？</p></article><article><h3>Witness</h3><p>内在聆听是否结出外在行动，而不是停在个人平静？</p></article></div>''','03 · CARE')}
{section('Community 也是对“内在声音”的外部检验','''<p>Patricia Loring 提醒，人的内部不只有 divine leading；还有自我意志、欲望、恐惧，以及父母、老师、文化留下的诸多声音。因此 Friends 历来重视把重要 leading 带到可信任的人和 Meeting 中接受检验。</p><p>这不是让群体接管个人良知，而是承认：<strong>完全没有外部检验的“内在灵性”也可能非常危险。</strong></p>''','04 · TESTING')}
{section('共同体的成熟，不看“活动很多”，而看能否承受真实','''<p>Meeting Community 最容易在顺境里显得和谐。真正的检验往往发生在成员生病、丧亲、意见分裂、权力失衡、资金压力或某个 leading 触犯既有习惯时。一个共同体如果只能承受温和分享，却无法承受分歧与责任，静默很容易沦为礼貌。</p><p>Brinton 的结构提醒我们，worship、decision、community 与 witness 不是四个部门，而是一条生命链：没有 inward source，组织会空洞；没有组织承载，体验会蒸发；没有 outward witness，内在生命会变成自我消费。</p>'''+research_note('共同体的四个体检问题','''<p>我们有没有真实的照顾关系？我们能不能处理冲突而不急着分阵营？我们能不能让少数声音被认真听见？我们做出的决定，是否真的改变了预算、时间分配与日常行为？</p>'''), '05 · MATURITY')}
{section('Queries', query_cards(['我们这个群体除了“活动”，有没有真正的互相照顾？','当某个人提出强烈的“内在引领”时，我们既不压制，也不盲从的方式是什么？','我们有没有把 peace、simplicity、integrity 等 testimony 当成口号，而没有让它们进入日常制度？']), '06 · QUERIES')}
</article>{source_box([('Howard H. Brinton, Friends for 300 Years','第7章 The Meeting Community，以及第6章组织与决策的历史。'),('Patricia Loring, Spiritual Discernment','个人 leading 与 community testing 的关系。')])}</div>
'''
pages['community.html'] = page_shell('community.html','Meeting 如何成为共同体','一次安静的聚集很容易；困难的是让静默结出关系、照顾、责任、冲突处理与共同见证。',community_body)

# --- history ---
history_body = f'''
<section class="history-lead"><div><span class="kicker">1640s → TODAY</span><h2>{smart_heading('历史不是一条直线：三百多年来，Meeting 一直在被重新解释')}</h2><p>Meeting 的历史不是从“宗教”逐渐变成“冥想”。形式不断改变，但几个问题反复回来：直接经验怎样不变成任性？共同体怎样不变成权威机器？静默怎样结出行动？传统怎样更新而不失去自身？</p></div></section>
<section class="history-thesis"><article><span>01</span><h3>形式会变，目的未必变</h3><p>Brinton 特别提醒：保存传统的“原始目的”，不等于复制十七世纪的可见形式。真正的问题是：一项新形式是否仍服务于等待、辨识、共同体与见证。</p></article><article><span>02</span><h3>“Quietism”不是一句贬义标签就能概括</h3><p>十八世纪既可以被看作活力下降，也可以被理解为保存、整合与纪律化。历史评价取决于我们用什么标准看“生命力”。</p></article><article><span>03</span><h3>今天没有单一版本的 Quakerism</h3><p>programmed / unprogrammed、evangelical / conservative / liberal 等传统在神学、牧者角色、敬拜形式与社会议题上差异显著。</p></article></section>
<section class="timeline-section"><div class="timeline-v2">
<div class="time-item"><time>1640s</time><span class="timeline-node"></span><div class="timeline-card"><h3>Seekers 与英格兰宗教动荡</h3><p>内战、宗教权威危机与大量激进宗教群体，为“直接经验是否可能超越既有制度”提供了历史土壤。George Fox 的寻找并非凭空发生，而是在一个普遍质疑既有教会形式的时代中成熟。</p><div class="timeline-tag">背景：authority crisis</div></div></div>
<div class="time-item"><time>1652</time><span class="timeline-node"></span><div class="timeline-card"><h3>从个人寻找变成运动</h3><p>Brinton 把 1652 视为关键节点：Fox 在英格兰西北遇到大量 Seekers，信息迅速扩散。早期 Friends 的突破不是发明“安静聚会”，而是把直接启示、共同敬拜、先知式行动与群体生活连在一起。</p><div class="timeline-tag">experience → movement</div></div></div>
<div class="time-item"><time>1650s–1670s</time><span class="timeline-node"></span><div class="timeline-card"><h3>Meeting 从灵性事件变成可持续共同体</h3><p>迫害、救济、婚姻、旅行 ministry、财务与纪律迫使 Friends 建立稳定组织。这里出现了一个重要转折：如果每个人都有直接引领，共同体如何检验引领、承担责任，又不重新制造教阶？Meeting for Business 的精神由此逐渐成熟。</p><div class="timeline-tag">charisma → discipline</div></div></div>
<div class="time-item"><time>1700s</time><span class="timeline-node"></span><div class="timeline-card"><h3>Quietism、保存与内在纪律</h3><p>外在扩张减弱，静默、谨慎、plainness 与共同体边界受到更多重视。Brinton 不愿简单把这一时期视作“衰退”；他更关注形式变化是否仍保存原始目的。这一争论至今仍影响我们怎样评价制度化与灵性活力。</p><div class="timeline-tag">consolidation</div></div></div>
<div class="time-item"><time>1800s</time><span class="timeline-node"></span><div class="timeline-card"><h3>分裂、福音派与多种 Quaker 形态</h3><p>十九世纪 Friends 内部发生重大分歧，福音派、理性主义、传统主义等力量重新排列。不同地区逐渐发展出 programmed / pastoral 与 unprogrammed 等明显不同的敬拜与组织形态。</p><div class="timeline-tag">plural traditions</div></div></div>
<div class="time-item"><time>1900–1930s</time><span class="timeline-node"></span><div class="timeline-card"><h3>现代重新解释：历史、教育与社会见证</h3><p>现代 Friends 开始系统重读自身传统。Rufus Jones 等人推动神秘主义研究；Pendle Hill 于 1930 年成立，成为学习、静修与实验性 Quaker life 的重要场域。Meeting 不再只被解释为宗派礼仪，也被重新思考为教育、共同体与社会行动的来源。</p><div class="timeline-tag">retrieval & experiment</div></div></div>
<div class="time-item"><time>1950s</time><span class="timeline-node"></span><div class="timeline-card"><h3>Brinton：Quakerism as method / group mysticism</h3><p>Howard Brinton 用“method”而不是固定教义体系来理解 Quakerism，并以“group mysticism”说明它既是 inward experience，也是社会性、共同体性的宗教实践。这一框架对今天理解 Meeting 仍极有解释力。</p><div class="timeline-tag">method, not mere form</div></div></div>
<div class="time-item"><time>1960s–1990s</time><span class="timeline-node"></span><div class="timeline-card"><h3>Clearness、discernment 与现代实践语言</h3><p>Patricia Loring 记录，北美年轻 Friends 在二十世纪六十年代重新发展 clearness committee，使它从婚姻、membership 等传统“clearance”用途，逐渐成为个人重要 leading 与生命问题的 discernment 工具。Palmer 等人进一步把 Quaker DNA 转译到教育与领导力领域。</p><div class="timeline-tag">tradition → translation</div></div></div>
<div class="time-item"><time>Today</time><span class="timeline-node"></span><div class="timeline-card"><h3>一个全球、多分支、内部差异很大的传统</h3><p>今天谈“Quaker Meeting”必须先问语境：哪一个国家、哪一个 Yearly Meeting、programmed 还是 unprogrammed、Christian language 是否居于中心？本站主要研究 unprogrammed Meeting 与 Pendle Hill 相关现代传统，同时明确标注这一视角的边界。</p><div class="timeline-tag">context matters</div></div></div>
</div></section>
<section class="content-section history-framework"><div class="section-head"><span>BRINTON’S LENS</span><h2>{smart_heading('Brinton 的“四时期”不是唯一答案，却提供了一张很有用的分析地图')}</h2><p>他把约 1650–1700、1700–1800、1800–1900、1900 以后分别描述为英雄／使徒期、文化创造期、冲突与衰落期、现代主义期，并用四种宗教力量观察各时期的重心变化。</p></div><div class="four-forces"><article><b>Mystical</b><span>向内</span><p>通过 inward experience、静默与直接感知认识宗教与道德真实。</p></article><article><b>Evangelical</b><span>历史／启示</span><p>强调基督教历史、圣经与公开宣讲的权威。</p></article><article><b>Rational</b><span>思想</span><p>通过理性、解释与现代知识重述传统。</p></article><article><b>Social Gospel</b><span>行动</span><p>把宗教真实性放在服务、和平、公义与社会改造中检验。</p></article></div>{research_note('不要把历史读成“谁取代了谁”','''<p>Brinton 的重点不是说某个时期只剩一种力量，而是观察四种倾向的比例怎样变化。真正有生命的 Quakerism 往往不是四选一，而是在 inward / outward、experience / history、mysticism / action 之间形成新的组合。</p>''')}</section>
<section class="content-section"><div class="section-head"><span>THREE THREADS</span><h2>{smart_heading('贯穿三百多年的三条张力')}</h2></div><div class="tension-grid"><article><b>Immediate experience ↔ Tradition</b><p>直接经验如何保持活力，同时不切断历史、文本与共同体检验？</p></article><article><b>Individual leading ↔ Corporate discernment</b><p>如何尊重每个人的 Light，又不把任何个人冲动绝对化？</p></article><article><b>Inward life ↔ Outward witness</b><p>静默如何不是逃离世界，而是成为关系、制度与社会行动的根？</p></article></div></section>
<section class="content-section">{source_box([('Howard H. Brinton, Friends for 300 Years','整体历史框架，尤其引言、第6章与第9章；“method”“group mysticism”及四时期分析。'),('Patricia Loring, Spiritual Discernment','20世纪 clearness committee 从 clearance 到个人 discernment 工具的演变。'),('Inward Light (Friends Conference on Religion and Psychology)','20世纪 Friends 与心理学、神学、现代思想之间的持续对话。'),('Parker J. Palmer, Meeting for Learning','Pendle Hill 语境中，Meeting 如何被转译为教育与共同探寻的形式。')])}</section>
'''
pages['history.html'] = page_shell('history.html','Meeting 的历史与演变','从17世纪 Seekers、George Fox 与早期 Friends，到 Quietism、现代分支、Pendle Hill 与心理学对话：Meeting 的形态不断变化，但核心张力一直存在。',history_body,label='HISTORY')

# --- comparisons ---
comparisons_body = '''
<section class="comparison-intro"><div><span class="kicker">DON’T COLLAPSE THE DIFFERENCES</span><h2>相似，不等于相同</h2><p>Meeting 与正念、禅修、团体治疗、教练、共识决策、信任圈、Bohm Dialogue 都有交集。但真正理解一个方法，往往要看它<strong>把什么当作中心、如何理解人、如何处理权威，以及什么算“成功”</strong>。</p></div></section>
<section class="comparison-lenses"><article><span>01</span><b>Center</b><p>这个方法最终把什么放在中心：觉察、来访者目标、共同方案、Truth、Spirit，还是关系本身？</p></article><article><span>02</span><b>Authority</b><p>谁有资格说“现在发生了什么”：老师、治疗师、facilitator、群体，还是一个更深的共同辨识？</p></article><article><span>03</span><b>Success</b><p>怎样算“成功”：减压、疗愈、达成一致、获得洞见、形成 unity，还是忠实行动？</p></article><article><span>04</span><b>Boundary</b><p>这个方法明确不做什么？它什么时候应该停下，并转介到别的专业或机制？</p></article></section>
<section class="content-section"><div class="matrix-wrap"><table class="matrix"><thead><tr><th>方法</th><th>主要中心</th><th>群体作用</th><th>带领权威</th><th>典型目标</th><th>与 Meeting 最关键差异</th></tr></thead><tbody>
<tr><th>Quaker Meeting</th><td>Light / Truth / Spirit / divine guidance（语言因传统而异）</td><td>共同等待、检验与明辨</td><td>角色服务于 Meeting，不拥有真理</td><td>faithfulness、unity、right action</td><td>不是以体验改善或问题解决为唯一目的</td></tr>
<tr><th>Mindfulness</th><td>当下经验与觉察</td><td>可个人也可团体</td><td>教师提供练习框架</td><td>觉察、减轻反应性等</td><td>Meeting 强调 corporate listening 与可能的 leading</td></tr>
<tr><th>禅修 / Zen</th><td>依宗派而异，常含觉悟实践</td><td>共同修行但未必共同明辨</td><td>师承通常更明确</td><td>禅定、洞见、觉悟</td><td>Meeting 无固定 meditation technique，也较少师徒结构</td></tr>
<tr><th>Consensus</th><td>可接受的共同方案</td><td>协商差异</td><td>facilitator 管理过程</td><td>达成一致</td><td>Sense of Meeting 追求的是被辨认的 unity / rightness，不只是接受度</td></tr>
<tr><th>Coaching</th><td>来访者目标与行动</td><td>通常一对一</td><td>coach 负责提问框架</td><td>清晰、行动、成长</td><td>澄心会避免以绩效目标或教练关系为中心</td></tr>
<tr><th>Group Therapy</th><td>心理健康与关系模式</td><td>治疗性互动</td><td>受训治疗师</td><td>治疗与功能改善</td><td>Meeting 不是临床治疗，不以诊断或心理病理为框架</td></tr>
<tr><th>Circle of Trust</th><td>Inner Teacher / soul / wholeness</td><td>用 touchstones 保护灵魂出现</td><td>facilitator 设计条件</td><td>wholeness、integrity</td><td>受 Quaker 影响，但结构更显性，且常使用第三物与特定 touchstones</td></tr>
<tr><th>Bohm Dialogue</th><td>collective thought process</td><td>观察思维如何共同生成</td><td>较弱中心</td><td>看见假设、整体性</td><td>哲学基础不同；Quaker Meeting 有更明确的 spiritual discernment 传统</td></tr>
</tbody></table></div></section>
<section class="content-section"><div class="section-head"><span>HOW TO CHOOSE</span><h2>什么场景更适合用什么？</h2></div><div class="scenario-grid"><article><span>需要临床支持</span><h3>优先心理治疗 / 医疗</h3><p>不要把 Meeting 或澄心会当治疗替代品。</p></article><article><span>要训练注意与减压</span><h3>Mindfulness 更直接</h3><p>Meeting 不承诺把“平静”作为输出。</p></article><article><span>团队要快速做可逆决定</span><h3>普通决策机制更高效</h3><p>并非所有事情都值得进入深度 corporate discernment。</p></article><article><span>价值冲突、使命方向、重大共同体议题</span><h3>Meeting for Business 值得尝试</h3><p>尤其当“赢得辩论”会伤害共同体时。</p></article><article><span>一个人面对重要人生选择</span><h3>澄心会可提供独特空间</h3><p>前提是问题不属于需要专业危机处理的范畴。</p></article><article><span>深度共读、教育、团队学习</span><h3>Meeting for Learning 很合适</h3><p>第三物 + 静默 + 经验检验，会改变普通讨论结构。</p></article></div></section>
<section class="content-section"><div class="section-head"><span>FALSE FRIENDS</span><h2>最容易“看起来很像”，其实差异最大的三组</h2></div><div class="false-friends"><article><h3>Meeting ≠ Meditation group</h3><p>两者都可能安静，但 Meeting 的单位不是“很多个正在练习的个人”，而是一个正在共同等待的群体。个体注意力训练可以发生，却不是全部。</p></article><article><h3>Sense of the Meeting ≠ Consensus</h3><p>两者都避免简单多数压制，但 consensus 常以“大家都能接受”为目标；Quaker practice 更关心群体是否辨认到一个可以被承担的 rightness / unity。</p></article><article><h3>Clearness ≠ Coaching</h3><p>两者都使用提问，但澄心会不以目标达成、绩效或行动计划为中心；它更严格地限制 advice，并给沉默与 spiritual discernment 更大位置。</p></article></div></section>
<section class="content-section"><div class="research-card"><span>比较方法</span><h3>不要问“哪个方法最好”，先问“它在解决什么问题”</h3><div><p>一个方法是否合适，取决于问题类型、风险、权力结构、时间尺度与参与者期待。Meeting 的优势在于处理那些不能只靠信息和偏好解决的价值性问题；它的弱点也同样明显：慢、依赖群体成熟度、容易被隐形权力伪装成“灵性共识”。</p></div></div></section>
<section class="content-section">''' + query_cards(['我是否因为喜欢某种方法，就急着说“其实都一样”？','我当前真正需要的是什么：疗愈、学习、决策、灵性实践、关系修复，还是行动？','一个方法的边界在哪里？什么情况应该明确转介给更合适的专业？']) + '''</section>
'''
pages['comparisons.html'] = page_shell('comparisons.html','Meeting 与其他方法，有何异同？','不要把所有“安静、倾听、圆圈、提问”都混成一种东西。通过目标、权威、群体作用与成功标准，建立清楚的方法边界。',comparisons_body,label='COMPARE')

# --- glossary ---
glossary_terms = [
('Meeting','Meeting／会聚','既指一次聚集，也可指长期存在的地方共同体；不宜一律译成“会议”。','核心'),
('Meeting for Worship','静默敬拜会','unprogrammed tradition 中以共同静默、等待与可能出现的 vocal ministry 为特征。','敬拜'),
('Waiting','等候 / 静默等候','不是等待时间过去，而是带着期待、开放与可被引领的姿态。','敬拜'),
('Inward Light','内在之光','Quaker 核心语言之一。历史上与 Christ / Spirit 关系紧密，现代不同 Friends 的解释不完全相同。','神学'),
('That of God in everyone','每个人里面“属神的那一份”','常见 Quaker 表达，但历史语境与现代通俗解释之间存在差异，使用时宜保留复杂性。','神学'),
('Gathered Meeting','被聚集的 Meeting','群体共同静默出现深层统一、临在或共同注意的经验。不是人为制造的“高峰状态”。','敬拜'),
('Vocal Ministry','受感分享 / 口头 ministry','在静默中经辨识后说出的分享；不是讨论发言或自由麦。','敬拜'),
('Leading','内在引领','一种持续推动人走向某行动或方向的内在感知，需要时间与共同体检验。','明辨'),
('Concern','内在关切','比“一时兴趣”更持续、更具责任感的召唤，可发展为行动或 witness。','明辨'),
('Discernment','明辨 / 辨识','分辨不同冲动、声音与可能引领的过程，既有个人层面，也有 corporate 层面。','明辨'),
('Unity','合一','不是意见完全相同，而是群体在一个方向上形成更深的共同清晰。','议事'),
('Sense of the Meeting','Meeting 的共同辨识','Clerk 与群体共同辨认“这个 Meeting 此刻正在形成什么判断”。不等同普通共识。','议事'),
('Clerk','Clerk / 书记','不是 chairman。照看议程、节奏与 minute，并尝试听出 sense of the meeting。','议事'),
('Minute','会议纪要 / 决议措辞','在 Quaker business 中常现场形成，用来记录已经被 Meeting 认可的 sense。','议事'),
('Standing Aside','保留但不阻挡','个人仍有不同判断，但不认为自己的保留足以阻挡 Meeting 前进。具体实践因群体而异。','议事'),
('Clearness Committee','澄心会','一小群人以开放问题、静默、保密帮助焦点人获得更清晰的辨识。','实践'),
('Query','省察问题 / Query','不是考试题，而是让个人与共同体持续检视实践与生命状态的问题。','实践'),
('Testimony','生活见证 / Testimony','不是抽象信条，而是从信仰实践中逐渐形成的生活方式与公共见证，如 peace、simplicity、integrity 等。','见证'),
('Third Thing','第三物','Palmer 的学习语境中，连接人与人的文本、诗歌、数据、经验等共同对象。','共学'),
('Meeting for Learning','共学 Meeting','把学习理解为人与人围绕第三物共同探寻 Truth 的过程。','共学'),
('Unprogrammed Worship','非程序化敬拜 / 无预设程序的敬拜','没有预先安排讲道、赞美诗或固定发言次序，以共同静默与可能出现的 vocal ministry 为主要形式。','敬拜'),
('Programmed Worship','程序化敬拜','在部分 Friends 传统中，有牧者、讲道、音乐与预先安排的礼拜结构；并不因此“不是真正的 Quaker”。','敬拜'),
('Seasoning','酝酿 / 让议题成熟','让一个 concern、proposal 或 leading 经历时间、祷告、讨论与共同体检验，不急于进入正式决定。','明辨'),
('Threshing Session','预备性深谈 / 梳理会','在正式 Meeting for Business 决策前，充分呈现事实、感受与分歧，但通常不在此时形成决定。','议事'),
('Right Ordering','合宜的秩序 / 正当安排','指角色、责任与程序服务于 Spirit / Truth，而不是单纯追求行政效率。不同传统用法有所差异。','议事'),
('Holding in the Light','在光中守望 / 把某人放在光中','为一个人或处境保持祷告式、非操控性的关注；不是在脑中替对方设计解决方案。','实践'),
('Elder','Elder / 长老性角色','历史上承担 ministry 与 worship 的照看、辨识和培育；现代不同 Meeting 是否正式设置该角色差异很大。','共同体'),
('Faith and Practice','Faith and Practice / 信仰与实践手册','许多 Yearly Meetings 编纂的传统、经验、纪律、Advices & Queries 等文本；不同 Yearly Meeting 版本并不相同。','共同体'),
('Advices & Queries','劝勉与省察问题','用于持续检视个人与共同体生活的劝勉和问题，不是统一教义问答。','实践'),
]
glossary_cards=''.join(f'<article class="glossary-card" data-term="{html.escape((en+cn+cat).lower())}"><span>{cat}</span><h3>{en}</h3><h4>{cn}</h4><p>{desc}</p></article>' for en,cn,desc,cat in glossary_terms)
glossary_body=f'''
<section class="glossary-top"><div><span class="kicker">WORDS MATTER</span><h2>很多误解，来自翻译过快</h2><p>贵格会大量词汇表面上很普通：meeting、concern、minute、clerk、unity……但进入传统语境后都有特殊含义。本站宁可暂时保留英文，也不急着用一个中文词把复杂性抹平。</p></div><label class="search-box">搜索术语<input id="glossarySearch" placeholder="例如：unity / 澄心 / 静默"/></label></section>
<section class="content-section"><div class="filter-row"><button class="filter active" data-filter="all">全部</button><button class="filter" data-filter="敬拜">敬拜</button><button class="filter" data-filter="明辨">明辨</button><button class="filter" data-filter="议事">议事</button><button class="filter" data-filter="实践">实践</button><button class="filter" data-filter="共学">共学</button><button class="filter" data-filter="神学">神学</button><button class="filter" data-filter="共同体">共同体</button></div><div class="glossary-grid" id="glossaryGrid">{glossary_cards}</div></section>
<section class="content-section"><div class="section-head"><span>HOW TO READ</span><h2>{smart_heading('术语不是“对照表”，而是一张传统内部的关系网')}</h2></div><div class="term-relations"><article><b>Waiting → Ministry</b><p>先有等候，才谈得上受感分享；否则 ministry 很容易退化成自由发言。</p></article><article><b>Leading → Seasoning → Testing</b><p>引领不是立即执行的冲动；它需要时间、共同体与生活后果的检验。</p></article><article><b>Unity → Sense of the Meeting → Minute</b><p>合一不是“大家都一样想”，而是在足够清晰时形成可被书写和承担的共同方向。</p></article><article><b>Inner Light → Testimony → Witness</b><p>Light 若只停在体验层面，会失去 Quaker tradition 强调的伦理与公共行动维度。</p></article></div></section>
<section class="content-section">{callout('翻译原则','<p>本站优先“先懂后译”：先确认词在贵格会实践中的功能，再选择中文。对于 <em>Meeting、Clerk、Sense of the Meeting</em> 这类一译就容易误导的词，宁可中英并列。</p>')}</section>
'''
pages['glossary.html']=page_shell('glossary.html','Quaker Meeting 术语表','从 Meeting、Waiting、Inward Light 到 Clerk、Unity、Sense of the Meeting：用准确而不僵硬的中文建立一张概念地图。',glossary_body,label='GLOSSARY')

# --- research ---
research_body = '''
<section class="research-intro"><div><span class="kicker">SOURCE-BASED · NOT QUOTE-MINING</span><h2>本站怎样做研究？</h2><p>不是先有一个“现代灵性”的结论，再去贵格会文献里找漂亮句子。我们尽量把概念放回历史、实践与作者自己的问题意识中：一个词在什么时候出现？解决了什么问题？后来如何变化？今天又有哪些不同解释？</p></div></section>
<section class="content-section"><div class="section-head"><span>PRIMARY LIBRARY</span><h2>第一版核心文献</h2></div><div class="book-grid">
<article><span>历史 / 方法</span><h3>Howard H. Brinton<br/><em>Friends for 300 Years</em></h3><p>本站最重要的骨架来源。尤其是 The Meeting for Worship、Vocal Ministry、Reaching Decisions、The Meeting Community。</p><small>1952；后有 Pendle Hill 版</small></article>
<article><span>实践 / 当代入门</span><h3>Jim Pym<br/><em>Listening to the Light</em></h3><p>把 Quaker meeting、日常实践、testimonies、business method 和生活整合起来，适合大众入口。</p><small>1999</small></article>
<article><span>教育 / Third Thing</span><h3>Parker J. Palmer<br/><em>Meeting for Learning</em></h3><p>把 Meeting 的精神转入教育：person–person–third thing、经验、群体、静默、教师角色。</p><small>Pendle Hill pamphlet</small></article>
<article><span>Discernment / Clearness</span><h3>Patricia Loring<br/><em>Spiritual Discernment</em></h3><p>解释 discernment、tests of leadings、community testing、unity 与 clearness committees 的精神背景。</p><small>Pendle Hill Pamphlet 305, 1992</small></article>
<article><span>Inward Life</span><h3>Thomas R. Kelly<br/><em>The Light Within</em></h3><p>理解 inward sanctuary、持续内在取向，以及 inward life 如何进入日常行动的重要文本。</p></article>
<article><span>哲学</span><h3>Michael Marsh<br/><em>Philosophy of the Inner Light</em></h3><p>尝试从哲学角度理解 inner light，不把它缩成情绪、直觉或视觉幻象。</p><small>Pendle Hill Pamphlet 209, 1976</small></article>
<article><span>心理学 / Jung</span><h3>John Yungblut<br/><em>Seeking Light in the Darkness of the Unconscious</em></h3><p>探索 Jung、无意识、阴影与 Quaker “Light” 的关系，也提醒“光/暗”二分的复杂性。</p><small>Pendle Hill Pamphlet 211, 1977</small></article>
<article><span>20世纪思想史</span><h3><em>Inward Light</em></h3><p>Friends Conference on Religion and Psychology 的资料，呈现现代 Friends 如何与心理学、神学和跨宗教问题对话。</p></article>
</div></section>
<section class="content-section"><div class="section-head"><span>METHOD</span><h2>每个概念页，理想上回答八个问题</h2></div><div class="method-grid"><b>它原本在解决什么问题？</b><b>17世纪 Friends 怎么说？</b><b>后来的实践怎样改变？</b><b>不同 Quaker 分支是否理解一致？</b><b>现代作者如何重述？</b><b>它最常被误解成什么？</b><b>有哪些可以实践的动作？</b><b>边界和争议在哪里？</b></div></section>
<section class="content-section"><div class="section-head"><span>RESEARCH DISCIPLINE</span><h2>六条研究纪律：避免把 Quakerism 做成“灵性语录库”</h2></div><div class="research-discipline"><article><span>01</span><h3>先确认语境</h3><p>同一个词在 1650s、Quietism、20世纪 liberal Quaker 与 evangelical Friends 中，含义可能并不相同。</p></article><article><span>02</span><h3>区分原典与现代转译</h3><p>Palmer、Loring、Pym 的现代实践语言很有价值，但不能反向假定早期 Friends 就以同样概念理解自己。</p></article><article><span>03</span><h3>不把“经验”绝对化</h3><p>经验是材料，也是证据来源之一；还需要历史、共同体、伦理后果与内部一致性来检验。</p></article><article><span>04</span><h3>保留传统内部争论</h3><p>Inner Light 是 Christological、mystical、humanist 还是 universalist？不同 Friends 会给出不同答案。</p></article><article><span>05</span><h3>描述实践，也描述失败方式</h3><p>“不投票”可能退化成隐形权力；“静默”可能掩盖冲突；“开放问题”可能变成精致的建议。</p></article><article><span>06</span><h3>把 inward 与 outward 放在一起</h3><p>如果研究只谈内在体验，却不看 testimony、community 与 witness，就会失去 Quaker tradition 的伦理结构。</p></article></div></section>
<section class="content-section"><div class="section-head"><span>SOURCE MAP</span><h2>不同文献，各自在回答什么问题？</h2></div><div class="source-matrix"><article><b>Brinton</b><span>结构问题</span><p>Meeting 为何是一种 group mysticism？Quakerism 为什么可以被理解为 method？Worship、ministry、decision、community 如何连成一个整体？</p></article><article><b>Thomas Kelly</b><span>内在生命</span><p>Inner Light 如何从固定静默时段变成 workaday life 中持续的 inward orientation？</p></article><article><b>Michael Marsh</b><span>哲学问题</span><p>Inner Light 是什么隐喻？“我看见了”为什么不自动等于“我看对了”？truth、love、rightness、beauty 如何成为辨识视角？</p></article><article><b>Patricia Loring</b><span>辨识问题</span><p>怎样区分 leading 与自我意志？时间、果实、共同体与 unity 如何成为 tests？澄心会为什么不是提问技巧？</p></article><article><b>Parker Palmer</b><span>教育问题</span><p>Meeting 的认识论如何进入学习？人—人—第三物、群体检验、静默与教师角色之间是什么关系？</p></article><article><b>Inward Light</b><span>现代思想史</span><p>20世纪 Friends 怎样面对神学模糊、心理学、Jung、跨宗教与“现代人还能怎样谈 Light”的问题？</p></article></div></section>
<section class="content-section"><div class="section-head"><span>CONTESTED CONCEPTS</span><h2>四个不能过早“讲简单”的概念</h2></div><div class="contested-grid"><article><h3>Inner Light</h3><p><b>不能只说：</b>“相信自己的直觉。”</p><p><b>需要追问：</b>Light 与 Christ / Spirit 的历史关系是什么？现代自然主义解释怎样出现？内在经验如何接受检验？</p></article><article><h3>Group Mysticism</h3><p><b>不能只说：</b>“大家一起能量更强。”</p><p><b>需要追问：</b>Brinton 所说的 group 是宗教共同体、社会有机体还是神学现实？现代心理学解释与传统解释如何区分层次？</p></article><article><h3>Sense of the Meeting</h3><p><b>不能只说：</b>“Quaker 版 consensus。”</p><p><b>需要追问：</b>unity、clerk、minute、standing aside、waiting 与 worship 如何共同构成这一实践？</p></article><article><h3>Clearness</h3><p><b>不能只说：</b>“用开放问题帮助对方找答案。”</p><p><b>需要追问：</b>它从 clearance 到 discernment 的历史变化是什么？为何 restraint、prayerful attentiveness 与 community testing 比“好问题”更核心？</p></article></div></section>
<section class="content-section"><div class="section-head"><span>RESEARCH ROADMAP</span><h2>后续研究专题</h2></div><div class="roadmap-list"><article><b>Waiting upon the Lord</b><p>Fox、Barclay、Quietism、Brinton 与现代 liberal Quaker 的语言变迁。</p></article><article><b>Gathered Meeting</b><p>历史见证、Rufus Jones / Brinton、群体心理学与宗教经验研究。</p></article><article><b>Sense of the Meeting</b><p>历史 practice、现代 consensus 理论、组织治理与 conflict transformation。</p></article><article><b>Inner Light</b><p>Christological、mystical、humanist、universalist 等不同解释路线。</p></article><article><b>Quakerism & Psychology</b><p>Jung、Friends Conference on Religion and Psychology、Clearness 与现代心理治疗边界。</p></article><article><b>From Meeting to Circle of Trust</b><p>Parker Palmer 如何把 Quaker DNA 转译成适用于教育、领导力与公共生活的实践。</p></article></div></section>
<section class="content-section"><div class="section-head"><span>READING PATHS</span><h2>三条进阶阅读路径</h2></div><div class="reading-trails"><article><span>A · Meeting 的骨架</span><p>Brinton → Jim Pym → Patricia Loring</p><small>先理解 worship / ministry / business / community，再进入现代 discernment。</small></article><article><span>B · Inner Light 的深处</span><p>Thomas Kelly → Michael Marsh → Inward Light</p><small>从实践语言进入哲学与心理学争论，避免把 Light 口号化。</small></article><article><span>C · 从 Quaker 到公共实践</span><p>Parker Palmer → Clearness → Circle of Trust</p><small>观察传统如何被转译到教育、领导力、组织与个人生命。</small></article></div></section>
<section class="content-section"><div class="research-note"><h2>一个重要提醒</h2><p>“贵格会”不是单一、静态、完全一致的传统。不同 Yearly Meetings、programmed / unprogrammed、evangelical / conservative / liberal 等分支，在基督论、圣经、牧师制度、敬拜形式和社会议题上可以有很大差异。本站当前版本以<strong>unprogrammed Meeting、Pendle Hill 传统与相关现代作者</strong>为主要研究入口，并会持续标注这一视角的边界。</p></div></section>
'''
pages['research.html']=page_shell('research.html','Quaker Meeting 研究室','原典、思想史、实践谱系与研究方法。这里不仅给“结论”，也尽量让你知道结论从哪里来、有哪些不同解释。',research_body,label='RESEARCH')

# --- toolkit ---
toolkit_body = '''
<section class="toolkit-top"><div><span class="kicker">FROM READING TO DOING</span><h2>把 Meeting 变成可以使用的实践</h2><p>下面的工具不是“贵格会标准流程”，而是基于传统精神整理的现代练习卡。每张卡都尽量保留一个原则：<strong>结构只负责创造条件，不负责制造结果。</strong></p></div></section>
<section class="content-section"><div class="tool-grid">
<article><span>15–20 min</span><h3>个人等待练习</h3><ol><li>带一个真实但不急于解决的问题坐下。</li><li>前 3 分钟只感受身体。</li><li>把问题轻轻放在心里，不反复分析。</li><li>注意反复出现的词、画面、阻力。</li><li>结束只写事实，不解释。</li></ol><button onclick="window.print()">打印这一页</button></article>
<article><span>30–45 min</span><h3>3–8 人简化 Meeting</h3><ol><li>围坐，说明保密与不强迫发言。</li><li>共同静默 25–35 分钟。</li><li>若有人说话，之后至少留 1–2 分钟沉默。</li><li>结束后每人一句“我注意到了什么”。</li><li>不讨论谁说得对。</li></ol></article>
<article><span>60–90 min</span><h3>Meeting for Learning</h3><ol><li>准备一个短而有张力的第三物。</li><li>阅读后个人书写。</li><li>两人深听。</li><li>大组回应第三物，而非分析彼此。</li><li>以静默与 Query 结束。</li></ol></article>
<article><span>90 min</span><h3>简化 Business Meeting</h3><ol><li>先把事实与立场分开。</li><li>让每个重要观点只说一次。</li><li>中段安排一段较长静默。</li><li>让 Clerk 试写“我们似乎清楚的是……”</li><li>若不清楚，就明确记录“不决定”。</li></ol></article>
<article><span>90–120 min</span><h3>澄心会</h3><ol><li>明确 focal person 的问题。</li><li>承诺保密。</li><li>只问开放问题。</li><li>允许长停顿。</li><li>不总结、不替对方决定。</li></ol></article>
<article><span>5 min</span><h3>日常 Micro-Meeting</h3><ol><li>重大回复前先停 60 秒。</li><li>问：我现在是在反应，还是在回应？</li><li>把对方也放回“不是问题对象，而是一个人”。</li><li>再决定是否回复。</li></ol></article>
</div></section>
<section class="content-section"><div class="section-head"><span>FACILITATOR CARD</span><h2>带领者只需要记住四句话</h2></div><div class="four-lines"><p>把规则讲清楚，然后少讲一点。</p><p>当空间变得焦躁，不要立刻填满它。</p><p>把人从“互相处理”带回共同中心。</p><p>结构越成熟，带领者越可以退后。</p></div></section>
<section class="content-section"><div class="section-head"><span>FAILURE MODES</span><h2>六种最常见的“看起来像 Meeting，实际上不是”的失败方式</h2></div><div class="myth-grid"><article><b>把静默当装饰</b><p>开头停 30 秒，后面仍完全按普通会议的速度、权力与辩论模式运行。</p></article><article><b>引导语太多</b><p>带领者不断告诉大家“此刻应该感受什么”，结果静默仍被一个中心人物占满。</p></article><article><b>把真诚等同即时表达</b><p>所有感受都立刻说出来，群体没有机会分辨哪些需要被说、哪些适合继续等待。</p></article><article><b>用“合一”压制异议</b><p>为了维持和谐而让关键保留意见消失，最后得到的只是礼貌性服从。</p></article><article><b>把开放问题变成隐藏建议</b><p>句尾虽然有问号，提问者其实已经替对方设计好答案。</p></article><article><b>体验结束后没有生活检验</b><p>当场很深刻，却不进入决定、关系与责任；久而久之 Meeting 只剩体验消费。</p></article></div></section>
<section class="content-section">''' + query_cards(['我现在设计的是“更多活动”，还是“更好的相遇条件”？','这个结构是否给静默留下了真正的时间，而不是象征性停顿？','我有没有把自己当成最知道答案的人？']) + '''</section>
'''
pages['toolkit.html']=page_shell('toolkit.html','实践工具箱','从个人等待、三五人简化 Meeting，到共学、议事与澄心会：把概念变成可以实际尝试的结构。',toolkit_body,label='TOOLKIT')

# --- assets ---
css = r'''
:root{--paper:#f2eee5;--paper2:#e8e1d4;--ink:#1f2723;--ink2:#3f4b45;--moss:#5d6d60;--sage:#8c9a8b;--gold:#b49a5c;--line:#cfc6b7;--white:#fffdf8;--shadow:0 16px 48px rgba(31,39,35,.08);--serif:ui-serif,"Songti SC","STSong","Noto Serif CJK SC",serif;--sans:ui-sans-serif,system-ui,-apple-system,"PingFang SC","Microsoft YaHei",sans-serif}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);line-height:1.78;letter-spacing:.01em}a{color:inherit;text-decoration:none}img,svg{max-width:100%}button,input,textarea{font:inherit}.skip-link{position:absolute;left:-999px;top:8px}.skip-link:focus{left:8px;background:#fff;padding:8px;z-index:99}.site-header{position:sticky;top:0;z-index:30;display:flex;align-items:center;justify-content:space-between;padding:14px clamp(20px,4vw,64px);background:rgba(242,238,229,.92);backdrop-filter:blur(16px);border-bottom:1px solid rgba(31,39,35,.08)}.brand{display:flex;align-items:center;gap:11px}.brand b{display:block;font-family:var(--serif);font-size:18px}.brand small{display:block;font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--moss)}.brand-mark{width:34px;height:34px;border:1px solid var(--moss);border-radius:50%;position:relative}.brand-mark i{position:absolute;border:1px solid var(--gold);border-radius:50%;left:50%;top:50%;transform:translate(-50%,-50%)}.brand-mark i:nth-child(1){width:6px;height:6px;background:var(--gold)}.brand-mark i:nth-child(2){width:16px;height:16px}.brand-mark i:nth-child(3){width:26px;height:26px;opacity:.45}.main-nav{display:flex;gap:18px;font-size:13px}.main-nav a{padding:8px 0;color:#4d5852;border-bottom:1px solid transparent}.main-nav a:hover,.main-nav a.active{color:var(--ink);border-color:var(--gold)}.nav-toggle{display:none;background:none;border:0;font-size:24px}.page-hero{padding:72px clamp(22px,8vw,140px) 44px;border-bottom:1px solid var(--line)}.page-hero .hero-copy{max-width:940px}.kicker,.section-eyebrow,.section-head>span,.big-question>span{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--moss);font-weight:700}.page-hero h1{font:500 clamp(42px,6vw,82px)/1.08 var(--serif);margin:12px 0 20px}.page-hero p{font-size:18px;max-width:760px;color:var(--ink2)}.hero-line{width:74px;height:1px;background:var(--gold);margin-top:30px}.home-hero{min-height:76vh;display:grid;grid-template-columns:1.05fr .95fr;align-items:center;padding:80px clamp(24px,7vw,120px);background:var(--ink);color:var(--paper)}.home-copy h1{font:500 clamp(60px,8vw,110px)/.96 var(--serif);margin:18px 0 30px;letter-spacing:-.04em}.home-copy>p{max-width:650px;color:#d8d9d1;font-size:18px}.home-hero .kicker{color:#c4b991}.cta-row{display:flex;gap:12px;flex-wrap:wrap;margin:34px 0}.btn{display:inline-flex;justify-content:center;align-items:center;border:1px solid var(--ink);padding:12px 18px;border-radius:999px;cursor:pointer;transition:.2s;background:transparent}.btn.primary{background:var(--ink);color:var(--white)}.home-hero .btn.primary{background:var(--paper);color:var(--ink);border-color:var(--paper)}.btn.ghost{border-color:var(--line)}.home-hero .btn.ghost{color:var(--paper);border-color:#657069}.btn:hover{transform:translateY(-1px);box-shadow:0 8px 20px rgba(0,0,0,.08)}.btn.inverted{background:var(--paper);color:var(--ink);border:0}.hero-note{margin-top:40px;display:flex;gap:12px;max-width:650px;color:#aeb7b0;font-size:13px}.hero-note span{width:34px;height:1px;background:var(--gold);margin-top:11px;flex:none}.circle-visual{text-align:center}.circle-visual svg{max-height:510px;overflow:visible}.circle-visual .seat circle{fill:#d8ddd8}.circle-visual .seat path{fill:none;stroke:#aab5ad;stroke-width:1.4;stroke-linecap:round}.circle-visual .center-dot{fill:var(--gold)}.circle-visual .halo{stroke:#c9ab61;stroke-width:.45;transform-origin:50px 50px;animation:pulse 6s ease-in-out infinite}.circle-visual .h2{animation-delay:1s}.circle-visual .h3{animation-delay:2s;opacity:.45}.circle-visual p{font:14px var(--serif);color:#9da7a0;margin-top:-20px}@keyframes pulse{0%,100%{opacity:.18;transform:scale(.92)}50%{opacity:.65;transform:scale(1.07)}}.home-intro{display:grid;grid-template-columns:1.05fr .95fr;gap:8vw;padding:110px clamp(24px,8vw,140px)}.big-question h2{font:500 clamp(34px,4.6vw,68px)/1.3 var(--serif);margin:16px 0}.intro-copy{font-size:17px;color:var(--ink2);padding-top:34px}.home-map{padding:100px clamp(24px,8vw,140px);background:#e6e0d4}.section-head{max-width:850px;margin-bottom:42px}.section-head h2,.content-section h2{font:500 clamp(30px,4vw,52px)/1.2 var(--serif);margin:10px 0 12px}.section-head p{color:var(--ink2)}.layer-diagram{display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:60px;max-width:980px;margin:30px auto}.layer-diagram svg{max-height:560px}.layer{fill:none;stroke:var(--moss);stroke-width:.7;opacity:.55}.l1{stroke:var(--gold);stroke-width:1.5}.core{fill:var(--gold)}.layer-legend{display:grid;gap:12px}.layer-legend>div{display:flex;align-items:center;gap:18px;padding:12px 0;border-bottom:1px solid rgba(31,39,35,.14)}.layer-legend b{color:var(--gold);font-weight:500}.layer-legend span{display:flex;flex-direction:column}.layer-legend strong{font-family:var(--serif);font-size:20px}.layer-legend small{color:var(--moss)}.map-links{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-top:50px}.map-links a{padding:18px;border-top:1px solid var(--ink)}.map-links b{display:block;color:var(--gold);font-weight:500}.map-links span{font-family:var(--serif);font-size:18px}.map-links small{display:block;font-family:var(--sans);font-size:11px;color:var(--moss);margin-top:6px}.meeting-family{padding:100px clamp(24px,8vw,140px)}.family-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}.family-grid a{min-height:260px;padding:24px;background:var(--white);border:1px solid var(--line);display:flex;flex-direction:column}.family-grid a span{color:var(--gold)}.family-grid h3{font:500 24px/1.2 var(--serif);margin-top:auto}.family-grid p{color:var(--ink2);font-size:14px}.practice-banner{margin:30px clamp(24px,6vw,100px) 100px;padding:54px 60px;background:var(--ink);color:var(--paper);display:flex;align-items:flex-end;justify-content:space-between;gap:40px}.practice-banner span{color:#bcb69f;font-size:12px;letter-spacing:.15em}.practice-banner h2{font:500 clamp(32px,4vw,54px)/1.2 var(--serif);margin:8px 0}.practice-banner p{color:#bfc7c1}.reading-path{padding:0 clamp(24px,8vw,140px) 120px}.path-grid{display:grid;grid-template-columns:1fr 1fr;gap:24px}.path-grid article{background:var(--white);padding:28px 34px;border:1px solid var(--line)}.path-grid article>span{color:var(--moss);font-weight:700;font-size:12px;letter-spacing:.13em}.path-grid ol{padding-left:24px}.path-grid li{padding:8px 0;border-bottom:1px solid #e5dfd5}.path-grid a:hover{color:var(--moss)}.article-grid{display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:80px;max-width:1240px;margin:0 auto;padding:30px 34px 120px}.article-main{min-width:0}.content-section{padding:54px 0;border-bottom:1px solid var(--line)}.content-section>p{font-size:17px;max-width:850px;color:var(--ink2)}.section-eyebrow{margin-bottom:8px}.callout{padding:26px 30px;margin:35px 0;background:#e4ddcf;border-left:3px solid var(--gold)}.callout.dark{background:var(--ink);color:var(--paper)}.callout strong{font:500 21px var(--serif)}.callout p{margin:8px 0}.sources{position:sticky;top:100px;align-self:start;margin-top:54px;padding:24px;background:var(--white);border:1px solid var(--line)}.source-head{display:flex;gap:12px;align-items:center;border-bottom:1px solid var(--line);padding-bottom:16px}.source-head svg{width:34px;stroke:var(--moss);fill:none}.source-head span{font-size:11px;color:var(--moss);display:block}.source-head strong{font:500 18px var(--serif)}.sources ul{list-style:none;padding:0;margin:18px 0}.sources li{padding:12px 0;border-bottom:1px dashed var(--line)}.sources li b,.sources li span{display:block}.sources li b{font:500 15px var(--serif)}.sources li span{font-size:12px;color:var(--ink2);margin-top:5px}.text-link{font-size:13px;color:var(--moss)}.compare-mini,.role-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}.compare-mini>div,.role-grid article{padding:24px;background:var(--white);border:1px solid var(--line)}.compare-mini b,.role-grid b{font:500 22px var(--serif)}.definition-list dl{display:grid;grid-template-columns:140px 1fr;margin:0}.definition-list dt,.definition-list dd{padding:15px 0;border-bottom:1px solid var(--line)}.definition-list dt{font-weight:700;color:var(--moss)}.definition-list dd{margin:0}.myth-grid,.signal-grid,.care-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}.myth-grid article,.signal-grid article,.care-grid article{padding:22px;background:var(--white);border:1px solid var(--line)}.myth-grid b,.signal-grid b{font:500 18px var(--serif)}.myth-grid p,.signal-grid p,.care-grid p{font-size:14px;color:var(--ink2)}.process-row{display:flex;align-items:center;flex-wrap:wrap;gap:8px}.process-row span{padding:9px 13px;border:1px solid var(--line);border-radius:999px;background:var(--white)}.process-row i{color:var(--gold)}.fineprint{font-size:12px!important;color:#68726c!important}.query-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:24px}.query-card{min-height:180px;padding:22px;background:var(--ink);color:var(--paper)}.query-card span{font-size:10px;letter-spacing:.16em;color:#b9b49f}.query-card p{font:500 20px/1.55 var(--serif)}.three-stage{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.three-stage article{padding:22px;border-top:2px solid var(--gold);background:var(--white)}.three-stage span{font-size:11px;color:var(--gold)}.three-stage h3{font:500 28px var(--serif);margin:8px 0}.practice-steps{display:grid;gap:10px}.practice-steps article{padding:19px 22px;background:var(--white);border-left:2px solid var(--moss)}.practice-steps b{font:500 19px var(--serif)}.practice-steps p{margin:5px 0;color:var(--ink2)}.ladder{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border:1px solid var(--line)}.ladder>div{padding:18px;border-right:1px solid var(--line)}.ladder>div:last-child{border:0}.ladder span{font-weight:700}.ladder p{font-size:13px;color:var(--ink2)}.cta-inline{display:flex;gap:12px;flex-wrap:wrap;margin-top:30px}.practice-intro,.after-practice,.timer-shell{max-width:1120px;margin:0 auto;padding:50px 34px}.practice-intro{display:grid;grid-template-columns:1.3fr .7fr;gap:50px}.practice-intro h2,.after-practice h2{font:500 clamp(34px,4vw,54px)/1.2 var(--serif)}.practice-rules{display:flex;flex-wrap:wrap;align-content:center;gap:8px}.practice-rules span{padding:8px 12px;border:1px solid var(--line);border-radius:999px;background:var(--white);font-size:13px}.timer-shell{background:var(--ink);color:var(--paper);margin-top:20px;box-shadow:var(--shadow)}.timer-top{display:grid;grid-template-columns:1fr 240px;align-items:center;gap:40px}.timer-top h2{font:500 clamp(30px,4vw,54px)/1.2 var(--serif);margin:10px 0}.timer-top p{color:#bdc6c0}.timer-circle{position:relative;width:220px;height:220px}.timer-circle svg{transform:rotate(-90deg)}.timer-bg,.timer-progress{fill:none;stroke-width:5}.timer-bg{stroke:#3b4641}.timer-progress{stroke:var(--gold);stroke-linecap:round;stroke-dasharray:327;stroke-dashoffset:0}.timer-circle strong{position:absolute;inset:0;display:grid;place-items:center;font:500 42px var(--serif)}.timer-controls{display:flex;gap:10px;margin:24px 0}.timer-shell .btn.primary{background:var(--paper);color:var(--ink);border-color:var(--paper)}.timer-shell .btn.ghost{color:var(--paper);border-color:#5d6862}.stage-track{display:grid;grid-template-columns:repeat(5,1fr);gap:6px}.stage-track span{height:4px;background:#46514c}.stage-track span.active{background:var(--gold)}.reflection-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.reflection-grid label{font-size:13px;font-weight:700}.reflection-grid textarea{width:100%;min-height:150px;margin-top:8px;padding:14px;border:1px solid var(--line);background:var(--white);resize:vertical}.reflection-actions{display:flex;align-items:center;gap:12px;margin-top:18px}.skill-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.skill-grid article{padding:20px;border:1px solid var(--line);background:var(--white)}.skill-grid svg{width:38px;height:38px;stroke:var(--moss);fill:none;stroke-width:1.4}.skill-grid h3{font:500 21px var(--serif)}.skill-grid p{font-size:13px;color:var(--ink2)}.ministry-flow{display:flex;flex-direction:column;max-width:520px;margin:20px auto}.ministry-flow span,.ministry-flow strong{padding:13px 18px;border:1px solid var(--line);background:var(--white);text-align:center}.ministry-flow i{text-align:center;color:var(--gold)}.discern-box{display:grid;gap:10px;background:var(--white);padding:24px;border:1px solid var(--line)}.discern-box label{display:flex;gap:10px;padding:8px 0;border-bottom:1px dashed var(--line)}.discern-box .btn{justify-self:start}.result-note{font:500 18px var(--serif);color:var(--moss)}.signal-grid{grid-template-columns:repeat(3,1fr)}.practice-card{padding:26px;background:var(--white);border:1px solid var(--line)}.practice-card>span{font-size:12px;color:var(--moss);font-weight:700}.practice-card li{margin:8px 0}.decision-visual{margin:30px 0;padding:28px;background:var(--ink);color:var(--paper)}.decision-track{display:flex;gap:8px;flex-wrap:wrap;align-items:center}.decision-track span,.decision-track strong{padding:8px 11px;border:1px solid #637068;border-radius:999px;font-size:12px}.decision-track i{color:var(--gold)}.decision-visual p{font-size:13px;color:#b9c1bc}.compare-table{border:1px solid var(--line);background:var(--white)}.compare-table .row{display:grid;grid-template-columns:.7fr 1.2fr 1fr 1.2fr}.compare-table .row>*{padding:14px;border-right:1px solid var(--line);border-bottom:1px solid var(--line)}.compare-table .row>*:last-child{border-right:0}.compare-table .head{background:#ddd5c7;font-size:12px;font-weight:700}.compare-table .accent{background:#ece6d8}.role-grid .accent{border-top:3px solid var(--gold)}.case-lab,.question-lab{padding:26px;background:var(--white);border:1px solid var(--line)}.case-options,.question-actions{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0}.case-options button,.question-actions button,.filter-row button,.tool-grid button{border:1px solid var(--line);background:var(--paper);padding:10px 12px;cursor:pointer}.case-result,.question-feedback{padding:16px;background:#eee8dc;border-left:3px solid var(--gold);min-height:76px}.agenda{border-top:1px solid var(--ink)}.agenda>div{display:grid;grid-template-columns:90px 1fr;gap:20px;padding:13px 0;border-bottom:1px solid var(--line)}.agenda b{color:var(--gold)}.clearness-flow{display:grid;grid-template-columns:1fr 1fr;gap:10px}.clearness-flow article{padding:18px;background:var(--white);border:1px solid var(--line)}.clearness-flow b{font:500 18px var(--serif)}.clearness-flow p{font-size:13px;color:var(--ink2)}.question-example{font:500 26px/1.55 var(--serif);padding:20px;background:#f5f1e8}.rewrite-list{display:grid;gap:12px}.rewrite-list article{padding:20px;background:var(--white);border:1px solid var(--line)}.rewrite-list small{color:var(--moss)}.rewrite-list b{display:block;color:var(--moss)}.triad-visual{margin:30px 0}.triad-visual svg circle{fill:var(--white);stroke:var(--moss);stroke-width:1.5}.triad-visual svg .third{fill:#e6ddc9;stroke:var(--gold)}.triad-line{fill:none;stroke:#a7aea9;stroke-width:1}.triad-visual text{text-anchor:middle;font:500 23px var(--serif);fill:var(--ink)}.triad-visual .sub{font:12px var(--sans);fill:var(--moss)}.triad-visual .center-label{font:12px var(--sans);fill:var(--gold)}.org-map{display:flex;align-items:center;gap:12px;flex-wrap:wrap}.org-map div{padding:16px 18px;border:1px solid var(--line);background:var(--white)}.org-map small{display:block;color:var(--moss)}.org-map i{color:var(--gold)}.history-lead,.comparison-intro,.research-intro,.toolkit-top,.glossary-top{max-width:1100px;margin:0 auto;padding:60px 34px}.history-lead h2,.comparison-intro h2,.research-intro h2,.toolkit-top h2,.glossary-top h2{font:500 clamp(38px,5vw,66px)/1.18 var(--serif);margin:12px 0}.timeline-section{max-width:1120px;margin:0 auto;padding:20px 34px 110px}.timeline{border-left:1px solid var(--moss);margin-left:100px}.time-item{display:grid;grid-template-columns:110px 1fr;gap:30px;margin-left:-110px;padding:0 0 42px}.time-item time{color:var(--gold);font:500 18px var(--serif);text-align:right;padding-top:7px}.time-item>div{position:relative;padding-left:30px}.time-item>div:before{content:"";position:absolute;width:9px;height:9px;border-radius:50%;background:var(--gold);left:-5px;top:12px}.time-item h3{font:500 28px var(--serif);margin:0}.time-item p{color:var(--ink2)}.tension-grid,.scenario-grid,.book-grid,.roadmap-list,.tool-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.tension-grid article,.scenario-grid article,.book-grid article,.roadmap-list article,.tool-grid article{padding:22px;background:var(--white);border:1px solid var(--line)}.tension-grid b,.roadmap-list b{font:500 19px var(--serif)}.comparison-intro,.research-intro,.toolkit-top{max-width:100%;padding-left:clamp(24px,8vw,140px);padding-right:clamp(24px,8vw,140px)}.matrix-wrap{overflow:auto}.matrix{width:100%;border-collapse:collapse;min-width:980px;background:var(--white);font-size:13px}.matrix th,.matrix td{padding:14px;border:1px solid var(--line);vertical-align:top}.matrix thead th{background:#ddd5c7;text-align:left}.matrix tbody th{font-family:var(--serif);font-size:15px}.scenario-grid article span{font-size:11px;color:var(--moss)}.scenario-grid h3{font:500 20px var(--serif)}.glossary-top{display:grid;grid-template-columns:1fr 340px;gap:70px;align-items:end}.search-box{display:grid;gap:8px;font-size:12px;color:var(--moss)}.search-box input{padding:14px 16px;border:1px solid var(--line);background:var(--white)}.filter-row{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:24px}.filter-row button.active{background:var(--ink);color:var(--paper)}.glossary-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.glossary-card{padding:22px;background:var(--white);border:1px solid var(--line)}.glossary-card>span{font-size:10px;color:var(--moss)}.glossary-card h3{font:500 22px var(--serif);margin:8px 0 2px}.glossary-card h4{margin:0;color:var(--moss)}.glossary-card p{font-size:13px;color:var(--ink2)}.book-grid article>span{font-size:10px;color:var(--moss);letter-spacing:.1em}.book-grid h3{font:500 22px/1.35 var(--serif)}.book-grid p{font-size:13px;color:var(--ink2)}.book-grid small{color:var(--moss)}.method-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.method-grid b{min-height:120px;display:flex;align-items:flex-end;padding:18px;background:var(--ink);color:var(--paper);font:500 17px/1.5 var(--serif)}.research-note{padding:40px;background:var(--ink);color:var(--paper)}.research-note h2{margin-top:0}.tool-grid article>span{font-size:11px;color:var(--moss)}.tool-grid h3{font:500 23px var(--serif)}.tool-grid li{margin:7px 0}.tool-grid button{margin-top:8px}.four-lines{display:grid;grid-template-columns:1fr 1fr;gap:10px}.four-lines p{margin:0;padding:28px;background:var(--white);border:1px solid var(--line);font:500 24px/1.45 var(--serif)}.site-footer{background:#19201d;color:#d8ddd8;padding:50px clamp(24px,6vw,100px);display:grid;grid-template-columns:1.3fr .7fr;gap:40px}.site-footer b{font-family:var(--serif);font-size:20px}.site-footer p{color:#9eaaa3;font-size:13px}.footer-links{display:flex;flex-direction:column;gap:8px}.footer-links a{color:#c9d0cb}.footer-note{grid-column:1/-1;border-top:1px solid #364039;padding-top:20px}
@media(max-width:980px){.main-nav{display:none;position:absolute;left:0;right:0;top:64px;background:var(--paper);padding:20px 24px;flex-wrap:wrap;border-bottom:1px solid var(--line)}.main-nav.open{display:flex}.nav-toggle{display:block}.home-hero,.home-intro,.layer-diagram,.practice-intro,.glossary-top{grid-template-columns:1fr}.home-hero{padding-top:60px}.circle-visual svg{max-height:400px}.map-links,.family-grid{grid-template-columns:1fr 1fr}.article-grid{grid-template-columns:1fr;gap:0}.sources{position:relative;top:auto}.tension-grid,.scenario-grid,.book-grid,.roadmap-list,.tool-grid,.glossary-grid{grid-template-columns:1fr 1fr}.method-grid{grid-template-columns:1fr 1fr}.query-grid,.signal-grid,.skill-grid{grid-template-columns:1fr 1fr}.timer-top{grid-template-columns:1fr}.timer-circle{width:190px;height:190px}.reflection-grid{grid-template-columns:1fr}.site-footer{grid-template-columns:1fr}}
@media(max-width:640px){.page-hero{padding-top:48px}.home-hero{grid-template-columns:1fr}.home-copy h1{font-size:58px}.map-links,.family-grid,.path-grid,.myth-grid,.care-grid,.compare-mini,.role-grid,.three-stage,.clearness-flow,.query-grid,.signal-grid,.skill-grid,.tension-grid,.scenario-grid,.book-grid,.roadmap-list,.tool-grid,.glossary-grid,.four-lines{grid-template-columns:1fr}.layer-legend{margin-top:-20px}.practice-banner{padding:34px;display:block}.practice-banner .btn{margin-top:20px}.ladder{grid-template-columns:1fr}.ladder>div{border-right:0;border-bottom:1px solid var(--line)}.compare-table .row{grid-template-columns:1fr}.compare-table .head{display:none}.compare-table .row>*{border-right:0}.stage-track{grid-template-columns:repeat(5,1fr)}.time-item{grid-template-columns:70px 1fr;margin-left:-80px}.timeline{margin-left:80px}.agenda>div{grid-template-columns:70px 1fr}.method-grid{grid-template-columns:1fr}.site-footer{padding:40px 24px}}
@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}.halo{animation:none!important}.btn{transition:none}}
@media print{.site-header,.site-footer,.nav-toggle,.btn,.case-options,.question-actions,.filter-row{display:none!important}body{background:#fff}.content-section{break-inside:avoid}.page-hero{padding-top:20px}}

/* ---- 2.0 reading & visual system ---- */
body{overflow-x:clip}
.site-header,.site-header>*{min-width:0}
h1,h2,h3,.query-card p,.four-lines p,.question-example{
  text-wrap:balance;
  word-break:keep-all;
  overflow-wrap:anywhere;
  line-break:strict;
}
p,li,dd{orphans:2;widows:2;overflow-wrap:anywhere}
.page-hero .hero-copy{max-width:1120px}
.page-hero h1{max-width:none;font-size:clamp(42px,5.5vw,76px);letter-spacing:-.025em}
.page-hero p{max-width:820px;line-height:1.9}
.home-copy{min-width:0}
.home-copy h1{max-width:6.2em;font-size:clamp(56px,7.4vw,104px);line-height:1.04;letter-spacing:-.035em}
.big-question h2{max-width:15ch;line-height:1.28}
.section-head h2,.content-section h2{max-width:21ch;line-height:1.28}
.content-section>p,.article-main .content-section>p{max-width:46rem;line-height:1.9}
.article-main{font-size:16px}
.article-main p{line-height:1.9}
main>.content-section{padding-left:clamp(24px,8vw,140px);padding-right:clamp(24px,8vw,140px)}
.article-main>.content-section{padding-left:0;padding-right:0}

.home-depth{padding:100px clamp(24px,8vw,140px);background:var(--white);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.home-depth>.section-head{margin-bottom:28px}
.depth-grid,.history-thesis,.four-forces,.term-relations,.comparison-lenses,.false-friends,.research-discipline,.source-matrix,.contested-grid,.reading-trails,.boundary-grid{
  display:grid;
  gap:14px;
}
.depth-grid{grid-template-columns:repeat(3,1fr);margin-top:28px}
.depth-grid article,.history-thesis article,.four-forces article,.term-relations article,.comparison-lenses article,.false-friends article,.research-discipline article,.source-matrix article,.contested-grid article,.reading-trails article,.boundary-grid article{
  background:var(--white);
  border:1px solid var(--line);
  padding:24px;
  min-width:0;
}
.home-depth .depth-grid article{background:var(--paper)}
.depth-grid span,.history-thesis span,.comparison-lenses span,.research-discipline span{font-size:11px;letter-spacing:.12em;color:var(--gold)}
.depth-grid h3,.history-thesis h3,.false-friends h3,.research-discipline h3,.contested-grid h3{
  font:500 22px/1.4 var(--serif);
  margin:10px 0;
}
.depth-grid p,.history-thesis p,.four-forces p,.term-relations p,.comparison-lenses p,.false-friends p,.research-discipline p,.source-matrix p,.contested-grid p,.reading-trails p,.boundary-grid p{
  color:var(--ink2);
  font-size:14px;
  line-height:1.8;
}

.concept-figure{margin:34px 0 42px;padding:28px;background:linear-gradient(135deg,#ebe5d9,#f7f3ea);border:1px solid var(--line)}
.concept-figure.compact{padding:20px 26px}
.concept-figure svg{display:block;width:100%;max-height:500px}
.concept-figure .field{fill:#748578;opacity:.14;stroke:#65776a;stroke-width:1}
.concept-figure .field.b{fill:#b49a5c;stroke:#9c8248}
.concept-figure .field.c{fill:#89969f;stroke:#6e7b83}
.concept-figure .center-glow{fill:#d6bb78;opacity:.42}
.concept-figure .node{fill:#f8f4eb;stroke:var(--moss);stroke-width:1.4}
.concept-figure .axis{stroke:#9aa39c;stroke-width:1.1}
.concept-figure .wave{fill:none;stroke:var(--moss);stroke-width:2}
.concept-figure .wave.faint{opacity:.3;stroke:var(--gold)}
.concept-figure .core-dot{fill:var(--gold)}
.concept-figure text{text-anchor:middle;fill:var(--ink);font:500 16px var(--serif)}
.concept-figure .figure-main{font:600 18px var(--sans)}
.concept-figure .figure-sub{font:12px var(--sans);fill:var(--ink2)}
.concept-figure figcaption{display:grid;grid-template-columns:190px 1fr;gap:24px;border-top:1px solid var(--line);padding-top:18px;margin-top:8px}
.concept-figure figcaption b{font:500 18px var(--serif)}
.concept-figure figcaption span{font-size:13px;line-height:1.8;color:var(--ink2)}

.research-card{margin:30px 0;padding:28px 30px;background:#202925;color:var(--paper);border-left:3px solid var(--gold)}
.research-card>span{display:block;font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:#cbbd94;margin-bottom:8px}
.research-card h3{font:500 25px/1.45 var(--serif);margin:0 0 10px;max-width:25ch}
.research-card p{color:#c9d0cb;margin:8px 0;line-height:1.85}

.history-thesis{grid-template-columns:repeat(3,1fr);max-width:1120px;margin:0 auto;padding:0 34px 70px}
.history-thesis article{background:#ece5d8;border-top:3px solid var(--gold)}
.timeline-section{max-width:1180px;padding-top:20px}
.timeline-v2{position:relative}
.timeline-v2:before{content:"";position:absolute;left:145px;top:18px;bottom:20px;width:1px;background:linear-gradient(to bottom,var(--gold),var(--moss) 18%,var(--moss) 82%,rgba(93,109,96,.15))}
.timeline-v2 .time-item{display:grid;grid-template-columns:110px 34px minmax(0,1fr);gap:18px;margin:0;padding:0 0 38px;align-items:start}
.timeline-v2 .time-item time{grid-column:1;color:var(--gold);font:500 17px/1.35 var(--serif);text-align:right;padding:7px 0 0}
.timeline-node{grid-column:2;width:13px;height:13px;border-radius:50%;background:var(--paper);border:3px solid var(--gold);justify-self:center;margin-top:8px;z-index:2;box-shadow:0 0 0 5px var(--paper)}
.timeline-card{grid-column:3;background:var(--white);border:1px solid var(--line);padding:22px 24px;position:relative}
.timeline-card:before{content:"";position:absolute;left:-19px;top:14px;width:18px;height:1px;background:var(--line);border-radius:0}
.timeline-card h3{font:500 27px/1.4 var(--serif);margin:0 0 8px}
.timeline-card p{margin:0;color:var(--ink2);line-height:1.85}
.timeline-tag{display:inline-block;margin-top:14px;padding:5px 9px;border:1px solid #d8d0c2;font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--moss)}
.history-framework{background:#e8e1d4}
.four-forces{grid-template-columns:repeat(4,1fr)}
.four-forces article{background:#f6f1e8}
.four-forces b{display:block;font:500 21px var(--serif)}
.four-forces span{display:block;color:var(--gold);font-size:11px;margin:4px 0 10px}

.boundary-grid{grid-template-columns:1fr 1fr;margin-top:22px}
.boundary-grid article{border-top:2px solid #8a6c55}
.practice-ladder-v2{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.practice-ladder-v2 article{padding:22px;background:var(--white);border-top:3px solid var(--moss);min-width:0}
.practice-ladder-v2 span{font-size:10px;letter-spacing:.12em;color:var(--gold)}
.practice-ladder-v2 h3{font:500 21px/1.4 var(--serif);margin:8px 0}
.practice-ladder-v2 p{font-size:13px;line-height:1.75;color:var(--ink2)}
.boundary-grid b{font:500 18px var(--serif)}

.term-relations{grid-template-columns:1fr 1fr}
.term-relations article{border-top:2px solid var(--moss)}
.term-relations b{font:500 19px var(--serif)}

.research-discipline,.source-matrix{grid-template-columns:repeat(3,1fr)}
.research-discipline article{min-height:200px}
.source-matrix article{border-top:2px solid var(--moss)}
.source-matrix b{font:500 21px var(--serif);display:block}
.source-matrix span{font-size:10px;color:var(--gold);letter-spacing:.12em}
.contested-grid{grid-template-columns:1fr 1fr}
.contested-grid article{background:#eee7da}
.contested-grid p{margin:9px 0}
.reading-trails{grid-template-columns:repeat(3,1fr)}
.reading-trails article{border-top:3px solid var(--gold)}
.reading-trails span{font-size:11px;color:var(--moss);letter-spacing:.08em}
.reading-trails p{font:500 19px/1.5 var(--serif);color:var(--ink)}
.reading-trails small{display:block;color:var(--ink2);line-height:1.7}

.comparison-lenses{grid-template-columns:repeat(4,1fr);padding:0 clamp(24px,8vw,140px) 60px}
.comparison-lenses article{background:#e8e1d4}
.comparison-lenses b{display:block;font:500 22px var(--serif);margin:8px 0}
.false-friends{grid-template-columns:repeat(3,1fr)}
.false-friends article{border-top:3px solid var(--gold)}

.family-grid a,.myth-grid article,.signal-grid article,.care-grid article,.book-grid article,.roadmap-list article,.tool-grid article,.glossary-card,.query-card,.scenario-grid article{
  transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease;
}
.family-grid a:hover,.book-grid article:hover,.glossary-card:hover,.scenario-grid article:hover{
  transform:translateY(-2px);
  box-shadow:0 12px 28px rgba(31,39,35,.07);
  border-color:#b9ad9b;
}

@media(max-width:980px){
  .depth-grid,.history-thesis,.research-discipline,.source-matrix,.reading-trails,.comparison-lenses,.practice-ladder-v2{grid-template-columns:1fr 1fr}
  .four-forces{grid-template-columns:1fr 1fr}
  .comparison-lenses{padding-bottom:42px}
  .concept-figure figcaption{grid-template-columns:1fr;gap:7px}
}
@media(max-width:640px){
  h1,h2,h3{text-wrap:wrap}
  .site-header .nav-toggle{display:block!important;position:absolute;right:18px;top:17px;color:var(--ink)}
  .site-header{padding-right:62px}
  .page-hero h1{font-size:clamp(38px,11vw,48px);max-width:none}
  .home-copy h1{font-size:clamp(48px,15vw,68px);max-width:6.2em}
  .big-question h2,.section-head h2,.content-section h2{max-width:100%}
  .home-depth{padding-top:70px;padding-bottom:70px}
  .depth-grid,.history-thesis,.four-forces,.term-relations,.comparison-lenses,.false-friends,.research-discipline,.source-matrix,.contested-grid,.reading-trails,.boundary-grid,.practice-ladder-v2{grid-template-columns:1fr}
  .history-thesis{padding:0 24px 54px}
  .timeline-section{padding-left:20px;padding-right:20px}
  .timeline-v2:before{left:88px}
  .timeline-v2 .time-item{grid-template-columns:64px 28px minmax(0,1fr);gap:10px;padding-bottom:28px}
  .timeline-v2 .time-item time{font-size:13px;padding-top:8px}
  .timeline-node{width:11px;height:11px;border-width:2px;box-shadow:0 0 0 4px var(--paper)}
  .timeline-card{padding:18px 17px}
  .timeline-card:before{left:-11px;width:10px}
  .timeline-card h3{font-size:21px}
  .timeline-card p{font-size:14px}
  .concept-figure{padding:12px;margin:24px 0 32px;overflow:hidden}
  .concept-figure svg{min-width:560px;transform:translateX(-12%)}
  .concept-figure figcaption{padding:14px 6px 4px}
  .research-card{padding:24px 22px}
  .comparison-lenses{padding-left:24px;padding-right:24px}
}
'''

js = r'''
(() => {
  const navToggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.main-nav');
  navToggle?.addEventListener('click', () => nav?.classList.toggle('open'));

  // 12 minute practice timer
  const display = document.getElementById('timeDisplay');
  if (display) {
    const total = 12*60;
    const stages = [
      {until:90,title:'坐下来，让自己到达这里。',prompt:'注意身体、房间和此刻的状态。不需要马上安静。',label:'到场'},
      {until:180,title:'允许声音与念头存在。',prompt:'不跟随，也不排斥。你只是在这里。',label:'安顿'},
      {until:600,title:'从“我要做什么”转向等待。',prompt:'不必寻找什么。只是等待，并留意什么正在出现。',label:'等候'},
      {until:690,title:'留意有没有什么变得稍微清楚。',prompt:'不是逼出答案。只是注意重量、方向、反复出现的东西。',label:'辨识'},
      {until:720,title:'准备结束。',prompt:'把注意带回身体和房间。带走问题，不必带走结论。',label:'返回'}
    ];
    let remain=total, timer=null, running=false;
    const progress=document.getElementById('timerProgress');
    const stageTitle=document.getElementById('stageTitle');
    const stagePrompt=document.getElementById('stagePrompt');
    const stageIndex=document.getElementById('stageIndex');
    const track=document.getElementById('stageTrack');
    track.innerHTML=stages.map(()=>'<span></span>').join('');
    const fmt=n=>`${String(Math.floor(n/60)).padStart(2,'0')}:${String(n%60).padStart(2,'0')}`;
    function bell(){ try{ const ctx=new (window.AudioContext||window.webkitAudioContext)(); const o=ctx.createOscillator(),g=ctx.createGain(); o.type='sine';o.frequency.value=523.25;g.gain.setValueAtTime(0.0001,ctx.currentTime);g.gain.exponentialRampToValueAtTime(.08,ctx.currentTime+.03);g.gain.exponentialRampToValueAtTime(.0001,ctx.currentTime+1.4);o.connect(g).connect(ctx.destination);o.start();o.stop(ctx.currentTime+1.5);}catch(e){} }
    function render(){
      display.textContent=fmt(remain);
      const elapsed=total-remain; const stage=stages.findIndex(s=>elapsed < s.until); const idx=stage<0?stages.length-1:stage;
      stageTitle.textContent=stages[idx].title; stagePrompt.textContent=stages[idx].prompt; stageIndex.textContent=stages[idx].label;
      [...track.children].forEach((el,i)=>el.classList.toggle('active',i<=idx));
      const circumference=327; progress.style.strokeDashoffset=(circumference*(1-remain/total)).toFixed(1);
    }
    function tick(){ if(remain<=0){clearInterval(timer);running=false;bell();return;} remain--; render(); }
    document.getElementById('startTimer').onclick=()=>{ if(running)return; running=true; bell(); timer=setInterval(tick,1000); };
    document.getElementById('pauseTimer').onclick=()=>{clearInterval(timer);running=false;};
    document.getElementById('resetTimer').onclick=()=>{clearInterval(timer);running=false;remain=total;render();};
    render();
    const ids=['r1','r2','r3']; ids.forEach(id=>{const el=document.getElementById(id); el.value=localStorage.getItem('meeting_'+id)||'';});
    document.getElementById('saveReflection').onclick=()=>{ids.forEach(id=>localStorage.setItem('meeting_'+id,document.getElementById(id).value));document.getElementById('saveStatus').textContent='已保存在此浏览器';};
    document.getElementById('clearReflection').onclick=()=>{ids.forEach(id=>{localStorage.removeItem('meeting_'+id);document.getElementById(id).value='';});document.getElementById('saveStatus').textContent='已清空';};
  }

  // Ministry self-test
  const mt=document.getElementById('ministryTest');
  if(mt){document.getElementById('evaluateMinistry').onclick=()=>{const n=mt.querySelectorAll('input:checked').length; const out=document.getElementById('ministryResult'); out.textContent=n>=4?'你已经在做一件很重要的事：让“说话的冲动”先接受等待。即使如此，也可以再多等一会儿。':n>=2?'可能值得继续等待。先别急着把“我很想说”解释成“我应该说”。':'先继续沉默也许更忠实。没有说出来，并不等于没有参与。';};}

  // Business case lab
  const caseLab=document.getElementById('caseLab');
  if(caseLab){const res=document.getElementById('caseResult');caseLab.querySelectorAll('[data-case]').forEach(b=>b.onclick=()=>{const k=b.dataset.case;res.innerHTML={vote:'<b>多数表决</b>优化的是速度与程序明确。7:3 很快有结果，但“离开原社区意味着什么”可能仍未被共同体真正消化。',consensus:'<b>Consensus</b>优化的是可接受度。大家会继续协商方案，但也可能把目标缩成“每个人都勉强能接受”。',sense:'<b>Sense of the Meeting</b>会把问题从“新址好不好”下沉到“我们的使命、邻里关系与可持续性中，什么方向最忠实？”结果可能是搬、也可能是不搬，甚至是暂缓决定。'}[k];});}

  // Clearness question lab
  const qLab=document.getElementById('questionLab');
  if(qLab){const data=[
    ['“你有没有想过，其实你应该先休息一段时间？”','advice','问题里已经塞进了答案：先休息。可以改问：“当你想象继续撑下去和停下来时，分别注意到什么？”'],
    ['“在这个决定里，哪一种担心最容易盖过你自己的声音？”','open','这是开放问题。它没有替对方命名答案，而是邀请他辨认内部声音。'],
    ['“你是不是因为太在意父母，所以才不敢离开？”','advice','这是一种解释加判断。可以改问：“在你考虑离开时，哪些人的声音会出现？它们分别对你有什么影响？”'],
    ['“如果暂时不用向任何人证明什么，你会怎样描述自己真正想保护的东西？”','open','这是开放问题。它提供一个角度，但不规定内容。']
  ];let i=0;const ex=document.getElementById('questionExample'),fb=document.getElementById('questionFeedback');function show(){ex.textContent=data[i][0];fb.textContent='先判断，再看为什么。';}qLab.querySelectorAll('[data-q]').forEach(b=>b.onclick=()=>{fb.textContent=(b.dataset.q===data[i][1]?'✓ ':'再看看：')+data[i][2];});document.getElementById('nextQuestion').onclick=()=>{i=(i+1)%data.length;show();};show();}

  // Glossary search & filter
  const gSearch=document.getElementById('glossarySearch');
  if(gSearch){let active='all';const cards=[...document.querySelectorAll('.glossary-card')];function apply(){const q=gSearch.value.trim().toLowerCase();cards.forEach(c=>{const txt=c.dataset.term+' '+c.textContent.toLowerCase();const cat=c.querySelector('span').textContent; c.style.display=(!q||txt.includes(q))&&(active==='all'||cat===active)?'block':'none';});}gSearch.oninput=apply;document.querySelectorAll('.filter').forEach(b=>b.onclick=()=>{document.querySelectorAll('.filter').forEach(x=>x.classList.remove('active'));b.classList.add('active');active=b.dataset.filter;apply();});}
})();
'''

(ROOT/'assets').mkdir(exist_ok=True)
(ROOT/'assets'/'style.css').write_text(css, encoding='utf-8')
(ROOT/'assets'/'app.js').write_text(js, encoding='utf-8')

# write pages
for fn, content in pages.items():
    (ROOT/fn).write_text(enhance_plain_headings(content), encoding='utf-8')


# favicon
(ROOT/'assets'/'favicon.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#1f2723"/><circle cx="32" cy="32" r="5" fill="#b49a5c"/><circle cx="32" cy="32" r="14" fill="none" stroke="#b49a5c" stroke-width="1.5"/><circle cx="32" cy="32" r="23" fill="none" stroke="#d8ddd8" stroke-width="1.5" opacity=".7"/></svg>''', encoding='utf-8')

# minimal README
readme = '''# 共同等候｜Quaker Meeting 研究与实践\n\n静态网站，无构建依赖。\n\n## 本地预览\n\n```bash\npython3 -m http.server 8000\n```\n然后访问 `http://localhost:8000/`。\n\n## 部署\n\n整个目录可直接发布到 GitHub Pages / Netlify / Cloudflare Pages。\n\n## 内容范围\n\n当前版本以 unprogrammed Quaker Meeting、Pendle Hill 相关文本、Howard Brinton、Thomas Kelly、Parker Palmer、Patricia Loring、Michael Marsh、Jim Pym 等为主要研究入口，并明确区分历史传统、现代转译与本站的实践性整理。\n\n## 主要交互\n\n- 12 分钟 Meeting 体验计时器\n- 本地反思记录（localStorage，不上传）\n- Vocal Ministry 自我辨识练习\n- Meeting for Business 决策案例\n- Clearness Committee 开放问题练习\n- 术语搜索与分类筛选\n'''
(ROOT/'README.md').write_text(readme, encoding='utf-8')

# basic link check
files=set(p.name for p in ROOT.glob('*.html'))
broken=[]
for p in ROOT.glob('*.html'):
    txt=p.read_text(encoding='utf-8')
    for m in re.finditer(r'href="([^"]+\.html)(?:#[^"]*)?"',txt):
        if m.group(1) not in files:
            broken.append((p.name,m.group(1)))
print(f'Wrote {len(pages)} pages. Broken links: {broken}')
