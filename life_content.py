"""Editorial life-course feature. Stories are explicitly fictional; sources are linked."""
import html

SOURCES = [
("trustees", "受托管理与档案", "英国《信仰与实践》第15章；组织资源、法律职责与记录。", "https://qfp.quaker.org.uk/chapter/15/"),
("service", "服务的不同形式", "英国《信仰与实践》第13章；不同服务与相关支持。", "https://qfp.quaker.org.uk/chapter/13/"),
("membership", "会籍与归属", "英国《信仰与实践》第11章；涵盖儿童、成人加入及迁居。", "https://qfp.quaker.org.uk/chapter/11/"),
("children", "儿童与青年", "英国贵格会儿童与青年工作的目标、活动及支持。", "https://www.quaker.org.uk/communities/children-and-young-people"),
("care", "彼此照顾", "英国《信仰与实践》第12章；共同关怀、专业边界与保密。", "https://qfp.quaker.org.uk/chapter/12/"),
("elder", "灵性照顾者", "英国贵格会关于 Elder 的职责、年龄与任期说明。", "https://www.quaker.org.uk/blog/exploring-the-role-of-the-elder"),
("nominations", "提名与任用", "青年贵格会聚会对提名过程及全体责任的解释。", "https://yfgm.quaker.org.uk/about/explainers/nominations-process/"),
("roles", "聚会如何运作", "FGC 对书记、委员会、财务与成员参与的介绍。", "https://www.fgcquaker.org/exercises/how-does-a-quaker-meeting-work/"),
("clearness", "澄心会", "FGC 的个人辨识与共同体辨识资源。", "https://www.fgcquaker.org/fgcresources/spiritual-practices/clearness-committees/"),
("ministry", "长期服务的支持", "FGC 关于支持小组、家庭负担、经费与回顾的指导。", "https://www.fgcquaker.org/fgcresources/spiritual-practices/care-of-friends-led-to-ministry/"),
("marriage", "婚姻照管", "英国《信仰与实践》第16章；须结合当地制度阅读。", "https://qfp.quaker.org.uk/chapter/16/"),
("funeral", "葬礼与纪念聚会", "英国《信仰与实践》第17章；组织、亲属协商与敬拜。", "https://qfp.quaker.org.uk/chapter/17/"),
("local", "地方社区实例", "Langley Hill 的委员会资料，展示具体分工与紧急援助基金；不能推广为所有社区的安排。", "https://quaker.org/legacy/langleyhill/committees.html"),
("branches", "全球传统差异", "世界贵格会协商委员会美洲分部对不同敬拜形态的说明。", "https://fwccamericas.org/explore"),
("history", "角色的历史变化", "英国《信仰与实践》12.05；早期灵性照顾、后来分工及名称变化。", "https://qfp.quaker.org.uk/passage/12-05/"),
("term", "任期与交接", "英国《信仰与实践》12.07与12.09；这里的任期属于英国特定职责。", "https://qfp.quaker.org.uk/passage/12-07/"),
]
def ref(*keys):
    return '<p class="life-ref">依据：' + ' · '.join('<a href="#src-'+k+'">'+next(s[1] for s in SOURCES if s[0]==k)+'</a>' for k in keys) + '</p>'

