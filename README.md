# AceBase

国际服电竞玩家入口（MkDocs Material）：下单 · 礼品卡 · 加速。

## 本地预览

```powershell
cd c:\1Work\acebase.cc
..\penv\Scripts\pip.exe install -r requirements.txt
..\penv\Scripts\mkdocs.exe serve -a 127.0.0.1:8003
```

打开：http://127.0.0.1:8003/

（TinyBox 默认用 8002，AceBase 用 **8003**，避免混站。）

## URL 结构

| 路径 | 说明 |
| --- | --- |
| `/` | 首页（各类目最新 6 条，由 `scripts/gen_home.py` 生成，勿手改；改完任何类目页都要重跑一次） |
| `/news/` | 游戏资讯（nav 第一格；每篇新闻一张卡，卡上没有价格，动作行「阅读原文」在卡里展开压缩稿，文中图点开是站内灯箱） |
| `/topup/` | 代储与礼品卡价格参考（18 张卡：5 款游戏代储 / 6 种礼品卡 / 7 种充值卡与充值码） |
| `/boosting/` | 游戏代练与陪玩（瓦罗兰特代练 / 英雄联盟代练 / 英雄联盟陪玩 / 坦克世界代练，每项 $9.9；四张卡） |
| `/services/` | 游戏调试服务（三角洲行动 / CS2 / 英雄联盟 / 绝地求生 / Apex / 无畏契约 电脑调试，每项 $9.9；六张卡） |
| `/sourcing/` | 代购与代拍（手办、谷子、周边；八套手办实拍样例，63 张） |
| `/faq/` | 购买指南（下单流程 / 付款 / 费用 / 常见问题） |
| `/gallery/` | 相册（手办 / 模型照片墙） |
| `/pc-components/` | 电脑组件 |
| `/games/gpu-deals/` | 显卡好价参考 |

`/gift-cards/` 与 `/cdkeys/` 2026-10-13 并回 `/topup/` 后不再是页面，两个 URL 由
`mkdocs.yml` 的 `redirect_maps` 出存根指过去（带锚点，十三张卡的 id 没改，所以
`/cdkeys/#gocash-card` 落得到卡片上）。

`/figures/` 2026-10-20 改名 `/sourcing/`（FIGURES → SOURCING，「改为代购」；
中途短暂叫过 `/proxy-buy/`），八张手办卡与 63 张图原样搬过去；`/figures/`、
`/proxy-buy/`、`/gear/`、`/tech/` 四个旧地址都由存根直接指过去，卡片 id 没改，
`/figures/#gear-13` 这类锚点仍然落在卡片上。

`/news/` 2026-10-20 接替 nav 第一格的 HOME（用户：「将 /card-test/ 改名为
news并将它替代home导航」）。它前一版是 `/card-test/` 的排版测试页，那个地址从未
进过 nav、也从未推送，所以没有存根。首页 `/` **没有删**：它仍是 `gen_home.py`
跑出来的「最近更新」流，只是不再占 nav 一格，入口是页头的字标 ACEBASE。反过来，
`/news/` 成了 nav 类目，资讯卡会经 `gen_home.py` 出现在首页第一排。

同一天的第二版（用户：「阅读原文 不需跳转到原页面，而是将原页面中的内容进行
压缩，点击阅读原文后是一个展开效果，并将原文中的图片变成灯箱效果」）：动作行从
外链改成 `ab-fold` 折子，「阅读原文 / 收起」就在原位，展开的是原文的压缩稿
（繁转简、四段 + 来源行）；文中的四张图排成 2×2，点开是站内灯箱（`photo-wall.js`
的 `.ab-news-shot`），可左右翻、Esc 关，且用 `data-buy=""` 关掉了灯箱里五秒后
弹出的购买按钮。原文不再外链，来源只写在文末。

2026-10-13 并回 Gift Cards 与 CDKeys 两格时，首页因此从 23 张缩到 12 张：
`scripts/gen_home.py` 按「每个类目取最新 6 张」抓卡，两个类目没了，那两排随之
消失；TOP-UP 有 18 张卡，按规则只上前 6 张（5 款游戏 + 第一张礼品卡）。要让首页
多露几张价格卡，改的是 `gen_home.py` 里的 `CATEGORY_LIMIT`（全站所有类目一起变）。
之后 BOOSTING（+4）、SERVICES（+6）与 NEWS（+1）各加一排，首页现在是 **23 张**。

## 部署

推送 `main` 后由 `.github/workflows/deploy-mkdocs.yml` 构建并发布到 GitHub Pages（`acebase.cc`）。
