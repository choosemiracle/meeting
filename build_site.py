from pathlib import Path
import html, json, re

ROOT = Path(__file__).resolve().parent

SITE_NAME = '共同等候｜贵格会聚会研究与实践'
TAGLINE = '研究贵格会聚会（Meeting）如何通过静默、共同聆听与群体明辨，让尚未被任何个人完全拥有的真实，有机会出现。'
ASSET_VERSION = '20261004-ux8'

NAV_PRIMARY = [
    ('index.html','首页'),
    ('meeting.html','聚会'),
    ('worship.html','静默敬拜'),
    ('practice.html','开始实践'),
    ('history.html','历史'),
    ('research.html','研究室'),
]

NAV_MORE = [
    ('ministry.html','受感分享'),
    ('gathered.html','深度聚集'),
    ('business.html','共同明辨'),
    ('clearness.html','澄心会'),
    ('learning.html','共学'),
    ('community.html','共同体'),
    ('comparisons.html','方法比较'),
    ('traditions.html','会聚传统'),
    ('china.html','中国语境'),
    ('glossary.html','术语'),
    ('toolkit.html','工具箱'),
]

NAV = NAV_PRIMARY + NAV_MORE

PAGE_CONTINUE = {
    'meeting.html': [('worship.html','理解静默与等候'), ('practice.html','做一次 12 分钟体验')],
    'worship.html': [('ministry.html','什么时候该说话？'), ('practice.html','把理解带进练习')],
    'practice.html': [('meeting.html','回到聚会的完整结构'), ('ministry.html','继续理解受感分享')],
    'ministry.html': [('gathered.html','什么是深度聚集？'), ('business.html','从说话走向共同明辨')],
    'gathered.html': [('business.html','共同体怎样做决定？'), ('community.html','聚会怎样成为共同体？')],
    'business.html': [('clearness.html','理解澄心会'), ('community.html','看见共同体维度')],
    'clearness.html': [('learning.html','进入共学会'), ('toolkit.html','查看实践模板')],
    'learning.html': [('community.html','从共学走向共同体'), ('history.html','回到历史脉络')],
    'community.html': [('history.html','理解传统如何形成'), ('comparisons.html','与其他方法比较')],
    'history.html': [('comparisons.html','比较相近方法'), ('traditions.html','放进更大的会聚传统')],
    'comparisons.html': [('traditions.html','横向看世界会聚传统'), ('toolkit.html','选择合适实践')],
    'traditions.html': [('china.html','进入中国语境'), ('research.html','回到来源与研究方法')],
    'china.html': [('toolkit.html','把本土化原则变成实践'), ('practice.html','先做一次静默练习')],
    'glossary.html': [('research.html','查阅原典与研究方法'), ('meeting.html','回到核心概念')],
    'research.html': [('visual-credits.html','查看图像与史料说明'), ('toolkit.html','把研究转成实践')],
    'toolkit.html': [('practice.html','开始一次练习'), ('meeting.html','回到聚会全貌')],
    'visual-credits.html': [('research.html','返回研究室'), ('history.html','回到历史脉络')],
}

VISUAL_SOURCES = {
    'fox': 'https://commons.wikimedia.org/wiki/File:Supposed_portrait_of_George_Fox,_1677.png',
    'fell': 'https://commons.wikimedia.org/wiki/File:Margaret_Fell.jpg',
    'woolman': 'https://commons.wikimedia.org/wiki/File:John_Woolman.jpg',
    'penn': 'https://commons.wikimedia.org/wiki/File:Francis_Place_Chalk_Portrait_of_William_Penn_1695.jpg',
    'swarthmoor': 'https://commons.wikimedia.org/wiki/File:Swarthmoor_Hall.jpg',
    'interior': 'https://commons.wikimedia.org/wiki/File:Interior_of_Quaker_meeting_house.jpg',
    'arch': 'https://commons.wikimedia.org/wiki/File:Arch_Street_Meetinghouse_from_front.jpg',
    'free_interior': 'https://commons.wikimedia.org/wiki/File:Free_Quaker_Meeting_House,_interior_(813d353d-1dd8-b71b-0b26-1682e0a20a30).jpg',
}

# 中文读者优先：页面中保留英文时，以“中文主称（English）”呈现。
# 这里统一处理术语、作者、书名与编辑标签，避免不同页面各译各的。
TEXT_REPLACEMENTS = {
    'Quaker Meeting Lab': '贵格会聚会研究室（Quaker Meeting Lab）',
    'Designed for slow reading, careful listening, and lived practice.': '为慢读、谨慎聆听与生活实践而设计。',
    'Practice & Action': '实践与行动（Practice & Action）',
    'MEETING FOR LEARNING': '共学会（MEETING FOR LEARNING）',
    '90-MINUTE DESIGN': '90 分钟设计（90-MINUTE DESIGN）',
    'METHOD': '研究方法（METHOD）',
    'Group Mysticism': '群体神秘主义（Group Mysticism）',
    'Clearness': '澄明（Clearness）',
    'Brinton': '布林顿（Brinton）',
    'Arch Street Friends': '拱街贵格会友（Arch Street Friends）',
    'Authority': '权威（Authority）',
    'Success': '成功标准（Success）',
    'Boundary': '边界（Boundary）',
    'Mindfulness': '正念（Mindfulness）',
    'Coaching': '教练（Coaching）',
    'Group Therapy': '团体治疗（Group Therapy）',
    'Bohm Dialogue': '博姆对话（Bohm Dialogue）',
    'Meditation group': '冥想小组（Meditation group）',
    'Clearness ≠ Coaching': '澄心会 ≠ 教练（Clearness ≠ Coaching）',
    'Inner Teacher / soul / wholeness': '内在导师／灵魂／完整性（Inner Teacher / soul / wholeness）',
    'wholeness、integrity': '完整性、诚信（wholeness, integrity）',
    'collective thought process': '集体思维过程（collective thought process）',
    'That of God in everyone': '每个人里面“属神的那一份”（That of God in everyone）',
    'From Meeting to Circle of Trust': '从聚会到信任圈（From Meeting to Circle of Trust）',
    'Waiting upon the Lord': '等候主（Waiting upon the Lord）',
    'House': '聚会所',
    'house interior': '聚会所室内',
    'House interior': '聚会所室内',
    'PORTRAIT · 1677': '肖像 · 1677（PORTRAIT）',
    'PORTRAIT · 1695': '肖像 · 1695（PORTRAIT）',
    'PORTRAIT / MEMORY SKETCH': '肖像／记忆性速写（PORTRAIT / MEMORY SKETCH）',
    'LATER IMPRESSION': '后世艺术印象（LATER IMPRESSION）',
    'FIELD PHOTO · 2021': '现场照片 · 2021（FIELD PHOTO）',
    'NPS DOCUMENTATION': '美国国家公园管理局记录（NPS DOCUMENTATION）',
    'PLACE · 2005': '地点 · 2005（PLACE）',
    'PLACE · 2013': '地点 · 2013（PLACE）',
    'Public domain in U.S.': '在美国属公有领域（Public domain in U.S.）',
    'Public domain (U.S.)': '美国公有领域（Public domain, U.S.）',
    'Public domain': '公有领域（Public domain）',
    'Probably Robert Smith III': '可能为罗伯特·史密斯三世（Probably Robert Smith III）',
    'Robert Spence engraving': '罗伯特·斯彭斯蚀刻（Robert Spence engraving）',
    'U.S. National Park Service': '美国国家公园管理局（U.S. National Park Service）',
    # Core Quaker terms — specific phrases must win before generic words.
    'Meeting for Worship for Business': '敬拜式议事（Meeting for Worship for Business）',
    'Meeting for Worship': '静默敬拜（Meeting for Worship）',
    'Meeting for Learning': '共学会（Meeting for Learning）',
    'Sense of the Meeting': '聚会的共同辨识（Sense of the Meeting）',
    'Clearness Committee': '澄心会（Clearness Committee）',
    'Vocal Ministry': '受感分享（Vocal Ministry）',
    'Gathered Meeting': '深度聚集的聚会（Gathered Meeting）',
    'Meeting for Business': '议事会（Meeting for Business）',
    'Meeting Community': '聚会共同体（Meeting Community）',
    'Business Meeting': '议事会（Business Meeting）',
    'Quaker Meeting': '贵格会聚会（Quaker Meeting）',
    'Meeting House': '聚会所（Meeting House）',
    'Inner Light': '内在之光（Inner Light）',
    'Inward Light': '内在之光（Inward Light）',
    'Third Thing': '第三物（Third Thing）',
    'Circle of Trust': '信任圈（Circle of Trust）',
    'Faith and Practice': '信仰与实践（Faith and Practice）',
    'Advices & Queries': '劝勉与省察问题（Advices & Queries）',
    'Standing Aside': '保留但不阻挡（Standing Aside）',
    'Threshing Session': '预备性深谈（Threshing Session）',
    'Right Ordering': '合宜秩序（Right Ordering）',
    'Holding in the Light': '在光中守望（Holding in the Light）',
    'Unprogrammed Worship': '非程序化敬拜（Unprogrammed Worship）',
    'Programmed Worship': '程序化敬拜（Programmed Worship）',
    'Quakerism': '贵格会传统（Quakerism）',
    'group mysticism': '群体神秘主义（group mysticism）',
    'Group mysticism': '群体神秘主义（Group mysticism）',
    'corporate discernment': '群体明辨（corporate discernment）',
    'community testing': '共同体检验（community testing）',
    'spiritual discernment': '灵性明辨（spiritual discernment）',
    'divine leading': '神圣引领（divine leading）',
    'Divine Presence': '神圣临在（Divine Presence）',
    'expectant waiting': '带着期待的等候（expectant waiting）',
    'reverent waiting': '敬虔等候（reverent waiting）',
    'spoken ministry': '口头受感分享（spoken ministry）',
    'designated Friends': '指定会友（designated Friends）',
    'routine business': '例行事务（routine business）',
    'emerging sense': '正在形成的共同辨识（emerging sense）',
    'draft minute': '决议纪要草案（draft minute）',
    'open questions': '开放式问题（open questions）',
    'focal person': '焦点人（focal person）',
    'inward experience': '内在经验（inward experience）',
    'inward guidance': '内在引导（inward guidance）',
    'inward orientation': '内在取向（inward orientation）',
    'inward attention': '内在注意（inward attention）',
    'inward sanctuary': '内在圣所（inward sanctuary）',
    'inward life': '内在生命（inward life）',
    'outward action': '外在行动（outward action）',
    'outward witness': '外在见证（outward witness）',
    'workaday life': '日常生活（workaday life）',
    'group worship': '群体敬拜（group worship）',
    'group meditation': '群体冥想（group meditation）',
    'meditation group': '冥想小组（meditation group）',
    'teacher role': '教师角色（teacher role）',
    'group trust': '群体信任（group trust）',
    'corporate attention': '群体注意（corporate attention）',
    'Corporate attention': '群体注意（Corporate attention）',
    'problems to solve': '待解决的问题（problems to solve）',
    'mysteries to ponder': '值得体会的奥秘（mysteries to ponder）',
    'programmed / pastoral / unprogrammed': '程序化／牧师制／非程序化（programmed / pastoral / unprogrammed）',
    'programmed / unprogrammed': '程序化／非程序化（programmed / unprogrammed）',
    'evangelical / conservative / liberal': '福音派／保守派／自由派（evangelical / conservative / liberal）',
    'liberal Friends': '自由派会友（liberal Friends）',
    'Christian language': '基督教语言（Christian language）',
    'Quaker life': '贵格会生活（Quaker life）',
    'Quaker DNA': '贵格会传统基因（Quaker DNA）',
    'Quaker tradition': '贵格会传统（Quaker tradition）',
    'Quaker discipline': '贵格会实践纪律（Quaker discipline）',
    'Quaker spirituality': '贵格会灵性传统（Quaker spirituality）',
    'equality testimony': '平等见证（equality testimony）',
    'Quaker movement': '贵格会运动（Quaker movement）',
    'Quaker corporate life': '贵格会共同体生活（Quaker corporate life）',
    'Quaker business method': '贵格会议事方法（Quaker business method）',
    'The Source—the Quaker meeting for worship': '《源头——贵格会静默敬拜》（The Source—the Quaker meeting for worship）',
    'the Quaker business method': '贵格会议事方法（the Quaker business method）',
    'meeting for business': '议事会（meeting for business）',
    'gathered meeting': '深度聚集的聚会（gathered meeting）',
    'Gathered meeting': '深度聚集的聚会（Gathered meeting）',
    'corporate listening': '群体聆听（corporate listening）',
    'corporate life': '共同体生活（corporate life）',
    'corporate guidance': '群体引导（corporate guidance）',
    'collective silent worship': '集体静默敬拜（collective silent worship）',
    'search for truth': '追寻真理（search for truth）',
    'tests of leadings': '引领检验（tests of leadings）',
    'clearness committees': '澄心会（clearness committees）',
    'Meetings for Clearness': '澄心会（Meetings for Clearness）',
    'unprogrammed tradition': '非程序化传统（unprogrammed tradition）',
    'unprogrammed Meeting': '非程序化聚会（unprogrammed Meeting）',
    'vocal ministry': '受感分享（vocal ministry）',
    'Holy Spirit': '圣灵（Holy Spirit）',
    'God reveals himself directly': '上帝直接启示自身（God reveals himself directly）',
    'local / monthly': '地方／月会层级（local / monthly）',
    'conflict transformation': '冲突转化（conflict transformation）',
    'meditation technique': '冥想技巧（meditation technique）',
    'right action': '合宜行动（right action）',
    'rightness': '合宜性（rightness）',
    'faithfulness': '忠实（faithfulness）',
    'touchstones': '基石（touchstones）',
    'inner light': '内在之光（inner light）',
    'inward source': '内在源泉（inward source）',
    'sense of the meeting': '聚会的共同辨识（sense of the meeting）',
    'sense of Meeting': '聚会的共同辨识（sense of Meeting）',
    'standing aside': '保留但不阻挡（standing aside）',
    'prayerful attentiveness': '祷告式专注（prayerful attentiveness）',
    'clearance': '资格审查（clearance）',
    'Christological': '基督论式（Christological）',
    'mystical': '神秘主义式（mystical）',
    'humanist': '人文主义式（humanist）',
    'universalist': '普世主义式（universalist）',

    # Authors and historical figures.
    'Howard H. Brinton': '霍华德·布林顿（Howard H. Brinton）',
    'Howard Brinton': '霍华德·布林顿（Howard Brinton）',
    'Thomas R. Kelly': '托马斯·凯利（Thomas R. Kelly）',
    'Thomas Kelly': '托马斯·凯利（Thomas Kelly）',
    'Parker J. Palmer': '帕克·J·帕尔默（Parker J. Palmer）',
    'Parker Palmer': '帕克·帕尔默（Parker Palmer）',
    'Patricia Loring': '帕特里夏·洛林（Patricia Loring）',
    'Michael Marsh': '迈克尔·马什（Michael Marsh）',
    'Jim Pym': '吉姆·皮姆（Jim Pym）',
    'John Yungblut': '约翰·扬布拉特（John Yungblut）',
    'George Fox': '乔治·福克斯（George Fox）',
    'Margaret Fell': '玛格丽特·费尔（Margaret Fell）',
    'William Penn': '威廉·佩恩（William Penn）',
    'John Woolman': '约翰·伍尔曼（John Woolman）',
    'Rufus Jones': '鲁弗斯·琼斯（Rufus Jones）',
    'Palmer': '帕尔默（Palmer）',
    'Loring': '洛林（Loring）',
    'Pym': '皮姆（Pym）',
    'Marsh': '马什（Marsh）',
    'Kelly': '凯利（Kelly）',
    'Woolman': '伍尔曼（Woolman）',
    'Fox': '福克斯（Fox）',
    'Penn': '佩恩（Penn）',
    'Fell': '费尔（Fell）',
    'Jung': '荣格（Jung）',
    'Barclay': '巴克莱（Barclay）',
    'Robert Spence': '罗伯特·斯彭斯（Robert Spence）',
    'Francis Place': '弗朗西斯·普莱斯（Francis Place）',
    'Robert Smith III': '罗伯特·史密斯三世（Robert Smith III）',
    'Cumbria': '坎布里亚（Cumbria）',
    'Wikimedia Commons': '维基共享资源（Wikimedia Commons）',
    'Commons': '维基共享资源（Commons）',
    'Supposed portrait': '“推定肖像”（Supposed portrait）',

    # Books / source titles.
    'Friends for 300 Years': '《三百年的贵格会友》（Friends for 300 Years）',
    'Listening to the Light': '《聆听内在之光》（Listening to the Light）',
    'Spiritual Discernment': '《灵性明辨》（Spiritual Discernment）',
    'The Light Within': '《内在之光》（The Light Within）',
    'Philosophy of the Inner Light': '《内在之光的哲学》（Philosophy of the Inner Light）',
    'Seeking Light in the Darkness of the Unconscious': '《在无意识的黑暗中寻光》（Seeking Light in the Darkness of the Unconscious）',
    'The Meeting Community': '《聚会共同体》（The Meeting Community）',
    'The Meeting for Worship': '《静默敬拜》（The Meeting for Worship）',
    'Reaching Decisions': '《达成决定》（Reaching Decisions）',
    'A New Way of Working': '《一种新的工作方式》（A New Way of Working）',
    'Friends Conference on Religion and Psychology': '贵格会宗教与心理学会议（Friends Conference on Religion and Psychology）',

    # Institutions / historical group labels.
    'Yearly Meeting': '年会（Yearly Meeting）',
    'Local / Area Meeting': '地方／区域聚会（Local / Area Meeting）',
    'Local worship': '地方敬拜（Local worship）',
    'Seekers': '寻道者（Seekers）',
    'Quietism': '静默主义（Quietism）',
    'Pendle Hill': '彭德尔山学习中心（Pendle Hill）',
    'Swarthmoor Hall': '斯沃斯莫庄园（Swarthmoor Hall）',
    'Arch Street Friends Meeting House': '拱街贵格会聚会所（Arch Street Friends Meeting House）',
    'Free Quaker Meeting House': '自由贵格会聚会所（Free Quaker Meeting House）',
    'Pennsylvania': '宾夕法尼亚（Pennsylvania）',

    # Diagram / interface terms kept bilingual for learning.
    'Truth emerges in relation': '真理在关系中显现（Truth emerges in relation）',
    'Speak / Remain Silent': '发言或保持静默（Speak / Remain Silent）',
    'Arrive': '到场（Arrive）',
    'Settle': '安顿（Settle）',
    'Wait': '等候（Wait）',
    'Listen': '聆听（Listen）',
    'Return': '返回（Return）',
    'Center': '共同中心（Center）',
    'Inward': '向内（Inward）',
    'Between': '关系之间（Between）',
    'Corporate': '群体层面（Corporate）',
    'Outward': '向外（Outward）',
    'Person': '人（Person）',
    'Voting': '表决（Voting）',
    'Consensus': '共识（Consensus）',
    'Chairperson': '主席（Chairperson）',
    'Clerk': '书记（Clerk）',
    'Minute': '决议纪要（Minute）',
    'Seasoning': '酝酿（Seasoning）',
    'Query': '省察问题（Query）',
    'Queries': '省察问题（Queries）',
    'Testimony': '生活见证（Testimony）',
    'Elder': '敬拜照看者（Elder）',
    'Hospitality': '接待与欢迎（Hospitality）',
    'Pastoral care': '牧养与关怀（Pastoral care）',
    'Conflict': '冲突处理（Conflict）',
    'Children & learning': '儿童与学习（Children & learning）',
    'Witness': '公共见证（Witness）',
    'Unity': '合一（Unity）',
    'Testing': '检验（Testing）',
    'Discernment': '明辨（Discernment）',
    'Leading?': '内在引领？（Leading?）',
    'Settling': '安顿（Settling）',
    'settling': '安顿',
    'listening': '聆听',
    'action': '行动',
    'minute': '决议纪要',
    'business': '议事',
    'Business': '议事',
    'silence': '静默',
    'Silence': '静默',
    'community': '共同体',
    'Community': '共同体',
    'decision': '决策',
    'witness': '见证',
    'inward': '向内',
    'outward': '向外',
    'peace': '和平',
    'simplicity': '简朴',
    'integrity': '诚信',
    'consensus': '共识',
    'discipline': '纪律',
    'truth': '真理',
    'together': '共同',
    'intellectual agreement': '观念一致',
    'Gatheredness': '深度聚集状态',
    'gatheredness': '深度聚集状态',
    'Presence': '临在',
    'Divine': '神圣',
    'Learning': '共学',
    'elders': '敬拜照看者（elders）',
    'proposal': '提案',
    'chairman': '主席',
    'clerk': '书记',
    'tests': '检验',
    'restraint': '克制',
    'practice': '实践',
    'programmed': '程序化',
    'unprogrammed': '非程序化',
    'pastoral': '牧师制',
    'coach': '教练',
    'vocal': '口头',
    'micro-meeting': '微型聚会',
    'Micro-Meeting': '微型聚会（Micro-Meeting）',
    'min': '分钟',
    'third thing': '第三物',
    'person–person–third thing': '人—人—第三物',
    'testimonies': '生活见证',
    'pamphlet': '小册子',
    'Pamphlet': '小册子',
    'liberal Quaker': '自由派贵格会',
    'evangelical Friends': '福音派会友',
    'love': '爱',
    'beauty': '美',
    'group': '群体',
    'Yearly Meetings': '各年会',
    'Psychology': '心理学',
    'agreement': '意见一致（agreement）',
    'compromise': '妥协（compromise）',
    'committee': '小组',
    'clearness committee': '澄心会（clearness committee）',
    'membership': '会籍（membership）',
    'history': '历史',
    'mysticism': '神秘主义',
    'plainness': '朴素生活（plainness）',
    'divine guidance': '神圣引导（divine guidance）',
    'Zen': '禅（Zen）',
    'advice': '建议（advice）',
    'KPI': '关键绩效指标（KPI）',
    'AI': '人工智能（AI）',
    'App': '应用（App）',
    'Immediate experience ↔ Tradition': '直接经验 ↔ 传统（Immediate experience ↔ Tradition）',
    'Individual leading ↔ Corporate discernment': '个人引领 ↔ 群体明辨（Individual leading ↔ Corporate discernment）',
    'Inward life ↔ Outward witness': '内在生命 ↔ 外在见证（Inward life ↔ Outward witness）',

    # Common English concepts: translate to Chinese so prose remains light.
    'waiting': '等候',
    'Waiting': '等候',
    'worship': '敬拜',
    'Worship': '敬拜',
    'ministry': '受感分享',
    'Ministry': '受感分享',
    'leading': '内在引领',
    'Leading': '内在引领',
    'concern': '内在关切',
    'Concern': '内在关切',
    'testimony': '生活见证',
    'unity': '合一',
    'clearness': '澄明',
    'discernment': '明辨',
    'Truth': '真理',
    'Light': '光',
    'Spirit': '灵',
    'God': '上帝',
    'Christ': '基督',
    'Scripture': '《圣经》',
    'Life': '生命',
    'Love': '爱',
    'method': '方法',
    'experience': '经验',
    'insight': '洞见',
    'mystery': '奥秘',
    'facilitation': '引导',
    'facilitator': '带领者',
    'sermon': '讲道',
    'discussion': '讨论',
    'Meeting': '聚会',
    'meeting': '聚会',
    'Friends': '会友',
    'Quaker': '贵格会',

    # Editorial / exhibition labels.
    'Primary sources': '主要来源（Primary sources）',
    'QUERY': '省察问题（QUERY）',
    'QUAKER MEETING · 研究 × 实践': '贵格会聚会 · 研究 × 实践（QUAKER MEETING）',
    'THE QUESTION': '核心问题（THE QUESTION）',
    'VISUAL ESSAY · 01': '视觉短章 01（VISUAL ESSAY）',
    'FIELD IMAGE · MEETING HOUSE': '现场图像 · 聚会所（FIELD IMAGE · MEETING HOUSE）',
    'WHY IT MATTERS': '为什么重要（WHY IT MATTERS）',
    'ONE MAP': '一张图理解（ONE MAP）',
    'PEOPLE · PLACE · ARCHIVE': '人物 · 地点 · 史料（PEOPLE · PLACE · ARCHIVE）',
    'MEETING FAMILY': '聚会形态（MEETING FAMILY）',
    'TWO PATHS': '两条进入路径（TWO PATHS）',
    'SOURCE-BASED · NOT QUOTE-MINING': '基于来源 · 不摘句拼贴（SOURCE-BASED · NOT QUOTE-MINING）',
    'VISUAL SOURCES': '视觉史料（VISUAL SOURCES）',
    'PRIMARY LIBRARY': '核心文献（PRIMARY LIBRARY）',
    'RESEARCH DISCIPLINE': '研究纪律（RESEARCH DISCIPLINE）',
    'SOURCE MAP': '来源地图（SOURCE MAP）',
    'CONTESTED CONCEPTS': '争议概念（CONTESTED CONCEPTS）',
    'RESEARCH ROADMAP': '研究路线图（RESEARCH ROADMAP）',
    'READING PATHS': '阅读路径（READING PATHS）',
    'PROVENANCE': '来源脉络（PROVENANCE）',
    'CURATORIAL NOTE': '策展说明（CURATORIAL NOTE）',
    'PROVENANCE · LICENSE · UNCERTAINTY': '来源 · 授权 · 不确定性（PROVENANCE · LICENSE · UNCERTAINTY）',
    'FROM READING TO DOING': '从阅读到实践（FROM READING TO DOING）',
    'FACILITATOR CARD': '带领者卡片（FACILITATOR CARD）',
    'FAILURE MODES': '常见失误（FAILURE MODES）',
    'DON’T COLLAPSE THE DIFFERENCES': '不要抹平差异（DON’T COLLAPSE THE DIFFERENCES）',
    'HOW TO CHOOSE': '如何选择（HOW TO CHOOSE）',
    'FALSE FRIENDS': '最易混淆之处（FALSE FRIENDS）',
    'WORDS MATTER': '词语很重要（WORDS MATTER）',
    'HOW TO READ': '如何阅读（HOW TO READ）',
    'FROM SOLO TO CORPORATE': '从个人到群体（FROM SOLO TO CORPORATE）',
    '12 MINUTES · BEGINNER PRACTICE': '12 分钟 · 初学者实践（BEGINNER PRACTICE）',
    'AFTER': '练习之后（AFTER）',
    'NEXT': '下一步（NEXT）',
    'HISTORY': '历史（HISTORY）',
    'RESEARCH': '研究（RESEARCH）',
    'PRACTICE': '实践（PRACTICE）',
    'COMPARE': '比较（COMPARE）',
    'GLOSSARY': '术语（GLOSSARY）',
    'TOOLKIT': '工具箱（TOOLKIT）',
    'BRINTON’S LENS': '布林顿的视角（BRINTON’S LENS）',
    'THREE THREADS': '三条主线（THREE THREADS）',
    'FOUR LIVES · FOUR WINDOWS': '四个人 · 四扇窗（FOUR LIVES · FOUR WINDOWS）',
    'FIELD IMAGE · WORSHIP SPACE': '现场图像 · 敬拜空间（FIELD IMAGE · WORSHIP SPACE）',
    'HISTORIC INTERIOR · PHILADELPHIA': '历史室内 · 费城（HISTORIC INTERIOR · PHILADELPHIA）',
    'SOURCE TYPE · PORTRAIT': '史料类型 · 肖像（SOURCE TYPE · PORTRAIT）',
    'SOURCE TYPE · LATER IMPRESSION': '史料类型 · 后世艺术印象（SOURCE TYPE · LATER IMPRESSION）',
    'THIRD THING · IMAGE': '第三物 · 图像（THIRD THING · IMAGE）',
    'PLACE · COMMUNITY': '地点 · 共同体（PLACE · COMMUNITY）',
    'PLACE · ORIGIN': '地点 · 源流（PLACE · ORIGIN）',
    'PLACE · CUMBRIA': '地点 · 坎布里亚（PLACE · CUMBRIA）',
    'PLACE · PHILADELPHIA': '地点 · 费城（PLACE · PHILADELPHIA）',

    # Historical tags.
    'authority crisis': '权威危机（authority crisis）',
    'experience → movement': '经验 → 运动（experience → movement）',
    'charisma → discipline': '感召 → 纪律（charisma → discipline）',
    'liberty · governance · colony': '自由 · 治理 · 殖民（liberty · governance · colony）',
    'consolidation': '整合与巩固（consolidation）',
    'leading → witness': '引领 → 见证（leading → witness）',
    'plural traditions': '多元传统（plural traditions）',
    'retrieval & experiment': '传统重访与实验（retrieval & experiment）',
    'method, not mere form': '方法，而非只有形式（method, not mere form）',
    'tradition → translation': '传统 → 转译（tradition → translation）',
    'context matters': '语境很重要（context matters）',
    'Today': '当代（Today）',
    '1640s → TODAY': '1640年代 → 当代（TODAY）',
    'Mystical': '神秘主义（Mystical）',
    'Evangelical': '福音派（Evangelical）',
    'Rational': '理性主义（Rational）',
    'Social Gospel': '社会福音（Social Gospel）',
}

SECTION_LABELS = {
    'DEFINITION':'定义', 'METHOD':'方法', 'NOT JUST MEDITATION':'不只是冥想',
    'FIVE LAYERS':'五个层次', 'INNER LIGHT':'内在之光', 'MISUNDERSTANDINGS':'常见误解',
    'OBSERVE':'观察', 'SILENCE':'静默', 'THREE DEPTHS':'三重深度',
    'THEOLOGICAL DIRECTION':'神学方向', 'HOW TO ENTER':'如何进入', 'DISTRACTION':'杂念',
    'RETURN':'返回', 'EVERYDAY LIGHT':'日常之光', 'MINISTRY':'受感分享', 'TESTING':'检验',
    'INTERACTIVE':'互动练习', 'AFTER WORDS':'话语之后', 'AUTHORITY':'权威', 'PITFALLS':'常见陷阱',
    'GATHEREDNESS':'聚集状态', 'SIGNALS':'观察信号', 'WHY GROUP':'为什么是群体',
    'GROUP MYSTICISM':'群体神秘主义', 'THIRD THING':'第三物', 'EPISTEMOLOGY':'认识论',
    'DISCIPLINES':'实践纪律', '90-MINUTE DESIGN':'90 分钟设计', 'FACILITATOR':'带领者',
    'EVIDENCE OF LEARNING':'学习发生的迹象', 'ORIGIN':'源流', 'THREE MODELS':'三种模式',
    'MEETING FOR LEARNING':'共学会', 'SOLO':'个人练习', 'SMALL GROUP':'小组练习',
    'CLERK':'书记角色', 'CASE LAB':'案例实验', 'WAITING':'等候', 'MINUTE':'决议纪要',
    'PRACTICAL TEMPLATE':'实践模板', 'CLEARNESS':'澄心', 'STRUCTURE':'结构',
    'DISCERNMENT':'明辨', 'QUESTION LAB':'提问实验', 'REWRITE':'改写练习',
    'TEMPLATE':'模板', 'BOUNDARIES':'边界', 'COMMUNITY':'共同体', 'ORGANIZATION':'组织',
    'CARE':'照顾', 'MATURITY':'成熟度', 'QUERIES':'省察问题', 'PRACTICE':'实践',
}