STAGES = [
("arrival","出生与幼年","被欢迎，也让家庭有地方安顿",
"小岚第一次进入聚会所时，还躺在父亲怀里。她后来记不得这一天，却会记得门边总有人弯下身，认真叫她的名字。父母偶尔抱着哭闹的她离开房间，也不必因此觉得自己破坏了整个聚会。",
"对一个新家庭来说，最重要的可能是能否带孩子来、谁能解释聚会的安排，以及疲惫的照顾者有没有被看见。这里的故事展示一种可能的欢迎方式，并不代表每个聚会都有托育条件。",
"儿童的归属与正式会籍需要分开说明。在英国，父母可以为未成年孩子申请会籍，但这既非必需，也非预期；不同社区对儿童会籍有不同理解。不能把出生写成全球统一的入会程序。",
"欢迎者、儿童工作者与生活关怀者可以协商适合家庭的参与方式。策划示例包括轮流陪伴、提供安静休息处、在获得同意后保持联系；这些都需要真实的人力安排。",
"如果照顾孩子的人总是无法进入聚会，谁来照顾他们的归属感？",("membership","children")),
("childhood","儿童时期","自己的声音开始被认真听见",
"七岁的小岚在儿童活动中画了一棵有很多门的树。带领者没有急着替她解释，只问她愿不愿意讲讲谁住在里面。她慢慢发现，安静可以有不同样子，也可以伴随着画画、走路和提问。",
"这一阶段可以探索友谊、公平、冲突与自然。孩子未必能长时间静坐，活动也不能只把他们安排在成人聚会之外；他们需要体验自己确实是共同生活的一部分。",
"英国儿童与青年工作的目标包括探索灵性、体验社区和参与改变世界。故事、游戏与绘画是本专题的呈现建议，具体课程应依年龄和当地资源决定。",
"儿童工作者组织适龄活动并支持家长；社区要倾听儿童的经验。可安排跨年龄共学，让孩子也讲述自己所关心的问题，而不是只让成年人对他们讲话。",
"当一个孩子提出成人没有答案的问题，社区能否陪他继续探索？",("children",)),
("youth","青少年时期","从家人的选择走向自己的选择",
"十五岁时，小岚说自己不想再跟父母来聚会。她觉得成人谈和平，却也会在会议上互相不耐烦。一位熟悉她的会友没有辩解，约她散步，问她这些年在这里感到过什么，又失望过什么。",
"人物会面对学业、同伴、身份与家庭期待，也可能质疑信仰。少来聚会不应被剧情自动解释成叛逆，更不能让某一次深刻体验成为她必须留下的理由。",
"英国的会籍指导承认儿童可能选择与父母不同的道路，并强调对青年决定保持敏感。参加青年活动、正式会籍和个人信仰，彼此相关，却不是同一个问题。",
"在这个故事中，社区提供同龄人活动与可信任的成年人；关系建立在青年愿意参与的基础上。遇到重要选择时可以考虑澄心会，但不能让青年感觉自己正接受集体审问。",
"我们是在帮助年轻人长出自己的判断，还是希望他们重复我们的答案？",("membership","clearness")),
("leaving","青年与离家","在陌生地方重新建立关系",
"二十二岁的小岚搬去另一座城市。新聚会的座椅、说话节奏和茶点都不同。她起初只坐在门边，几个月后才愿意留下聊天，也开始意识到，熟悉贵格会并不等于熟悉每一个贵格会社区。",
"读书、求职、迁居和经济压力可能使参与时断时续。人物也可能长期离开，直到生命转折时返回；时间轴允许这种往复。",
"英国有迁居联络与会籍转移安排，原社区和新社区可以协助建立联系。行政转移并不能替代真实关系，新的归属仍需要共同生活慢慢形成。",
"新社区的欢迎者解释实践，关怀者了解她是否需要联系。个人可以先参与，再决定是否加入或转移会籍；程序与时间应按当地安排说明。",
"我们怎样迎接一个已经有故事的人，而不把他当作需要从头教起的新人？",("membership",)),
("belonging","成年后的加入","把归属变成双方的承诺",
"支线人物阿宁四十一岁才第一次来到聚会。她并没有一套完整的信仰说法，只知道在这里能够承认自己不知道。参加一段时间后，她开始问：如果这里是我的精神家园，我愿意为它承担什么？",
"成年加入的人可以先作为常来参与者建立联系。有人会申请正式会籍，也有人长期参与而不申请；参与哪些职责，仍要看当地规则。",
"英国把加入视为个人与社区双方的辨识：申请人理解归属与责任，社区也确认是否适合接纳。过程可能包括探访、讨论或澄心会，由相关聚会作正式决定。",
"欢迎与灵性陪伴应在申请前后持续。故事可呈现双方商量一项可承担的贡献，避免把入会写成购买服务，或要求个人先达到某种灵性成就。",
"我愿意把什么带给这个家？这个家又愿意怎样认识和支持我？",("membership","roles")),
("relationships","亲密关系与家庭","让承诺进入共同生活",
"小岚与伴侣决定结婚时，真正难谈的不是典礼，而是钱、照顾老人和彼此需要的独处。他们与几位会友共同辨识，也谈到伴侣并非贵格会士，这段关系将怎样与社区相处。",
"婚姻、独身、不生育、养育与不同家庭形态都应有叙事位置。关系也可能破裂；这时需要聆听双方的处境，不能把维持表面和谐当作唯一目标。",
"一些贵格会社区接受婚姻在其照管之下，并有婚前辨识与组织程序。英国的正式婚姻制度有当地法律背景，不能原样移植到其他国家。不同分支对伴侣关系也存在差异。",
"剧情可以让婚姻联络者说明程序，让关怀小组讨论婚后联系。若涉及暴力或安全问题，应及时连接适当的外部支持，而不以一般关系对话取代处理。",
"社区支持的是两个人真实而自由的承诺，还是我们心中的家庭样子？",("marriage","care")),
("work","工作与谋生","把信念带进每天的选择",
"三十六岁时，小岚的公司接到一项令她不安的业务。她想离职，又担心家庭失去收入。澄心会没有把她推向一个漂亮结局，而是陪她分清：哪些是事实，哪些是恐惧，哪些是自己真正愿意承担的后果。",
"诚实、和平、平等与简朴会碰到薪资、客户、住房与照顾责任。职业生活可以是实践信念的场所，但不能假设贵格会士只从事某些职业，或会因信仰获得工作保障。",
"澄心会可以帮助个人辨明重要选择；社区是否认可、资助一项对外服务，则还要进行相应的共同辨识。个人职业选择与代表社区行动应当分开。",
"策划示例可以安排求职信息交流、技能互助与生活关怀。有紧急基金的地方社区可能提供有限帮助，但这不构成普遍的薪资、就业或住房承诺。",
"在现实条件中，我能怎样更忠于良心，并认真照顾受我决定影响的人？",("clearness","local")),
("service","承担社区职责","能力被看见，责任也被说清楚",
"小岚四十二岁时被邀请参与生活关怀。她很愿意，却以为自己必须随时接电话。第一次交接中，前任告诉她：要先说清楚能承担的时间，还要知道什么情况应请其他人一起处理。",
"角色通常从日常关系与能力中逐渐被辨认。一个善于倾听的人可能参与关怀，熟悉财务的人可能照管账目；能力、意愿与当下生活条件需要一起考虑。",
"提名是社区辨识合适承担者的过程，正式职责一般需由相应聚会确认；简单日常劳动也可能由自愿者直接承担。不能把所有贡献都变成复杂任命。",
"社区应给出任务范围、交接资料、学习机会与同伴联系。本专题建议定期回顾负担，让家庭与职业繁忙的人能协商分工，而非默认可靠的人永远有空。",
"如果我们邀请一个人承担责任，是否也已经准备好支持他？",("nominations","term")),
("calling","中年转折与长期服务","让行动得到陪伴与检验",
"后来，小岚希望投入青年和平教育。她花了很久辨识这项愿望，也听见家人担心她过度投入。社区没有只说一句鼓励，而是一起看时间、能力和经费，并约定数月后再回顾。",
"一项持续的关切可能逐渐成为服务召唤，但热情并不能单独证明方向。工作内容、合作方式、家庭影响与现实资源，都需要进入辨识。",
"FGC 的服务支持指导介绍持续支持小组及服务纪要：社区可承认一项具体工作，并陪伴承担者。认可并不意味着成员都必须参与，资助也需要明确条件。",
"支持小组可以讨论方向变化、工作成果、经费及休息，必要时建议暂停、转型或结束。服务者仍需要接受质询；社区也要检查是否只赞美奉献，却忽略代价。",
"这项行动是否仍有生命力？我们是否允许它改变，甚至结束？",("ministry",)),
("crisis","疾病、失去与耗竭","接受照顾也是一种学习",
"五十六岁时，小岚经历了丧亲，又因长期劳累病倒。她第一次不想参加任何讨论。会友先问她愿意怎样保持联系，有人陪她坐一会儿，有人协商帮忙送饭，也有人帮她把正在承担的事务交出去。",
"疾病、失业、离婚、抑郁和丧亲不会按照年龄表出现，所以这是贯穿整条旅程的分支。人物不必通过一次聚会就恢复，更不必把苦难立即解释成成长。",
"英国的关怀指导强调倾听、保密、了解实际需要，也承认有些需要超出会友能力，应寻求专业帮助。静默陪伴可以支持人，但不能被写成治疗保证。",
"故事中的帮助要由当事人同意并落实到具体人、时间和后续联系。照顾者也应有人支持；当资源不足时，要坦诚商量其他渠道，不能靠一位志愿者无限承担。",
"当一个人已经无法贡献，我们的关系是否仍然可靠？",("care",)),
("ageing","晚年与交棒","放下职务，保留关系",
"七十一岁的小岚结束了又一个任期。她把联系人与待办事项整理给继任者，也忍住每件事都想插手的冲动。后来她行动不便，会友来接她参加聚会；有时她只能在家里与两个人静坐。",
"退休既可能带来新的时间，也可能伴随身体变化、孤独与经济压力。故事要区分年龄、经验与能力：年长者不自动成为灵性照顾者，年轻人也可能承担重要职责。",
"英国灵性照顾职责的说明强调任期与交接，并不以年龄作为资格。卸任后，个人仍可参与，也可以休息；职务结束不能等于关系结束。",
"接送、家中探访或适合的远程联系是本专题建议的可选安排，需看本人意愿和社区条件。经验传递可以通过共同工作完成，同时给继任者真正的决定空间。",
"我们能否珍惜一个人，同时允许他不再承担原来的工作？",("elder","term")),
("farewell","临终、死亡与身后","共同承受告别，继续照顾活着的人",
"小岚生命的最后阶段，家人与会友商量她希望怎样被陪伴。她去世后的纪念聚会里，有人讲起一段小事，也有人始终沉默。几个月后，她的伴侣仍会收到问候；悲伤没有因为典礼结束就结束。",
"临终意愿、亲属关系、葬礼安排与遗属需要都要被认真对待。故事中的医疗及临终照护由相应专业系统承担，社区提供的陪伴依本人和家人的意愿安排。",
"英国贵格会葬礼与纪念聚会没有必须套用的刚性形式；相关会友与亲属商议，灵性照顾者帮助聚会合宜开展。纪念聚会也可在不同时间另行举行。",
"社区可以解释静默和分享方式、协调联络与后续探访。留下的文字与记忆应真实，不必把逝者写成毫无缺点的人；是否形成正式纪念文字，应按当地传统处理。",
"一个人离开之后，我们怎样让他的亲人继续拥有关系，也允许记忆保持真实？",("funeral",)),
]

