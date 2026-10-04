# 共同等候｜Quaker Meeting 研究与实践

静态网站，无构建依赖。当前版本以“策展式研究网站”为方向：原典研究、历史图像、地点史料、知识图解与可实践工具并置。

## 本地预览

```bash
python3 -m http.server 8000
```
然后访问 `http://localhost:8000/`。

## 部署

整个目录可直接发布到 GitHub Pages / Netlify / Cloudflare Pages。

## 内容范围

当前版本以 unprogrammed Quaker Meeting、Pendle Hill 相关文本、Howard Brinton、Thomas Kelly、Parker Palmer、Patricia Loring、Michael Marsh、Jim Pym 等为主要研究入口，并明确区分历史传统、现代转译与本站的实践性整理。

## 图像与史料原则

- 历史人物、Meeting House 与地点照片优先使用可追溯来源的真实史料或授权照片。
- 图说尽量保留作者、年代、授权与不确定性，不把“后世艺术印象”冒充同时代肖像。
- 解释性 SVG 用于概念结构；若未来使用 AI 场景复原，必须明确标记为“编辑性复原 / 非历史照片”。
- 全站图像来源与许可集中记录在 `visual-credits.html`。

## 主要交互

- 12 分钟 Meeting 体验计时器
- 本地反思记录（localStorage，不上传）
- Vocal Ministry 自我辨识练习
- Meeting for Business 决策案例
- Clearness Committee 开放问题练习
- 术语搜索与分类筛选