def _replace_terms(text):
    """Replace visible English with Chinese-first wording without touching HTML attributes."""
    if not re.search(r'[A-Za-z]', text):
        return text
    replacements = dict(TEXT_REPLACEMENTS)
    # Section eyebrow pattern: 05 · OBSERVE -> 05 · 观察（OBSERVE）
    m = re.fullmatch(r"(\d{2}\s*·\s*)([A-Z0-9][A-Z0-9 &/’'\-]+)", text.strip())
    if m and m.group(2) in SECTION_LABELS:
        return text.replace(m.group(0), f'{m.group(1)}{SECTION_LABELS[m.group(2)]}（{m.group(2)}）')

    placeholders = {}
    out = text
    # Preserve English that is already intentionally placed after a Chinese term.
    keep = {}
    def protect_parenthetical(match):
        token = f'@@KEEP{len(keep)}@@'
        keep[token] = match.group(0)
        return token
    out = re.sub(r'（[^）]*[A-Za-z][^）]*）', protect_parenthetical, out)
    for idx, (en, zh) in enumerate(sorted(replacements.items(), key=lambda kv: len(kv[0]), reverse=True)):
        token = f'@@ZH{idx}@@'
        # Word-like terms should not match inside a longer Latin token.
        if re.fullmatch(r"[A-Za-z][A-Za-z0-9 .&/’'?\-]*", en):
            pat = rf'(?<![A-Za-z]){re.escape(en)}(?![A-Za-z])'
        else:
            pat = re.escape(en)
        new, n = re.subn(pat, token, out)
        if n:
            out = new
            placeholders[token] = zh
    for token, zh in placeholders.items():
        out = out.replace(token, zh)
    for token, original in keep.items():
        out = out.replace(token, original)
    # Chinese prose should not inherit the spaces that surrounded an English term
    # in the source sentence. Keep Latin spacing inside parentheses untouched.
    out = re.sub(r'(?<=[\u4e00-\u9fff，。！？；：“”‘’）》）])\s+(?=[\u4e00-\u9fff，。！？；：“”‘’《（])', '', out)
    out = re.sub(r'(?<=[\u4e00-\u9fff）》）])\s*/\s*(?=[\u4e00-\u9fff《（])', '／', out)
    return out


def localize_visible_text(doc):
    """Chinese-first editorial pass for text nodes; markup/URLs/classes stay untouched."""
    return re.sub(r'(?<=>)([^<>]+)(?=<)', lambda m: _replace_terms(m.group(1)), doc)


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
    return f'<aside class="sources"><div class="source-head">{icon("book")}<div><strong>主要来源</strong><small>Primary sources</small></div></div><ul>{lis}</ul><a href="research.html" class="text-link">进入研究室 →</a></aside>'


def callout(title, body, tone='light'):
    return f'<div class="callout {tone}"><strong>{title}</strong><div>{body}</div></div>'


def query_cards(qs):
    return '<div class="query-grid">' + ''.join(f'<article class="query-card"><span>QUERY {i+1:02d}</span><p>{q}</p></article>' for i,q in enumerate(qs)) + '</div>'


HEADING_TERMS = [
    'Meeting for Worship', 'Meeting for Learning', 'Sense of the Meeting',
    'Clearness Committee', 'Vocal Ministry', 'Gathered Meeting',
    'Inner Light', 'Third Thing', 'Quaker Meeting', 'Group Mysticism',
    'Faith and Practice', 'Advices & Queries', 'Circle of Trust',
    'Meeting for Business', 'Meeting Community', 'Business Meeting',
    'Quakerism', 'Meeting'
]

HEADING_LAYOUTS = {
    '在静默中，共同聆听。': ['在静默中，', '共同聆听。'],
    'Meeting 到底是什么？': ['Meeting 到底', '是什么？'],
    'Meeting：不是“会议”的同义词': ['Meeting：', '不是“会议”的同义词'],
    '它与“大家一起静坐”有什么不同？': ['它与“大家一起静坐”', '有什么不同？'],
    '不投票，怎么做决定？': ['不投票，', '怎么做决定？'],
    '澄心会：不替你决定': ['澄心会：', '不替你决定'],
    '什么时候该说话？': ['什么时候', '该说话？'],
    '静默，不是什么都不做': ['静默，', '不是什么都不做'],
    'Meeting 的历史与演变': ['Meeting 的', '历史与演变'],
    'Quaker Meeting 研究室': ['Quaker Meeting', '研究室'],
    'Quaker Meeting 术语表': ['Quaker Meeting', '术语表'],
    'Meeting 如何成为共同体': ['Meeting 如何成为', '共同体'],
    'Meeting 与其他方法，有何异同？': ['Meeting 与其他方法，', '有何异同？'],
    '每一张历史图片，都应该知道自己从哪里来':
        ['每一张历史图片，', '都应该知道自己从哪里来'],
    '如果一群人暂时不争着表达立场，会不会有一些东西，反而更容易被听见？':
        ['如果一群人暂时', '不争着表达立场，', '会不会有一些东西，', '反而更容易被听见？'],
    '不只读概念，也看见传统留下的痕迹':
        ['不只读概念，', '也看见传统', '留下的痕迹'],
    # Worship / practice — manually edited as Chinese editorial headlines.
    '进入Meeting 时，具体可以怎么做？': ['进入Meeting 时，', '具体可以怎么做？'],
    '一次尽量少指导的Meeting体验': ['一次尽量少指导的Meeting体验'],
    '不要把 12 分钟练习误当成Meeting的缩小版': ['不要把 12 分钟练习误当成Meeting的缩小版'],
    '坐下来，让自己到达这里。': ['坐下来，', '让自己到达这里。'],
    '不要把 12 分钟练习误当成聚会的缩小版':
        ['不要把 12 分钟练习', '误当成聚会的缩小版'],

    # Long-form article headings: break only at complete thought units.
    '为什么一个宗教群体发展出一种独特的决策法？':
        ['为什么一个宗教群体', '发展出一种独特的', '决策法？'],
    'Voting、Consensus、Sense of the Meeting':
        ['Voting、Consensus、', 'Sense of the Meeting'],
    'Discernment：真正要分辨的，是“这个声音从哪里来”':
        ['Discernment：真正要分辨的，', '是“这个声音从哪里来”'],
    'Vocal Ministry：不是“自由发言”':
        ['Vocal Ministry：', '不是“自由发言”'],
    '一句话从出现到说出，中间可以有一段路':
        ['一句话从出现到说出，', '中间可以有一段路'],
    '别人说完之后，为什么不立即接话？':
        ['别人说完之后，', '为什么不立即接话？'],
    '一句 ministry 的“权威”从哪里来？':
        ['一句 ministry 的“权威”', '从哪里来？'],
    'Meeting 既是一场聚集，也是一个共同体':
        ['Meeting 既是一场聚集，', '也是一个共同体'],
    '一个 Meeting Community 需要照顾什么？':
        ['一个 Meeting Community', '需要照顾什么？'],
    'Community 也是对“内在声音”的外部检验':
        ['Community 也是对“内在声音”的', '外部检验'],
    '共同体的成熟，不看“活动很多”，而看能否承受真实':
        ['共同体的成熟，不看“活动很多”，', '而看能否承受真实'],
    'Gathered Meeting：当圆圈变成“一个整体”':
        ['Gathered Meeting：', '当圆圈变成', '“一个整体”'],
    'Group mysticism：既不是“集体情绪”，也不是“大家想法一样”':
        ['Group mysticism：', '既不是“集体情绪”，', '也不是“大家想法一样”'],
    '练习：感受“群体”，而不是只听自己':
        ['练习：感受“群体”，', '而不是只听自己'],
    '历史不是一条直线：三百多年来，Meeting 一直在被重新解释':
        ['历史不是一条直线：', '三百多年来，', 'Meeting 一直在被重新解释'],
    'Brinton 的“四时期”不是唯一答案，却提供了一张很有用的分析地图':
        ['Brinton 的“四时期”不是唯一答案，', '却提供了一张很有用的分析地图'],
    'Meeting 不只是安静下来，而是在练习“如何共同认识”':
        ['Meeting 不只是', '安静下来，', '而是在练习', '“如何共同认识”'],
    '如果学习也被当作 Meeting，会发生什么？':
        ['如果学习也被当作', 'Meeting，', '会发生什么？'],
    'Meeting for Learning 背后，其实是一种知识观':
        ['Meeting for Learning', '背后，', '其实是一种知识观'],
    '一场 90 分钟共读，如何从“读书会”变成 Meeting for Learning？':
        ['一场 90 分钟共读，', '如何从“读书会”', '变成 Meeting for Learning？'],
    '怎样判断一次共学是否真的“发生了学习”？':
        ['怎样判断一次共学', '是否真的', '“发生了学习”？'],
    '为什么 Brinton 说 Quakerism 首先是一种 method？':
        ['为什么 Brinton 说', 'Quakerism，', '首先是一种 method？'],
    'Inner Light 不是“我的感觉就是对的”':
        ['Inner Light', '不是“我的感觉就是对的”'],
    '“等候”为什么不是一种注意力技巧？':
        ['“等候”为什么不是', '一种注意力技巧？'],
    '从 inward life 到 workaday life':
        ['从 inward life', '到 workaday life'],
    '试着这样观察下一次静默':
        ['试着这样观察', '下一次静默'],
    'Clerk：不是主席':
        ['Clerk：', '不是主席'],
    '互动案例：12个人要不要搬迁社区空间？':
        ['互动案例：', '12个人要不要', '搬迁社区空间？'],
    '什么时候“不决定”反而更成熟？':
        ['什么时候“不决定”', '反而更成熟？'],
    'Minute：不是会后整理，而是现场检验':
        ['Minute：', '不是会后整理，', '而是现场检验'],
    '一场 90 分钟 Meeting for Business 的简化模板':
        ['一场 90 分钟', 'Meeting for Business', '的简化模板'],
    '一场澄心会的核心结构':
        ['一场澄心会', '的核心结构'],
    '互动：这是开放问题，还是伪装建议？':
        ['互动：这是开放问题，', '还是伪装建议？'],
    '什么时候不适合用澄心会？':
        ['什么时候', '不适合用澄心会？'],
    '第三物为什么如此重要？':
        ['第三物为什么', '如此重要？'],
    'Meeting for Learning 的五条纪律':
        ['Meeting for Learning', '的五条纪律'],
    '从圆圈到组织，但不让组织吞掉圆圈':
        ['从圆圈到组织，', '但不让组织', '吞掉圆圈'],
    'Community 也是对“内在声音”的外部检验':
        ['Community 也是对', '“内在声音”的', '外部检验'],
    '先从四个人进入这段历史':
        ['先从四个人', '进入这段历史'],
    '什么场景更适合用什么？':
        ['什么场景', '更适合用什么？'],
    '很多误解，来自翻译过快':
        ['很多误解，', '来自翻译过快'],
    '不同文献，各自在回答什么问题？':
        ['不同文献，', '各自在回答', '什么问题？'],
    '四个不能过早“讲简单”的概念':
        ['四个不能过早', '“讲简单”的概念'],
    '把 Meeting 变成可以使用的实践':
        ['把 Meeting', '变成可以使用的实践'],
    '带领者只需要记住四句话':
        ['带领者只需要', '记住四句话'],
    '六条研究纪律：避免把 Quakerism 做成“灵性语录库”':
        ['六条研究纪律：', '避免把 Quakerism', '做成“灵性语录库”'],
    '六条研究纪律：避免把贵格会传统（Quakerism）做成“灵性语录库”':
        ['六条研究纪律：', '避免把贵格会传统（Quakerism）', '做成“灵性语录库”'],
    '六种最常见的“看起来像 Meeting，实际上不是”的失败方式':
        ['六种最常见的', '“看起来像 Meeting，', '实际上不是”的失败方式'],
    '六种最常见的“看起来像聚会，实际上不是”的失败方式':
        ['六种最常见的', '“看起来像聚会，', '实际上不是”的失败方式'],
    '最容易“看起来很像”，其实差异最大的三组':
        ['最容易“看起来很像”，', '其实差异最大的三组'],
    '术语不是“对照表”，而是一张传统内部的关系网':
        ['术语不是“对照表”，', '而是一张传统内部的关系网'],
}


def _split_heading_piece(piece):
    """Split a heading into readable semantic fragments, never single orphan characters."""
    piece = piece.strip()
    if not piece:
        return []

    # Keep important English terms together, so "Meeting for / Learning" never happens.
    term_pat = '(' + '|'.join(re.escape(x) for x in sorted(HEADING_TERMS, key=len, reverse=True)) + ')'
    atoms = [x for x in re.split(term_pat, piece) if x and x.strip()]
    out = []

    # These cues usually begin a natural Chinese thought-unit.
    cues = ['为什么', '如何', '怎样', '怎么', '是否', '能否', '背后', '其实', '而是',
            '不是', '不只是', '不等于', '意味着', '究竟', '什么时候', '从', '到']

    for atom in atoms:
        atom = atom.strip()
        if atom in HEADING_TERMS:
            out.append((atom, True))
            continue

        # Separate Latin words/names from Chinese text before any length-based split.
        mixed_atoms = [x.strip() for x in re.split(r'([A-Za-z][A-Za-z0-9.&’\'-]*(?:\s+[A-Za-z][A-Za-z0-9.&’\'-]*)*)', atom) if x and x.strip()]
        for mixed in mixed_atoms:
            if re.fullmatch(r'[A-Za-z][A-Za-z0-9.&’\'-]*(?:\s+[A-Za-z][A-Za-z0-9.&’\'-]*)*', mixed):
                out.append((mixed, True))
                continue

            chunks = [mixed]
            for cue in cues:
                next_chunks = []
                for chunk in chunks:
                    pos = chunk.find(cue)
                    if pos >= 3 and len(chunk) - pos >= 3:
                        left, right = chunk[:pos].strip(), chunk[pos:].strip()
                        if left and left[-1] in '“‘《（(':
                            right = left[-1] + right
                            left = left[:-1].rstrip()
                        next_chunks.extend([left, right])
                    else:
                        next_chunks.append(chunk)
                chunks = [x for x in next_chunks if x]

            # Fallback for very long Chinese fragments: prefer grammatical boundaries
            # near the visual middle instead of breaking a final character off.
            for chunk in chunks:
                if len(chunk) <= 10:
                    out.append((chunk, False))
                    continue
                remaining = chunk
                while len(remaining) > 10:
                    target = min(10, len(remaining) - 4)
                    candidates = []
                    for i in range(max(5, target - 3), min(len(remaining) - 3, target + 4) + 1):
                        if remaining[i-1:i] in '的了是与和中后前上下来' or remaining[i:i+1] in '把让向为在':
                            candidates.append(i)
                    cut = min(candidates, key=lambda i: abs(i-target)) if candidates else target
                    out.append((remaining[:cut].strip(), False))
                    remaining = remaining[cut:].strip()
                if remaining:
                    out.append((remaining, False))
    return out


def _protect_terms(text):
    # English already placed in full-width parentheses is secondary annotation:
    # keep it intact, smaller and lighter, and never let term locking split it.
    held = {}
    locked = {}

    def hold_parenthetical(match):
        token = f'@@PAREN{len(held)}@@'
        held[token] = match.group(0)
        return token

    def hold_short_quote(match):
        token = f'@@QUOTE{len(locked)}@@'
        locked[token] = match.group(0)
        return token

    protected = re.sub(r'（[^）]*[A-Za-z][^）]*）', hold_parenthetical, text)
    # Short quoted phrases are semantic units in Chinese headlines. Keeping them
    # together prevents awkward mobile breaks such as “不会 / 静默”.
    protected = re.sub(r'“[^”\n]{1,10}”|‘[^’\n]{1,10}’|《[^》\n]{1,10}》', hold_short_quote, protected)

    pattern = '(' + '|'.join(re.escape(x) for x in sorted(HEADING_TERMS, key=len, reverse=True)) + ')'
    parts = [x for x in re.split(pattern, protected) if x]
    rendered = ''.join(
        f'<span class="term-lock">{html.escape(part)}</span>'
        if part in HEADING_TERMS else html.escape(part)
        for part in parts
    )
    for token, original in held.items():
        rendered = rendered.replace(html.escape(token), f'<span class="en-paren">{html.escape(original)}</span>')
    for token, original in locked.items():
        rendered = rendered.replace(html.escape(token), f'<span class="term-lock">{html.escape(original)}</span>')
    return rendered


def _heading_segments(text, soft_limit=18):
    """Keep headings whole; only expose semantic wrap points for genuinely long titles."""
    clean = text.strip()
    compact = re.sub(r'\s+', '', clean)

    # Prefer punctuation as a wrap opportunity. Nothing is hard-broken: <wbr>
    # only gives the browser a better place to wrap when the container needs it.
    pieces = re.findall(r'.+?[，,；;：:](?=.)|.+$', clean)
    pieces = [p.strip() for p in pieces if p.strip()]

    # Punctuation already gives us the best semantic boundaries. Keep each
    # punctuation-delimited phrase intact on desktop and let the browser wrap only
    # between phrases. This avoids ugly breaks such as “不会 / 静默”.
    if len(pieces) > 1:
        return [(piece, False) for piece in pieces]

    # No useful punctuation: allow ordinary wrapping only for genuinely long titles.
    return [(clean, len(compact) > soft_limit)]


def smart_heading(text):
    """Chinese-first headings: intact by default, semantic wrap points only when long."""
    localized = _replace_terms(text)
    annotations = []

    def pull_annotation(match):
        note = match.group(0)
        if note not in annotations:
            annotations.append(note)
        return ''

    clean = re.sub(r'（[^）]*[A-Za-z][^）]*）', pull_annotation, localized)
    clean = re.sub(r'\s+([，。！？；：])', r'\1', clean)
    clean = re.sub(r'([（《“])\s+', r'\1', clean)
    clean = re.sub(r'\s{2,}', ' ', clean).strip()

    rendered = []
    segments = _heading_segments(clean)
    for i, (segment, fluid) in enumerate(segments):
        seg_len = len(re.sub(r'\s+', '', segment))
        classes = ['title-segment']
        if fluid:
            classes.append('fluid')
        if seg_len > 7:
            classes.append('mobile-fluid')
        rendered.append(f'<span class="{" ".join(classes)}">{_protect_terms(segment)}</span>')
        if i < len(segments) - 1:
            rendered.append('<wbr>')

    main = f'<span class="title-line">{"".join(rendered)}</span>'
    notes = ''
    if annotations:
        note_text = ' · '.join(annotations)
        notes = f'<span class="heading-annotations">{html.escape(note_text)}</span>'
    return main + notes


def enhance_plain_headings(doc):
    """Add semantic break opportunities to plain-text h1/h2/h3 left in hand-authored blocks."""
    pattern = re.compile(r'<(h[1-3])([^>]*)>([^<]+)</\1>')
    def repl(match):
        tag, attrs, text_only = match.groups()
        return f'<{tag}{attrs}>{smart_heading(html.unescape(text_only))}</{tag}>'
    return pattern.sub(repl, doc)


def research_note(title, body, label='研究札记'):
    return f'''<aside class="research-card"><span>{label}</span><h3>{smart_heading(title)}</h3><div>{body}</div></aside>'''


def section_glyph(title):
    """A lightweight visual cue so long-form pages never become a wall of text."""
    lower = title.lower()
    if any(k in lower for k in ['为什么', '如何', '怎样', '什么', 'query', '问题', '误解']):
        key = 'question'
    elif any(k in lower for k in ['学习', '第三物', '阅读', '术语', '原典', '知识']):
        key = 'book'
    elif any(k in lower for k in ['静默', 'waiting', 'worship', '等候']):
        key = 'silence'
    elif any(k in lower for k in ['共同', '群体', 'community', 'meeting', 'ministry', '合一']):
        key = 'group'
    elif any(k in lower for k in ['历史', '演变', '路径', '进入', '下一步', '行动']):
        key = 'path'
    else:
        key = 'light'
    return f'<div class="section-glyph" aria-hidden="true">{icon(key)}</div>'


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
    clean_eyebrow = re.sub(r'^\s*\d{1,2}\s*·\s*', '', eyebrow or '').strip()
    eyebrow_zh = SECTION_LABELS.get(clean_eyebrow)
    eyebrow_text = f'{eyebrow_zh}（{clean_eyebrow}）' if eyebrow_zh else clean_eyebrow
    ey = f'<div class="section-eyebrow"><span class="section-auto-no" aria-hidden="true"></span><span>{eyebrow_text}</span></div>' if clean_eyebrow else ''
    return f'''<section class="content-section {cls}">
      <div class="section-heading-row"><div>{ey}<h2>{smart_heading(title)}</h2></div>{section_glyph(title)}</div>
      {body}
    </section>'''


def exhibit_figure(src, kicker, title, caption, credit='', source_url='', license_label='', cls=''):
    credit_bits = []
    if credit:
        credit_bits.append(f'图像作者／来源：{html.escape(credit)}')
    if license_label:
        credit_bits.append(f'授权：{html.escape(license_label)}')
    credit_html = ' · '.join(credit_bits)
    if source_url:
        credit_html += ((' · ' if credit_html else '') +
                        f'<a href="{html.escape(source_url)}" target="_blank" rel="noreferrer">查看原始来源 ↗</a>')
    return f'''<figure class="exhibit-figure {cls}">
      <div class="exhibit-image-wrap"><img src="{html.escape(src)}" alt="{html.escape(title)}" loading="lazy" decoding="async"/></div>
      <figcaption>
        <span class="exhibit-kicker">{html.escape(kicker)}</span>
        <h3>{html.escape(title)}</h3>
        <p>{caption}</p>
        {f'<small>{credit_html}</small>' if credit_html else ''}
      </figcaption>
    </figure>'''


def exhibit_pair(a, b, cls=''):
    return f'<div class="exhibit-pair {cls}">{a}{b}</div>'


def portrait_card(src, name, years, note, source_url, credit, license_label):
    return f'''<article class="portrait-card">
      <div class="portrait-image"><img src="{html.escape(src)}" alt="{html.escape(name)}" loading="eager" decoding="async"/></div>
      <div class="portrait-copy"><span>{html.escape(years)}</span><h3>{html.escape(name)}</h3><p>{note}</p>
      <small>图像作者／来源：{html.escape(credit)} · 授权：{html.escape(license_label)} · <a href="{html.escape(source_url)}" target="_blank" rel="noreferrer">查看来源 ↗</a></small></div>
    </article>'''


def exhibit_label(number, title, text):
    return f'''<aside class="exhibit-label"><span>{html.escape(number)}</span><div><b>{html.escape(title)}</b><p>{text}</p></div></aside>'''