ROLES = [
("参与者与成员","归属与共同贡献","参与敬拜、学习与日常生活，以合适方式贡献时间、能力和资源。常来参与者与正式成员并不完全相同；是否能担任特定职位，按当地规则决定。","通过参与建立关系；正式会籍需依当地程序辨识。","没有职务也仍是社区中的人。"),
("议事主持人／书记","Clerk","准备议题、主持议事、帮助群体辨认并表述共同决定，保持沟通。其职责需要判断与经验，不能把自己的偏好直接当作聚会的决定。","经提名与相关聚会确认；可以由助手或共同书记协作。","需要清楚的授权与熟悉议事的人支持。"),
("记录书记","Recording Clerk","把聚会形成的决定准确写下来，分清决定、待办与尚未清楚的问题。记录不是逐字抄下所有发言，而是让后续工作有可靠依据。","经当地任用程序进入，学习当地纪要方式。","需与主持书记配合，并留出核对时间。"),
("灵性照顾者","Elder，传统称长老","关照敬拜质量与灵性生活，帮助会友理解实践、辨识分享及服务。有些地方由委员会共同承担；这项职责不以年纪或资历奖励为基础。","在英国通常是有任期的任用；不能推广为全球统一制度。","需要同伴交流、培训与卸任空间。"),
("生活关怀者","Pastoral care","了解会友及参与者的需要，协调联系、探访与实际帮助。照顾依赖熟悉关系，也需要保密意识和识别能力边界。","可能由专门小组、任用者或与灵性照顾合并的团队承担。","需要分工与专业转介，不能要求随时承担所有困难。"),
("提名委员会","Nominations","了解职责空缺和人们的能力、意愿与处境，提出合适人选。既考虑社区需要，也考虑承担者能否在职责中学习和成长。","由相应聚会按自己的程序设立。","应避免长期依赖同一小圈子，并说明任务而非只说缺人。"),
("财务负责人与受托管理者","资源与法律责任","财务工作包括预算、账目与报告；在有相应法人或慈善机构的地方，受托管理者承担特定法律责任。两者相关，但不能随意混为同一职位。","依据当地组织结构与法律安排任用。","需要清晰流程、必要专业知识和持续交接。"),
("儿童、青年与家庭工作者","跨年龄社区","组织合适的学习与活动，支持儿童表达和家长参与。不同地方可能设协调者、教师、青年工作者或倡议联络人。","按任务招募、任用或雇用，并获得相应培训。","工作条件应让照顾者能持续承担，而非靠热情硬撑。"),
("欢迎、联谊与场地工作者","让共同生活能够发生","接待新人、准备共同用餐、维护聚会所和组织日常活动。看似普通的劳动，会直接影响人是否感到欢迎以及能否顺利参与。","简单任务可自愿认领；长期事务可能由小组承担。","劳动需被看见，也需要轮换和实际预算。"),
("澄心会参与者","具体问题的共同辨识","围绕个人、婚姻或服务的具体问题共同等候、聆听与提问。个人澄清与社区判断能否承担支持，有时会在同一过程相遇，但须说明目的。","依具体需要与当地程序组织；通常具有临时性。","先说明问题、参与者、保密与结束方式。"),
("持续支持小组","Anchor / support committee","在一项已得到社区照管的服务期间持续陪伴，回顾方向、家庭负担、资源与成果，必要时提出调整建议。并非每个人都必须配一个小组。","针对特定服务设立，安排回顾周期。","支持与责任相连，经费与结束条件应明确。"),
("公共行动与对外联络者","和平、公义及更广网络","组织社区认可的行动，与其他贵格会机构及社会伙伴联系。成员个人关心的议题，不自动成为整个社区的立场。","可由工作小组或被任用的代表承担。","需要具体授权，行动后把经验和责任带回社区。"),
("婚姻与告别联络者","重要生命事件","与伴侣、亲属及相关会友协商，解释婚姻或葬礼安排，并协调实际工作。英国婚姻登记职责具有当地法律背景；灵性照顾者与联络者的工作可能相互配合。","依当地制度明确任用或委托，相关专业职责另行说明。","需要清楚的程序与替补安排，也应与持续生活关怀衔接。"),
("档案与通信工作者","共同体的记忆","维护相关记录、通信及档案，使会籍、决议和社区历史可以连续传递。资料管理需要尊重隐私，个人关怀记录不应随意变成公开故事。","可由指定会友或小组承担，规模较大的组织可能有专职人员。","需要明确保存与访问规则，交接时避免资料只掌握在一个人手里。"),
("分享者与受认可的服务者","能力与召唤","静默聚会中的受感分享，不要求每个人先获得固定职位。有些传统会正式认可具有特定服务能力的人；一项工作受社区照管，也不自动等同于牧师身份。","各传统对认可方式不同，不能与正式职务或个人热情混为一谈。","可以通过同伴交流和持续支持小组检视工作，保留调整或结束的可能。"),
("牧师及受雇工作人员","其他传统与组织条件","有牧师的贵格会传统可以包含讲道、教导与牧养；其他社区也可能聘用行政、清洁或儿童工作人员。有薪工作需单独说明雇用责任。","由当地教会或组织按所属传统任用或雇用。","薪资、职责与支持按实际制度约定，不能用无薪志愿角色的模板代替。"),
]
SUPPORT = [
("daily","日常生活","先认识一个人，才可能知道怎样支持他。",
"共同用餐、聊天、欢迎和持续联系，使社区逐渐知道谁正在照顾病人、谁最近搬家、谁长期没有来。具体帮助要先询问；一个人的缺席可能有许多原因，不能擅自解释。",
"示例：关怀者先询问一位术后会友需要什么，再协调两周送饭与交通；每件事都有明确承担者和结束日期。"),
("work","工作与家庭","让辨识面对收入、时间和受影响的人。",
"倾听与澄心会帮助分清选择，地方社区也可能交流信息或提供有限援助。但会众主要仍依自己的工作及家庭、社会支持系统生活，社区并不普遍提供就业与终身供养。",
"示例：一位会友想转行，支持者帮他列出实际条件与需要咨询的问题；决定仍由他承担，社区援助则另行商量。"),
("spirit","灵性成长","共同等候，也把经验带回现实。",
"敬拜、共学与同伴交流，可以帮助人认识自己的经验。成长也可能体现为更诚实地道歉、重新安排时间、面对冲突及照顾家人；不能只用分享次数或特别体验来衡量。",
"示例：学习小组读一段文本后，成员讨论它怎样影响一次实际争执，并约定下次回顾，而不急着形成统一答案。"),
("responsibility","承担职责","受托的人也需要有人支持。",
"清楚的任务范围、可学习的程序、同伴关系与交接，能让职责持续。本专题建议任用时一并商量时间投入、求助渠道与退出方式，避免把照顾社区等同于牺牲个人生活。",
"示例：新任书记与前任共同准备两次议事，再独立承担；半年后由相关小组回顾负担和所需协助。"),
("ministry","长期公共服务","把热情落实为可承担的承诺。",
"对于受社区照管的服务，可以定期查看方向、能力、家庭、资源与工作结果。支持不只是在困难时鼓励，也包括诚实讨论是否缩小范围、暂停或结束。",
"示例：和平教育项目获六个月有限支持，期满后讨论效果与资金条件；这些时间与额度是示例，不是贵格会通用规定。"),
("grief","疾病与告别","关系要延续到活动之外。",
"陪伴生病、衰老与失去的人，需要尊重联系意愿和实际能力。必要时连接外部专业服务。葬礼之后，遗属仍可能需要长期联系，但频率与方式应一起商量。",
"示例：纪念聚会一个月后，关怀者再次询问家属愿意怎样保持关系，而非以一次探访作为所有关怀的终点。"),
]

LIFE_CSS = r"""
body[data-page="life.html"] .life-wrap{max-width:1240px;margin:auto;padding:36px clamp(22px,5vw,72px) 70px}
.life-lead{display:grid;grid-template-columns:1.15fr 1fr;gap:34px;align-items:center;padding:26px 0 42px}
.life-lead p{font-size:17px;line-height:1.95}.life-note{padding:22px 26px;background:var(--white);border-left:3px solid var(--gold);margin:24px 0}
.life-note p{margin:8px 0}.life-map{margin:0;background:var(--paper2);padding:20px;border:1px solid var(--line);border-radius:160px 160px 12px 12px}
.life-map svg{display:block;width:100%;height:auto}.life-map figcaption{text-align:center;font-size:13px;color:var(--moss);margin-top:10px}
.life-jumps{display:flex;flex-wrap:wrap;gap:8px;margin:22px 0}.life-jumps a{border:1px solid var(--line);border-radius:30px;padding:7px 14px;font-size:14px;background:var(--white)}
.life-jumps a:hover,.life-jumps a:focus-visible{border-color:var(--moss);background:var(--paper2)}
.life-chapter{padding:30px 0 36px;border-top:1px solid var(--line);scroll-margin-top:110px}
.life-chapter-head{display:flex;align-items:flex-start;gap:18px}.life-number{font:italic 38px/1.3 var(--serif);color:var(--gold);min-width:50px}
.life-chapter-head small{color:var(--moss);font-size:13px}.life-chapter h3{font:500 clamp(24px,2.6vw,34px)/1.5 var(--serif);margin:6px 0 20px}
.life-story{font-family:var(--serif);font-size:19px;line-height:2;background:var(--paper2);padding:24px 28px;border-radius:4px;margin:0 0 22px}
.life-columns{display:grid;grid-template-columns:1fr 1fr;gap:20px 30px}.life-columns h4{margin:0;color:var(--moss);font-size:14px}.life-columns p{margin:8px 0 18px;line-height:1.95}
.life-query{border-left:2px solid var(--gold);padding:8px 18px;margin:20px 0;font-family:var(--serif);font-size:18px}
.life-ref{font-size:13px;color:var(--moss)}.life-ref a{text-decoration:underline;text-underline-offset:4px}
.life-roles{display:grid;grid-template-columns:1fr 1fr;gap:16px}.life-role{padding:23px;background:var(--white);border:1px solid var(--line)}
.life-role>small{font-size:12px;color:var(--moss)}.life-role h3{font:500 24px/1.5 var(--serif);margin:6px 0 14px}.life-role p{line-height:1.9}
.life-role details{border-top:1px solid var(--line);padding-top:12px}.life-role summary{cursor:pointer;font-size:14px;color:var(--moss)}.life-role details p{font-size:14px}
.life-process{list-style:none;padding:0;counter-reset:life-process;display:grid;grid-template-columns:1fr 1fr;gap:18px}
.life-process li{counter-increment:life-process;border:1px solid var(--line);padding:22px;background:var(--white)}
.life-process li:before{content:counter(life-process,decimal-leading-zero);display:block;color:var(--gold);font:italic 30px var(--serif);margin-bottom:10px}
.life-process b{font-size:19px;font-family:var(--serif)}.life-process p{margin-bottom:0}
.life-switch{display:flex;gap:10px;flex-wrap:wrap;margin:20px 0}.life-switch button{padding:10px 18px;border:1px solid var(--moss);background:transparent;color:var(--ink);cursor:pointer;border-radius:28px}
.life-switch button[aria-pressed="true"]{background:var(--ink);color:var(--paper)}
.life-support{border:1px solid var(--line);padding:24px;margin:16px 0;background:var(--white)}
.life-support summary{cursor:pointer;font:500 22px/1.5 var(--serif)}.life-support summary small{display:block;font:14px/1.8 var(--sans);color:var(--moss);margin:7px 0}
.life-view{color:var(--moss);border-top:1px solid var(--line);padding-top:16px}
.life-history{display:grid;gap:14px;border-left:2px solid var(--gold);padding-left:22px}.life-history article{padding:12px 0}
.life-history h3{font:500 23px/1.5 var(--serif);margin:0}.life-sources{display:grid;grid-template-columns:1fr 1fr;gap:15px}
.life-sources article{padding:20px;border:1px solid var(--line);scroll-margin-top:110px}
.life-sources a{text-decoration:underline;text-underline-offset:4px}.life-sources p{font-size:14px;color:var(--moss);margin-bottom:0}
.life-template{display:grid;grid-template-columns:1fr 1fr;gap:16px}.life-template div{border-top:1px solid var(--line);padding:18px 0}
body[data-page="life.html"] .content-section{padding:40px 0;margin:0}
@media(max-width:720px){.life-lead,.life-columns,.life-roles,.life-process,.life-sources,.life-template{grid-template-columns:1fr}.life-map{max-width:380px;margin:auto}.life-story{padding:20px;font-size:18px}.life-number{min-width:40px;font-size:32px}.life-chapter-head{gap:12px}.life-role h3{font-size:23px}}
@media print{.life-switch{display:none}.life-wrap details{display:block}.life-map{max-width:300px}.life-roles,.life-sources{grid-template-columns:1fr}.life-chapter{break-inside:auto}}
"""
LIFE_JS = """<script>
(()=>{const root=document.querySelector('.life-support-area');if(!root)return;
const views={receive:'我可以说清楚需要与联系意愿，也可以询问社区目前能够提供什么。',give:'我可以先商量一项具体而有限的帮助，明确时间、能力与后续联系。'};
root.querySelectorAll('[data-life-view]').forEach(b=>b.addEventListener('click',()=>{
root.querySelectorAll('[data-life-view]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));
root.querySelectorAll('.life-view').forEach(p=>p.textContent=p.dataset[b.dataset.lifeView]);
}));})();
</script>"""