def page_shell(filename, title, intro, body, label='研究与实践', extra_js=''):
    def nav_links(items):
        return ''.join(
            f'<a href="{u}" class="{"active" if filename==u else ""}"' +
            (' aria-current="page"' if filename==u else '') +
            f'>{t}</a>'
            for u,t in items
        )

    primary_nav = nav_links(NAV_PRIMARY)
    more_nav = nav_links(NAV_MORE)
    more_active = ' active' if any(filename == u for u, _ in NAV_MORE) else ''
    mobile_core = nav_links(NAV_PRIMARY[1:])
    mobile_deep = nav_links(NAV_MORE)
    nav = f'''<nav class="desktop-nav" aria-label="主导航">{primary_nav}<details class="nav-more{more_active}"><summary>更多<span aria-hidden="true">⌄</span></summary><div class="nav-more-menu">{more_nav}</div></details></nav>
    <nav class="mobile-nav" id="mobileNav" aria-label="移动导航" aria-hidden="true"><div class="mobile-nav-group"><span>核心入口</span>{mobile_core}</div><div class="mobile-nav-group"><span>深入探索</span>{mobile_deep}</div></nav>'''
    body_text = re.sub(r'<[^>]+>', '', body)
    reading_units = len(re.findall(r'[\u4e00-\u9fff]', body_text)) + len(re.findall(r'\b[A-Za-z0-9][A-Za-z0-9\-]*\b', body_text)) * 2
    reading_minutes = max(3, (reading_units + 499) // 500)
    hero_meta = f'<div class="hero-meta"><span>约 {reading_minutes} 分钟阅读</span><span>可按“本页导览”跳读</span></div>' if 'article-grid' in body else f'<div class="hero-meta"><span>约 {reading_minutes} 分钟阅读</span></div>'
    hero_html = '' if filename == 'index.html' else f'''<section class="page-hero"><div class="hero-copy"><span class="kicker">{label}</span><h1>{smart_heading(title)}</h1><p>{intro}</p>{hero_meta}<div class="hero-line"></div></div></section>'''
    continue_items = PAGE_CONTINUE.get(filename, [])
    continue_html = ''
    if continue_items:
        cards = ''.join(f'<a href="{u}"><span>继续探索</span><b>{label}</b><i aria-hidden="true">→</i></a>' for u, label in continue_items)
        continue_html = f'<section class="continue-reading" aria-label="继续阅读"><div><span>接下来</span><h2>继续沿着这条线索走下去</h2></div><div class="continue-grid">{cards}</div></section>'
    doc_title = SITE_NAME if filename == 'index.html' else _replace_terms(f'{title}｜{SITE_NAME}')
    meta_intro = _replace_terms(intro)
    return f'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{html.escape(doc_title)}</title>
<meta name="description" content="{html.escape(meta_intro[:155])}"/>
<meta name="theme-color" content="#1f2723"/>
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml"/>
<link rel="stylesheet" href="assets/style.css?v={ASSET_VERSION}"/>
</head>
<body data-page="{filename}">
<a class="skip-link" href="#main">跳到正文</a>
<header class="site-header">
  <a class="brand" href="index.html"><span class="brand-mark"><i></i><i></i><i></i></span><span><b>共同等候</b><small>贵格会聚会研究室</small></span></a>
  <button class="nav-toggle" type="button" aria-label="打开目录" aria-controls="mobileNav" aria-expanded="false"><span class="nav-toggle-icon" aria-hidden="true"><i></i><i></i></span><span>目录</span></button>
  {nav}
</header>
<div class="nav-scrim" aria-hidden="true"></div>
<div class="reading-progress" aria-hidden="true"><span></span></div>
<main id="main">
{hero_html}
{body}
{continue_html}
</main>
<footer class="site-footer"><div><b>{SITE_NAME}</b><p>这是一个中文研究与实践项目，不代表任何贵格会年会或官方机构。</p></div><div class="footer-links"><a href="research.html">来源与研究方法</a><a href="visual-credits.html">图像与史料说明</a><a href="glossary.html">术语表</a><a href="practice.html">开始一次练习</a></div><p class="footer-note">为慢读、谨慎聆听与生活实践而设计。</p></footer>
<script src="assets/app.js?v={ASSET_VERSION}"></script>{extra_js}
</body></html>'''

# --- Home page ---
index_body = f'''
<section class="home-hero"><div class="home-copy"><span class="kicker">QUAKER MEETING · 研究 × 实践</span><h1>{smart_heading('在静默中，共同聆听。')}</h1><p>{TAGLINE}</p><div class="cta-row"><a class="btn primary" href="practice.html">体验 12 分钟等候练习</a><a class="btn ghost" href="meeting.html">先理解聚会是什么</a></div><div class="hero-note"><span></span>不是冥想应用，也不是宗教百科；这里把贵格会聚会（Meeting）作为“共同聆听、共同检验与共同明辨”的实践来研究。</div></div>{circle_visual()}</section>
<section class="home-intro"><div class="big-question"><span>THE QUESTION</span><h2>{smart_heading('如果一群人暂时不争着表达立场，会不会有一些东西，反而更容易被听见？')}</h2></div><div class="intro-copy"><p>贵格会 Meeting 最令人着迷的地方，不只是“安静”。真正独特的是：一群人共同停下来，不把某个人、某套理论或某种程序放在中心，而是通过等待、聆听、说与不说，让一个更深的共同辨识逐渐出现。</p><p>Howard Brinton 把 Quakerism 描述为一种以经验为基础的 <em>method</em>，并把它称为一种 <em>group mysticism</em>：内在经验不是终点，必须进入群体、历史与行动。Parker Palmer 又把 “meeting” 这一精神延伸到学习，使它成为一种关于“我们怎样共同认识真实”的实践。</p></div></section>
<section class="curated-opening"><div class="section-head"><span>VISUAL ESSAY · 01</span><h2>{smart_heading('先看见一个 Meeting 的空间')}</h2><p>没有讲台、没有屏幕，也没有一个天然占据中心的人。建筑与座位本身，就已经在表达一种关于权威、注意力与共同体的理解。</p></div>
{exhibit_figure('assets/curated/meetinghouse-interior.jpg','FIELD IMAGE · MEETING HOUSE','贵格会聚会所的室内空间','这张真实场景照片显示一个传统聚会所（Meeting House）的内部：长椅、可移动隔断、几乎没有视觉焦点。空间并不会自动制造共同聆听，却会减少“谁站在中心”的暗示。','Pi3.124','https://commons.wikimedia.org/wiki/File:Interior_of_Quaker_meeting_house.jpg','CC BY-SA 4.0','hero-exhibit')}
<div class="exhibit-annotations">{exhibit_label('A','没有舞台','空间把注意力从“台上的人”移回共同体与共同中心。')}{exhibit_label('B','可被重组的空间','历史上的 Meeting House 常因性别、事务与地方实践存在不同空间安排；形式并不等于本质。')}{exhibit_label('C','建筑也在教人','朴素并不是“没有设计”，而是让结构服务于等待、可见性与共同承担。')}</div></section>
<section class="home-depth"><div class="section-head"><span>WHY IT MATTERS</span><h2>{smart_heading('Meeting 不只是安静下来，而是在练习“如何共同认识”')}</h2><p>它既涉及灵性，也涉及认识论、群体动力、组织治理与伦理行动。</p></div>{epistemology_visual()}<div class="depth-grid"><article><span>01</span><h3>经验，不等于任性</h3><p>个人经验被认真对待，但重要的 leading 需要时间、共同体与生活后果的检验。</p></article><article><span>02</span><h3>群体，不等于多数</h3><p>Meeting 重视 corporate discernment，却不把人数优势当作 Truth 的替代品。</p></article><article><span>03</span><h3>静默，不等于退避</h3><p>Thomas Kelly 与 Brinton 都把 inward life 指向 outward action：内在聆听若有生命，会进入关系、决定与公共见证。</p></article></div></section>
<section class="home-map"><div class="section-head"><span>ONE MAP</span><h2>一张图，理解 Meeting 的五个层次</h2><p>从“我里面发生什么”，到“我们如何一起行动”。</p></div>{layer_visual()}<div class="map-links"><a href="worship.html"><b>01</b><span>静默与等候<small>Silence / Waiting</small></span></a><a href="ministry.html"><b>02</b><span>说与不说<small>Vocal Ministry</small></span></a><a href="gathered.html"><b>03</b><span>被聚集的时刻<small>Gathered Meeting</small></span></a><a href="business.html"><b>04</b><span>共同明辨<small>Sense of the Meeting</small></span></a><a href="toolkit.html"><b>05</b><span>进入日常<small>Practice & Action</small></span></a></div></section>
<section class="visual-index"><div class="section-head"><span>PEOPLE · PLACE · ARCHIVE</span><h2>不只读概念，也看见传统留下的痕迹</h2><p>人物肖像、Meeting House 与历史地点不是装饰；它们帮助我们把抽象词放回时间、空间和具体的人。</p></div><div class="visual-index-grid">
<a href="history.html"><div class="visual-index-image"><img src="assets/curated/george-fox.jpg" alt="George Fox 肖像" loading="lazy"/></div><span>人物</span><h3>从 George Fox 到 John Woolman</h3><p>四个生命切面，看 Meeting 如何进入组织、治理与见证。</p></a>
<a href="community.html"><div class="visual-index-image"><img src="assets/curated/swarthmoor-hall.jpg" alt="Swarthmoor Hall" loading="lazy"/></div><span>地点</span><h3>Swarthmoor Hall 与 Meeting House</h3><p>看建筑、家庭与共同体怎样成为实践长期发生的容器。</p></a>
<a href="research.html"><div class="visual-index-image"><img src="assets/curated/margaret-fell.jpg" alt="Margaret Fell 后世艺术形象" loading="lazy"/></div><span>史料</span><h3>一张图，也需要知道它从哪里来</h3><p>同时代图像、后世印象、现代照片，各自能支持不同程度的判断。</p></a>
</div></section>
<section class="meeting-family"><div class="section-head"><span>MEETING FAMILY</span><h2>Meeting 不是只有一种</h2></div><div class="family-grid">
<a href="worship.html"><span>01</span><h3>Meeting for Worship</h3><p>共同静默、等候、聆听；必要时出现受感分享。</p></a>
<a href="business.html"><span>02</span><h3>Meeting for Worship for Business</h3><p>不以投票决定，而在敬拜精神中辨认群体是否形成清晰。</p></a>
<a href="clearness.html"><span>03</span><h3>Clearness Committee</h3><p>以开放问题、静默和保密，帮助一个人更清楚地听见自己的引领。</p></a>
<a href="learning.html"><span>04</span><h3>Meeting for Learning</h3><p>让人、人和“第三物”真正相遇，把学习从信息摄取变成共同探寻。</p></a>
</div></section>
<section class="practice-banner"><div><span>不要只读。</span><h2>Meeting 最终只能通过 Meeting 来理解。</h2><p>先做一次 12 分钟练习。没有指导语轰炸，也没有“放松成功”的要求。</p></div><a class="btn inverted" href="practice.html">进入实践 →</a></section>
<section class="reading-path"><div class="section-head"><span>TWO PATHS</span><h2>你可以这样进入</h2></div><div class="path-grid"><article><span>第一次接触</span><ol><li><a href="meeting.html">Meeting 到底是什么？</a></li><li><a href="worship.html">静默不是空白</a></li><li><a href="practice.html">12 分钟体验</a></li><li><a href="ministry.html">什么时候该说话？</a></li><li><a href="business.html">为什么不投票？</a></li></ol></article><article><span>想刨根究底</span><ol><li><a href="history.html">从 Seekers 到现代</a></li><li><a href="gathered.html">Gathered Meeting</a></li><li><a href="research.html">原典与研究书目</a></li><li><a href="comparisons.html">与其他方法比较</a></li><li><a href="traditions.html">世界会聚传统与 AI 时代</a></li><li><a href="china.html">在中国：文化整合与当代实践</a></li><li><a href="glossary.html">建立术语坐标</a></li></ol></article></div></section>
'''

pages = {}
pages['index.html'] = page_shell('index.html','共同等候',TAGLINE,index_body,label='QUAKER MEETING LAB')

# --- Meeting overview ---
meeting_body = f'''
<div class="article-grid"><article class="article-main">
{section('Meeting：不是“会议”的同义词','''<p>在贵格会语境里，<strong>Meeting</strong> 同时指一次聚集、一个持续存在的共同体，也指一种特殊的共同实践。把它全部翻成“会议”，会让最重要的东西消失。</p><p>在 Meeting 中，中心并不预先被一个讲者、主持人、教义或议程占据。人们首先做的，是让自己安顿下来，进入一种共同的等待：不急着制造结果，也不假装什么都没有发生。</p>''','01 · DEFINITION')}
{callout('一个抓手','<p><strong>Meeting 可以理解为：一群人共同为“尚未完全显现的真实”腾出空间。</strong></p><p>这不是严格定义，却是理解 Worship、Business、Clearness 和 Learning 的共同钥匙。</p>')}
{exhibit_figure('assets/curated/arch-street.jpg','PLACE · PHILADELPHIA','Arch Street Friends Meeting House','一座聚会所（Meeting House）既是建筑，也是共同体长期记忆的容器。拱街贵格会聚会所（Arch Street Friends Meeting House）建于 1803–05 年；它提醒我们，“聚会”从来不只是一次活动，也指持续存在、承担事务与见证的地方共同体。','Beyond My Ken',VISUAL_SOURCES['arch'],'CC BY-SA 4.0','article-exhibit')}
{section('为什么 Brinton 说 Quakerism 首先是一种 method？','''<p>Howard Brinton 的一个关键判断是：要理解贵格会，不能只列出“它相信什么”，还要看<strong>它如何抵达、检验和修正这些相信</strong>。因此他把 Quakerism 比作一种方法：它不像科学那样测量外部对象，而是面向内在生命、道德要求、宗教洞见与群体经验。</p><p>这使 Meeting 变成一种持续的认识实践。经验很重要，但经验不是“我感觉如此，所以就是真理”；它需要在时间、历史、共同体与行动后果中不断被检验。也正因为如此，Brinton 所说的 <em>group mysticism</em> 不是一群人各自拥有神秘体验，而是个人经验在共同体中被承接、修正并获得社会形态。</p>'''+research_note('把“体验”变成“可检验的实践”','''<p>如果只强调 inward experience，Meeting 很容易滑向私人灵性消费；如果只强调组织规则，它又会失去直接经验的生命。贵格会长期存在的张力，正是在两者之间保持开放：既不把权威外包给制度，也不把权威收回到个人情绪。</p>'''), '02 · METHOD')}
{section('它与“大家一起静坐”有什么不同？','''<div class="compare-mini"><div><b>一起静坐</b><p>重点可能在个体专注、觉察、放松或禅修。</p></div><div><b>Quaker Meeting</b><p>个人内在安顿很重要，但始终处在一个群体场域中：我在听自己，也在听这个房间、这个共同体，以及可能超越个人意志的引领。</p></div></div><p>Jim Pym 早年把 Meeting 误以为 meditation group，后来才意识到它并不是佛教意义上的冥想团体。这种误解今天依然非常普遍。</p>''','02 · NOT JUST MEDITATION')}
{section('五个层次同时发生','''<p>一个成熟的 Meeting 往往同时有五个层次。它们不是五步流程，而是五种可以被观察的维度。</p>'''+layer_visual()+'''<div class="definition-list"><dl><dt>Center</dt><dd>这个圆圈最终忠于什么？早期 Friends 会说 God、Christ、Truth、Light；现代不同传统的 Friends 会使用不同语言。</dd><dt>Inward</dt><dd>我是否从惯性反应、紧张和自我表演中稍微退开，变得可听？</dd><dt>Between</dt><dd>我如何听别人？一句 spoken ministry 如何被整个房间接住，而不是立刻讨论？</dd><dt>Corporate</dt><dd>群体有没有出现一种任何单个人都无法制造的清晰、深度或 unity？</dd><dt>Outward</dt><dd>这份清晰最后如何进入决定、关系、工作与社会行动？</dd></dl></div>'''+epistemology_visual(), '03 · FIVE LAYERS')}
{section('Inner Light 不是“我的感觉就是对的”','''<p>“内在之光”最容易在现代语境里被误读成直觉主义：只要我内在有强烈感觉，就应该忠于它。Michael Marsh 对这一点提出了有价值的哲学追问：<strong>Light 是一个隐喻，它让原本隐藏的关系变得可见；但“看见”本身不自动保证客观正确。</strong></p><p>Patricia Loring 也从实践面提醒：我们内部同时存在愿望、恐惧、自我意志、父母和文化留下的声音。所谓 discernment，恰恰是学习分辨这些声音，而不是把“来自内在”当作免检标签。</p>'''+research_note('专业性来自“允许复杂性存在”','''<p>一个成熟的 Meeting 不急着把 Light 心理学化，也不急着把所有体验神学化。它更像一套长期实践：经验出现——停下来——交给时间——交给共同体——观察果实——再决定是否行动。</p>'''), '04 · INNER LIGHT')}
{section('最常见的七个误解','''<div class="myth-grid"><article><b>“就是沉默一小时”</b><p>沉默只是外在形式；核心是 expectant waiting。</p></article><article><b>“每个人做自己的内观”</b><p>Meeting 是群体实践，不是并排进行的私人练习。</p></article><article><b>“想说就说”</b><p>传统上 spoken ministry 需要经过内在辨识。</p></article><article><b>“没有领导者”</b><p>不是没有角色，而是角色不拥有 Truth。Clerk、elders 等都服务于共同体。</p></article><article><b>“没有教义，所以什么都可以”</b><p>贵格会长期以 experience、testimony、community testing 形成非常严肃的纪律。</p></article><article><b>“不投票就是共识决策”</b><p>Sense of the Meeting 与现代 consensus 有重叠，但目标与精神基础并不相同。</p></article><article><b>“安静一定会让人平静”</b><p>真正的聆听也可能让人面对不愿承认的冲突、责任或召唤。</p></article></div>''','05 · MISUNDERSTANDINGS')}
{section('一个极简观察框架','''<div class="process-row bilingual-process"><span><b>到场</b><small>（Arrive）</small></span><i>→</i><span><b>安顿</b><small>（Settle）</small></span><i>→</i><span><b>等候</b><small>（Wait）</small></span><i>→</i><span><b>聆听</b><small>（Listen）</small></span><i>→</i><span class="wide"><b>发言或保持静默</b><small>（Speak / Remain Silent）</small></span><i>→</i><span><b>返回</b><small>（Return）</small></span></div><p class="fineprint">注意：这不是“贵格会聚会（Quaker Meeting）六步法”。它只是本站为了帮助初学者观察内部动态而做的一张地图。</p>''','05 · OBSERVE')}
{section('带着这些问题继续','''<p>贵格会传统喜欢用 Queries 而不是“标准答案”结束学习。你也可以从这几个问题继续。</p>'''+query_cards(['当我安静下来时，我最先遇到的通常是什么：焦躁、计划、疲惫，还是别的东西？','我能否分辨“我很想表达”与“这句话真的需要被这个圆圈听见”之间的差别？','如果一个群体迟迟没有形成清晰，我是否愿意把“暂不决定”也看作一种成熟的结果？']))}
</article>{source_box([('Howard H. Brinton, Friends for 300 Years','重点参见第4章 The Meeting for Worship、第5章 Vocal Ministry、第6章 Reaching Decisions。'),('Jim Pym, Listening to the Light','“The Source—the Quaker meeting for worship” 与 “A New Way of Working”。'),('Parker J. Palmer, Meeting for Learning','以 Meeting 作为教育与共同探寻的核心隐喻。')])}</div>
'''
pages['meeting.html'] = page_shell('meeting.html','Meeting 到底是什么？','它不是“会议”的简单翻译，也不只是多人静坐。理解 Meeting，要同时看到内在、关系、群体与行动四个方向。',meeting_body)

# --- worship ---
worship_body = f'''
<div class="article-grid"><article class="article-main">
{section('静默不是空白','''<p>贵格会 Meeting 的静默常常被误解为“清空头脑”。但传统中的 waiting 更接近<strong>带着期待的开放</strong>：人不必把念头清掉，也不急着跟随每个念头，而是让注意力逐渐从惯性反应中松开。</p><p>Brinton 在讨论 worship 时强调，与其说要消灭纷乱思想，不如说要“活在那超越它们的地方”。这使静默不是一种对心智的暴力控制，而是一种重新排序注意力的方式。</p>''','01 · SILENCE')}
{exhibit_figure('assets/curated/meetinghouse-interior.jpg','FIELD IMAGE · WORSHIP SPACE','静默不是发生在真空里','这张 Meeting House 室内照片让一个抽象概念变得具体：人进入的不是“个人冥想隔间”，而是一个能看见彼此、共同承受静默的空间。历史上不同 Meeting House 的座位、隔断与礼仪安排并不相同，但“共同在场”一直是关键。','Pi3.124',VISUAL_SOURCES['interior'],'CC BY-SA 4.0','article-exhibit')}
{section('Silence → Waiting → Worship','''<div class="three-stage"><article><span>01</span><h3>Silence</h3><p>外在声音减少，身体和注意力开始有空间。</p></article><article><span>02</span><h3>Waiting</h3><p>不只是没有讲话，而是期待某种尚未被制造出来的清晰。</p></article><article><span>03</span><h3>Worship</h3><p>等待带有关系性：我把自己置于 Light / Truth / God 的可能引领之下。</p></article></div>''','02 · THREE DEPTHS')}
{silence_visual()}
{callout('重要区别','<p><strong>静默是外在条件；waiting 是内在姿态；worship 是关系与方向。</strong></p>','dark')}
{section('“等候”为什么不是一种注意力技巧？','''<p>如果只从心理训练看，waiting 很容易被理解成“延迟反应”或“保持开放”。这些描述有帮助，却还没有触到传统语境的全部。对早期 Friends 而言，等候之所以有方向，是因为他们相信 Divine Presence 并非缺席；人不是在制造启示，而是在学习停止遮蔽、停止抢先。</p><p>这也是为什么 Brinton 会说，Quaker worship 把“God reveals himself directly”这一信念推到实践层面：如果启示并非只属于过去，那么 worship 的基本动作就不是不断填充语言，而是 reverent waiting 与 listening。</p>'''+research_note('历史语言与当代语言之间，需要保持张力','''<p>今天一些 liberal Friends 会更多使用 Truth、Light、Life、Love 或 inward guidance；另一些 Friends 仍明确以 Christ、Scripture 与 Holy Spirit 为中心。把所有这些语言强行统一，会失去传统内部真实存在的差异。本站会尽量标注语境，而不是把某一支当成全部。</p>'''), '03 · THEOLOGICAL DIRECTION')}
{section('进入Meeting 时，具体可以怎么做？','''<div class="practice-steps"><article><b>先允许自己还没有安静</b><p>注意身体接触椅子、脚底、呼吸和房间里的声音。不要把“马上进入状态”变成新任务。</p></article><article><b>不追赶每一个念头</b><p>你可以知道它在，却不必完成它。计划、回忆、情绪都可以经过。</p></article><article><b>从“我要做什么”转向“有什么值得被听见”</b><p>不是逼自己找答案，而是让问题在空间里待一会儿。</p></article><article><b>同时听房间</b><p>Meeting 不是私人练习。感受其他人的存在，不必想象他们在做什么。</p></article><article><b>有人说话后，不立即回应</b><p>让话语重新落回静默。它可能不是讨论的开端，而是共同聆听的一部分。</p></article></div>''','03 · HOW TO ENTER')}
{section('杂念怎么办？','''<p>最容易把初学者带偏的问题，就是：“怎样才能没有杂念？” Meeting 并不要求达到某种纯净意识状态。一个更实用的观察方式是：</p><div class="ladder"><div><span>念头出现</span><p>我注意到了。</p></div><div><span>自动跟随</span><p>我已经在心里写完三封邮件。</p></div><div><span>重新回来</span><p>不责备，重新感到身体、房间、等待。</p></div><div><span>渐渐变深</span><p>某些念头退到背景，某些问题反而显出重量。</p></div></div>''','04 · DISTRACTION')}
{section('什么时候结束？','''<p>正式 Meeting 的结束方式因群体而异，常见做法是 designated Friends 握手，其他人随之握手，表示 worship 已结束。本站的练习采用轻微提示音，只是数字环境中的替代。</p><p>更重要的是：结束不意味着把静默留在房间。Thomas Kelly 的一个核心关切，正是让内在注意逐渐进入日常行动，使“内在圣所”成为工作日也可返回的参照。</p>''','05 · RETURN')}
{section('从 inward life 到 workaday life','''<p>Thomas Kelly 反复强调，内在生命若只发生在固定的安静时段，仍然是不完整的。他所描述的是一种“同时生活在两层”的能力：表层继续工作、说话、做决定；更深一层保持对 Light 的注意。</p><p>这使 Meeting 的价值不在于把人从生活中抽离，而在于训练一种能够回到市场、办公室、家庭与公共事务中的注意方式。外在见证不是附加的“公益活动”，而是 inward attention 结出的果实。</p>'''+research_note('一个可观察的检验','''<p>一次 Meeting 是否“有效”，不只看当场是否平静、感动或深刻。更值得问的是：离开以后，我是否更诚实？更能承担关系？更少被自我防卫驱动？更愿意做一件代价真实、但更忠实的事？</p>'''), '06 · EVERYDAY LIGHT')}
{section('试着这样观察下一次静默', query_cards(['我是在等“某件事发生”，还是在练习不预设会发生什么？','沉默里最难放下的是什么：控制、效率、表现、解释，还是被看见的需要？','如果我把今天一个真实处境带入 Light 中重新看，它的意义有没有发生一点变化？']) + '<div class="cta-inline"><a class="btn primary" href="practice.html">开始 12 分钟体验</a><a class="btn ghost" href="ministry.html">继续：什么时候该说话？</a></div>', '07 · PRACTICE')}
</article>{source_box([('Howard H. Brinton, Friends for 300 Years','第4章 The Meeting for Worship，尤其关于 waiting、silence、unity 与 worship 的讨论。'),('Thomas R. Kelly, The Light Within','关于持续的 inward orientation，以及把内在之光带入日常行动。')])}</div>
'''
pages['worship.html'] = page_shell('worship.html','静默，不是什么都不做','从 Silence 到 Waiting，再到 Worship：贵格会静默的关键不是“脑中无念”，而是从立即反应中退开，进入共同等候。',worship_body)

# --- practice ---
practice_body = f'''
<section class="practice-intro"><div><span class="kicker">12 MINUTES · BEGINNER PRACTICE</span><h2>一次尽量少指导的Meeting体验</h2><p>这不是正式 Meeting for Worship 的替代品，而是一段帮助初学者理解“共同等候”内部质感的数字练习。最好把手机调静音，坐直但不僵硬，允许自己不进入任何特殊状态。</p></div><div class="practice-rules"><span>不追求放松</span><span>不强迫清空</span><span>不解释体验</span><span>不急着得答案</span></div></section>
<section class="timer-shell"><div class="timer-top"><div><span id="stageIndex">准备</span><h2 id="stageTitle">坐下来，让自己到达这里。</h2><p id="stagePrompt">注意身体、房间和此刻的状态。不需要马上安静。</p></div><div class="timer-circle"><svg viewBox="0 0 120 120"><circle class="timer-bg" cx="60" cy="60" r="52"/><circle id="timerProgress" class="timer-progress" cx="60" cy="60" r="52"/></svg><strong id="timeDisplay">12:00</strong></div></div><div class="timer-controls"><button class="btn primary" id="startTimer">开始</button><button class="btn ghost" id="pauseTimer">暂停</button><button class="btn ghost" id="resetTimer">重置</button></div><div class="stage-track" id="stageTrack"></div></section>
<section class="after-practice"><div class="section-head"><span>AFTER</span><h2>结束后，不急着评价“做得好不好”</h2><p>只记录一点事实。记录会保存在当前浏览器中，不会上传。</p></div><div class="reflection-grid"><label>刚才什么最明显？<textarea id="r1" placeholder="例如：很躁、听到空调、某个问题一直回来……"></textarea></label><label>有没有什么变得稍微清楚？<textarea id="r2" placeholder="不必是答案，也可以只是一个感觉或方向。"></textarea></label><label>我现在想带走什么？<textarea id="r3" placeholder="一个问题、一句提醒、一件准备去做或暂时不做的事。"></textarea></label></div><div class="reflection-actions"><button class="btn primary" id="saveReflection">保存到本机</button><button class="btn ghost" id="clearReflection">清空</button><span id="saveStatus"></span></div></section>
<section class="content-section"><div class="section-head"><span>NEXT</span><h2>这 12 分钟里，你其实在练习什么？</h2></div><div class="skill-grid"><article>{icon('silence')}<h3>Settling</h3><p>从外部刺激与内部惯性中慢慢收回注意。</p></article><article>{icon('light')}<h3>Waiting</h3><p>不预设答案，却保持可被触动的状态。</p></article><article>{icon('group')}<h3>Corporate attention</h3><p>即使不说话，也把自己理解为群体的一部分。</p></article><article>{icon('question')}<h3>Discernment</h3><p>分辨“很多声音”里，哪些值得继续等待和检验。</p></article></div>{callout('下一步','<p>真正的 Meeting 需要人与人同处。数字练习只能帮你熟悉一些内在动作。下一步最好是参加真实 Meeting，或与 3–8 位伙伴举行一次 30–45 分钟的简化实践。</p>')}</section>
<section class="content-section"><div class="section-head"><span>FROM SOLO TO CORPORATE</span><h2>不要把 12 分钟练习误当成Meeting的缩小版</h2><p>个人练习只能帮助你熟悉 settling 与 waiting。真正独特的部分，要等到“别人也在场”以后才开始出现。</p></div><div class="practice-ladder-v2"><article><span>01 · SOLO</span><h3>12 分钟个人练习</h3><p>认识自己的自动反应：急于找答案、追念头、追求特殊状态。</p></article><article><span>02 · SMALL GROUP</span><h3>30–45 分钟共同静默</h3><p>开始练习 corporate attention：别人存在，却不需要被我分析、照顾或回应。</p></article><article><span>03 · MINISTRY</span><h3>学习“说与不说”</h3><p>让 insight 经历等待；区分“我想表达”与“这个 Meeting 需要听见”。</p></article><article><span>04 · DISCERNMENT</span><h3>把真实议题带进群体</h3><p>当群体具有足够信任与纪律，再进入 clearness、business 与共同辨识。</p></article></div></section>
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
{section('练习：感受“群体”，而不是只听自己','''<div class="practice-card"><span>20–30 分钟 · 3–8 人</span><ol><li>围成圆形，不放桌子或只放一个很小的中心物。</li><li>开始前只说明：这是共同静默，不要求分享。</li><li>前 3 分钟感受身体和房间。</li><li>接下来不再给指导；同时留意“我”与“我们”的注意如何变化。</li><li>结束后每人只用一句话回答：“刚才房间里，有什么是我一个人做不出来的？”</li><li>不互相评论。</li></ol></div>''','05 · PRACTICE')}
{section('Queries', query_cards(['我有没有把“群体经验”浪漫化，以至于害怕普通、干燥、没有感觉的 Meeting？','当别人和我意见不同，我是否仍有可能体验到一种不等于认同的 unity？','什么样的空间、节奏与规则，会帮助一群人少一点表演，多一点共同注意？']), '06 · QUERIES')}
</article>{source_box([('Howard H. Brinton, Friends for 300 Years','第4章关于 collective silent worship、unity 与 group meditation 的讨论。'),('Patricia Loring, Spiritual Discernment','Gathered meeting 与 corporate discernment / unity 的关系。')])}</div>
'''
pages['gathered.html'] = page_shell('gathered.html','当 Meeting 被“聚集”','有些 Meeting 只是很多人一起安静；有些时刻，圆圈会出现一种难以归属于任何个人的共同深度。贵格会称之为 gathered meeting。',gathered_body)

# --- business ---
business_body = f'''
<div class="article-grid"><article class="article-main">
{section('为什么一个宗教群体发展出一种独特的决策法？','''<p>17世纪的 Friends 很快就遇到现实问题：救济受迫害者、婚姻、教育、旅行传道、财务、纪律与公共行动都需要组织。但一个强调“内在引领”的群体，怎样避免又建立一个由外部权威支配的制度？</p><p>由此逐渐形成 <strong>Meeting for Worship for Business</strong>：议事不是从 worship 中抽离出来的世俗事务，而是在同一种共同聆听与明辨中处理具体事项。</p>''','01 · ORIGIN')}
{exhibit_figure('assets/curated/free-quaker-interior.jpg','HISTORIC INTERIOR · PHILADELPHIA','议事并不需要“董事会式”的空间','这是费城 Free Quaker Meeting House 的历史建筑内部，并不是某一次 Business Meeting 的现场照片。它在这里作为空间史料出现：Quaker corporate life 长期在朴素、可彼此看见的环境中处理敬拜与公共事务。','U.S. National Park Service',VISUAL_SOURCES['free_interior'],'Public domain (U.S.)','article-exhibit')}
{decision_visual()}
{section('表决、共识与聚会的共同辨识','''<div class="compare-table"><div class="row head"><span>机制</span><span>核心问题</span><span>结束条件</span><span>风险</span></div><div class="row"><b>多数表决（Voting）</b><span>哪个选项票更多？</span><span>达到规则票数</span><span>少数意见被合法压过</span></div><div class="row"><b>共识（Consensus）</b><span>我们能接受什么？</span><span>达到足够一致</span><span>可能滑向最低共同点或谈判</span></div><div class="row accent"><b>聚会的共同辨识（Sense of the Meeting）</b><span>此刻什么方向最忠于真理与内在引领？</span><span>聚会形成可被辨认和承担的合一与清晰</span><span>若缺少敬拜精神，也可能只是假装的“无投票共识”</span></div></div><p>帕特里夏·洛林（Patricia Loring）特别强调，贵格会的合一不是意见完全一致（agreement）、普通共识（consensus）、妥协（compromise）或最低共同点。不同意见仍可能存在，但群体可能对“现在应该怎样前进”出现更深的共同清晰。</p>''','02 · THREE MODELS')}
{research_note('为什么“没有反对意见”仍然可能不是 unity？','''<p>沉默可能来自清晰，也可能来自权力差异、疲惫、害怕冲突或对 Clerk 的顺从。因此严肃的 Meeting for Business 会主动听取关键保留意见，尤其当议题重大时。真正的 unity 不是把分歧消音，而是让分歧在共同敬拜中获得足够空间，直到它被理解、转化，或被承认仍然存在。</p>''')}
{section('Clerk：不是主席','''<div class="role-grid"><article><b>Chairperson</b><p>通常负责控制议程、分配发言、维持程序，必要时推动表决。</p></article><article class="accent"><b>Clerk</b><p>准备议程并照看秩序，但关键任务是<strong>听整个 Meeting</strong>：辨认何时接近清晰，并尝试把 emerging sense 写成 minute，交回群体检验。</p></article></div><p>因此 Clerk 的权威不是“我决定”，而是“我试着说出我听见这个 Meeting 正在形成的东西”。如果群体认为措辞不对，minute 就继续修改，甚至整个议题被推迟。</p>''','03 · CLERK')}
{section('互动案例：12个人要不要搬迁社区空间？','''<div class="case-lab" id="caseLab"><div class="case-story"><p><strong>情境</strong>：租约即将到期。新空间更大、更便宜，但离原社区 4 公里。12位核心成员中，7人赞成、3人反对、2人不确定。</p><p>你会怎么处理？</p></div><div class="case-options"><button data-case="vote">A · 现在投票</button><button data-case="consensus">B · 继续协商到大家都能接受</button><button data-case="sense">C · 进入 Meeting for Business 的明辨过程</button></div><div id="caseResult" class="case-result">选择一种路径，看它真正优化的是什么。</div></div>''','04 · CASE LAB')}
{section('什么时候“不决定”反而更成熟？','''<p>Brinton 记录，Friends 在重大议题上可能长时间等待 unity。这个传统很容易被现代组织理解成低效率，但它提醒我们：<strong>“做出决定”与“真正清楚”不是同一件事。</strong></p><p>当然，现实并非所有事项都能无限等待。成熟实践需要区分：哪些只是执行层面的 routine business，哪些会伤及共同体、使命或重大价值，需要更多时间。</p>''','05 · WAITING')}
{section('Minute：不是会后整理，而是现场检验','''<p>Quaker business 中的 minute 常常在现场形成。Clerk 尝试把自己听见的 emerging sense 写成一句或几句清楚的文字，再读回给 Meeting。这个动作非常重要，因为“感觉差不多了”会被迫转化为具体语言。</p><p>文字一旦不准确，隐藏的分歧就会显现出来。于是 minute 既是记录，也是检验工具：群体是在认可同一个方向，还是只是在各自脑中认可不同的东西？</p>'''+research_note('Clerk 的艺术：既不能过早总结，也不能永远不总结','''<p>过早 minute 会把活的明辨压成结论；过晚 minute 又可能让 Meeting 在重复意见中失去方向。Clerk 需要同时听内容、情绪、沉默与群体能量，却不能把个人偏好偷偷写成“Meeting 的声音”。</p>'''), '06 · MINUTE')}
{section('一场 90 分钟 Meeting for Business 的简化模板','''<div class="agenda"><div><b>00–10</b><span>共同静默，重新记住“为何在这里”</span></div><div><b>10–20</b><span>事实澄清：只说已知信息，不抢着立场辩论</span></div><div><b>20–50</b><span>围绕议题贡献，Clerk 保护节奏与静默</span></div><div><b>50–60</b><span>更长静默；让意见从“我的方案”退回共同中心</span></div><div><b>60–75</b><span>Clerk 尝试陈述 emerging sense / draft minute</span></div><div><b>75–85</b><span>Meeting 检验措辞；必要时承认尚未形成 clearness</span></div><div><b>85–90</b><span>静默结束，确认后续责任</span></div></div><p class="fineprint">这是现代学习用模板，不是贵格会统一规定。</p>''','07 · PRACTICAL TEMPLATE')}
</article>{source_box([('Howard H. Brinton, Friends for 300 Years','第6章《达成决定》（Reaching Decisions）：无投票、书记、聚会的共同辨识与合一的历史及方法。'),('Jim Pym, Listening to the Light','《一种新的工作方式》（A New Way of Working），讨论贵格会议事方法。'),('Patricia Loring, Spiritual Discernment','关于议事会中的合一与群体引导。')])}</div>
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
{exhibit_figure('assets/curated/john-woolman.jpg','THIRD THING · IMAGE','一张历史肖像，也可以成为“第三物”','不要先问“这是谁、代表什么”。可以先观察：姿态、服饰、绘画方式、后来添加的符号；再查看来源说明。John Woolman 这张图本身就带着不确定性——来源页把它描述为很可能出自同时代友人之手，但又包含后来时代的元素。学习因此不是“认图”，而是让对象反过来挑战我们的快速判断。','Probably Robert Smith III',VISUAL_SOURCES['woolman'],'Public domain in U.S.','article-exhibit')}
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
{exhibit_pair(
  exhibit_figure('assets/curated/arch-street.jpg','PLACE · COMMUNITY','Meeting House：共同体的长期容器','建筑不是共同体本身，却让照顾、敬拜、教育、议事和纪念拥有可持续发生的地方。','Beyond My Ken',VISUAL_SOURCES['arch'],'CC BY-SA 4.0','compact'),
  exhibit_figure('assets/curated/swarthmoor-hall.jpg','PLACE · ORIGIN','Swarthmoor Hall：家庭、运动与网络的交汇点','Swarthmoor Hall 与 Margaret Fell 及早期 Friends 的形成密切相关。它提醒我们，Quaker movement 一开始就不仅是思想，也依赖具体家庭、旅行网络与接待关系。','Marion Dutcher',VISUAL_SOURCES['swarthmoor'],'CC BY-SA 2.0','compact')
)}
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
<section class="history-gallery"><div class="section-head"><span>FOUR LIVES · FOUR WINDOWS</span><h2>{smart_heading('先从四个人进入这段历史')}</h2><p>人物不是“伟人名单”。更有价值的是看他们分别把 Meeting 的哪一个维度推到了前景：直接经验、组织与女性声音、宗教自由、以及由 inward leading 走向社会见证。</p></div>
<div class="portrait-grid">
{portrait_card('assets/curated/george-fox.jpg','George Fox','1624–1691','早期 Friends 最重要的见证者之一。这里使用的是一幅“被认为是 1677 年 Fox 肖像”的同时代图像；图像归属本身也应被当作史料问题，而不是无条件当成写真。',VISUAL_SOURCES['fox'],'Egbert van Heemskerk（归属）','Public domain')}
{portrait_card('assets/curated/margaret-fell.jpg','Margaret Fell','1614–1702','Swarthmoor Hall 的核心人物、早期运动的重要组织者与作者，也是女性 ministry 的有力辩护者。此图来自后世蚀刻中的艺术家印象，并非同时代肖像。',VISUAL_SOURCES['fell'],'Robert Spence engraving','Public domain')}
{portrait_card('assets/curated/william-penn.jpg','William Penn','1644–1718','Pennsylvania 的建立，使 Friends 的宗教自由、治理与公共伦理进入制度实验。这里采用 Francis Place 1695 年粉笔肖像，被资料描述为已知唯一一幅在 Penn 生前写生的肖像。',VISUAL_SOURCES['penn'],'Francis Place, 1695','Public domain')}
{portrait_card('assets/curated/john-woolman.jpg','John Woolman','1720–1772','他的日记和旅行 ministry 展示了一个 inward leading 如何经由长期检验，进入反奴隶制、消费伦理与 simplicity 的生活实践。图像来源页将原作归为“很可能”由同时代友人 Robert Smith III 所作。',VISUAL_SOURCES['woolman'],'Probably Robert Smith III','Public domain in U.S.')}
</div>
<div class="curator-note"><span>CURATORIAL NOTE</span><p><strong>历史人物图像也需要辨识。</strong>“有一张脸”不等于“我们确知他/她当时长这样”。本站会区分同时代肖像、后世艺术家印象、建筑照片与现代复原图，并把不确定性直接写进图说。</p></div>
</section>
<section class="history-place-study">
{exhibit_pair(
  exhibit_figure('assets/curated/swarthmoor-hall.jpg','PLACE · CUMBRIA','Swarthmoor Hall','这里不是“贵格会圣地”的浪漫背景，而是早期 Friends 网络得以聚集、接待、书写与组织的重要地点。空间、家庭与运动史在这里交叠。','Marion Dutcher',VISUAL_SOURCES['swarthmoor'],'CC BY-SA 2.0','compact'),
  exhibit_figure('assets/curated/arch-street.jpg','PLACE · PHILADELPHIA','Arch Street Friends Meeting House','十九世纪初的 Meeting House 让我们看见传统跨越大西洋后如何进入城市、制度和持续性共同体。建筑本身也是治理与记忆的容器。','Beyond My Ken',VISUAL_SOURCES['arch'],'CC BY-SA 4.0','compact')
)}</section>
<section class="history-thesis"><article><span>01</span><h3>形式会变，目的未必变</h3><p>Brinton 特别提醒：保存传统的“原始目的”，不等于复制十七世纪的可见形式。真正的问题是：一项新形式是否仍服务于等待、辨识、共同体与见证。</p></article><article><span>02</span><h3>“Quietism”不是一句贬义标签就能概括</h3><p>十八世纪既可以被看作活力下降，也可以被理解为保存、整合与纪律化。历史评价取决于我们用什么标准看“生命力”。</p></article><article><span>03</span><h3>今天没有单一版本的 Quakerism</h3><p>programmed / unprogrammed、evangelical / conservative / liberal 等传统在神学、牧者角色、敬拜形式与社会议题上差异显著。</p></article></section>
<section class="timeline-section"><div class="timeline-v2">
<div class="time-item"><time>1640s</time><span class="timeline-node"></span><div class="timeline-card"><h3>Seekers 与英格兰宗教动荡</h3><p>内战、宗教权威危机与大量激进宗教群体，为“直接经验是否可能超越既有制度”提供了历史土壤。George Fox 的寻找并非凭空发生，而是在一个普遍质疑既有教会形式的时代中成熟。</p><div class="timeline-tag">背景：authority crisis</div></div></div>
<div class="time-item"><time>1652</time><span class="timeline-node"></span><div class="timeline-card"><h3>从个人寻找变成运动</h3><p>Brinton 把 1652 视为关键节点：Fox 在英格兰西北遇到大量 Seekers，信息迅速扩散。早期 Friends 的突破不是发明“安静聚会”，而是把直接启示、共同敬拜、先知式行动与群体生活连在一起。</p><div class="timeline-tag">experience → movement</div></div></div>
<div class="time-item"><time>1650s–1670s</time><span class="timeline-node"></span><div class="timeline-card"><h3>Meeting 从灵性事件变成可持续共同体</h3><p>迫害、救济、婚姻、旅行 ministry、财务与纪律迫使 Friends 建立稳定组织。这里出现了一个重要转折：如果每个人都有直接引领，共同体如何检验引领、承担责任，又不重新制造教阶？Meeting for Business 的精神由此逐渐成熟。</p><div class="timeline-tag">charisma → discipline</div></div></div>
<div class="time-item"><time>1681–1701</time><span class="timeline-node"></span><div class="timeline-card"><h3>Pennsylvania：把宗教自由带进政治实验</h3><p>William Penn 获得 Pennsylvania 特许后，Friends 的问题不再只是“如何在迫害中保持忠实”，也变成“如果有机会治理，一个强调良知与平等的传统会怎样设计公共生活？”这段历史既包含宗教宽容的实验，也包含殖民扩张必须被重新审视的复杂性。</p><div class="timeline-tag">liberty · governance · colony</div></div></div>
<div class="time-item"><time>1700s</time><span class="timeline-node"></span><div class="timeline-card"><h3>Quietism、保存与内在纪律</h3><p>外在扩张减弱，静默、谨慎、plainness 与共同体边界受到更多重视。Brinton 不愿简单把这一时期视作“衰退”；他更关注形式变化是否仍保存原始目的。这一争论至今仍影响我们怎样评价制度化与灵性活力。</p><div class="timeline-tag">consolidation</div></div></div>
<div class="time-item"><time>1720–1772</time><span class="timeline-node"></span><div class="timeline-card"><h3>John Woolman：当 inward leading 变成生活伦理</h3><p>Woolman 的反奴隶制见证不是一次“立场表态”，而是长期旅行、劝说、消费选择与自我检验的过程。他把一个重要问题留给后来的 Friends：一份 leading 如何经过时间与共同体检验，最终改变生活方式与公共见证？</p><div class="timeline-tag">leading → witness</div></div></div>
<div class="time-item"><time>1800s</time><span class="timeline-node"></span><div class="timeline-card"><h3>分裂、福音派与多种 Quaker 形态</h3><p>十九世纪 Friends 内部发生重大分歧，福音派、理性主义、传统主义等力量重新排列。不同地区逐渐发展出 programmed / pastoral 与 unprogrammed 等明显不同的敬拜与组织形态。</p><div class="timeline-tag">plural traditions</div></div></div>
<div class="time-item"><time>1900–1930s</time><span class="timeline-node"></span><div class="timeline-card"><h3>现代重新解释：历史、教育与社会见证</h3><p>现代 Friends 开始系统重读自身传统。Rufus Jones 等人推动神秘主义研究；Pendle Hill 于 1930 年成立，成为学习、静修与实验性 Quaker life 的重要场域。Meeting 不再只被解释为宗派礼仪，也被重新思考为教育、共同体与社会行动的来源。</p><div class="timeline-tag">retrieval & experiment</div></div></div>
<div class="time-item"><time>1950s</time><span class="timeline-node"></span><div class="timeline-card"><h3>布林顿：把贵格会理解为“方法”与“群体神秘主义”</h3><p>Howard Brinton 用“method”而不是固定教义体系来理解 Quakerism，并以“group mysticism”说明它既是 inward experience，也是社会性、共同体性的宗教实践。这一框架对今天理解 Meeting 仍极有解释力。</p><div class="timeline-tag">method, not mere form</div></div></div>
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
<tr><th>共识（Consensus）</th><td>可接受的共同方案</td><td>协商差异</td><td>带领者管理过程</td><td>达成一致</td><td>聚会的共同辨识追求的是可被群体辨认和承担的合一／合宜性，而不只是“大家都能接受”</td></tr>
<tr><th>Coaching</th><td>来访者目标与行动</td><td>通常一对一</td><td>coach 负责提问框架</td><td>清晰、行动、成长</td><td>澄心会避免以绩效目标或教练关系为中心</td></tr>
<tr><th>Group Therapy</th><td>心理健康与关系模式</td><td>治疗性互动</td><td>受训治疗师</td><td>治疗与功能改善</td><td>Meeting 不是临床治疗，不以诊断或心理病理为框架</td></tr>
<tr><th>Circle of Trust</th><td>Inner Teacher / soul / wholeness</td><td>用 touchstones 保护灵魂出现</td><td>facilitator 设计条件</td><td>wholeness、integrity</td><td>受 Quaker 影响，但结构更显性，且常使用第三物与特定 touchstones</td></tr>
<tr><th>Bohm Dialogue</th><td>collective thought process</td><td>观察思维如何共同生成</td><td>较弱中心</td><td>看见假设、整体性</td><td>哲学基础不同；Quaker Meeting 有更明确的 spiritual discernment 传统</td></tr>
</tbody></table></div></section>
<section class="content-section"><div class="section-head"><span>HOW TO CHOOSE</span><h2>什么场景更适合用什么？</h2></div><div class="scenario-grid"><article><span>需要临床支持</span><h3>优先心理治疗 / 医疗</h3><p>不要把 Meeting 或澄心会当治疗替代品。</p></article><article><span>要训练注意与减压</span><h3>Mindfulness 更直接</h3><p>Meeting 不承诺把“平静”作为输出。</p></article><article><span>团队要快速做可逆决定</span><h3>普通决策机制更高效</h3><p>并非所有事情都值得进入深度 corporate discernment。</p></article><article><span>价值冲突、使命方向、重大共同体议题</span><h3>Meeting for Business 值得尝试</h3><p>尤其当“赢得辩论”会伤害共同体时。</p></article><article><span>一个人面对重要人生选择</span><h3>澄心会可提供独特空间</h3><p>前提是问题不属于需要专业危机处理的范畴。</p></article><article><span>深度共读、教育、团队学习</span><h3>Meeting for Learning 很合适</h3><p>第三物 + 静默 + 经验检验，会改变普通讨论结构。</p></article></div></section>
<section class="content-section"><div class="section-head"><span>FALSE FRIENDS</span><h2>最容易“看起来很像”，其实差异最大的三组</h2></div><div class="false-friends"><article><h3>Meeting ≠ Meditation group</h3><p>两者都可能安静，但 Meeting 的单位不是“很多个正在练习的个人”，而是一个正在共同等待的群体。个体注意力训练可以发生，却不是全部。</p></article><article><h3>Sense of the Meeting ≠ Consensus</h3><p>两者都避免简单多数压制，但 consensus 常以“大家都能接受”为目标；Quaker practice 更关心群体是否辨认到一个可以被承担的 rightness / unity。</p></article><article><h3>Clearness ≠ Coaching</h3><p>两者都使用提问，但澄心会不以目标达成、绩效或行动计划为中心；它更严格地限制 advice，并给沉默与 spiritual discernment 更大位置。</p></article></div></section>
<section class="content-section"><div class="research-card"><span>比较方法</span><h3>不要问“哪个方法最好”，先问“它在解决什么问题”</h3><div><p>一个方法是否合适，取决于问题类型、风险、权力结构、时间尺度与参与者期待。Meeting 的优势在于处理那些不能只靠信息和偏好解决的价值性问题；它的弱点也同样明显：慢、依赖群体成熟度、容易被隐形权力伪装成“灵性共识”。</p></div></div></section>
<section class="content-section"><div class="research-card"><span>把镜头拉远</span><h3>不只比较现代方法，也把贵格会放回人类的“会聚传统”</h3><div><p>苏菲记念、禅宗坐禅、犹太同伴研习、吠檀多真理共聚、锡克圣众与东正教静修，都提供了不同答案：一群人为什么聚在一起？共同中心在哪里？权威如何被约束？实践怎样回到生活？</p><p><a class="text-link" href="traditions.html">进入「会聚传统与 AI 时代」专题 →</a></p></div></div></section>
<section class="content-section">''' + query_cards(['我是否因为喜欢某种方法，就急着说“其实都一样”？','我当前真正需要的是什么：疗愈、学习、决策、灵性实践、关系修复，还是行动？','一个方法的边界在哪里？什么情况应该明确转介给更合适的专业？']) + '''</section>
'''
pages['comparisons.html'] = page_shell('comparisons.html','Meeting 与其他方法，有何异同？','不要把所有“安静、倾听、圆圈、提问”都混成一种东西。通过目标、权威、群体作用与成功标准，建立清楚的方法边界。',comparisons_body,label='COMPARE')

# --- gathering traditions / AI age ---
traditions_body = f'''
<section class="traditions-intro">
  <div class="traditions-intro-copy">
    <span class="kicker">跨传统会聚（ACROSS TRADITIONS）</span>
    <h2 class="semantic-title"><span>古往今来，</span><wbr><span>人类如何共同求真？</span></h2>
    <p>贵格会聚会不是人类历史上唯一把“群体”当作灵性器官的传统。苏菲的记念（dhikr）、禅宗的坐禅（zazen）、犹太传统的同伴研习（havruta）、印度传统的真理共聚（satsang）、锡克教的圣众（sadh sangat）、东正教的静修祈祷（hesychasm），都在回答相近却不相同的问题：<strong>当个人经验不够时，一群人怎样共同靠近真实、善、神圣或觉醒？</strong></p>
    <div class="curator-note"><span>比较原则</span><p>这里比较的是<strong>群体实践的结构</strong>，不是说这些传统“本质上一样”，更不是建立一条虚构的影响谱系。每一种实践都只能放回自己的神学、历史、语言与权威结构中理解。</p></div>
  </div>
  <div class="tradition-orbit" aria-label="七种会聚传统的关系示意图">
    <div class="orbit-center"><b>共同会聚</b><small>Gathering</small></div>
    <span style="--i:0">贵格会<br/><small>Meeting</small></span>
    <span style="--i:1">苏菲<br/><small>Dhikr</small></span>
    <span style="--i:2">禅宗<br/><small>Zazen</small></span>
    <span style="--i:3">犹太<br/><small>Havruta</small></span>
    <span style="--i:4">吠檀多<br/><small>Vedanta · Satsang</small></span>
    <span style="--i:5">锡克教<br/><small>Sangat</small></span>
    <span style="--i:6">东正教<br/><small>Hesychasm</small></span>
  </div>
</section>

<section class="content-section">
  <div class="section-head"><span>七扇窗口（SEVEN WINDOWS）</span><h2>{smart_heading('七种传统，不是七个版本的同一件事')}</h2><p>如果只看表面，它们都可能出现安静、围坐、诵念、老师、经文、共同体。但真正决定实践气质的，是“中心是什么、权威在哪里、群体做什么、最后如何回到生活”。</p></div>
  <div class="tradition-cards">
    <article><div class="tradition-icon">{icon('light')}</div><span>17世纪英国 · 基督教贵格会</span><h3>静默敬拜与共同明辨<br/><small>静默敬拜（Meeting for Worship）/ 明辨（Discernment）</small></h3><p>共同静默不是并排冥想，而是一起等候、聆听，并让可能出现的受感分享接受群体检验。带领角色服务于聚会，不拥有真理。</p><b>核心动作：等候 → 聆听 → 检验 → 行动</b></article>
    <article><div class="tradition-icon">{icon('group')}</div><span>伊斯兰神秘传统</span><h3>记念与苏菲圆圈<br/><small>记念（Dhikr）/ 苏菲圆圈（Sufi Circle）</small></h3><p>记念（dhikr）意为“记得并记念真主”。不同苏菲教团可能通过诵念真主之名、呼吸、诗歌、音乐、动作或静默来实践，并通常处在导师（shaykh / pir）与教团（tariqa）的传承脉络中。</p><b>核心动作：记念 → 聚焦心灵 → 归向真主</b></article>
    <article><div class="tradition-icon">{icon('silence')}</div><span>佛教 · 曹洞禅</span><h3>坐禅与僧团共修<br/><small>坐禅（Zazen）/ 僧团（Sangha）</small></h3><p>共同坐禅强调姿势、呼吸、觉照与持续练习。群体提供纪律、节奏和传承环境；它与贵格会最明显的差别，是禅有更清楚的身体方法与师承传统。</p><b>核心动作：坐 → 觉察 → 回到姿势 → 持续修行</b></article>
    <article><div class="tradition-icon">{icon('book')}</div><span>犹太学习传统</span><h3>同伴研习<br/><small>同伴研习（Havruta）/ 学习院（Beit Midrash）</small></h3><p>两人围绕文本反复诘问、争论、解释，让“另一双眼睛”打破自己的理解局限。这里的神圣共同体并不以安静为主，反而常常通过声音、分歧与文本生成理解。</p><b>核心动作：读 → 问 → 辩 → 重新理解</b></article>
    <article><div class="tradition-icon">{icon('path')}</div><span>印度 · 吠檀多（Vedanta）语境</span><h3>真理共聚<br/><small>真理共聚（Satsang）</small></h3><p>真理共聚（satsang）常包含祈祷、诵唱（bhajan）、经文学习、老师讲解与问答。它强调“与真理及寻求真理的人相伴”，群体既是学习空间，也是价值与生活方式的共同塑造。</p><b>核心动作：亲近善知识 → 学习 → 反思 → 生活化</b></article>
    <article><div class="tradition-icon">{icon('group')}</div><span>锡克教</span><h3>圣众与共同敬拜<br/><small>圣众（Sadh Sangat）</small></h3><p>圣众（Sangat）不只是“来听讲的人群”。在锡克传统中，共同诵唱古尔巴尼（Gurbani）、祈祷、聆听经文与服务（seva）彼此联结；个人修持与共同体生活不可完全分开。</p><b>核心动作：聆听经文 → 共同记念 → 服务</b></article>
    <article><div class="tradition-icon">{icon('silence')}</div><span>东方基督教</span><h3>静修与心祷<br/><small>静修传统（Hesychasm）/ 耶稣祷文（Jesus Prayer）</small></h3><p>静修传统（hesychasm）强调静止、心祷与持续祈祷，历史上深植修道与教会传统。它能帮助理解“静默不是空白”，但其祈祷结构与贵格会的群体明辨仍非常不同。</p><b>核心动作：静止 → 心祷 → 持续记念 → 与神相交</b></article>
  </div>
</section>

<section class="content-section tradition-matrix-section">
  <div class="section-head"><span>横向矩阵（HORIZONTAL MAP）</span><h2>{smart_heading('把“聚在一起”拆成六个可以比较的维度')}</h2></div>
  <div class="matrix-wrap"><table class="matrix tradition-matrix">
    <thead><tr><th>传统 / 实践</th><th>共同中心</th><th>主要媒介</th><th>群体在做什么</th><th>权威结构</th><th>从会聚走向哪里</th></tr></thead>
    <tbody>
      <tr class="accent"><th>贵格会聚会<br/><small>Quaker Meeting</small></th><td>神圣临在、内在之光、真理（不同分支语言有差异）</td><td>静默、受感分享、共同等候</td><td>共同聆听与明辨</td><td>低讲台化；书记、长老等角色服务群体</td><td>忠实行动、合一、公共见证</td></tr>
      <tr><th>苏菲记念<br/><small>Dhikr</small></th><td>真主、记念、爱的临在</td><td>诵念、呼吸、诗、音乐、动作或静默</td><td>共同记念并调谐心灵</td><td>常有导师（shaykh / pir）与教团（tariqa）传承</td><td>净化自我、爱、服务、亲近真主</td></tr>
      <tr><th>曹洞禅坐禅<br/><small>Zazen</small></th><td>修行本身、觉照、佛道</td><td>身体姿势、呼吸、坐与行禅</td><td>共同维持修行纪律与场</td><td>僧团与老师 / 法脉较明确</td><td>觉醒、日常修行、菩萨道</td></tr>
      <tr><th>犹太同伴研习<br/><small>Havruta</small></th><td>《妥拉》（Torah）、文本与解释传统</td><td>朗读、问题、争论、互相纠正</td><td>用差异深化理解</td><td>文本与传统权威 + 同伴互证</td><td>更深理解、实践、共同体记忆</td></tr>
      <tr><th>真理共聚<br/><small>Satsang</small></th><td>真理、经文、自性（Self）/ 梵（Brahman，依传统而异）</td><td>讲解、经文、诵唱（bhajan）、问答</td><td>与老师及同道共同学习</td><td>教师、导师（acharya / swami / guru）角色通常较强</td><td>内在转化、价值生活、修持</td></tr>
      <tr><th>锡克圣众<br/><small>Sadh Sangat</small></th><td>《古鲁·格兰特·萨希卜》（Guru Granth Sahib）、圣名（Naam）、神圣旨意（Hukam）</td><td>古尔巴尼（Gurbani）、赞颂（kirtan）、祈祷、服务</td><td>在圣众中共同敬拜与塑造生活</td><td>经典中心 + 圣众与潘特（Panth）</td><td>记念圣名、平等、服务（seva）、共同体责任</td></tr>
      <tr><th>东正教静修<br/><small>Hesychasm</small></th><td>基督、神的临在</td><td>静默、耶稣祷文（Jesus Prayer）、修道纪律</td><td>共同体承托个人持续祈祷</td><td>教会、修道传统与属灵指导</td><td>悔改、医治、与神相交</td></tr>
    </tbody>
  </table></div>
  <p class="fineprint">这张表是研究地图，不是神学裁判。每一行内部都存在巨大的地区、宗派、历史与当代差异；尤其苏菲主义（Sufism）、印度宗教传统与佛教本身，都不能被当成单一体系。</p>
</section>

<section class="content-section">
  <div class="section-head"><span>共同语法（COMMON GRAMMAR）</span><h2>{smart_heading('跨越差异之后，可以看见六个反复出现的人类设计')}</h2></div>
  <div class="shared-grammar">
    <article><b>01</b><h3>把“我”放回一个更大的中心</h3><p>神、真理、经典、觉醒、Naam、共同辨识——名字完全不同，但都通过某种方式限制“我的即时偏好就是答案”。</p></article>
    <article><b>02</b><h3>让身体进入认识过程</h3><p>坐姿、呼吸、诵念、步行、围坐、共同歌唱：人类传统很少把深层认识只交给抽象思考。</p></article>
    <article><b>03</b><h3>用节奏抵抗冲动</h3><p>静默、重复、仪轨、等待、轮流发言、反复读经，都在制造“不要立刻反应”的时间。</p></article>
    <article><b>04</b><h3>让另一个人纠正我的盲区</h3><p>无论是 havruta 的争论、sangha 的纪律，还是 Meeting 的 corporate testing，成熟传统都不把私人感觉自动升级为真理。</p></article>
    <article><b>05</b><h3>让传统成为“第三方”</h3><p>经典、法脉、师承、Faith & Practice、诗歌或故事，把群体从“只有我们当下的意见”连接到更长的时间轴。</p></article>
    <article><b>06</b><h3>最后必须回到生活</h3><p>如果会聚只制造舒服体验，却不改变关系、伦理、服务与行动，多数传统都会认为实践尚未完成。</p></article>
  </div>
</section>

<section class="content-section">
  <div class="section-head"><span>不要抹平差异（DO NOT COLLAPSE）</span><h2>{smart_heading('真正有价值的跨传统学习，先从“不借壳”开始')}</h2></div>
  <div class="do-not-collapse">
    <article><span>苏菲主义（Sufism）</span><h3>不要只借“旋转、鲁米、爱”</h3><p>记念（dhikr）位于伊斯兰的《古兰经》、记念真主、教团与师承语境中。把它抽成“高能量圆圈技巧”，会失去它真正的宗教骨架。</p></article>
    <article><span>禅（Zen）</span><h3>不要只借“安静地坐”</h3><p>坐禅（zazen）有身体规范、僧团秩序、法脉与佛教思想背景；它不是贵格会聚会（Meeting）的东方版本。</p></article>
    <article><span>同伴研习（Havruta）</span><h3>不要把争论误解为不够灵性</h3><p>有些传统通过安静认识，有些通过高密度的问答与争论认识。声音的多少并不是深度的通用指标。</p></article>
    <article><span>真理共聚（Satsang）</span><h3>不要忽略老师与传承的不对称</h3><p>许多真理共聚（satsang）的结构比贵格会聚会（Quaker Meeting）更明确地围绕老师与教法组织；这既可能带来传承深度，也带来权力与依赖问题。</p></article>
  </div>
</section>

<section class="ai-era">
  <div class="ai-era-head">
    <span>未来会聚（FUTURE GATHERING）</span>
    <h2 class="semantic-title"><span>机器越来越会说话，</span><wbr><span>人类为何还要相聚？</span></h2>
    <p>AI 可以在几秒钟内总结经典、模拟争论、生成祷词、提出问题、归纳“群体共识”。这恰恰让一个更古老的问题重新变得尖锐：<strong>哪些事情可以交给机器，哪些必须由有身体、会受伤、要承担后果的人亲自完成？</strong></p>
  </div>
  <div class="ai-rings">
    <div class="ai-ring ai-ring-outer"><span>AI 可以协助<br/><small>研究 · 翻译 · 检索 · 记录 · 无障碍</small></span>
      <div class="ai-ring ai-ring-middle"><span>AI 只能在旁<br/><small>提问 · 显示差异 · 提醒遗漏</small></span>
        <div class="ai-ring ai-ring-center"><strong>人类共同中心</strong><small>临在 · 静默 · 良知 · 责任 · 关系</small></div>
      </div>
    </div>
  </div>
</section>

<section class="content-section">
  <div class="section-head"><span>人类核心（HUMAN CORE）</span><h2 class="semantic-title"><span>人工智能越强，</span><wbr><span>人类更要保留“慢能力”</span></h2></div>
  <div class="human-core-grid">
    <article><span>01</span><h3>未经优化的静默</h3><p>没有提示词、没有下一句建议、没有自动总结。人必须承受“不知道接下来会发生什么”。</p></article>
    <article><span>02</span><h3>身体共在</h3><p>一张脸的迟疑、呼吸变慢、房间里的紧张与温度，不只是“待处理信号”，而是关系本身的一部分。</p></article>
    <article><span>03</span><h3>真正的分歧</h3><p>AI 很擅长把差异压成漂亮摘要；人类共同体需要练习让冲突仍然存在，同时不把彼此逐出关系。</p></article>
    <article><span>04</span><h3>不可外包的良知</h3><p>“模型建议这样做”不能成为道德免责条款。决定影响谁，谁就必须进入责任链。</p></article>
    <article><span>05</span><h3>有代价的承诺</h3><p>真正的 minute、vow、leading 或 concern 最后要有人用时间、金钱、名誉与生活去承担。</p></article>
    <article><span>06</span><h3>代际记忆</h3><p>AI 可以检索传统，但不能替一个共同体活过它的历史。传统不是数据库，而是被实践、争论和修正过的记忆。</p></article>
  </div>
</section>

<section class="content-section">
  <div class="section-head"><span>人工智能使用边界</span><h2>{smart_heading('让 AI 做“第三物”，不要让它坐上“内在导师”的位置')}</h2><p>一个简单原则：AI 可以增加材料、可见性与可访问性，却不应被赋予最后的属灵权威、关系权威或道德责任。</p></div>
  <div class="ai-boundary-grid">
    <article class="ai-yes"><span>可以积极使用</span><h3>外圈辅助</h3><ul><li>跨语言翻译与术语比对</li><li>史料检索、时间线与来源导航</li><li>会前事实整理与多视角资料包</li><li>经明确同意后的行政记录</li><li>为听障、视障等提供无障碍支持</li></ul></article>
    <article class="ai-caution"><span>只能谨慎使用</span><h3>反照与提问</h3><ul><li>指出群体可能遗漏的观点</li><li>生成开放问题供人重新筛选</li><li>比较不同措辞隐藏的假设</li><li>帮助回顾过程，但不替代人的记忆</li><li>任何总结必须回到现场参与者验证</li></ul></article>
    <article class="ai-no"><span>应设明确红线</span><h3>不可外包</h3><ul><li>让 AI 判定某人是否“真的有 leading”</li><li>自动宣布聚会已形成 unity</li><li>未经同意录音、转写或推断情绪</li><li>把澄心会等高度私密内容上传公共模型</li><li>用生成式权威冒充神谕、老师或 Clerk</li></ul></article>
  </div>
</section>

<section class="content-section">
  <div class="section-head"><span>面向未来（PROTOCOL 2035）</span><h2>{smart_heading('一个 AI 时代 Meeting 可以怎样设计？')}</h2></div>
  <div class="future-protocol">
    <article><b>01</b><h3>先有人，再有工具</h3><p>开场先共同到场与静默，AI 不参与前几分钟，不用屏幕替代彼此的脸。</p></article>
    <article><b>02</b><h3>把 AI 使用说出来</h3><p>谁调用了什么模型、输入了什么资料、输出会保存多久，都成为显性伦理契约。</p></article>
    <article><b>03</b><h3>先让差异完整出现</h3><p>禁止一开始就让 AI “总结共识”。先保护少数意见、异议和还未成形的语言。</p></article>
    <article><b>04</b><h3>AI 只提供候选，不宣布答案</h3><p>它可以生成三个版本、指出遗漏、追溯来源；最终判断与措辞必须由群体承担。</p></article>
    <article><b>05</b><h3>保留一段无机器时间</h3><p>重大价值议题至少有一段完全离线、无转写、无建议的共同静默。</p></article>
    <article><b>06</b><h3>结束时回到责任人</h3><p>每个行动都回答：谁决定？谁承担？谁受影响？何时复盘？不能写“由 AI 建议”。</p></article>
  </div>
  {research_note('继往开来，不是把古老形式数字化','''<p>更深的方向，是把不同传统几百上千年积累的<strong>注意、节制、师承、互证、共同体、伦理与行动</strong>重新理解成 AI 时代的“人类基础设施”。机器越擅长生成语言，人类越需要保存那些不能靠生成完成的能力：等待、承担、关系、身体、良知与共同生活。</p>''')}
</section>

<section class="content-section tradition-sources">
  <div class="section-head"><span>研究线索（RESEARCH TRAIL）</span><h2>继续查证，而不是停在漂亮类比</h2><p>以下链接用于核对各传统自己的表述；贵格会部分继续以本站研究室中的 Brinton、Loring、Palmer 等原典为主。</p></div>
  <div class="source-link-grid">
    <a href="https://pluralism.org/remembrance-of-god-the-sufi-circle" target="_blank" rel="noopener"><b>苏菲记念（Dhikr）</b><span>哈佛多元主义项目（Harvard Pluralism Project）</span></a>
    <a href="https://www.sotozen.com/eng/zazen/howto/" target="_blank" rel="noopener"><b>曹洞禅坐禅（Zazen）</b><span>曹洞宗国际网站（Soto Zen）</span></a>
    <a href="https://www.myjewishlearning.com/article/havruta-learning-in-pairs/" target="_blank" rel="noopener"><b>同伴研习（Havruta）</b><span>犹太学习网（My Jewish Learning）</span></a>
    <a href="https://www.chinmayamission.com/global/chinmaya-mission-satsang" target="_blank" rel="noopener"><b>真理共聚（Satsang）</b><span>钦马亚灵修组织（Chinmaya Mission）</span></a>
    <a href="https://sgpc.net/sadh-sangat/" target="_blank" rel="noopener"><b>锡克圣众（Sadh Sangat）</b><span>锡克教中央管理机构（SGPC）</span></a>
    <a href="https://www.goarch.org/-/did-you-know-sunday-of-saint-gregory-palamas" target="_blank" rel="noopener"><b>静修祈祷（Hesychasm）</b><span>希腊正教总教区（Greek Orthodox Archdiocese）</span></a>
    <a href="https://www.unesco.org/zh/artificial-intelligence/recommendation-ethics" target="_blank" rel="noopener"><b>人工智能伦理</b><span>联合国教科文组织（UNESCO）</span></a>
  </div>
</section>

<section class="content-section">''' + query_cards([
  '如果把贵格会聚会（Meeting）放进世界会聚传统中，哪些特征会突然显得不再理所当然？',
  '我的群体最需要从哪个传统学习：静默、记念、文本争辩、身体纪律、共同服务，还是师承？为什么？',
  '如果明天所有 AI 工具都消失，我们的共同体还剩下哪些真正属于人的能力？'
]) + '''</section>
'''
pages['traditions.html'] = page_shell(
    'traditions.html',
    '人类聚在一起，如何寻找真实？',
    '从贵格会聚会、苏菲记念、禅宗坐禅、犹太同伴研习、吠檀多（Vedanta）真理共聚、锡克圣众到东正教静修：横向比较古往今来的会聚传统，并追问 AI 时代人类必须继续亲自承担什么。',
    traditions_body,
    label='会聚传统（GATHERING TRADITIONS）'
)

# --- China context / cultural integration ---
china_body = f'''
<section class="china-intro">
  <div class="china-intro-copy">
    <span class="kicker">中国语境（CHINA CONTEXT）</span>
    <h2 class="semantic-title"><span>不是把 Meeting “中国化”，</span><wbr><span>而是让传统彼此相遇。</span></h2>
    <p>如果只是把“静默”等同于禅，把“内在之光”等同于良知或佛性，把“合一”等同于和为贵，表面上很亲切，实际上会同时误读两边。更有生命力的做法，是先问：<strong>中国文化里，哪些长期实践也在训练人放慢、反省、倾听差异、共同求真，并把认识落实到生活？</strong></p>
    <div class="china-principle"><b>本页的整合原则</b><p>找<strong>结构上的共鸣</strong>，保留<strong>思想上的差异</strong>，最后才进入<strong>当代实践的再设计</strong>。</p></div>
  </div>
  <div class="china-bridge-visual" aria-label="贵格会传统与中国文化的对话示意图">
    <div class="china-side china-side-left"><span>贵格会</span><b>Meeting</b><small>等候 · 群体明辨 · 见证</small></div>
    <div class="china-bridge-center"><span>共同问题</span><strong>怎样共同<br/>靠近真实？</strong><small>注意 · 关系 · 辨识 · 行动</small></div>
    <div class="china-side china-side-right"><span>中国传统</span><b>修身与会聚</b><small>慎独 · 心斋 · 和而不同 · 会讲</small></div>
  </div>
</section>

<section class="content-section">
  <div class="section-head"><span>六条文化桥梁（SIX BRIDGES）</span><h2>{smart_heading('真正值得连接的，不是名词，而是修习结构')}</h2><p>以下六条线索并不是说“贵格会早就在中国出现过”，而是帮助中国读者从自己熟悉的思想资源出发，理解 Meeting 中那些不容易被现代“会议文化”看见的部分。</p></div>
  <div class="china-bridge-grid">
    <article><div class="tradition-icon">{icon('light')}</div><span>儒家 · 《中庸》</span><h3>慎独</h3><p>“慎独”把道德真实放在无人看见、无人监督之处。它能帮助理解 Meeting 为什么如此看重<strong>内外一致与诚信</strong>：真正的辨识不是表态正确，而是先对自己诚实。</p><b>共鸣：内在真实 · Integrity</b><em>差异：慎独首先是个人修身；Meeting 还要求个人经验进入群体检验。</em></article>
    <article><div class="tradition-icon">{icon('silence')}</div><span>道家 · 《庄子》</span><h3>心斋</h3><p>《庄子》以“虚而待物”描述一种不急于用已有成见占满心灵的状态。这与贵格会的“等候”在姿态上有明显共鸣：<strong>先腾出空间，再看什么会出现。</strong></p><b>共鸣：虚 · 等候 · 非强求</b><em>差异：心斋的哲学语境并不等于基督教贵格会的神学与祷告经验。</em></article>
    <article><div class="tradition-icon">{icon('group')}</div><span>儒家 · 《论语》</span><h3>和而不同</h3><p>“和而不同”非常适合帮助中国群体理解：关系没有破裂，不等于意见必须一致。真正的“和”，反而需要差异仍然能够存在。</p><b>共鸣：Unity ≠ Uniformity</b><em>差异：贵格会的合一（Unity）不是一般意义的和谐，而是共同明辨后形成的可承担方向。</em></article>
    <article><div class="tradition-icon">{icon('book')}</div><span>书院传统</span><h3>会讲</h3><p>从朱张会讲到鹅湖之会，书院传统里存在一种跨门户、围绕问题与经典切磋的公共学习形式。它与共学会（Meeting for Learning）都把<strong>共同探究</strong>放在单向讲授之前。</p><b>共鸣：共同求学 · 第三物</b><em>差异：Meeting for Learning 会更有意识地加入静默、经验与“第三物”的关系结构。</em></article>
    <article><div class="tradition-icon">{icon('path')}</div><span>阳明心学</span><h3>知行合一</h3><p>如果辨识只停在“我想明白了”，它还没有完成。知行合一提醒我们：真正的认识必须进入日用伦常与具体行动，这与贵格会从内在引领走向<strong>生活见证</strong>高度呼应。</p><b>共鸣：认识 → 行动 → 生活</b><em>差异：Leading、Testimony 与“良知”并非同一套概念系统。</em></article>
    <article><div class="tradition-icon">{icon('group')}</div><span>礼 · 空间 · 器物｜本站转译</span><h3>让形式承载关系</h3><p>座次、茶水、门槛、开场与收束都会悄悄告诉参与者“谁重要、谁可以说、什么时候该停”。中国文化对礼与空间的敏感，可以转化为 Meeting 的<strong>场域设计能力</strong>。</p><b>共鸣：结构塑造行为</b><em>差异：本土化设计应减少身份等级的暗示，而不是把传统尊卑秩序带回圆圈。</em></article>
  </div>
</section>

<section class="content-section">
  <div class="section-head"><span>不要强行等同（FALSE EQUIVALENCE）</span><h2>{smart_heading('越是看起来相像的词，越需要保留边界')}</h2></div>
  <div class="china-not-equal">
    <article><b>内在之光 ≠ 佛性 / 良知</b><p>这些概念都可能触及“人里面有可被信任的深层资源”，但历史、神学和修行结构不同。中文表达可以互相照明，不能互相替代。</p></article>
    <article><b>静默敬拜 ≠ 禅坐 / 静坐</b><p>都可能安静，但贵格会静默敬拜的单位是一个正在共同等候的群体，不只是许多个正在做个人修习的人。</p></article>
    <article><b>合一 ≠ 一团和气</b><p>真正的合一有时会让分歧更清楚，而不是更快消失。若“为了和气”不敢说出关键差异，反而离共同明辨更远。</p></article>
    <article><b>书记 ≠ 主持人 / 领导</b><p>书记（Clerk）不是替大家下结论的人，而是照看过程、倾听群体并尝试写出已经形成的共同辨识。</p></article>
    <article><b>受感分享 ≠ 轮流发言</b><p>不是每个人都必须说，也不是“每人两分钟”。沉默本身可能是完整参与；说话需要经过内在辨识。</p></article>
    <article><b>澄心会 ≠ 劝导 / 心理咨询</b><p>澄心会通过开放问题与静默帮助焦点人自己听清，不替对方做决定，也不承担心理治疗与危机干预功能。</p></article>
  </div>
</section>

<section class="china-tension-section">
  <div class="section-head"><span>文化张力（CULTURAL TENSIONS）</span><h2>{smart_heading('落到中国群体里，真正困难的往往不是“不会静默”')}</h2><p>更难的是我们已经非常熟练的关系习惯：尊长、面子、求和、给建议、追效率，以及默认记录一切的数字生活。好的本土化不是批评这些习惯，而是为不同需要重新设计容器。</p></div>
  <div class="china-tension-grid">
    <article><span>01 · 尊长 / 职位</span><h3>有权威的人一开口，其他人就很难再自由表达</h3><p><strong>设计回应：</strong>发起人、老师、管理者尽量最后发言；书记与主持角色轮换；重大议题先静默或先书写，再进入口头交流。</p></article>
    <article><span>02 · 面子 / 体面</span><h3>“别让关系难看”容易压过真实</h3><p><strong>设计回应：</strong>只说自己的经验，不解释别人；明确保密；禁止会后追问“你刚才为什么那样说”。</p></article>
    <article><span>03 · 和为贵</span><h3>和谐有时被误用成“不要有不同意见”</h3><p><strong>设计回应：</strong>把“和而不同”写进规则；书记必须主动询问是否仍有重要保留；允许“尚未清晰”成为合法结果。</p></article>
    <article><span>04 · 建议冲动</span><h3>很多群体容易从倾听滑向替别人解决问题</h3><p><strong>设计回应：</strong>澄心会与深度聆听场景采用“只提开放问题、不建议”；想给建议时先问对方是否需要。</p></article>
    <article><span>05 · 效率压力</span><h3>静默常被体验成“浪费时间”</h3><p><strong>设计回应：</strong>先用 3–5 分钟可预期的短静默；用清晰钟声和时间标记建立安全感，再逐渐延长。</p></article>
    <article><span>06 · 数字默认</span><h3>录音、转写、AI 总结正在变成会议的默认动作</h3><p><strong>设计回应：</strong>深度会聚默认不录音；如需 AI 或转写，必须事先说明用途、保存期限与谁可访问，并保留一段完全无机器的时间。</p></article>
  </div>
</section>

<section class="content-section">
  <div class="section-head"><span>当代中国的八个场景（USE CASES）</span><h2>{smart_heading('Meeting 不必先进入宗教场所，也可以从真实生活的问题开始')}</h2><p>以下不是把所有问题都交给 Meeting，而是指出那些“仅靠信息、辩论和投票不够”的场景。</p></div>
  <div class="china-use-grid">
    <article><span>城市社区</span><h3>邻里议题与共同生活</h3><p>适合：公共空间、共享规则、共同项目等价值性议题。<br/><b>可用：简化议事会 + 共同明辨。</b></p></article>
    <article><span>成人学习 / 书院</span><h3>经典不只读懂，还要照见经验</h3><p>围绕一段文本、诗歌、案例或影像，加入静默、二人对谈与全体回应。<br/><b>可用：共学会。</b></p></article>
    <article><span>学校与教师团队</span><h3>从“教学技术”回到教育使命</h3><p>适合处理“我们究竟想保护什么样的学习”这类不能只靠绩效数据回答的问题。<br/><b>可用：共学会 + 澄心式提问。</b></p></article>
    <article><span>组织与企业</span><h3>使命、价值冲突与重大方向</h3><p>不是替代所有管理决策，而是用于高价值、高不确定、需要长期承担的议题。<br/><b>可用：议事会。</b></p></article>
    <article><span>家庭与代际</span><h3>重要选择前，先让彼此真正出现</h3><p>尤其适合成年家庭成员面对照护、迁居、教育、职业选择等重大变化。<br/><b>可用：短静默 + 轮流聆听。</b></p></article>
    <article><span>人生转折</span><h3>职业、关系、去留与使命选择</h3><p>当事人不是缺建议，而是需要把自己的声音从众多期待里分辨出来。<br/><b>可用：澄心会。</b></p></article>
    <article><span>公益 / 志愿者</span><h3>让价值与行动重新接上</h3><p>帮助群体在疲惫、分歧或使命漂移时重新辨认“我们为何还在这里”。<br/><b>可用：静默等候 + 议事会。</b></p></article>
    <article><span>线上 / AI 混合群体</span><h3>在高连接中保留真正的临在</h3><p>显性约定静默、离屏、隐私与 AI 边界，让工具服务会聚，而不是占据中心。<br/><b>可用：线上共学会 / 共同明辨。</b></p></article>
  </div>
</section>

<section class="china-prototype">
  <div class="section-head"><span>一场可以直接试的版本（75 MINUTES）</span><h2>{smart_heading('中国语境的 75 分钟会聚实验')}</h2><p>这是一个受 Meeting for Learning 与贵格会聆听原则启发的<strong>世俗共学版本</strong>，不是 Meeting for Worship。第三物可以是一首诗、一段经典、一幅画、一个真实案例，或一小段纪录片。</p></div>
  <div class="china-protocol">
    <article><b>00–05</b><div><span>入场</span><h3>茶、水、手机收起</h3><p>说明保密、非评判、可沉默、不强迫分享。</p></div></article>
    <article><b>05–10</b><div><span>安顿</span><h3>共同静默 5 分钟</h3><p>不播引导语，只邀请大家感受身体、呼吸与此刻。</p></div></article>
    <article><b>10–20</b><div><span>第三物</span><h3>一起读 / 看一个对象</h3><p>例如《庄子》一段、鲁迅一页、Mary Oliver 一首诗或一个现实案例。</p></div></article>
    <article><b>20–32</b><div><span>二人</span><h3>一人说，一人只听</h3><p>每人 5 分钟，中间留一分钟静默；不追问、不点评。</p></div></article>
    <article><b>32–52</b><div><span>圆圈</span><h3>只说此刻真正重要的</h3><p>不用轮流；每次发言后留一点空白，让话落地。</p></div></article>
    <article><b>52–60</b><div><span>再静默</span><h3>我们遗漏了什么？</h3><p>从“我怎么看”转向“这个群体正在看见什么”。</p></div></article>
    <article><b>60–70</b><div><span>明辨</span><h3>形成一句共同认识</h3><p>不追求漂亮共识；可以写成“我们已经看清……”或“我们仍未看清……”。</p></div></article>
    <article><b>70–75</b><div><span>返回生活</span><h3>一件愿意承担的小行动</h3><p>不做宏大承诺，只说下一步具体、可验证的行动。</p></div></article>
  </div>
</section>

<section class="content-section">
  <div class="section-head"><span>本土化原则（LOCALIZATION）</span><h2>{smart_heading('真正的“中国版本”，应该越来越少依赖带领者')}</h2></div>
  <div class="china-local-grid">
    <article><b>01</b><h3>译功能，不只译名词</h3><p>“Clerk”为什么不是主持人？“Unity”为什么不是共识？先把实践功能说清，再决定中文。</p></article>
    <article><b>02</b><h3>保留共同中心</h3><p>根据场景如实命名共同中心，可以使用“真实、良知、神圣、上帝”等不同语言，但不要把它们当作同义词，更不能把中心退化成“大家舒服就好”。</p></article>
    <article><b>03</b><h3>结构保护弱声音</h3><p>让职位高的人晚说，让慢的人有时间，让“不知道”与“不认同”都能留下来。</p></article>
    <article><b>04</b><h3>静默要被命名</h3><p>不要突然“大家安静一下”。说明为什么静默、多久、如何结束，陌生参与者才有安全感。</p></article>
    <article><b>05</b><h3>第三物连接文化经验</h3><p>诗词、山水、书信、电影、现实案例都可以成为共同中心，避免一上来就直接谈自我暴露。</p></article>
    <article><b>06</b><h3>不强迫表达</h3><p>“可以不说”必须是真的。安静参与不能被解释成不投入、不开放或不合群。</p></article>
    <article><b>07</b><h3>隐私比记录更重要</h3><p>深度对话默认不录音；AI、转写和云端存储都要单独征得同意。</p></article>
    <article><b>08</b><h3>最后回到行动</h3><p>中国文化的知行传统提醒我们：一次会聚是否有生命，要看它是否改变了关系与生活。</p></article>
  </div>
</section>

<section class="china-digital-note">
  <div><span>2026 · DIGITAL CHINA</span><h2>为什么今天尤其需要“无算法的共同时间”？</h2></div>
  <p>中国互联网络信息中心 2026 年报告显示，生成式人工智能已经进入数亿人的问答、文本处理、工作总结和会议纪要等日常场景。工具越能替我们迅速组织语言，越值得刻意保留一些<strong>不被转写、不被推荐、不被立即总结</strong>的共同时间——让尚未成形的感受、少数意见和沉默也有位置。</p>
</section>

<section class="content-section tradition-sources">
  <div class="section-head"><span>中国文化研究线索（SOURCE TRAIL）</span><h2>从原典与当代资料继续往下查</h2><p>这些来源用于理解中国文化自身的语境，而不是为了给贵格会寻找“东方祖先”。</p></div>
  <div class="source-link-grid">
    <a href="https://ctext.org/text.pl?if=en&node=416604&remap=gb&show=parallel" target="_blank" rel="noopener"><b>慎独 · 《中庸》</b><span>中国哲学书电子化计划（CTP）</span></a>
    <a href="https://ctext.org/zhuangzi/man-in-the-world-associated-with" target="_blank" rel="noopener"><b>心斋 · 《庄子·人间世》</b><span>中国哲学书电子化计划（CTP）</span></a>
    <a href="https://ctext.org/text.pl?if=en&node=416808&show=parallel" target="_blank" rel="noopener"><b>和而不同 · 《论语》</b><span>中国哲学书电子化计划（CTP）</span></a>
    <a href="https://www.chinesethought.cn/shuyu_show.aspx?shuyu_id=3530" target="_blank" rel="noopener"><b>知行合一</b><span>中华思想文化术语传播工程</span></a>
    <a href="https://www.xyc.tsinghua.edu.cn/info/1061/3916.htm" target="_blank" rel="noopener"><b>会讲传统的当代延续</b><span>清华大学新雅书院</span></a>
    <a href="https://www.cnnic.cn/n4/2026/0930/c326-11690.html" target="_blank" rel="noopener"><b>生成式人工智能应用发展报告（2026）</b><span>中国互联网络信息中心（CNNIC）</span></a>
  </div>
</section>

<section class="content-section">''' + query_cards([
  '在我的群体里，最容易压住真实表达的是职位、面子、和气、效率，还是“给建议”的冲动？',
  '如果不用任何宗教术语，我怎样仍然保留 Meeting 的“共同中心”，而不是把它变成普通分享会？',
  '哪一种中国文化资源最适合成为我们下一次会聚的第三物：一段经典、一首诗、一幅画、一封信，还是一个现实案例？'
]) + '''</section>
'''

pages['china.html'] = page_shell(
    'china.html',
    '在中国，Meeting 可以长成什么样？',
    '让贵格会 Meeting 与慎独、心斋、和而不同、书院会讲、知行合一等中国文化传统认真对话，并发展出适合当代中国社区、教育、组织、家庭与线上空间的实践方法。',
    china_body,
    label='中国语境（CHINA CONTEXT）'
)

# --- glossary ---
glossary_terms = [
('Meeting','聚会／会聚','既指一次聚集，也可指长期存在的地方共同体；因此不宜一律译成日常行政语境里的“会议”。','核心'),
('Meeting for Worship','静默敬拜','非程序化传统中，以共同静默、等候，以及可能出现的受感分享为主要特征。','敬拜'),
('Waiting','等候／静默等候','不是等待时间过去，而是带着期待、开放与可被引领的姿态。','敬拜'),
('Inward Light','内在之光','贵格会核心语言之一。历史上与基督、圣灵的语言紧密相连；现代不同会友对此有不同理解。','神学'),
('That of God in everyone','每个人里面“属神的那一份”','贵格会常见表达，但历史语境与现代通俗解释并不完全相同，使用时宜保留这种复杂性。','神学'),
('Gathered Meeting','深度聚集的聚会','群体在共同静默中出现深层合一、临在或共同注意的经验；不是人为制造的“高峰状态”。','敬拜'),
('Vocal Ministry','受感分享／口头事奉','在静默中经明辨后说出的分享；不是普通讨论发言，也不是自由麦。','敬拜'),
('Leading','内在引领','一种持续推动人走向某行动或方向的内在感知，需要时间与共同体检验。','明辨'),
('Concern','内在关切','比“一时兴趣”更持续、更具责任感的召唤，可发展为行动或 witness。','明辨'),
('Discernment','明辨／辨识','分辨不同冲动、声音与可能引领的过程，既有个人层面，也有群体层面。','明辨'),
('Unity','合一','不是意见完全相同，而是群体在一个方向上形成更深的共同清晰。','议事'),
('Sense of the Meeting','聚会的共同辨识','书记与群体共同辨认“这个聚会此刻正在形成什么判断”；它不等同于普通意义上的共识。','议事'),
('Clerk','书记','不是主席。书记照看议程、节奏与决议纪要，并尝试听出整个聚会正在形成的共同辨识。','议事'),
('Minute','决议纪要／决议措辞','在贵格会议事中常于现场形成，用来记录已经被聚会认可的共同辨识。','议事'),
('Standing Aside','保留但不阻挡','个人仍有不同判断，但不认为自己的保留足以阻挡聚会继续前进；具体实践因群体而异。','议事'),
('Clearness Committee','澄心会','一小群人以开放问题、静默、保密帮助焦点人获得更清晰的辨识。','实践'),
('Query','省察问题','不是考试题，而是让个人与共同体持续检视实践与生命状态的问题。','实践'),
('Testimony','生活见证','不是抽象信条，而是从信仰实践中逐渐形成的生活方式与公共见证，例如和平、简朴与诚信。','见证'),
('Third Thing','第三物','在帕尔默的学习语境中，指连接人与人的共同对象，例如文本、诗歌、数据、案例、图像或经验。','共学'),
('Meeting for Learning','共学会','把学习理解为人与人围绕第三物共同探寻真实的过程。','共学'),
('Unprogrammed Worship','非程序化敬拜／无预设程序的敬拜','没有预先安排讲道、赞美诗或固定发言次序，以共同静默和可能出现的受感分享为主要形式。','敬拜'),
('Programmed Worship','程序化敬拜','在部分贵格会传统中，会有牧者、讲道、音乐与预先安排的礼拜结构；这并不表示它“不是真正的贵格会”。','敬拜'),
('Seasoning','酝酿／让议题成熟','让一份内在关切、提案或内在引领经历时间、祷告、讨论与共同体检验，不急于进入正式决定。','明辨'),
('Threshing Session','预备性深谈／梳理会','在正式议事决策前，充分呈现事实、感受与分歧，但通常不在此阶段形成决定。','议事'),
('Right Ordering','合宜秩序／正当安排','指角色、责任与程序服务于灵与真理，而不是单纯追求行政效率；不同传统的具体用法有所差异。','议事'),
('Holding in the Light','在光中守望／把某人放在光中','为一个人或处境保持祷告式、非操控性的关注；不是在脑中替对方设计解决方案。','实践'),
('Elder','敬拜照看者／长老性角色','历史上承担敬拜与受感分享的照看、辨识和培育；现代不同聚会是否正式设置该角色，差异很大。','共同体'),
('Faith and Practice','信仰与实践手册','许多年会编纂的传统、经验、纪律、劝勉与省察问题等文本；不同年会的版本并不相同。','共同体'),
('Advices & Queries','劝勉与省察问题','用于持续检视个人与共同体生活的劝勉和问题，不是统一教义问答。','实践'),
]
glossary_cards=''.join(f'<article class="glossary-card" data-term="{html.escape((en+cn+cat).lower())}"><span>{cat}</span><h3>{cn}</h3><h4>（{en}）</h4><p>{desc}</p></article>' for en,cn,desc,cat in glossary_terms)
glossary_body=f'''
<section class="glossary-top"><div><span class="kicker">WORDS MATTER</span><h2>很多误解，来自翻译过快</h2><p>贵格会许多术语表面上很普通，例如聚会、关切、纪要、书记、合一；但进入传统语境后，都有更具体的历史与实践含义。本站以中文主称帮助阅读，同时保留英文原词，方便继续查阅原典。</p></div><label class="search-box">搜索术语<input id="glossarySearch" type="search" autocomplete="off" placeholder="例如：合一 / unity / 澄心 / 静默" aria-describedby="glossaryStatus"/></label></section>
<section class="content-section"><div class="filter-row" role="group" aria-label="按术语类别筛选"><button class="filter active" data-filter="all" aria-pressed="true">全部</button><button class="filter" data-filter="核心" aria-pressed="false">核心</button><button class="filter" data-filter="敬拜" aria-pressed="false">敬拜</button><button class="filter" data-filter="明辨" aria-pressed="false">明辨</button><button class="filter" data-filter="议事" aria-pressed="false">议事</button><button class="filter" data-filter="实践" aria-pressed="false">实践</button><button class="filter" data-filter="共学" aria-pressed="false">共学</button><button class="filter" data-filter="神学" aria-pressed="false">神学</button><button class="filter" data-filter="共同体" aria-pressed="false">共同体</button><button class="filter" data-filter="见证" aria-pressed="false">见证</button></div><div class="glossary-status"><span id="glossaryStatus" aria-live="polite"></span><button id="clearGlossary" type="button">清除筛选</button></div><div class="glossary-grid" id="glossaryGrid">{glossary_cards}</div><div class="glossary-empty" id="glossaryEmpty">没有找到相符术语。可以换一个关键词，或清除筛选后再看。</div></section>
<section class="content-section"><div class="section-head"><span>HOW TO READ</span><h2>{smart_heading('术语不是“对照表”，而是一张传统内部的关系网')}</h2></div><div class="term-relations"><article><b>等候 → 受感分享</b><small>Waiting → Ministry</small><p>先有等候，才谈得上受感分享；否则受感分享很容易退化成自由发言。</p></article><article><b>内在引领 → 酝酿 → 检验</b><small>Leading → Seasoning → Testing</small><p>引领不是立即执行的冲动；它需要时间、共同体与生活后果的检验。</p></article><article><b>合一 → 聚会的共同辨识 → 决议纪要</b><small>Unity → Sense of the Meeting → Minute</small><p>合一不是“大家都一样想”，而是在足够清晰时形成可被书写和承担的共同方向。</p></article><article><b>内在之光 → 生活见证 → 公共见证</b><small>Inner Light → Testimony → Witness</small><p>内在之光若只停在体验层面，就会失去贵格会传统强调的伦理与公共行动维度。</p></article></div></section>
<section class="content-section">{callout('翻译原则','<p>本站优先“先懂后译”：先确认词在贵格会实践中的功能，再选择中文。对于 <em>Meeting、Clerk、Sense of the Meeting</em> 这类一译就容易误导的词，宁可中英并列。</p>')}</section>
'''
pages['glossary.html']=page_shell('glossary.html','Quaker Meeting 术语表','从 Meeting、Waiting、Inward Light 到 Clerk、Unity、Sense of the Meeting：用准确而不僵硬的中文建立一张概念地图。',glossary_body,label='GLOSSARY')

# --- research ---
research_body = '''
<section class="research-intro"><div><span class="kicker">SOURCE-BASED · NOT QUOTE-MINING</span><h2>本站怎样做研究？</h2><p>不是先有一个“现代灵性”的结论，再去贵格会文献里找漂亮句子。我们尽量把概念放回历史、实践与作者自己的问题意识中：一个词在什么时候出现？解决了什么问题？后来如何变化？今天又有哪些不同解释？</p></div></section>
<section class="content-section visual-method"><div class="section-head"><span>VISUAL SOURCES</span><h2>图像也要像文本一样被校对</h2><p>研究型网站不能把历史图片当“气氛素材”。我们会问：图像什么时候制作？是同时代记录、后世艺术想象，还是现代建筑照片？谁拥有版权？它能支持什么判断，又不能支持什么判断？</p></div>
''' + exhibit_pair(
  exhibit_figure('assets/curated/george-fox.jpg','SOURCE TYPE · PORTRAIT','George Fox：一张带着限定词的肖像','Commons 将这幅 1677 年图像标为“Supposed portrait”。这意味着它具有同时代价值，却仍不应被写成“这就是 Fox 的确定长相”。','Egbert van Heemskerk（归属）',VISUAL_SOURCES['fox'],'Public domain','compact'),
  exhibit_figure('assets/curated/margaret-fell.jpg','SOURCE TYPE · LATER IMPRESSION','玛格丽特·费尔：后世如何想象一位早期会友','这幅形象来自后世蚀刻。它适合研究 Margaret Fell 在后世记忆中的视觉形象，却不能被当作十七世纪现场肖像。','Robert Spence engraving',VISUAL_SOURCES['fell'],'Public domain','compact')
) + '''<div class="curator-note"><span>PROVENANCE</span><p>因此，本站图说会把“作者 / 年代 / 授权 / 不确定性”尽可能留在图片旁边，而不是把来源藏到页面最底部。<a href="visual-credits.html">查看全站图像与史料说明 →</a></p></div></section>
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
<section class="content-section"><div class="section-head"><span>RESEARCH ROADMAP</span><h2>后续研究专题</h2></div><div class="roadmap-list"><article><b>等候主（Waiting upon the Lord）</b><p>福克斯、巴克莱、静默主义、布林顿与现代自由派贵格会的语言变迁。</p></article><article><b>深度聚集的聚会（Gathered Meeting）</b><p>历史见证、鲁弗斯·琼斯与布林顿、群体心理学及宗教经验研究。</p></article><article><b>聚会的共同辨识（Sense of the Meeting）</b><p>历史实践、现代共识理论、组织治理与冲突转化。</p></article><article><b>内在之光（Inner Light）</b><p>基督论式、神秘主义式、人文主义式、普世主义式等不同解释路线。</p></article><article><b>贵格会与心理学（Quakerism & Psychology）</b><p>荣格、贵格会宗教与心理学会议、澄心会与现代心理治疗边界。</p></article><article><b>从聚会到信任圈（From Meeting to Circle of Trust）</b><p>帕克·帕尔默如何把贵格会传统基因转译成适用于教育、领导力与公共生活的实践。</p></article></div></section>
<section class="content-section"><div class="section-head"><span>READING PATHS</span><h2>三条进阶阅读路径</h2></div><div class="reading-trails"><article><span>A · Meeting 的骨架</span><p>Brinton → Jim Pym → Patricia Loring</p><small>先理解 worship / ministry / business / community，再进入现代 discernment。</small></article><article><span>B · Inner Light 的深处</span><p>Thomas Kelly → Michael Marsh → Inward Light</p><small>从实践语言进入哲学与心理学争论，避免把 Light 口号化。</small></article><article><span>C · 从 Quaker 到公共实践</span><p>Parker Palmer → Clearness → Circle of Trust</p><small>观察传统如何被转译到教育、领导力、组织与个人生命。</small></article></div></section>
<section class="content-section"><div class="research-note"><h2>一个重要提醒</h2><p>“贵格会”不是单一、静态、完全一致的传统。不同 Yearly Meetings、programmed / unprogrammed、evangelical / conservative / liberal 等分支，在基督论、圣经、牧师制度、敬拜形式和社会议题上可以有很大差异。本站当前版本以<strong>unprogrammed Meeting、Pendle Hill 传统与相关现代作者</strong>为主要研究入口，并会持续标注这一视角的边界。</p></div></section>
'''
pages['research.html']=page_shell('research.html','Quaker Meeting 研究室','原典、思想史、实践谱系与研究方法。这里不仅给“结论”，也尽量让你知道结论从哪里来、有哪些不同解释。',research_body,label='RESEARCH')

# --- visual credits / provenance ---
visual_credits_body = f'''
<section class="credits-intro"><div><span class="kicker">PROVENANCE · LICENSE · UNCERTAINTY</span><h2>{smart_heading('每一张历史图片，都应该知道自己从哪里来')}</h2><p>本站把图片分成三类：历史图像、现代地点/建筑照片、解释性图解。历史图像会尽量说明它是否同时代、是否属于后世艺术家印象；现代照片则保留作者与授权。图像帮助理解，但不替代原典。</p></div></section>
<section class="content-section"><div class="credits-grid">
{exhibit_figure('assets/curated/george-fox.jpg','PORTRAIT · 1677','George Fox（被认为是同时代肖像）','维基共享资源将此图标为“推定肖像”（Supposed portrait），并注明 1677 年。本站保留这个限定语，不把归属不确定性抹掉。','Egbert van Heemskerk（归属）',VISUAL_SOURCES['fox'],'Public domain','credit')}
{exhibit_figure('assets/curated/margaret-fell.jpg','LATER IMPRESSION','Margaret Fell','Robert Spence 的蚀刻细节，属于后世艺术形象，不是十七世纪写生肖像。','Robert Spence',VISUAL_SOURCES['fell'],'Public domain','credit')}
{exhibit_figure('assets/curated/william-penn.jpg','PORTRAIT · 1695','William Penn','Francis Place 1695 年粉笔肖像；来源页称其为已知唯一一幅在 Penn 生前写生的肖像。','Francis Place',VISUAL_SOURCES['penn'],'Public domain','credit')}
{exhibit_figure('assets/curated/john-woolman.jpg','PORTRAIT / MEMORY SKETCH','John Woolman','来源页认为原作很可能与 Woolman 的同时代友人 Robert Smith III 有关，同时指出图像存在后来的记忆性元素。','Probably Robert Smith III',VISUAL_SOURCES['woolman'],'Public domain in U.S.','credit')}
{exhibit_figure('assets/curated/swarthmoor-hall.jpg','PLACE · 2005','Swarthmoor Hall','Cumbria 的 Swarthmoor Hall，与 Margaret Fell 及早期 Friends 网络密切相关。','Marion Dutcher',VISUAL_SOURCES['swarthmoor'],'CC BY-SA 2.0','credit')}
{exhibit_figure('assets/curated/meetinghouse-interior.jpg','FIELD PHOTO · 2021','贵格会聚会所室内','现代建筑照片，用来观察聚会所（Meeting House）的座位、隔断与朴素空间语言；不作为十七世纪室内的直接复原。','Pi3.124',VISUAL_SOURCES['interior'],'CC BY-SA 4.0','credit')}
{exhibit_figure('assets/curated/arch-street.jpg','PLACE · 2013','Arch Street Friends Meeting House','费城重要 Quaker 建筑。建于 1803–05 年，后来扩建。','Beyond My Ken',VISUAL_SOURCES['arch'],'CC BY-SA 4.0','credit')}
{exhibit_figure('assets/curated/free-quaker-interior.jpg','NPS DOCUMENTATION','自由贵格会聚会所室内','美国国家公园管理局的建筑记录图像；作为美国联邦政府雇员职务作品，在美国属于公有领域。','U.S. National Park Service',VISUAL_SOURCES['free_interior'],'Public domain (U.S.)','credit')}
</div></section>
<section class="content-section">{callout('使用原则','<p>如果未来加入 AI 场景复原，本站会明确标记为“编辑性复原 / 非历史照片”，不让生成图像冒充档案材料。历史研究页优先使用可追溯来源的真实史料与建筑照片。</p>')}</section>
'''
pages['visual-credits.html']=page_shell('visual-credits.html','图像与史料说明','人物肖像、Meeting House、历史地点与建筑照片的来源、授权与史料层级。',visual_credits_body,label='VISUAL SOURCES')

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
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);line-height:1.78;letter-spacing:.01em}a{color:inherit;text-decoration:none}img,svg{max-width:100%}button,input,textarea{font:inherit}.skip-link{position:absolute;left:-999px;top:8px}.skip-link:focus{left:8px;background:#fff;padding:8px;z-index:99}.site-header{position:sticky;top:0;z-index:30;display:flex;align-items:center;justify-content:space-between;padding:14px clamp(20px,4vw,64px);background:rgba(242,238,229,.92);backdrop-filter:blur(16px);border-bottom:1px solid rgba(31,39,35,.08)}.brand{display:flex;align-items:center;gap:11px}.brand b{display:block;font-family:var(--serif);font-size:18px}.brand small{display:block;font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--moss)}.brand-mark{width:34px;height:34px;border:1px solid var(--moss);border-radius:50%;position:relative}.brand-mark i{position:absolute;border:1px solid var(--gold);border-radius:50%;left:50%;top:50%;transform:translate(-50%,-50%)}.brand-mark i:nth-child(1){width:6px;height:6px;background:var(--gold)}.brand-mark i:nth-child(2){width:16px;height:16px}.brand-mark i:nth-child(3){width:26px;height:26px;opacity:.45}.main-nav{display:flex;gap:18px;font-size:13px}.main-nav a{padding:8px 0;color:#4d5852;border-bottom:1px solid transparent}.main-nav a:hover,.main-nav a.active{color:var(--ink);border-color:var(--gold)}.nav-toggle{display:none;background:none;border:0;font-size:24px}.page-hero{padding:72px clamp(22px,8vw,140px) 44px;border-bottom:1px solid var(--line)}.page-hero .hero-copy{max-width:940px}.kicker,.section-eyebrow,.section-head>span,.big-question>span{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--moss);font-weight:700}.page-hero h1{font:500 clamp(42px,6vw,82px)/1.08 var(--serif);margin:12px 0 20px}.page-hero p{font-size:18px;max-width:760px;color:var(--ink2)}.hero-line{width:74px;height:1px;background:var(--gold);margin-top:30px}.home-hero{min-height:76vh;display:grid;grid-template-columns:1.05fr .95fr;align-items:center;padding:80px clamp(24px,7vw,120px);background:var(--ink);color:var(--paper)}.home-copy h1{font:500 clamp(60px,8vw,110px)/.96 var(--serif);margin:18px 0 30px;letter-spacing:-.04em}.home-copy>p{max-width:650px;color:#d8d9d1;font-size:18px}.home-hero .kicker{color:#c4b991}.cta-row{display:flex;gap:12px;flex-wrap:wrap;margin:34px 0}.btn{display:inline-flex;justify-content:center;align-items:center;border:1px solid var(--ink);padding:12px 18px;border-radius:999px;cursor:pointer;transition:.2s;background:transparent}.btn.primary{background:var(--ink);color:var(--white)}.home-hero .btn.primary{background:var(--paper);color:var(--ink);border-color:var(--paper)}.btn.ghost{border-color:var(--line)}.home-hero .btn.ghost{color:var(--paper);border-color:#657069}.btn:hover{transform:translateY(-1px);box-shadow:0 8px 20px rgba(0,0,0,.08)}.btn.inverted{background:var(--paper);color:var(--ink);border:0}.hero-note{margin-top:40px;display:flex;gap:12px;max-width:650px;color:#aeb7b0;font-size:13px}.hero-note span{width:34px;height:1px;background:var(--gold);margin-top:11px;flex:none}.circle-visual{text-align:center}.circle-visual svg{max-height:510px;overflow:visible}.circle-visual .seat circle{fill:#d8ddd8}.circle-visual .seat path{fill:none;stroke:#aab5ad;stroke-width:1.4;stroke-linecap:round}.circle-visual .center-dot{fill:var(--gold)}.circle-visual .halo{stroke:#c9ab61;stroke-width:.45;transform-origin:50px 50px;animation:pulse 6s ease-in-out infinite}.circle-visual .h2{animation-delay:1s}.circle-visual .h3{animation-delay:2s;opacity:.45}.circle-visual p{font:14px var(--serif);color:#9da7a0;margin-top:-20px}@keyframes pulse{0%,100%{opacity:.18;transform:scale(.92)}50%{opacity:.65;transform:scale(1.07)}}.home-intro{display:grid;grid-template-columns:1.25fr .75fr;gap:5vw;padding:110px clamp(24px,8vw,140px)}.big-question h2{font:500 clamp(34px,4.1vw,56px)/1.28 var(--serif);margin:16px 0}.intro-copy{font-size:17px;color:var(--ink2);padding-top:34px}.home-map{padding:100px clamp(24px,8vw,140px);background:#e6e0d4}.section-head{max-width:850px;margin-bottom:42px}.section-head h2,.content-section h2{font:500 clamp(30px,4vw,52px)/1.2 var(--serif);margin:10px 0 12px}.section-head p{color:var(--ink2)}.layer-diagram{display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:60px;max-width:980px;margin:30px auto}.layer-diagram svg{max-height:560px}.layer{fill:none;stroke:var(--moss);stroke-width:.7;opacity:.55}.l1{stroke:var(--gold);stroke-width:1.5}.core{fill:var(--gold)}.layer-legend{display:grid;gap:12px}.layer-legend>div{display:flex;align-items:center;gap:18px;padding:12px 0;border-bottom:1px solid rgba(31,39,35,.14)}.layer-legend b{color:var(--gold);font-weight:500}.layer-legend span{display:flex;flex-direction:column}.layer-legend strong{font-family:var(--serif);font-size:20px}.layer-legend small{color:var(--moss)}.map-links{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-top:50px}.map-links a{padding:18px;border-top:1px solid var(--ink)}.map-links b{display:block;color:var(--gold);font-weight:500}.map-links span{font-family:var(--serif);font-size:18px}.map-links small{display:block;font-family:var(--sans);font-size:11px;color:var(--moss);margin-top:6px}.meeting-family{padding:100px clamp(24px,8vw,140px)}.family-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}.family-grid a{min-height:260px;padding:24px;background:var(--white);border:1px solid var(--line);display:flex;flex-direction:column}.family-grid a span{color:var(--gold)}.family-grid h3{font:500 24px/1.2 var(--serif);margin-top:auto}.family-grid p{color:var(--ink2);font-size:14px}.practice-banner{margin:30px clamp(24px,6vw,100px) 100px;padding:54px 60px;background:var(--ink);color:var(--paper);display:flex;align-items:flex-end;justify-content:space-between;gap:40px}.practice-banner span{color:#bcb69f;font-size:12px;letter-spacing:.15em}.practice-banner h2{font:500 clamp(32px,4vw,54px)/1.2 var(--serif);margin:8px 0}.practice-banner p{color:#bfc7c1}.reading-path{padding:0 clamp(24px,8vw,140px) 120px}.path-grid{display:grid;grid-template-columns:1fr 1fr;gap:24px}.path-grid article{background:var(--white);padding:28px 34px;border:1px solid var(--line)}.path-grid article>span{color:var(--moss);font-weight:700;font-size:12px;letter-spacing:.13em}.path-grid ol{padding-left:24px}.path-grid li{padding:8px 0;border-bottom:1px solid #e5dfd5}.path-grid a:hover{color:var(--moss)}.article-grid{display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:80px;max-width:1240px;margin:0 auto;padding:30px 34px 120px}.article-main{min-width:0}.content-section{padding:54px 0;border-bottom:1px solid var(--line)}.content-section>p{font-size:17px;max-width:850px;color:var(--ink2)}.section-eyebrow{margin-bottom:8px}.callout{padding:26px 30px;margin:35px 0;background:#e4ddcf;border-left:3px solid var(--gold)}.callout.dark{background:var(--ink);color:var(--paper)}.callout strong{font:500 21px var(--serif)}.callout p{margin:8px 0}.sources{position:sticky;top:100px;align-self:start;margin-top:54px;padding:24px;background:var(--white);border:1px solid var(--line)}.source-head{display:flex;gap:12px;align-items:center;border-bottom:1px solid var(--line);padding-bottom:16px}.source-head svg{width:34px;stroke:var(--moss);fill:none}.source-head span{font-size:11px;color:var(--moss);display:block}.source-head strong{font:500 18px var(--serif)}.sources ul{list-style:none;padding:0;margin:18px 0}.sources li{padding:12px 0;border-bottom:1px dashed var(--line)}.sources li b,.sources li span{display:block}.sources li b{font:500 15px var(--serif)}.sources li span{font-size:12px;color:var(--ink2);margin-top:5px}.text-link{font-size:13px;color:var(--moss)}.compare-mini,.role-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}.compare-mini>div,.role-grid article{padding:24px;background:var(--white);border:1px solid var(--line)}.compare-mini b,.role-grid b{font:500 22px var(--serif)}.definition-list dl{display:grid;grid-template-columns:140px 1fr;margin:0}.definition-list dt,.definition-list dd{padding:15px 0;border-bottom:1px solid var(--line)}.definition-list dt{font-weight:700;color:var(--moss)}.definition-list dd{margin:0}.myth-grid,.signal-grid,.care-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}.myth-grid article,.signal-grid article,.care-grid article{padding:22px;background:var(--white);border:1px solid var(--line)}.myth-grid b,.signal-grid b{font:500 18px var(--serif)}.myth-grid p,.signal-grid p,.care-grid p{font-size:14px;color:var(--ink2)}.process-row{display:flex;align-items:center;flex-wrap:wrap;gap:8px}.process-row span{padding:9px 13px;border:1px solid var(--line);border-radius:999px;background:var(--white)}.process-row i{color:var(--gold)}.bilingual-process{gap:clamp(4px,.55vw,8px);flex-wrap:nowrap;width:100%}.bilingual-process span{min-width:80px;padding:9px 11px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px;white-space:nowrap}.bilingual-process span.wide{min-width:174px}.bilingual-process b{font:500 17px/1.2 var(--serif)}.bilingual-process small{font:9px/1.3 var(--sans);color:var(--moss);letter-spacing:0}.fineprint{font-size:12px!important;color:#68726c!important}.query-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:24px}.query-card{min-height:180px;padding:22px;background:var(--ink);color:var(--paper)}.query-card span{font-size:10px;letter-spacing:.16em;color:#b9b49f}.query-card p{font:500 20px/1.55 var(--serif)}.three-stage{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.three-stage article{padding:22px;border-top:2px solid var(--gold);background:var(--white)}.three-stage span{font-size:11px;color:var(--gold)}.three-stage h3{font:500 28px var(--serif);margin:8px 0}.practice-steps{display:grid;gap:10px}.practice-steps article{padding:19px 22px;background:var(--white);border-left:2px solid var(--moss)}.practice-steps b{font:500 19px var(--serif)}.practice-steps p{margin:5px 0;color:var(--ink2)}.ladder{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border:1px solid var(--line)}.ladder>div{padding:18px;border-right:1px solid var(--line)}.ladder>div:last-child{border:0}.ladder span{font-weight:700}.ladder p{font-size:13px;color:var(--ink2)}.cta-inline{display:flex;gap:12px;flex-wrap:wrap;margin-top:30px}.practice-intro,.after-practice,.timer-shell{max-width:1120px;margin:0 auto;padding:50px 34px}.practice-intro{display:grid;grid-template-columns:1.3fr .7fr;gap:50px}.practice-intro h2,.after-practice h2{font:500 clamp(34px,4vw,54px)/1.2 var(--serif)}.practice-rules{display:flex;flex-wrap:wrap;align-content:center;gap:8px}.practice-rules span{padding:8px 12px;border:1px solid var(--line);border-radius:999px;background:var(--white);font-size:13px}.timer-shell{background:var(--ink);color:var(--paper);margin-top:20px;box-shadow:var(--shadow)}.timer-top{display:grid;grid-template-columns:1fr 240px;align-items:center;gap:40px}.timer-top h2{font:500 clamp(30px,4vw,54px)/1.2 var(--serif);margin:10px 0}.timer-top p{color:#bdc6c0}.timer-circle{position:relative;width:220px;height:220px}.timer-circle svg{transform:rotate(-90deg)}.timer-bg,.timer-progress{fill:none;stroke-width:5}.timer-bg{stroke:#3b4641}.timer-progress{stroke:var(--gold);stroke-linecap:round;stroke-dasharray:327;stroke-dashoffset:0}.timer-circle strong{position:absolute;inset:0;display:grid;place-items:center;font:500 42px var(--serif)}.timer-controls{display:flex;gap:10px;margin:24px 0}.timer-shell .btn.primary{background:var(--paper);color:var(--ink);border-color:var(--paper)}.timer-shell .btn.ghost{color:var(--paper);border-color:#5d6862}.stage-track{display:grid;grid-template-columns:repeat(5,1fr);gap:6px}.stage-track span{height:4px;background:#46514c}.stage-track span.active{background:var(--gold)}.reflection-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.reflection-grid label{font-size:13px;font-weight:700}.reflection-grid textarea{width:100%;min-height:150px;margin-top:8px;padding:14px;border:1px solid var(--line);background:var(--white);resize:vertical}.reflection-actions{display:flex;align-items:center;gap:12px;margin-top:18px}.skill-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.skill-grid article{padding:20px;border:1px solid var(--line);background:var(--white)}.skill-grid svg{width:38px;height:38px;stroke:var(--moss);fill:none;stroke-width:1.4}.skill-grid h3{font:500 21px var(--serif)}.skill-grid p{font-size:13px;color:var(--ink2)}.ministry-flow{display:flex;flex-direction:column;max-width:520px;margin:20px auto}.ministry-flow span,.ministry-flow strong{padding:13px 18px;border:1px solid var(--line);background:var(--white);text-align:center}.ministry-flow i{text-align:center;color:var(--gold)}.discern-box{display:grid;gap:10px;background:var(--white);padding:24px;border:1px solid var(--line)}.discern-box label{display:flex;gap:10px;padding:8px 0;border-bottom:1px dashed var(--line)}.discern-box .btn{justify-self:start}.result-note{font:500 18px var(--serif);color:var(--moss)}.signal-grid{grid-template-columns:repeat(3,1fr)}.practice-card{padding:26px;background:var(--white);border:1px solid var(--line)}.practice-card>span{font-size:12px;color:var(--moss);font-weight:700}.practice-card li{margin:8px 0}.decision-visual{margin:30px 0;padding:28px;background:var(--ink);color:var(--paper)}.decision-track{display:flex;gap:8px;flex-wrap:wrap;align-items:center}.decision-track span,.decision-track strong{padding:8px 11px;border:1px solid #637068;border-radius:999px;font-size:12px}.decision-track i{color:var(--gold)}.decision-visual p{font-size:13px;color:#b9c1bc}.compare-table{border:1px solid var(--line);background:var(--white)}.compare-table .row{display:grid;grid-template-columns:.7fr 1.2fr 1fr 1.2fr}.compare-table .row>*{padding:14px;border-right:1px solid var(--line);border-bottom:1px solid var(--line)}.compare-table .row>*:last-child{border-right:0}.compare-table .head{background:#ddd5c7;font-size:12px;font-weight:700}.compare-table .accent{background:#ece6d8}.role-grid .accent{border-top:3px solid var(--gold)}.case-lab,.question-lab{padding:26px;background:var(--white);border:1px solid var(--line)}.case-options,.question-actions{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0}.case-options button,.question-actions button,.filter-row button,.tool-grid button{border:1px solid var(--line);background:var(--paper);padding:10px 12px;cursor:pointer}.case-result,.question-feedback{padding:16px;background:#eee8dc;border-left:3px solid var(--gold);min-height:76px}.agenda{border-top:1px solid var(--ink)}.agenda>div{display:grid;grid-template-columns:90px 1fr;gap:20px;padding:13px 0;border-bottom:1px solid var(--line)}.agenda b{color:var(--gold)}.clearness-flow{display:grid;grid-template-columns:1fr 1fr;gap:10px}.clearness-flow article{padding:18px;background:var(--white);border:1px solid var(--line)}.clearness-flow b{font:500 18px var(--serif)}.clearness-flow p{font-size:13px;color:var(--ink2)}.question-example{font:500 26px/1.55 var(--serif);padding:20px;background:#f5f1e8}.rewrite-list{display:grid;gap:12px}.rewrite-list article{padding:20px;background:var(--white);border:1px solid var(--line)}.rewrite-list small{color:var(--moss)}.rewrite-list b{display:block;color:var(--moss)}.triad-visual{margin:30px 0}.triad-visual svg circle{fill:var(--white);stroke:var(--moss);stroke-width:1.5}.triad-visual svg .third{fill:#e6ddc9;stroke:var(--gold)}.triad-line{fill:none;stroke:#a7aea9;stroke-width:1}.triad-visual text{text-anchor:middle;font:500 23px var(--serif);fill:var(--ink)}.triad-visual .sub{font:12px var(--sans);fill:var(--moss)}.triad-visual .center-label{font:12px var(--sans);fill:var(--gold)}.org-map{display:flex;align-items:center;gap:12px;flex-wrap:wrap}.org-map div{padding:16px 18px;border:1px solid var(--line);background:var(--white)}.org-map small{display:block;color:var(--moss)}.org-map i{color:var(--gold)}.history-lead,.comparison-intro,.research-intro,.toolkit-top,.glossary-top{max-width:1100px;margin:0 auto;padding:60px 34px}.history-lead h2,.comparison-intro h2,.research-intro h2,.toolkit-top h2,.glossary-top h2{font:500 clamp(38px,5vw,66px)/1.18 var(--serif);margin:12px 0}.timeline-section{max-width:1120px;margin:0 auto;padding:20px 34px 110px}.timeline{border-left:1px solid var(--moss);margin-left:100px}.time-item{display:grid;grid-template-columns:110px 1fr;gap:30px;margin-left:-110px;padding:0 0 42px}.time-item time{color:var(--gold);font:500 18px var(--serif);text-align:right;padding-top:7px}.time-item>div{position:relative;padding-left:30px}.time-item>div:before{content:"";position:absolute;width:9px;height:9px;border-radius:50%;background:var(--gold);left:-5px;top:12px}.time-item h3{font:500 28px var(--serif);margin:0}.time-item p{color:var(--ink2)}.tension-grid,.scenario-grid,.book-grid,.roadmap-list,.tool-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.tension-grid article,.scenario-grid article,.book-grid article,.roadmap-list article,.tool-grid article{padding:22px;background:var(--white);border:1px solid var(--line)}.tension-grid b,.roadmap-list b{font:500 19px var(--serif)}.comparison-intro,.research-intro,.toolkit-top{max-width:100%;padding-left:clamp(24px,8vw,140px);padding-right:clamp(24px,8vw,140px)}.matrix-wrap{overflow:auto}.matrix{width:100%;border-collapse:collapse;min-width:980px;background:var(--white);font-size:13px}.matrix th,.matrix td{padding:14px;border:1px solid var(--line);vertical-align:top}.matrix thead th{background:#ddd5c7;text-align:left}.matrix tbody th{font-family:var(--serif);font-size:15px}.scenario-grid article span{font-size:11px;color:var(--moss)}.scenario-grid h3{font:500 20px var(--serif)}.glossary-top{display:grid;grid-template-columns:1fr 340px;gap:70px;align-items:end}.search-box{display:grid;gap:8px;font-size:12px;color:var(--moss)}.search-box input{padding:14px 16px;border:1px solid var(--line);background:var(--white)}.filter-row{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:24px}.filter-row button.active{background:var(--ink);color:var(--paper)}.glossary-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.glossary-card{padding:22px;background:var(--white);border:1px solid var(--line)}.glossary-card>span{font-size:10px;color:var(--moss)}.glossary-card h3{font:500 22px var(--serif);margin:8px 0 2px}.glossary-card h4{margin:0;color:var(--moss)}.glossary-card p{font-size:13px;color:var(--ink2)}.book-grid article>span{font-size:10px;color:var(--moss);letter-spacing:.1em}.book-grid h3{font:500 22px/1.35 var(--serif)}.book-grid p{font-size:13px;color:var(--ink2)}.book-grid small{color:var(--moss)}.method-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.method-grid b{min-height:120px;display:flex;align-items:flex-end;padding:18px;background:var(--ink);color:var(--paper);font:500 17px/1.5 var(--serif)}.research-note{padding:40px;background:var(--ink);color:var(--paper)}.research-note h2{margin-top:0}.tool-grid article>span{font-size:11px;color:var(--moss)}.tool-grid h3{font:500 23px var(--serif)}.tool-grid li{margin:7px 0}.tool-grid button{margin-top:8px}.four-lines{display:grid;grid-template-columns:1fr 1fr;gap:10px}.four-lines p{margin:0;padding:28px;background:var(--white);border:1px solid var(--line);font:500 24px/1.45 var(--serif)}.site-footer{background:#19201d;color:#d8ddd8;padding:50px clamp(24px,6vw,100px);display:grid;grid-template-columns:1.3fr .7fr;gap:40px}.site-footer b{font-family:var(--serif);font-size:20px}.site-footer p{color:#9eaaa3;font-size:13px}.footer-links{display:flex;flex-direction:column;gap:8px}.footer-links a{color:#c9d0cb}.footer-note{grid-column:1/-1;border-top:1px solid #364039;padding-top:20px}
@media(max-width:1100px){.main-nav{display:none;position:absolute;left:0;right:0;top:64px;background:var(--paper);padding:20px 24px;flex-wrap:wrap;border-bottom:1px solid var(--line)}.main-nav.open{display:flex}.nav-toggle{display:block}.home-hero,.home-intro,.layer-diagram,.practice-intro,.glossary-top{grid-template-columns:1fr}.home-hero{padding-top:60px}.circle-visual svg{max-height:400px}.map-links,.family-grid{grid-template-columns:1fr 1fr}.article-grid{grid-template-columns:1fr;gap:0}.sources{position:relative;top:auto}.tension-grid,.scenario-grid,.book-grid,.roadmap-list,.tool-grid,.glossary-grid{grid-template-columns:1fr 1fr}.method-grid{grid-template-columns:1fr 1fr}.query-grid,.signal-grid,.skill-grid{grid-template-columns:1fr 1fr}.timer-top{grid-template-columns:1fr}.timer-circle{width:190px;height:190px}.reflection-grid{grid-template-columns:1fr}.site-footer{grid-template-columns:1fr}}
@media(max-width:640px){.page-hero{padding-top:48px}.home-hero{grid-template-columns:1fr}.home-copy h1{font-size:58px}.map-links,.family-grid,.path-grid,.myth-grid,.care-grid,.compare-mini,.role-grid,.three-stage,.clearness-flow,.query-grid,.signal-grid,.skill-grid,.tension-grid,.scenario-grid,.book-grid,.roadmap-list,.tool-grid,.glossary-grid,.four-lines{grid-template-columns:1fr}.layer-legend{margin-top:-20px}.practice-banner{padding:34px;display:block}.practice-banner .btn{margin-top:20px}.ladder{grid-template-columns:1fr}.ladder>div{border-right:0;border-bottom:1px solid var(--line)}.compare-table .row{grid-template-columns:1fr}.compare-table .head{display:none}.compare-table .row>*{border-right:0}.stage-track{grid-template-columns:repeat(5,1fr)}.time-item{grid-template-columns:70px 1fr;margin-left:-80px}.timeline{margin-left:80px}.agenda>div{grid-template-columns:70px 1fr}.method-grid{grid-template-columns:1fr}.site-footer{padding:40px 24px}}
@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}.halo{animation:none!important}.btn{transition:none}}
@media print{.site-header,.site-footer,.nav-toggle,.btn,.case-options,.question-actions,.filter-row{display:none!important}body{background:#fff}.content-section{break-inside:avoid}.page-hero{padding-top:20px}}

/* ---- 2.0 reading & visual system ---- */
body{overflow-x:clip}
.site-header,.site-header>*{min-width:0}
h1,h2,h3,.query-card p,.four-lines p,.question-example{
  text-wrap:pretty;
  word-break:normal;
  overflow-wrap:normal;
  line-break:strict;
}
.title-line{display:inline;max-width:100%}
.title-segment{white-space:nowrap}
.title-segment.fluid{white-space:normal}
h3 .title-segment{white-space:normal}
.term-lock{display:inline-block;white-space:nowrap;letter-spacing:-.015em}
.en-paren{font-family:var(--sans);font-size:.58em;font-weight:500;color:var(--moss);letter-spacing:0;white-space:nowrap;vertical-align:.08em}.page-hero h1 .en-paren,.history-lead h2 .en-paren,.research-intro h2 .en-paren,.glossary-top h2 .en-paren{font-size:.48em}
.heading-annotations{display:block;margin-top:.42em;font-family:var(--sans);font-size:.34em;font-weight:500;line-height:1.45;letter-spacing:.015em;color:var(--moss);white-space:normal}
.content-section h2 .heading-annotations,.section-head h2 .heading-annotations{font-size:.38em;margin-top:.5em}
.exhibit-figure h3 .title-line,.portrait-card h3 .title-line,.visual-index-grid h3 .title-line,.family-grid h3 .title-line,.research-card h3 .title-line,.history-thesis h3 .title-line,.timeline-card h3 .title-line,.false-friends h3 .title-line,.tool-grid h3 .title-line{white-space:normal}
p,li,dd{orphans:2;widows:2;overflow-wrap:anywhere}
.section-heading-row{display:flex;flex-direction:column;gap:10px;align-items:flex-start}
.section-heading-row>div:first-child{min-width:0;width:100%}
.section-glyph{order:-1;width:48px;height:48px;border:1px solid var(--line);border-radius:50%;display:grid;place-items:center;background:rgba(255,253,248,.62);margin:0 0 2px}
.section-glyph svg{width:27px;height:27px;stroke:var(--moss);fill:none;stroke-width:1.35}
.section-glyph svg circle:not([fill="none"]){fill:none}
.section-heading-row+.concept-figure,.section-heading-row+.triad-visual,.section-heading-row+.decision-visual{margin-top:20px}
.page-hero .hero-copy{max-width:1120px}
.page-hero h1{max-width:none;font-size:clamp(40px,4.7vw,68px);letter-spacing:-.025em;line-height:1.12}
.page-hero p{max-width:820px;line-height:1.9}
.home-copy{min-width:0}
.home-copy h1{max-width:6.2em;font-size:clamp(56px,7.4vw,104px);line-height:1.04;letter-spacing:-.035em}
.big-question h2{max-width:18em;line-height:1.26}
.section-head h2,.content-section h2{max-width:none;line-height:1.32;font-size:clamp(31px,3.15vw,42px)}
.content-section>p,.article-main .content-section>p{max-width:46rem;line-height:1.9}
.article-main{font-size:16px}
.article-main p{line-height:1.9}
main>.content-section{padding-left:clamp(24px,8vw,140px);padding-right:clamp(24px,8vw,140px)}
.article-main>.content-section{padding-left:0;padding-right:0}
.practice-intro{display:block}
.practice-intro>div:first-child{max-width:880px}
.practice-intro h2{font-size:clamp(34px,3.55vw,48px);line-height:1.22;margin:14px 0 18px}
.practice-intro .practice-rules{margin-top:28px}
.practice-intro .practice-rules span{margin-bottom:4px}

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
.research-card h3{font:500 25px/1.45 var(--serif);margin:0 0 10px;max-width:22em}
.research-card p{color:#c9d0cb;margin:8px 0;line-height:1.85}

/* ---- curated visual / archive system ---- */
.curated-opening,.history-gallery,.history-place-study,.credits-intro{
  padding:88px clamp(24px,8vw,140px);
}
.curated-opening{background:#e9e2d5;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.history-gallery{background:#ebe4d7}
.history-place-study{padding-top:0;background:#ebe4d7}
.credits-intro{max-width:1120px}
.credits-intro>div{max-width:860px}
.credits-intro h2{font:500 clamp(38px,4.8vw,62px)/1.18 var(--serif);margin:16px 0}
.credits-intro p{font-size:17px;color:var(--ink2);max-width:760px}

.exhibit-figure{
  margin:30px 0 42px;
  background:var(--white);
  border:1px solid var(--line);
  overflow:hidden;
  min-width:0;
  box-shadow:0 20px 60px rgba(31,39,35,.06);
}
.exhibit-image-wrap{
  position:relative;
  overflow:hidden;
  background:#dcd4c7;
  aspect-ratio:16/9;
}
.exhibit-image-wrap:after{
  content:"";
  position:absolute;
  inset:0;
  pointer-events:none;
  background:linear-gradient(180deg,rgba(255,250,240,.05),rgba(31,39,35,.08));
  mix-blend-mode:multiply;
}
.exhibit-image-wrap img{
  width:100%;
  height:100%;
  object-fit:cover;
  display:block;
  filter:saturate(.72) contrast(.96) sepia(.08);
  transition:transform .6s ease,filter .3s ease;
}
.exhibit-figure:hover .exhibit-image-wrap img{transform:scale(1.012);filter:saturate(.9) contrast(.98) sepia(.04)}
.exhibit-figure figcaption{padding:24px 26px 26px}
.exhibit-kicker{
  display:block;
  margin-bottom:8px;
  font-size:10px;
  letter-spacing:.18em;
  text-transform:uppercase;
  color:var(--moss);
  font-weight:700;
}
.exhibit-figure h3{font:500 clamp(22px,2.4vw,30px)/1.32 var(--serif);margin:0 0 9px}
.exhibit-figure figcaption p{margin:0;color:var(--ink2);line-height:1.78}
.exhibit-figure figcaption small{display:block;margin-top:14px;padding-top:12px;border-top:1px solid #e2dbcf;color:#7a817d;font-size:10px;line-height:1.6}
.exhibit-figure figcaption small a{text-decoration:underline;text-underline-offset:3px}
.exhibit-figure.hero-exhibit .exhibit-image-wrap{aspect-ratio:2.15/1}
.exhibit-figure.article-exhibit{margin:36px 0 52px}
.exhibit-figure.article-exhibit .exhibit-image-wrap{aspect-ratio:1.85/1}
.exhibit-figure.compact{margin:0}
.exhibit-figure.compact .exhibit-image-wrap{aspect-ratio:4/3}
.exhibit-figure.compact figcaption{padding:20px}
.exhibit-figure.credit{margin:0;box-shadow:none}
.exhibit-figure.credit .exhibit-image-wrap{aspect-ratio:4/3}
.exhibit-figure.credit h3{font-size:22px}

.exhibit-pair{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin:34px 0 46px}
.exhibit-annotations{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:-18px}
.exhibit-label{display:grid;grid-template-columns:34px 1fr;gap:14px;padding:18px;background:rgba(255,253,248,.62);border-top:1px solid var(--moss)}
.exhibit-label>span{font:500 18px var(--serif);color:var(--gold)}
.exhibit-label b{font:500 17px var(--serif)}
.exhibit-label p{margin:4px 0 0;font-size:12px;line-height:1.65;color:var(--ink2)}

.portrait-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:34px}
.portrait-card{background:var(--white);border:1px solid var(--line);min-width:0}
.portrait-image{aspect-ratio:4/5;overflow:hidden;background:#d8d0c3}
.portrait-image img{width:100%;height:100%;object-fit:cover;display:block;filter:grayscale(.18) sepia(.16) saturate(.72);transition:.35s}
.portrait-card:hover .portrait-image img{filter:grayscale(0) sepia(.08) saturate(.9);transform:scale(1.015)}
.portrait-copy{padding:20px}
.portrait-copy>span{font-size:10px;letter-spacing:.14em;color:var(--gold)}
.portrait-copy h3{font:500 25px/1.25 var(--serif);margin:5px 0 9px}
.portrait-copy p{font-size:13px;line-height:1.72;color:var(--ink2)}
.portrait-copy small{display:block;border-top:1px solid #e2dbcf;padding-top:11px;margin-top:13px;font-size:9px;line-height:1.55;color:#7d847f}
.portrait-copy small a{text-decoration:underline;text-underline-offset:2px}

.curator-note{display:grid;grid-template-columns:160px minmax(0,1fr);gap:28px;align-items:start;margin:32px 0 0;padding:26px 0;border-top:1px solid var(--moss);border-bottom:1px solid var(--line)}
.curator-note>span{font-size:10px;letter-spacing:.18em;color:var(--moss);font-weight:700}
.curator-note p{margin:0;max-width:760px;color:var(--ink2);line-height:1.85}
.curator-note a{text-decoration:underline;text-underline-offset:4px}
.credits-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}
.visual-index{padding:92px clamp(24px,8vw,140px);background:#202925;color:var(--paper)}
.visual-index .section-head span{color:#c7b47b}
.visual-index .section-head h2{color:#fffaf0}
.visual-index .section-head p{color:#c9d0cb;max-width:720px}
.visual-index-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:34px}
.visual-index-grid>a{display:block;background:#29332f;border:1px solid rgba(255,255,255,.12);min-width:0;transition:transform .2s ease,border-color .2s ease}
.visual-index-grid>a:hover{transform:translateY(-3px);border-color:#a88f58}
.visual-index-image{aspect-ratio:4/3;overflow:hidden;background:#343d39}
.visual-index-image img{display:block;width:100%;height:100%;object-fit:cover;filter:grayscale(.18) sepia(.14) saturate(.65);transition:.35s}
.visual-index-grid>a:hover img{filter:grayscale(0) sepia(.06) saturate(.88);transform:scale(1.015)}
.visual-index-grid>a>span{display:block;padding:18px 20px 0;color:#c7b47b;font-size:10px;letter-spacing:.16em}
.visual-index-grid h3{font:500 24px/1.4 var(--serif);margin:8px 20px 6px;color:#fffaf0;overflow-wrap:break-word}
.visual-index-grid p{margin:0;padding:0 20px 22px;color:#cbd2cd;font-size:13px;line-height:1.75}

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

/* ---- cross-tradition gathering / AI age ---- */
.traditions-intro{
  display:grid;
  grid-template-columns:minmax(0,1.08fr) minmax(360px,.92fr);
  gap:clamp(48px,7vw,110px);
  align-items:center;
  padding:88px clamp(24px,8vw,140px) 94px;
  background:linear-gradient(135deg,#eee8dc 0%,#f7f3ea 58%,#e9e2d5 100%);
  border-bottom:1px solid var(--line);
}
.traditions-intro-copy{max-width:760px}
.semantic-title>span{display:inline;white-space:nowrap}
.traditions-intro h2{
  font:500 clamp(38px,4.5vw,62px)/1.2 var(--serif);
  margin:16px 0 24px;
  letter-spacing:-.025em;
}
.traditions-intro-copy>p{font-size:17px;line-height:1.92;color:var(--ink2)}
.traditions-intro .curator-note{margin-top:28px}

.tradition-orbit{
  position:relative;
  width:min(100%,520px);
  aspect-ratio:1;
  margin:auto;
  border:1px solid rgba(93,109,96,.36);
  border-radius:50%;
  background:
    radial-gradient(circle at center,rgba(180,154,92,.18) 0 2%,transparent 2.5% 26%,rgba(93,109,96,.09) 26.5% 27%,transparent 27.5% 48%,rgba(180,154,92,.12) 48.5% 49%,transparent 49.5%);
}
.tradition-orbit:before,.tradition-orbit:after{
  content:"";
  position:absolute;
  left:50%;top:50%;
  transform:translate(-50%,-50%);
  border:1px solid rgba(93,109,96,.2);
  border-radius:50%;
  pointer-events:none;
}
.tradition-orbit:before{width:72%;height:72%}
.tradition-orbit:after{width:42%;height:42%}
.orbit-center{
  position:absolute;
  left:50%;top:50%;
  transform:translate(-50%,-50%);
  width:118px;height:118px;
  display:grid;place-content:center;text-align:center;
  border-radius:50%;
  background:var(--ink);
  color:var(--paper);
  box-shadow:0 16px 40px rgba(31,39,35,.14);
  z-index:2;
}
.orbit-center b{font:500 20px/1.25 var(--serif)}
.orbit-center small{color:#bdb69f;font-size:10px;letter-spacing:.1em;margin-top:4px}
.tradition-orbit>span{
  position:absolute;
  transform:translate(-50%,-50%);
  min-width:108px;
  padding:10px 12px;
  border:1px solid var(--line);
  border-radius:999px;
  background:rgba(255,253,248,.94);
  text-align:center;
  font:500 15px/1.25 var(--serif);
  box-shadow:0 8px 24px rgba(31,39,35,.06);
}
.tradition-orbit>span small{font:10px/1.2 var(--sans);color:var(--moss)}
.tradition-orbit>span:nth-of-type(1){left:50%;top:5%}
.tradition-orbit>span:nth-of-type(2){left:83%;top:21%}
.tradition-orbit>span:nth-of-type(3){left:94%;top:54%}
.tradition-orbit>span:nth-of-type(4){left:74%;top:87%}
.tradition-orbit>span:nth-of-type(5){left:28%;top:90%}
.tradition-orbit>span:nth-of-type(6){left:5%;top:58%}
.tradition-orbit>span:nth-of-type(7){left:16%;top:22%}

.tradition-cards{
  display:grid;
  grid-template-columns:repeat(3,minmax(0,1fr));
  gap:14px;
}
.tradition-cards article{
  min-width:0;
  padding:26px;
  background:var(--white);
  border:1px solid var(--line);
  display:flex;
  flex-direction:column;
  min-height:330px;
}
.tradition-cards article:first-child{
  grid-column:1/-1;
  min-height:0;
  display:grid;
  grid-template-columns:64px 1.1fr 1.4fr;
  gap:24px;
  align-items:center;
  background:#e7dfd0;
  border-top:3px solid var(--gold);
}
.tradition-icon{
  width:52px;height:52px;
  display:grid;place-items:center;
  border:1px solid var(--line);
  border-radius:50%;
  margin-bottom:18px;
}
.tradition-icon svg{width:30px;height:30px;stroke:var(--moss);fill:none;stroke-width:1.3}
.tradition-cards article:first-child .tradition-icon{margin:0;grid-column:1;grid-row:1/4}
.tradition-cards article:first-child>span{grid-column:2;grid-row:1}
.tradition-cards article:first-child h3{grid-column:2;grid-row:2;margin-top:4px}
.tradition-cards article:first-child p{grid-column:3;grid-row:1/3;margin:0}
.tradition-cards article:first-child>b{grid-column:2/4;grid-row:3}
.tradition-cards article>span{
  color:var(--moss);
  font-size:11px;
  letter-spacing:.06em;
}
.tradition-cards h3{
  font:500 23px/1.35 var(--serif);
  margin:12px 0;
}
.tradition-cards h3 small{
  display:block;
  margin-top:4px;
  font:500 11px/1.4 var(--sans);
  color:var(--moss);
}
.tradition-cards p{font-size:14px;line-height:1.82;color:var(--ink2)}
.tradition-cards article>b{
  display:block;
  margin-top:auto;
  padding-top:18px;
  border-top:1px solid var(--line);
  color:#756338;
  font-size:12px;
  font-weight:600;
}

.tradition-matrix{min-width:1180px}
.tradition-matrix th:first-child{min-width:175px}
.tradition-matrix td,.tradition-matrix th{line-height:1.65}
.tradition-matrix small{color:var(--moss);font-weight:500}

.shared-grammar,.human-core-grid,.future-protocol{
  display:grid;
  grid-template-columns:repeat(3,minmax(0,1fr));
  gap:12px;
}
.shared-grammar article,.human-core-grid article,.future-protocol article{
  padding:24px;
  min-width:0;
  border:1px solid var(--line);
  background:var(--white);
}
.shared-grammar article>b,.future-protocol article>b{
  color:var(--gold);
  font-size:12px;
  letter-spacing:.12em;
}
.shared-grammar h3,.human-core-grid h3,.future-protocol h3{
  font:500 21px/1.4 var(--serif);
  margin:10px 0 8px;
}
.shared-grammar p,.human-core-grid p,.future-protocol p{
  margin:0;
  color:var(--ink2);
  font-size:14px;
  line-height:1.82;
}

.do-not-collapse{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:12px;
}
.do-not-collapse article{
  padding:26px 28px;
  border-top:3px solid var(--gold);
  background:#e9e2d5;
}
.do-not-collapse span{font-size:11px;color:var(--moss);letter-spacing:.06em}
.do-not-collapse h3{font:500 23px/1.4 var(--serif);margin:10px 0}
.do-not-collapse p{font-size:14px;line-height:1.82;color:var(--ink2)}

.ai-era{
  display:grid;
  grid-template-columns:minmax(0,1fr) minmax(420px,.8fr);
  gap:clamp(40px,7vw,100px);
  align-items:center;
  padding:92px clamp(24px,8vw,140px);
  background:var(--ink);
  color:var(--paper);
}
.ai-era-head>span{
  color:#cbbd94;
  font-size:11px;
  letter-spacing:.18em;
  font-weight:700;
}
.ai-era h2{
  font:500 clamp(38px,4.7vw,64px)/1.18 var(--serif);
  margin:16px 0 24px;
  max-width:12em;
}
.ai-era p{color:#c5ccc7;font-size:17px;line-height:1.9;max-width:720px}
.ai-era p strong{color:var(--paper)}
.ai-rings{display:grid;place-items:center;min-width:0}
.ai-ring{
  border-radius:50%;
  display:grid;
  place-items:center;
  text-align:center;
}
.ai-ring-outer{
  width:min(100%,500px);
  aspect-ratio:1;
  border:1px solid rgba(203,189,148,.48);
  background:radial-gradient(circle,rgba(180,154,92,.04),rgba(255,255,255,.015));
}
.ai-ring-middle{
  width:68%;aspect-ratio:1;
  border:1px solid rgba(173,186,178,.42);
  background:#222d28;
}
.ai-ring-center{
  width:53%;aspect-ratio:1;
  border:1px solid var(--gold);
  background:#efe8d9;
  color:var(--ink);
  box-shadow:0 0 60px rgba(180,154,92,.15);
}
.ai-ring>span{font:500 17px/1.35 var(--serif);color:#ddd7c9}
.ai-ring>span small,.ai-ring-center small{
  display:block;
  margin-top:5px;
  font:10px/1.5 var(--sans);
  color:#9eaaa3;
}
.ai-ring-center strong{font:500 20px/1.3 var(--serif)}
.ai-ring-center small{color:var(--moss);padding:0 14px}

.human-core-grid article{background:#eee7da}
.human-core-grid article>span{
  color:var(--gold);
  font-size:11px;
  letter-spacing:.12em;
}

.ai-boundary-grid{
  display:grid;
  grid-template-columns:repeat(3,minmax(0,1fr));
  gap:14px;
}
.ai-boundary-grid article{
  padding:26px;
  border:1px solid var(--line);
  background:var(--white);
}
.ai-boundary-grid article>span{
  display:inline-block;
  padding:5px 8px;
  border-radius:999px;
  font-size:10px;
  letter-spacing:.08em;
  background:#e7e1d5;
  color:var(--moss);
}
.ai-boundary-grid h3{font:500 26px/1.3 var(--serif);margin:12px 0}
.ai-boundary-grid ul{padding-left:19px;margin:0;color:var(--ink2)}
.ai-boundary-grid li{margin:8px 0;line-height:1.7}
.ai-boundary-grid .ai-yes{border-top:4px solid #718275}
.ai-boundary-grid .ai-caution{border-top:4px solid var(--gold)}
.ai-boundary-grid .ai-no{border-top:4px solid #7b6359}

.source-link-grid{
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:10px;
}
.source-link-grid a{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:20px;
  padding:18px 20px;
  border:1px solid var(--line);
  background:var(--white);
}
.source-link-grid a:hover{border-color:#9e9079;box-shadow:0 8px 24px rgba(31,39,35,.06)}
.source-link-grid b{font:500 17px/1.4 var(--serif)}
.source-link-grid span{font-size:11px;color:var(--moss);text-align:right}

/* ---- China context / cultural integration ---- */
.china-intro{
  display:grid;
  grid-template-columns:minmax(0,1.06fr) minmax(420px,.94fr);
  gap:clamp(44px,7vw,100px);
  align-items:center;
  padding:88px clamp(24px,8vw,140px) 96px;
  background:
    linear-gradient(90deg,rgba(180,154,92,.05) 1px,transparent 1px) 0 0/52px 52px,
    linear-gradient(rgba(180,154,92,.05) 1px,transparent 1px) 0 0/52px 52px,
    #eee8dc;
  border-bottom:1px solid var(--line);
}
.china-intro-copy{max-width:760px}
.china-intro h2{font:500 clamp(40px,4.6vw,64px)/1.18 var(--serif);margin:16px 0 24px}
.china-intro-copy>p{font-size:17px;line-height:1.92;color:var(--ink2)}
.china-principle{
  margin-top:28px;
  display:grid;
  grid-template-columns:128px 1fr;
  gap:18px;
  padding-top:20px;
  border-top:1px solid var(--ink);
}
.china-principle b{font-size:11px;letter-spacing:.08em;color:var(--moss)}
.china-principle p{margin:0;font-size:14px;line-height:1.8;color:var(--ink2)}

.china-bridge-visual{
  position:relative;
  min-height:470px;
  display:grid;
  grid-template-columns:1fr .95fr 1fr;
  align-items:center;
  gap:0;
}
.china-bridge-visual:before,
.china-bridge-visual:after{
  content:"";
  position:absolute;
  top:50%;
  width:28%;
  height:1px;
  background:linear-gradient(90deg,var(--moss),var(--gold));
  opacity:.55;
}
.china-bridge-visual:before{left:18%}
.china-bridge-visual:after{right:18%;transform:scaleX(-1)}
.china-side,.china-bridge-center{
  position:relative;
  z-index:2;
  text-align:center;
}
.china-side{
  padding:28px 18px;
  border:1px solid var(--line);
  background:rgba(255,253,248,.92);
}
.china-side span,.china-bridge-center span{
  display:block;
  color:var(--moss);
  font-size:10px;
  letter-spacing:.12em;
}
.china-side b{
  display:block;
  margin:8px 0 6px;
  font:500 26px/1.25 var(--serif);
}
.china-side small{display:block;color:var(--ink2);font-size:10px;line-height:1.5}
.china-bridge-center{
  aspect-ratio:1;
  border-radius:50%;
  display:grid;
  place-content:center;
  padding:22px;
  background:var(--ink);
  color:var(--paper);
  box-shadow:0 18px 46px rgba(31,39,35,.13);
}
.china-bridge-center strong{font:500 24px/1.35 var(--serif);margin:8px 0}
.china-bridge-center small{color:#b9c1bc;font-size:10px;line-height:1.45}

.china-bridge-grid{
  display:grid;
  grid-template-columns:repeat(3,minmax(0,1fr));
  gap:12px;
}
.china-bridge-grid article{
  min-width:0;
  display:flex;
  flex-direction:column;
  padding:26px;
  border:1px solid var(--line);
  background:var(--white);
}
.china-bridge-grid article>span{font-size:11px;color:var(--moss);letter-spacing:.05em}
.china-bridge-grid h3{font:500 30px/1.25 var(--serif);margin:10px 0}
.china-bridge-grid p{font-size:14px;line-height:1.84;color:var(--ink2)}
.china-bridge-grid article>b{
  display:block;
  margin-top:auto;
  padding-top:16px;
  border-top:1px solid var(--line);
  color:#756338;
  font-size:12px;
}
.china-bridge-grid article>em{
  display:block;
  margin-top:10px;
  color:var(--moss);
  font-size:11px;
  line-height:1.65;
  font-style:normal;
}

.china-not-equal{
  display:grid;
  grid-template-columns:repeat(3,minmax(0,1fr));
  gap:10px;
}
.china-not-equal article{
  padding:24px;
  background:#e7dfd0;
  border-top:3px solid var(--gold);
}
.china-not-equal b{font:500 21px/1.35 var(--serif)}
.china-not-equal p{margin:10px 0 0;color:var(--ink2);font-size:14px;line-height:1.8}

.china-tension-section{
  padding:88px clamp(24px,8vw,140px);
  background:var(--ink);
  color:var(--paper);
}
.china-tension-section .section-head>span{color:#cbbd94}
.china-tension-section .section-head p{color:#b8c0bb}
.china-tension-grid{
  display:grid;
  grid-template-columns:repeat(3,minmax(0,1fr));
  gap:1px;
  background:#435049;
  border:1px solid #435049;
}
.china-tension-grid article{
  padding:26px;
  background:#202925;
}
.china-tension-grid article>span{color:#cbbd94;font-size:10px;letter-spacing:.08em}
.china-tension-grid h3{font:500 22px/1.4 var(--serif);margin:10px 0}
.china-tension-grid p{margin:0;color:#c5ccc7;font-size:14px;line-height:1.8}
.china-tension-grid strong{color:var(--paper)}

.china-use-grid{
  display:grid;
  grid-template-columns:repeat(4,minmax(0,1fr));
  gap:12px;
}
.china-use-grid article{
  min-width:0;
  padding:24px;
  border:1px solid var(--line);
  background:var(--white);
}
.china-use-grid article>span{font-size:10px;color:var(--moss);letter-spacing:.08em}
.china-use-grid h3{font:500 21px/1.4 var(--serif);margin:10px 0}
.china-use-grid p{font-size:13px;line-height:1.78;color:var(--ink2)}
.china-use-grid b{color:#756338}

.china-prototype{
  padding:88px clamp(24px,8vw,140px);
  background:#e8e0d3;
  border-top:1px solid var(--line);
  border-bottom:1px solid var(--line);
}
.china-protocol{
  position:relative;
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:0 48px;
}
.china-protocol:before{
  content:"";
  position:absolute;
  left:50%;
  top:0;bottom:0;
  width:1px;
  background:#bfb4a0;
}
.china-protocol article{
  display:grid;
  grid-template-columns:72px 1fr;
  gap:18px;
  padding:22px 0;
  border-bottom:1px solid rgba(31,39,35,.12);
}
.china-protocol article:nth-child(odd){padding-right:28px}
.china-protocol article:nth-child(even){padding-left:28px}
.china-protocol article>b{color:var(--gold);font:600 12px var(--sans);padding-top:7px}
.china-protocol span{font-size:10px;color:var(--moss);letter-spacing:.1em}
.china-protocol h3{font:500 21px/1.35 var(--serif);margin:4px 0}
.china-protocol p{margin:0;font-size:13px;line-height:1.75;color:var(--ink2)}

.china-local-grid{
  display:grid;
  grid-template-columns:repeat(4,minmax(0,1fr));
  gap:10px;
}
.china-local-grid article{
  padding:22px;
  border:1px solid var(--line);
  background:var(--white);
}
.china-local-grid article>b{font-size:10px;color:var(--gold);letter-spacing:.12em}
.china-local-grid h3{font:500 20px/1.4 var(--serif);margin:8px 0}
.china-local-grid p{margin:0;color:var(--ink2);font-size:13px;line-height:1.78}

.china-digital-note{
  display:grid;
  grid-template-columns:.85fr 1.15fr;
  gap:60px;
  align-items:start;
  padding:70px clamp(24px,8vw,140px);
  background:#dcd5c7;
}
.china-digital-note span{font-size:10px;color:var(--moss);letter-spacing:.12em}
.china-digital-note h2{font:500 clamp(32px,4vw,50px)/1.22 var(--serif);margin:10px 0}
.china-digital-note p{margin:4px 0 0;font-size:16px;line-height:1.9;color:var(--ink2)}

.family-grid a,.myth-grid article,.signal-grid article,.care-grid article,.book-grid article,.roadmap-list article,.tool-grid article,.glossary-card,.query-card,.scenario-grid article{
  transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease;
}
.family-grid a:hover,.book-grid article:hover,.glossary-card:hover,.scenario-grid article:hover{
  transform:translateY(-2px);
  box-shadow:0 12px 28px rgba(31,39,35,.07);
  border-color:#b9ad9b;
}

@media(max-width:980px){
  .bilingual-process{flex-wrap:wrap}
  .depth-grid,.history-thesis,.research-discipline,.source-matrix,.reading-trails,.comparison-lenses,.practice-ladder-v2{grid-template-columns:1fr 1fr}
  .four-forces{grid-template-columns:1fr 1fr}
  .comparison-lenses{padding-bottom:42px}
  .concept-figure figcaption{grid-template-columns:1fr;gap:7px}
  .portrait-grid{grid-template-columns:1fr 1fr}
  .credits-grid{grid-template-columns:1fr 1fr}
  .exhibit-annotations{grid-template-columns:1fr}
  .visual-index-grid{grid-template-columns:1fr 1fr}
  .traditions-intro,.ai-era,.china-intro{grid-template-columns:minmax(0,1fr)}
  .traditions-intro>* ,.ai-era>* ,.china-intro>*{min-width:0}
  .tradition-orbit{max-width:480px}
  .tradition-cards{grid-template-columns:1fr 1fr}
  .tradition-cards article:first-child{grid-column:1/-1;grid-template-columns:52px 1fr 1.25fr}
  .shared-grammar,.human-core-grid,.future-protocol,.china-bridge-grid,.china-not-equal,.china-tension-grid,.china-use-grid,.china-local-grid{grid-template-columns:1fr 1fr}
  .ai-boundary-grid{grid-template-columns:1fr}
  .china-bridge-visual{max-width:720px;width:100%;margin:0 auto;min-height:400px}
  .china-protocol{grid-template-columns:1fr;gap:0}
  .china-protocol:before{left:0}
  .china-protocol article,.china-protocol article:nth-child(odd),.china-protocol article:nth-child(even){padding:20px 0 20px 24px}
  .china-digital-note{grid-template-columns:1fr;gap:24px}
  .source-link-grid{grid-template-columns:1fr 1fr}
}
@media(max-width:1100px){
  .visual-index-grid{grid-template-columns:1fr 1fr}
}
@media(max-width:640px){
  h1,h2,h3{text-wrap:wrap}
  .site-header .nav-toggle{display:block!important;position:absolute;right:18px;top:17px;color:var(--ink)}
  .site-header{padding-right:62px}
  .page-hero h1{font-size:clamp(36px,10.5vw,46px);max-width:none}
  .home-copy h1{font-size:clamp(48px,15vw,68px);max-width:6.2em}
  .history-lead h2,.comparison-intro h2,.research-intro h2,.toolkit-top h2,.glossary-top h2{font-size:clamp(30px,8.4vw,34px);line-height:1.24}
  .big-question h2,.section-head h2,.content-section h2{max-width:100%}
  .section-head h2,.content-section h2{font-size:clamp(28px,8.2vw,36px)}
  .section-heading-row{display:flex;flex-direction:column;gap:10px}
  .section-glyph{order:-1;width:46px;height:46px;margin:0 0 2px}
  .section-glyph svg{width:26px;height:26px}
  .title-line{white-space:normal}
  .title-segment.fluid,.title-segment.mobile-fluid{white-space:normal}
  .term-lock{white-space:nowrap;font-size:.90em}
  .page-hero h1 .term-lock{font-size:.86em}
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
  .concept-figure{padding:12px;margin:24px 0 32px;overflow:visible}
  .concept-figure svg{min-width:0;width:100%;height:auto;transform:none}
  .concept-figure figcaption{padding:14px 6px 4px}
  .research-card{padding:24px 22px}
  .comparison-lenses{padding-left:24px;padding-right:24px}
  .curated-opening,.history-gallery,.history-place-study,.credits-intro{padding:58px 24px}
  .history-place-study{padding-top:0}
  .exhibit-pair,.portrait-grid,.credits-grid{grid-template-columns:1fr}
  .exhibit-figure.hero-exhibit .exhibit-image-wrap,.exhibit-figure.article-exhibit .exhibit-image-wrap{aspect-ratio:4/3}
  .exhibit-figure figcaption{padding:20px}
  .curator-note{grid-template-columns:1fr;gap:10px}
  .visual-index{padding:62px 24px}
  .visual-index-grid{grid-template-columns:1fr}
  .traditions-intro,.china-intro{padding:58px 22px 68px;gap:42px}
  .traditions-intro h2,.china-intro h2{font-size:clamp(31px,9vw,38px)}
  .semantic-title>span{display:block;white-space:nowrap}
  .title-line>wbr+.title-segment{display:block}
  .traditions-intro h2.semantic-title,.ai-era h2.semantic-title,.china-intro h2.semantic-title{font-size:clamp(28px,7.6vw,33px)}
  .content-section h2.semantic-title{font-size:clamp(27px,7.2vw,31px)}
  .china-principle{grid-template-columns:1fr;gap:8px}
  .china-bridge-visual{display:grid;grid-template-columns:1fr;min-height:0;gap:0;width:100%}
  .china-bridge-visual:before,.china-bridge-visual:after{display:none}
  .china-side{width:100%;padding:22px 16px}
  .china-bridge-center{width:158px;aspect-ratio:1;margin:-1px auto;padding:18px}
  .china-bridge-center strong{font-size:20px}
  .tradition-orbit{width:min(100%,360px);max-width:100%}
  .tradition-orbit>span{min-width:86px;padding:8px 9px;font-size:13px}
  .tradition-orbit>span:nth-of-type(2){left:80%}
  .tradition-orbit>span:nth-of-type(3){left:88%}
  .tradition-orbit>span:nth-of-type(6){left:12%}
  .tradition-orbit>span:nth-of-type(7){left:20%}
  .orbit-center{width:96px;height:96px}
  .orbit-center b{font-size:17px}
  .tradition-cards,.shared-grammar,.human-core-grid,.future-protocol,.do-not-collapse,.china-bridge-grid,.china-not-equal,.china-tension-grid,.china-use-grid,.china-local-grid,.source-link-grid{grid-template-columns:1fr}
  .tradition-cards article{min-height:0}
  .tradition-cards article:first-child{grid-column:auto;display:flex;min-height:0}
  .tradition-cards article:first-child .tradition-icon{margin-bottom:18px}
  .ai-era{padding:64px 22px;gap:46px}
  .ai-era h2{font-size:clamp(32px,9.5vw,42px);max-width:none}
  .ai-ring-outer{width:min(100%,360px);max-width:100%}
  .ai-ring>span{font-size:14px}
  .ai-ring-center strong{font-size:16px}
  .china-tension-section,.china-prototype{padding:64px 22px}
  .china-digital-note{padding:54px 22px;grid-template-columns:1fr;gap:18px}
  .china-digital-note h2{font-size:clamp(29px,8vw,34px)}
  .china-protocol article{grid-template-columns:58px 1fr;gap:12px}
  .china-bridge-grid article,.china-not-equal article,.china-tension-grid article,.china-use-grid article,.china-local-grid article{padding:22px}
  .source-link-grid a{align-items:flex-start;flex-direction:column;gap:4px}
  .source-link-grid span{text-align:left}
  .bilingual-process{display:grid;grid-template-columns:1fr;gap:6px;max-width:100%}
  .bilingual-process span,.bilingual-process span.wide{width:100%;min-width:0;padding:11px 16px}
  .bilingual-process i{justify-self:center;transform:rotate(90deg);line-height:1}
}

/* ---- 3.0 UX / navigation / reading system ---- */
html,body{max-width:100%;overflow-x:clip}
body{-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}

.page-hero .hero-copy{max-width:900px}
.page-hero>div{margin-inline:auto}
.page-hero p{max-width:720px;line-height:1.85}
.hero-meta{
  display:flex;
  gap:8px 18px;
  flex-wrap:wrap;
  margin-top:22px;
  color:var(--moss);
  font-size:12px;
}
.hero-meta span{display:flex;align-items:center;gap:7px}
.hero-meta span:before{content:"";width:4px;height:4px;border-radius:50%;background:var(--gold)}
.hero-line{margin-top:24px}

.article-grid{
  grid-template-columns:minmax(0,760px) minmax(250px,300px);
  gap:56px;
  max-width:1180px;
  justify-content:center;
  padding-top:42px;
}
.article-main{
  min-width:0;
  font-size:18px;
  line-height:1.92;
  counter-reset:article-section;
}
.article-main>.content-section{counter-increment:article-section}
.article-main .content-section>p{max-width:43em;font-size:1em;line-height:1.95}
.article-main .content-section li{line-height:1.85}
.article-main p a:not(.btn),.article-main li a:not(.btn),.text-link{
  text-decoration:underline;
  text-decoration-thickness:1px;
  text-underline-offset:3px;
  text-decoration-color:rgba(93,109,96,.55);
}
.article-main p a:hover,.article-main li a:hover,.text-link:hover{color:var(--moss);text-decoration-color:currentColor}

.section-eyebrow{display:flex;align-items:center;gap:0}
.section-auto-no:before{content:counter(article-section,decimal-leading-zero) " · "}
.section-eyebrow>span:last-child{min-width:0}

.site-header{
  min-height:72px;
  padding-top:10px;
  padding-bottom:10px;
}
.brand{flex:none}
.brand b{font-size:19px;line-height:1.18}
.brand small{font-size:9px;letter-spacing:.12em;margin-top:2px}
.desktop-nav{display:flex;align-items:center;gap:24px;font-size:14.5px}
.desktop-nav>a,.nav-more>summary{
  min-height:44px;
  display:flex;
  align-items:center;
  color:#46514b;
  border-bottom:1px solid transparent;
  cursor:pointer;
  list-style:none;
}
.desktop-nav>a:hover,.desktop-nav>a.active,.nav-more.active>summary,.nav-more[open]>summary{
  color:var(--ink);
  border-color:var(--gold);
}
.nav-more{position:relative}
.nav-more>summary::-webkit-details-marker{display:none}
.nav-more>summary{gap:6px}
.nav-more>summary span{font-size:11px;transition:transform .18s ease}
.nav-more[open]>summary span{transform:rotate(180deg)}
.nav-more-menu{
  position:absolute;
  right:0;
  top:calc(100% + 8px);
  width:210px;
  padding:8px;
  background:rgba(255,253,248,.98);
  border:1px solid var(--line);
  box-shadow:0 18px 45px rgba(31,39,35,.12);
  display:grid;
  z-index:50;
}
.nav-more-menu a{
  display:flex;
  align-items:center;
  min-height:42px;
  padding:7px 10px;
  border-radius:6px;
  color:var(--ink2);
}
.nav-more-menu a:hover,.nav-more-menu a.active{background:#eee7da;color:var(--ink)}
.nav-toggle,.mobile-nav,.nav-scrim{display:none}

.reading-progress{
  position:fixed;
  left:0;
  right:0;
  top:71px;
  height:2px;
  z-index:31;
  pointer-events:none;
}
.reading-progress span{display:block;width:0;height:100%;background:var(--gold);transition:width .08s linear}

a,button,input,textarea,summary{outline:none}
a:focus-visible,button:focus-visible,input:focus-visible,textarea:focus-visible,summary:focus-visible{
  outline:2px solid #8c743d;
  outline-offset:3px;
  border-radius:4px;
}
button,.btn,.filter-row button,.case-options button,.question-actions button{min-height:44px}
input,textarea{font-size:16px}

.article-rail{min-width:0;align-self:start}
.article-toc{
  position:sticky;
  top:96px;
  margin-top:54px;
  padding:20px 20px 18px;
  max-height:calc(100vh - 116px);
  overflow:auto;
  scrollbar-width:thin;
  scrollbar-color:#c5b89d transparent;
  background:#e9e2d5;
  border:1px solid var(--line);
}
.article-toc+.sources{position:relative;top:auto;margin-top:14px}
.article-toc>span{
  display:block;
  font-size:10px;
  letter-spacing:.16em;
  color:var(--moss);
  margin-bottom:10px;
  font-weight:700;
}
.article-toc ol{list-style:none;margin:0;padding:0;counter-reset:toc}
.article-toc li{counter-increment:toc}
.article-toc a{
  display:grid;
  grid-template-columns:22px 1fr;
  gap:8px;
  padding:7px 0;
  border-top:1px solid rgba(93,109,96,.16);
  color:#56605a;
  font-size:13px;
  line-height:1.58;
}
.article-toc a:before{
  content:counter(toc,decimal-leading-zero);
  color:var(--gold);
  font-size:9px;
  padding-top:2px;
}
.article-toc a:hover,.article-toc a.active{color:var(--ink)}
.article-toc a.active{font-weight:700;background:rgba(180,154,92,.10);margin-inline:-8px;padding-inline:8px;border-top-color:rgba(180,154,92,.35)}
.article-toc-mobile{display:none}

.section-glyph{
  width:38px;
  height:38px;
  opacity:.82;
  border-color:rgba(93,109,96,.28);
}
.section-glyph svg{width:22px;height:22px}
.section-eyebrow{font-size:10px;letter-spacing:.16em;color:#738078;font-weight:600}
.content-section{padding-top:50px;padding-bottom:50px}
.content-section h2[id]{scroll-margin-top:104px}

.sources{
  border-color:#d8d0c3;
  box-shadow:none;
}
.source-head strong{display:block;font:500 18px/1.3 var(--serif)}
.source-head small{display:block;margin-top:3px;font-size:9px;letter-spacing:.08em;color:var(--moss)}
.sources li b{font-size:14px}
.sources li span{line-height:1.65}

.glossary-status{
  display:flex;
  justify-content:space-between;
  align-items:center;
  gap:16px;
  margin:0 0 16px;
  color:var(--moss);
  font-size:12px;
}
.glossary-empty{
  display:none;
  padding:44px 24px;
  text-align:center;
  border:1px dashed var(--line);
  color:var(--ink2);
  background:rgba(255,253,248,.55);
}
.glossary-status button{
  border:0;
  border-bottom:1px solid currentColor;
  background:none;
  color:var(--moss);
  padding:3px 0;
  cursor:pointer;
}
.glossary-status button[hidden]{display:none}

.continue-reading{
  margin:0;
  padding:58px clamp(24px,8vw,140px) 64px;
  display:grid;
  grid-template-columns:minmax(220px,.55fr) minmax(0,1.45fr);
  gap:44px;
  align-items:start;
  border-top:1px solid var(--line);
  background:#e8e1d4;
}
.continue-reading>div:first-child>span{
  display:block;
  font-size:10px;
  letter-spacing:.16em;
  color:var(--moss);
  font-weight:700;
}
.continue-reading h2{
  font:500 clamp(27px,2.7vw,38px)/1.28 var(--serif);
  margin:9px 0 0;
}
.continue-reading h2 .title-line,.continue-reading h2 .title-segment{white-space:normal}
.continue-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.continue-grid a{
  min-height:128px;
  display:grid;
  grid-template-columns:1fr auto;
  grid-template-rows:auto 1fr;
  gap:8px 20px;
  padding:20px 22px;
  background:var(--white);
  border:1px solid var(--line);
  transition:transform .18s ease,border-color .18s ease,box-shadow .18s ease;
}
.continue-grid a:hover{
  transform:translateY(-2px);
  border-color:#b6aa98;
  box-shadow:0 12px 30px rgba(31,39,35,.06);
}
.continue-grid span{
  grid-column:1;
  font-size:10px;
  letter-spacing:.12em;
  color:var(--gold);
}
.continue-grid b{
  grid-column:1;
  align-self:end;
  font:500 20px/1.45 var(--serif);
}
.continue-grid i{
  grid-column:2;
  grid-row:1/3;
  align-self:center;
  font-style:normal;
  color:var(--moss);
  font-size:20px;
}

@media(max-width:1100px){
  .desktop-nav{display:none}
  .site-header{
    padding:10px 20px;
    padding-right:118px;
    min-height:70px;
  }
  .site-header .nav-toggle{
    position:absolute;
    right:18px;
    top:14px;
    display:flex!important;
    align-items:center;
    gap:8px;
    min-height:42px;
    padding:0 12px;
    color:var(--paper)!important;
    background:var(--ink);
    border:1px solid var(--ink);
    border-radius:999px;
    font-size:12px;
    z-index:61;
  }
  .nav-toggle-icon{width:16px;height:13px;position:relative;display:block}
  .nav-toggle-icon i{position:absolute;left:0;width:16px;height:1px;background:currentColor;transition:.2s}
  .nav-toggle-icon i:first-child{top:3px}
  .nav-toggle-icon i:last-child{top:9px}
  body.nav-open .nav-toggle-icon i:first-child{top:6px;transform:rotate(45deg)}
  body.nav-open .nav-toggle-icon i:last-child{top:6px;transform:rotate(-45deg)}
  .mobile-nav{
    display:none;
    position:fixed;
    z-index:60;
    left:12px;
    right:12px;
    top:78px;
    max-height:calc(100vh - 92px);
    overflow:auto;
    padding:18px;
    background:#fffdf8;
    border:1px solid var(--line);
    box-shadow:0 24px 70px rgba(31,39,35,.20);
  }
  .mobile-nav.open{display:grid;grid-template-columns:1fr 1fr;gap:18px}
  .mobile-nav-group{display:grid;align-content:start}
  .mobile-nav-group>span{
    padding:0 10px 8px;
    font-size:10px;
    letter-spacing:.15em;
    color:var(--gold);
    font-weight:700;
  }
  .mobile-nav a{
    min-height:46px;
    display:flex;
    align-items:center;
    padding:7px 10px;
    border-top:1px solid #e4ddd1;
    color:var(--ink2);
  }
  .mobile-nav a.active{font-weight:700;color:var(--ink);background:#f1eadf}
  .nav-scrim{
    position:fixed;
    inset:70px 0 0;
    background:rgba(31,39,35,.26);
    z-index:55;
  }
  body.nav-open .nav-scrim{display:block}
  body.nav-open{overflow:hidden}
  .reading-progress{top:69px}
  .article-grid{grid-template-columns:1fr}
  .article-rail{order:2}
  .article-toc{display:none}
  .article-toc-mobile{
    display:block;
    margin:0 0 18px;
    padding:14px 16px;
    border:1px solid var(--line);
    background:#ebe4d8;
  }
  .article-toc-mobile summary{
    cursor:pointer;
    font-size:13px;
    font-weight:700;
    color:var(--ink);
  }
  .article-toc-mobile nav{display:grid;margin-top:10px}
  .article-toc-mobile a{
    padding:9px 0;
    border-top:1px solid rgba(93,109,96,.16);
    font-size:13px;
    color:var(--ink2);
  }
  .continue-reading{grid-template-columns:1fr;gap:22px}
}

@media(max-width:640px){
  .site-header{padding-left:18px;padding-right:108px}
  .brand b{font-size:18px}
  .article-grid{padding:24px 22px 84px}
  .page-hero p{font-size:17px;line-height:1.9}
  .hero-meta{font-size:11.5px;gap:6px 14px}
  .brand small{font-size:9px}
  .brand-mark{width:32px;height:32px}
  .nav-toggle{right:14px;padding:0 11px}
  .mobile-nav{left:8px;right:8px;grid-template-columns:1fr!important;padding:14px;gap:12px}
  .home-hero{min-height:auto;padding:62px 28px 54px}
  .home-copy>p{font-size:17px;line-height:1.88}
  .home-copy h1{margin-bottom:24px}
  .circle-visual{margin-top:36px}
  .circle-visual svg{max-height:340px}
  .hero-note{margin-top:30px}
  .cta-row{gap:8px}
  .cta-row .btn{padding:11px 14px;font-size:14px}
  .content-section{padding-top:44px;padding-bottom:44px}
  .section-glyph{width:34px;height:34px}
  .section-glyph svg{width:19px;height:19px}
  .continue-reading{padding:44px 20px 50px}
  .continue-grid{grid-template-columns:1fr}
  .continue-grid a{min-height:106px}
  .glossary-status{align-items:flex-start}
}

@media(prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  .reading-progress span,.nav-toggle-icon i,.nav-more>summary span,.btn,.continue-grid a{transition:none!important}
  .circle-visual .halo{animation:none!important}
}
'''

js = r'''
(() => {
  // Navigation: explicit state, keyboard escape, scrim close, and mobile focus.
  const navToggle = document.querySelector('.nav-toggle');
  const mobileNav = document.querySelector('.mobile-nav');
  const navScrim = document.querySelector('.nav-scrim');
  let navPreviousFocus = null;
  const setNavOpen = (open, restoreFocus=false) => {
    if (!navToggle || !mobileNav) return;
    if (open) navPreviousFocus = document.activeElement;
    mobileNav.classList.toggle('open', open);
    document.body.classList.toggle('nav-open', open);
    navToggle.setAttribute('aria-expanded', String(open));
    navToggle.setAttribute('aria-label', open ? '关闭目录' : '打开目录');
    mobileNav.setAttribute('aria-hidden', String(!open));
    if (open) requestAnimationFrame(() => mobileNav.querySelector('a')?.focus());
    if (!open && restoreFocus && navPreviousFocus instanceof HTMLElement) navPreviousFocus.focus();
  };
  navToggle?.addEventListener('click', () => setNavOpen(navToggle.getAttribute('aria-expanded') !== 'true'));
  navScrim?.addEventListener('click', () => setNavOpen(false, true));
  mobileNav?.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setNavOpen(false)));
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && navToggle?.getAttribute('aria-expanded') === 'true') setNavOpen(false, true);
  });
  addEventListener('resize', () => { if (innerWidth > 1100 && navToggle?.getAttribute('aria-expanded') === 'true') setNavOpen(false); }, {passive:true});
  document.addEventListener('click', e => {
    document.querySelectorAll('.nav-more[open]').forEach(menu => {
      if (!menu.contains(e.target)) menu.removeAttribute('open');
    });
  });

  // Reading progress for every page.
  const readingBar = document.querySelector('.reading-progress span');
  const renderReadingProgress = () => {
    if (!readingBar) return;
    const root = document.documentElement;
    const max = Math.max(1, root.scrollHeight - innerHeight);
    const ratio = Math.min(1, Math.max(0, scrollY / max));
    readingBar.style.width = `${(ratio * 100).toFixed(2)}%`;
  };
  addEventListener('scroll', renderReadingProgress, {passive:true});
  addEventListener('resize', renderReadingProgress, {passive:true});
  renderReadingProgress();

  // Long-form navigation: build a desktop rail + compact mobile table of contents.
  const articleGrid = document.querySelector('.article-grid');
  const articleMain = articleGrid?.querySelector('.article-main');
  if (articleGrid && articleMain) {
    const headings = [...articleMain.querySelectorAll('.content-section h2')]
      .filter(h => h.textContent.trim().length > 0);
    if (headings.length >= 3) {
      headings.forEach((h, i) => { if (!h.id) h.id = `section-${i+1}`; });
      const links = headings.map(h => `<li><a href="#${h.id}">${h.textContent.trim()}</a></li>`).join('');
      const toc = document.createElement('nav');
      toc.className = 'article-toc';
      toc.setAttribute('aria-label', '本页导览');
      toc.innerHTML = `<span>本页导览</span><ol>${links}</ol>`;

      const rail = document.createElement('aside');
      rail.className = 'article-rail';
      rail.setAttribute('aria-label', '本页辅助导航与来源');
      rail.appendChild(toc);
      const sources = [...articleGrid.children].find(el => el.classList?.contains('sources'));
      if (sources) rail.appendChild(sources);
      articleGrid.appendChild(rail);

      const mobileToc = document.createElement('details');
      mobileToc.className = 'article-toc-mobile';
      mobileToc.innerHTML = `<summary>本页导览 · ${headings.length} 个部分</summary><nav>${headings.map(h => `<a href="#${h.id}">${h.textContent.trim()}</a>`).join('')}</nav>`;
      articleMain.insertBefore(mobileToc, articleMain.firstChild);
      mobileToc.querySelectorAll('a').forEach(a => a.addEventListener('click', () => { mobileToc.open = false; }));

      const tocLinks = [...toc.querySelectorAll('a')];
      const observer = new IntersectionObserver(entries => {
        const visible = entries.filter(x => x.isIntersecting).sort((a,b) => a.boundingClientRect.top - b.boundingClientRect.top);
        if (!visible.length) return;
        const id = visible[0].target.id;
        tocLinks.forEach(a => a.classList.toggle('active', a.getAttribute('href') === `#${id}`));
      }, {rootMargin:'-20% 0px -68% 0px', threshold:0});
      headings.forEach(h => observer.observe(h));
    }
  }

  // Interaction feedback should be announced without stealing focus.
  document.querySelectorAll('#ministryResult,#caseResult,#questionFeedback,#saveStatus').forEach(el=>el.setAttribute('aria-live','polite'));

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
  if(caseLab){const res=document.getElementById('caseResult');caseLab.querySelectorAll('[data-case]').forEach(b=>b.onclick=()=>{const k=b.dataset.case;res.innerHTML={vote:'<b>多数表决</b>优化的是速度与程序明确。7:3 很快有结果，但“离开原社区意味着什么”可能仍未被共同体真正消化。',consensus:'<b>共识（Consensus）</b>优化的是可接受度。大家会继续协商方案，但也可能把目标缩成“每个人都勉强能接受”。',sense:'<b>聚会的共同辨识（Sense of the Meeting）</b>会把问题从“新址好不好”下沉到“我们的使命、邻里关系与可持续性中，什么方向最忠实？”结果可能是搬、也可能是不搬，甚至是暂缓决定。'}[k];});}

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
  if(gSearch){
    let active='all';
    const cards=[...document.querySelectorAll('.glossary-card')];
    const filters=[...document.querySelectorAll('.filter')];
    const status=document.getElementById('glossaryStatus');
    const empty=document.getElementById('glossaryEmpty');
    const clear=document.getElementById('clearGlossary');
    function apply(){
      const q=gSearch.value.trim().toLowerCase();
      let visible=0;
      cards.forEach(c=>{
        const txt=c.dataset.term+' '+c.textContent.toLowerCase();
        const cat=c.querySelector('span').textContent;
        const show=(!q||txt.includes(q))&&(active==='all'||cat===active);
        c.style.display=show?'block':'none';
        if(show) visible++;
      });
      if(status) status.textContent=`显示 ${visible} / ${cards.length} 个术语`;
      if(empty) empty.style.display=visible?'none':'block';
      if(clear) clear.hidden=!q&&active==='all';
    }
    gSearch.addEventListener('input',apply);
    filters.forEach(b=>b.addEventListener('click',()=>{
      filters.forEach(x=>{x.classList.remove('active');x.setAttribute('aria-pressed','false');});
      b.classList.add('active');
      b.setAttribute('aria-pressed','true');
      active=b.dataset.filter;
      apply();
    }));
    clear?.addEventListener('click',()=>{
      gSearch.value='';
      active='all';
      filters.forEach(x=>{const isAll=x.dataset.filter==='all';x.classList.toggle('active',isAll);x.setAttribute('aria-pressed',String(isAll));});
      apply();
      gSearch.focus();
    });
    apply();
  }
})();
'''

(ROOT/'assets').mkdir(exist_ok=True)
(ROOT/'assets'/'style.css').write_text(css, encoding='utf-8')
(ROOT/'assets'/'app.js').write_text(js, encoding='utf-8')

# write pages
for fn, content in pages.items():
    # Localize before heading enhancement so entities such as '&' are still plain text.
    rendered = localize_visible_text(content)
    rendered = enhance_plain_headings(rendered)
    (ROOT/fn).write_text(rendered, encoding='utf-8')


# favicon
(ROOT/'assets'/'favicon.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#1f2723"/><circle cx="32" cy="32" r="5" fill="#b49a5c"/><circle cx="32" cy="32" r="14" fill="none" stroke="#b49a5c" stroke-width="1.5"/><circle cx="32" cy="32" r="23" fill="none" stroke="#d8ddd8" stroke-width="1.5" opacity=".7"/></svg>''', encoding='utf-8')

# minimal README
readme = '''# 共同等候｜Quaker Meeting 研究与实践\n\n静态网站，无构建依赖。当前版本以“策展式研究网站”为方向：原典研究、历史图像、地点史料、知识图解与可实践工具并置。\n\n## 本地预览\n\n```bash\npython3 -m http.server 8000\n```\n然后访问 `http://localhost:8000/`。\n\n## 部署\n\n整个目录可直接发布到 GitHub Pages / Netlify / Cloudflare Pages。\n\n## 内容范围\n\n当前版本以 unprogrammed Quaker Meeting、Pendle Hill 相关文本、Howard Brinton、Thomas Kelly、Parker Palmer、Patricia Loring、Michael Marsh、Jim Pym 等为主要研究入口，并明确区分历史传统、现代转译与本站的实践性整理。\n\n## 图像与史料原则\n\n- 历史人物、Meeting House 与地点照片优先使用可追溯来源的真实史料或授权照片。\n- 图说尽量保留作者、年代、授权与不确定性，不把“后世艺术印象”冒充同时代肖像。\n- 解释性 SVG 用于概念结构；若未来使用 AI 场景复原，必须明确标记为“编辑性复原 / 非历史照片”。\n- 全站图像来源与许可集中记录在 `visual-credits.html`。\n\n## 主要交互\n\n- 12 分钟 Meeting 体验计时器\n- 本地反思记录（localStorage，不上传）\n- Vocal Ministry 自我辨识练习\n- Meeting for Business 决策案例\n- Clearness Committee 开放问题练习\n- 术语搜索与分类筛选\n'''
(ROOT/'README.md').write_text(readme, encoding='utf-8')

# basic link check
files=set(p.name for p in ROOT.glob('*.html'))
broken=[]
for p in ROOT.glob('*.html'):
    txt=p.read_text(encoding='utf-8')
    for m in re.finditer(r'href="([^"]+\.html)(?:#[^"]*)?"',txt):
        href = m.group(1)
        if href.startswith(('http://','https://')):
            continue
        if href not in files:
            broken.append((p.name,href))
print(f'Wrote {len(pages)} pages. Broken links: {broken}')