def build_life(section, page_shell):
    figure = """<figure class="life-map"><svg viewBox="0 0 400 370" role="img" aria-labelledby="life-map-title life-map-desc"><title id="life-map-title">一生中的关系与责任</title><desc id="life-map-desc">生命在童年、选择、承担与交棒之间展开，共同体持续提供关系、静默与照顾。</desc><path d="M75 270 C20 150 100 40 200 45 S370 145 330 260" fill="none" stroke="#8c9a8b" stroke-width="2"/><path d="M130 250 Q200 155 275 250" fill="none" stroke="#b49a5c" stroke-width="2"/><circle cx="200" cy="185" r="54" fill="#f2eee5" stroke="#b49a5c"/><circle cx="200" cy="185" r="70" fill="none" stroke="#b49a5c" opacity=".35"/><text x="200" y="179" text-anchor="middle" fill="#1f2723" font-size="18">共同生活</text><text x="200" y="203" text-anchor="middle" fill="#5d6d60" font-size="12">静默 · 关系 · 照顾</text><g fill="#f2eee5" stroke="#5d6d60"><circle cx="65" cy="260" r="8"/><circle cx="95" cy="89" r="8"/><circle cx="295" cy="89" r="8"/><circle cx="335" cy="260" r="8"/></g><g fill="#1f2723" font-size="16" text-anchor="middle"><text x="65" y="292">被欢迎</text><text x="95" y="66">作选择</text><text x="295" y="66">担责任</text><text x="335" y="292">交接与告别</text></g><path d="M100 330 Q200 280 300 330" fill="none" stroke="#b49a5c"/><text x="200" y="357" text-anchor="middle" fill="#5d6d60" font-size="13">需要与能力会变化，关系继续生长</text></svg><figcaption>编辑性概念图，非制度流程或灵性等级。</figcaption></figure>"""
    body = '<div class="life-wrap">'
    body += '<div class="life-lead"><div><span class="kicker">生命旅程 · 社区角色 · 彼此支持</span><p>一个人出生、长大、离家、工作，经历爱与失去，也逐渐发现自己能够承担什么。把这一生放进贵格会社区，才能看见每周的聚会怎样延伸到平日：谁欢迎新家庭，谁陪伴重要选择，谁照顾承担责任的人，谁在告别之后继续与遗属保持关系。</p><p>这份生命模板帮助我们理解关系怎样持续，职责怎样传递，以及一个人在能力变化时如何继续拥有归属。</p></div>'+figure+'</div>'
    body += '<aside class="life-note"><b>阅读约定：故事与事实分别标明</b><p>小岚与阿宁是虚构综合人物，情节用于说明可能发生的处境，不是某位真实会友的传记。“实践说明”依据所列资料；“社区可以怎样回应”和具体案例包含本站的策划建议，不能理解为所有聚会必然提供的服务。</p><p>主线参考英国及北美部分非程序化、以静默为主的社区。贵格会是具有基督教起源、且内部多样的宗教传统；有牧师的教会、保守派聚会及不同国家的制度，需要分别理解。婚姻、生育、入会和任职都是可能的分支，不是人生必修关卡。</p>'+ref('branches')+'</aside>'
    body += '<nav class="life-jumps" aria-label="专题导览"><a href="#journey">生命旅程</a><a href="#roles">社区角色</a><a href="#appointment">任用与交接</a><a href="#role-history">角色的历史</a><a href="#support">支持怎样发生</a><a href="#reality">困难与边界</a><a href="#template">复用模板</a><a href="#sources">资料出处</a></nav>'
    intro = '<p>年龄不规定精神成熟的顺序。一个人可以在任何阶段第一次来到社区，也可能离开、返回或保持松散联系。疾病、迁居和失去贯穿人生，不能只安放在某一年龄。</p><nav class="life-jumps" aria-label="生命阶段">'+''.join('<a href="#life-'+s[0]+'">'+s[1]+'</a>' for s in STAGES)+'</nav>'
    chapters=''
    for i,(key,age,title,story,question,fact,response,query,refs) in enumerate(STAGES,1):
        chapters += '<article class="life-chapter" id="life-'+key+'"><div class="life-chapter-head"><span class="life-number" aria-hidden="true">'+str(i).zfill(2)+'</span><div><small>'+age+'</small><h3>'+title+'</h3></div></div><div class="life-story"><small>虚构情境</small><p>'+story+'</p></div><div class="life-columns"><div><h4>此刻的生命问题</h4><p>'+question+'</p><h4>实践说明</h4><p>'+fact+'</p></div><div><h4>社区可以怎样回应</h4><p>'+response+'</p><p class="life-query">'+query+'</p>'+ref(*refs)+'</div></div></article>'
    body += '<div id="journey">'+section('在生命变化中，持续认识彼此',intro+chapters,'生命旅程')+'</div>'
    roles='<p>这里列出常见的工作，而不是一份人人适用的组织编制。小型聚会可能合并职责，较大的组织可能分设小组。有职务的人成为明确联络点，全体成员仍共同维持社区生活。</p><div class="life-roles">'
    for title,tag,desc,entry,support in ROLES:
        roles += '<article class="life-role"><small>'+tag+'</small><h3>'+title+'</h3><p>'+desc+'</p><details><summary>如何进入职责，怎样获得支持？</summary><p><b>进入：</b>'+entry+'</p><p><b>支持：</b>'+support+'</p></details></article>'
    roles+='</div>'+ref('roles','elder','local','branches','marriage','funeral','trustees','service')
    body += '<div id="roles">'+section('不同的人，照顾不同的事情',roles,'社区角色')+'</div>'
    process=[
    ('先辨认需要','问清楚社区现在需要什么，原职责是否仍合适。人手不足时，也可以重新分配、合并或缩小工作，而不是只寻找愿意接下全部事务的人。'),
    ('认识能力与处境','提名者了解相关经验、学习意愿、家庭与职业条件。善于倾听、能可靠完成工作、愿意共同学习，都比在聚会中显眼更值得讨论。'),
    ('邀请本人共同辨识','先说明职责、任期与可能的投入，让受邀者有时间考虑。本人愿意并不代表已经有条件承担；社区应一起商量必要支持。'),
    ('由相应聚会确认','提名是建议，正式任用依当地程序由相关聚会形成决定。记录应清楚，避免把一段时期的受托责任变成模糊的个人权威。'),
    ('交接、学习与协作','介绍现有程序、资料、联络人及未完事项，安排经验交流。建议让新任者先与熟悉工作的人共同准备，逐渐独立承担。'),
    ('回顾工作与负担','本专题建议同时回顾任务进展和承担者的生活条件。需要时调整分工、寻求协助或结束任用，不能只问工作是否完成。'),
    ('卸任并真正交棒','经验、记录与关系需要移交，继任者也需要自己的空间。卸任者可以休息或转换贡献方式，社区仍应与他保持关系。')]
    text='<p>英国灵性及生活关怀职责通常以三年为一任，可续任；这一例子不能套用于所有国家和职位。提名过程关注当下是否适合承担，任期则使责任可以重新检视和传递。</p><ol class="life-process">'+''.join('<li><b>'+a+'</b><p>'+b+'</p></li>' for a,b in process)+'</ol>'+ref('nominations','term')
    body += '<div id="appointment">'+section('从被邀请，到能够放下责任',text,'职责的生命过程')+'</div>'
    history='<div class="life-history"><article><h3>早期：共同体辨认灵性照顾的能力</h3><p>英国资料记载，1653年威廉·杜斯伯里已建议各聚会安排适合的人照顾灵性福祉。共同敬拜没有消除领导与照顾的需要，相关能力逐渐得到辨认。</p></article><article><h3>后来：生活关怀逐步形成专门分工</h3><p>十八世纪末，英国较实际的关怀工作逐渐交给另行任用的人，传统称 Overseer；灵性照顾仍与 Elder 相关。这是特定传统的演变，不能画成全球同一条发展线。</p></article><article><h3>今天：名称与组织方式继续调整</h3><p>英国在2022年要求采用其他词语替代 Overseer，因为该词与奴役及压迫的历史关联。一些社区也把灵性与生活关怀合并，或用团队方式承担。</p></article><article><h3>不同分支：牧师与委员会并存</h3><p>有牧师、讲道与固定程序的贵格会传统，需要同时理解牧师和其他工作者的职责。非程序化敬拜与自由派信仰立场也不是同义词；保守派同样可能保持静默敬拜。</p></article></div>'+ref('history','elder','branches')
    body += '<div id="role-history">'+section('角色随着社区需要而变化',history,'历史与差异')+'</div>'
    supports='<div class="life-support-area"><p>下面把支持拆成具体场景。按钮切换的是读者的观察视角，不是贵格会官方服务分类；案例均为编辑示例，需按社区的资源、意愿与制度判断。</p><div class="life-switch" role="group" aria-label="选择支持视角"><button type="button" data-life-view="receive" aria-pressed="true">我此刻需要支持</button><button type="button" data-life-view="give" aria-pressed="false">我此刻能够承担</button></div>'
    perspectives = {
        'daily': ('我可以表达希望怎样保持联系，也说清楚现在不方便参与的事情。', '我可以先认识对方的实际生活，商量一项有限而持续的联系。'),
        'work': ('我可以提出职业与家庭的真实顾虑，请求倾听或辨识，并另行讨论实际援助。', '我可以提供信息或有限的帮助，不替对方作职业决定，也不代社区承诺资助。'),
        'spirit': ('我可以带着疑问参加敬拜与共学，寻找能讨论真实经验的同伴。', '我可以共同学习与倾听，让经验接受生活检验，不急着替他人解释。'),
        'responsibility': ('我可以说明工作负担，请求培训、分工或交接，不必用无限承担证明忠诚。', '我可以协助新任者熟悉任务，安排回顾，并尊重他提出休息与卸任。'),
        'ministry': ('我可以把工作方向、家庭影响与资源条件说清楚，请社区共同辨识。', '我可以参与定期回顾，提出具体而有限的支持，也诚实讨论调整或结束。'),
        'grief': ('我可以表达希望怎样被陪伴，选择联系频率，并请求连接外部资源。', '我可以先征求同意，协调具体帮助，并在告别后继续询问需要。')
    }
    for key,title,sub,desc,example in SUPPORT:
        receive, give = perspectives[key]
        supports+='<details class="life-support" open><summary>'+title+'<small>'+sub+'</small></summary><p>'+desc+'</p><p><b>虚构示例：</b>'+example+'</p><p class="life-view" data-receive="'+html.escape(receive, quote=True)+'" data-give="'+html.escape(give, quote=True)+'">'+receive+'</p></details>'
    supports+='</div>'+ref('local','care','ministry','roles')
    body += '<div id="support">'+section('支持落实到人、时间与承诺',supports,'生活 · 工作 · 灵性')+'</div>'
    reality='<div class="life-columns"><div><h3>社区也可能让人失望</h3><p>熟悉的人容易被优先看见，安静的人可能被忽略；少数可靠的人可能长期超负荷；不愿面对的冲突也可能被沉默遮盖。这些是需要检查的失败方式，不能让漂亮的故事掩盖它们。</p><p>英国关怀指导也承认共同体会在照顾与支持上失误。一个成熟社区需要承认不足，再看谁能够修复关系，以及哪里需要外部协助。</p></div><div><h3>把可承担的帮助说清楚</h3><p>本专题建议每次支持都谈清楚：当事人愿意怎样被联系；谁承担；提供什么；什么时候回顾；什么信息需要保密。涉及专业需要时，应请合适的外部人员参与。</p><p>共同体拥有的时间和钱是有限的。明确说明限制，使个人能够继续寻找其他资源，也让志愿者不必通过无限付出来证明关心。</p></div></div><p class="life-query">如果一个成员长期缺席、无法贡献，或与多数人意见不同，我们怎样知道他的真实处境，而不急着替他下结论？</p>'+ref('care')
    body += '<div id="reality">'+section('可靠的关系，需要诚实面对限制',reality,'现实中的检验')+'</div>'
    template='<p>这份模板也可用于采访真实会友。应先取得同意，把个人经验、地方制度与编辑解释分别记录；不以一个人的经历代表所有贵格会士。</p><div class="life-template">'
    for a,b in [('一个具体时刻','发生在哪里？谁在场？本人当时面临什么困难或选择？'),('个人的理解','本人如何理解静默、信仰、关系与这次经历？保留当时的疑问和后来改变的认识。'),('真实的支持过程','谁首先知道，谁联络，谁组织，谁承担后续？帮助持续多久，哪些需要没有被满足？'),('角色如何形成','承担者怎样被邀请与任用？有哪些学习、监督、同伴及卸任安排？'),('地方制度与差异','区分本人经验与正式规则，注明国家、分支、年代及所在社区。'),('回到今日生活','这件事怎样改变了工作、关系、预算或时间？留下什么仍未解决的问题？')]:
        template+='<div><b>'+a+'</b><p>'+b+'</p></div>'
    template+='</div><p>进一步阅读：<a class="text-link" href="community.html">共同体如何形成 →</a>　<a class="text-link" href="clearness.html">澄心会怎样支持辨识 →</a>　<a class="text-link" href="business.html">社区怎样共同决定 →</a></p>'
    body += '<div id="template">'+section('把生命故事写得真实而具体',template,'采访与复用模板')+'</div>'
    sources='<p>资料核对：2026年10月9日。英国制度、FGC 指导与地方实例具有各自范围；以下为继续研究的原始入口。图解为本站绘制的编辑性概念图，人物故事均为虚构。</p><div class="life-sources">'+''.join('<article id="src-'+k+'"><a href="'+url+'" target="_blank" rel="noreferrer">'+title+' ↗</a><p>'+desc+'</p></article>' for k,title,desc,url in SOURCES)+'</div>'
    body += '<div id="sources">'+section('从故事回到可以核对的资料',sources,'资料出处')+'</div></div>'
    return page_shell('life.html','贵格会士的一生','从出生到死亡，理解一个人如何在共同体中成长、选择、承担与告别，以及社区怎样支持他的生活、工作与灵性成长。',body,label='生命与共同体',extra_js=LIFE_JS)
