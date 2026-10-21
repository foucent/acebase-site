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
| `/blog/` | Game News（英文；2026-10-21 前叫 `/news/`，那条地址现在指过来；**九行资讯列表**，2026-10-22 起每行 16:9 缩略图在左、标题与导语在右，Read article 跳到该条自己的页 `/blog/<slug>/`） |
| `/topup/` | Live Streaming & Entertainment Top-Ups（英文；**30 张卡**：2026-10-22 从 topuplist entertainment 分类精选的直播 / 语音房 / 社交 App 代储；卡片由 `scripts/build_topup_page.py` 生成，档位价来自 `capture_topuplist_entertainment.py` → `merge_ent_prices.py` → `prices.json`） |
| `/boosting/` | Game Boosting & Coaching（英文；数据驱动的统一代练页：12 款游戏 / 服务 / 段位阶梯来自 `docs/assets/boosting/boosting.json`，配置器只收需求、$9.9 起价、报价在聊天里给；页面到 FAQ 结束，不再列服务卡） |
| `/gift-cards/` | Gift Card Prices（英文；Amazon、Apple、Google Play、Netflix、Xbox、Kammelna 六种；卡片从 `/topup/` 复制，两页价格同源） |
| `/games/` | Game Top-Up Prices（英文；**30 张卡**：原有 5 张 + 2026-10-21 从 topuplist 游戏分类复刻的 25 款；卡片由 `scripts/build_games_page.py` 生成，档位价来自 `capture_topuplist_game.py` → `merge_game_prices.py` → `prices.json`） |
| `/gallery/` | 相册（手办 / 模型照片墙） |
| `/pc-components/` | 电脑组件 |
| `/games/gpu-deals/` | 显卡好价参考 |

`/topup/` 2026-10-22 整体换掉（用户：「同样的方式，将
https://topuplist.com/category/entertainment 页中的商品添加到 /topup/，并将原来
的 /topup/ 页中的商品删除」；问过之后选「精选约 30 款」「品牌字标」「全部用新抓
的单一来源价」）。原来的 **13 张卡全部撤掉**：六张礼品卡在 `/gift-cards/` 有同 id
副本、不受影响，七张充值码卡（Fortnite / Apex / PlayStation / Switch Online /
eShop / Steam / GoCash）从此全站不再出现，只在 `prices.json` 里留档。新页面是
**30 款**直播 / 语音房 / 社交 App 代储（Douyin、Kuaishou、Bigo、MICO、Poppo、
Tango、Starmaker、SUGO、IMO、Chamet、Likee、Telegram、Party Star、CapCut、
ZEPETO、HeeSay、Soulchill、DiDO、QQ Coin、QQ VIP、YY、Nimo TV ……），版式照
`/games/` 那一套（`--plate` + `--picker` + `--wordmark`），另加了 H1 与一句导语。
数据链与 `/games/` 同形：`scripts/capture_topuplist_entertainment.py`（同源 fetch
它的 JSON API，`lang=en` + `user_currency=USD`，USD 原价，**没有换汇这一步**；每
个 sku 记 `price - coupon_discount_amount`）→ `scripts/merge_ent_prices.py`
（`ENTERTAINMENT` 那张 30 条表是唯一事实源；中文单位（比心币 / 快币 / 抖币 / 元）
换成英文、同名取最低价、**按币种分组后组内按价格升序** —— 这些平台的档位价不随
面额递增，同一币种取最便宜的一档做卡面价；每组最多 24 档，`original_price` 更高
时首档写 `off`，卡片角标显示折扣、否则显示 `Live`）→
`scripts/build_topup_page.py`（从同一张表生成卡片与 JSON-LD，卡片区带
`TOPUP:CARDS` 标记，Product 列表同样按 `ItemList` 形状就地重写）。
合并脚本写盘前断言 30 组档位名里**一个 CJK 字符都没有**（选择器会把 title 原样
显示）。品牌图仍走 `_tmp_ocr/brand_img`，30 款全部 `prep_brands.py --safe` 出
2400×500（卡片的 `object-fit: cover` 只画中段 52%，poppo 原来的字标就占 63.6%）；
Bing 这一批已经降级，新图主要来自 Logopedia、iTunes 的 1024px 商店图与 Google Play
的 512px 图标，两张 QQ 卡特意用了不同的标（QQ COIN 用企鹅 + 「QQ」字标，QQ VIP 用
红色 SVIP 企鹅）。`/cdkeys/` 的存根原来带锚点落在那七张码卡上，锚点已失效，改指
`/gift-cards/`。首页仍是 **19 张**（TOP-UP 6 / GAME 6 / GIFT CARDS 6 / BLOG 1），
TOP-UP 那六张换成 Douyin / Kuaishou / Bigo / MICO / Poppo / Tango。`prices.json`
的 `updated` 与 `games-prices.js` 的缓存字面量升到 `20261022`；`update_prices.py`
**不要跑**（它会整份重写 prices.json，只剩 4 个键）。新增探针
`_tmp_ocr/topup_page_probe.py`（30 张卡、选择器、标题价、品牌图、JSON-LD 顺序、
无 CJK、首页 19 张、四档宽度）；`_tmp_ocr` 里写死 13/18/22 张的旧探针
（`game_category_probe`、`gift_cards_probe`、`verify_topup_cards`、
`_topup_merge_check`、`_topup_cut_check` 等）是历史脚本，本次不维护。

**2026-10-21 英文改写**：`/blog/`、`/games/`、`/topup/`、`/gift-cards/`、`/boosting/`
五页的可见文字（frontmatter 的 title/description、H1 与导语、卡片标题/文案/角标/页脚、
alt / aria-label / data-caption、`data-crisp-msg` 聊天话术、JSON-LD、页尾「相关」云）
全部换成英文；HTML 注释仍是中文。连带改：`prices.json` 里 hok 的点券档位、
kammelna 的天数/金卡、Switch Online 的月数改成英文（`games-prices.js` 去掉
`document.lang` 判断、只发英文，缓存版本升到 20261021）；`gen_home.py` 的首页
title/description/「Latest updates」/页脚；`/games/gpu-deals/`、`/pc-components/`
「相关」云里的链接文字。**站级外壳仍是中文**（页头搜索框、抽屉、页脚、
「在线咨询」浮层，以及 `<html lang="zh">`），因为其余页面还是中文。

`/boosting/` 2026-10-21 改成**能兼容所有游戏的统一代练页**（用户：参考
Eldorado 的 Valorant boosting 页，「修改为一个能兼容所有游戏的统一的boosting页」）：
「选游戏 → 选服务 → 段位 / 服务器 / 选项 → 聊天报价」的配置器 + 流程 / 保障 /
FAQ，页面到 FAQ 结束。游戏清单与每款游戏的段位阶梯、服务、字段、选项都在
`docs/assets/boosting/boosting.json`（12 款，目前含 VALORANT、League of Legends、
CS2、Dota 2、Apex Legends、Fortnite、Overwatch 2、Rainbow Six Siege、Rocket League、
Call of Duty、Marvel Rivals、World of Tanks）；**加游戏只改这个 JSON**，同时把
`docs/javascripts/boosting.js` 顶部的 `?v=` 缓存版本改掉。脚本只认
`[data-boost-root]`，别的页不会跑；样式在 `docs/stylesheets/boosting.css`。
价格口径没变：起价 $9.9，配置器不算价，最终报价在 Crisp 聊天里给。
**同日用户又要求「Featured services 以下的内容去掉」**：原来的四张服务卡和
Related 云整段删掉，所以 `/boosting/` 不再向首页供卡，`gen_home.py` 现在抓到
BOOSTING 0 张，首页从 **22 张变 18 张**（TOP-UP 6 / GAME 5 / GIFT CARDS 6 /
BLOG 1）。JSON-LD 里仍保留那四个 Product。全页没有 article 标签，配置器也不会
被复制到首页。

2026-10-21 同一天还**全站去掉了左侧导航栏**（用户：「将左侧的导航去掉」→「是所有的」）：
`docs/stylesheets/extra.css` 末尾一段 `@media (min-width: 76.25em)` 把
`.md-sidebar--primary` 设为 `display: none`，再让 `.md-main__inner` 居中、
`.md-content` 为 `flex: 0 1 1000px`（**用 px 不用 rem**：Material 根字号是 125%，
`62.5rem` 会算成 1250px，限制不住；1000px 减去页边距正好是 `.ab-mag` 的 960px）。
规则必须留在媒体查询里 —— 76.25em 以下同一个元素就是抽屉本体，拿出来写会让手机
没有菜单。页头的两行主导航（`.ab-mainnav`）不变；`/` 仍靠 frontmatter 的
`hide: navigation` 在手机上也不出抽屉，其余页面手机端照常有汉堡。

`/cdkeys/` 2026-10-13 并回 `/topup/` 后不再是页面，URL 由 `mkdocs.yml` 的
`redirect_maps` 出存根指过去（带锚点，七张卡的 id 没改，所以
`/cdkeys/#gocash-card` 落得到卡片上）。`/gift-cards/` 同一天也并了回去，但
2026-10-21 又变回正式页面 —— 见下一条。**2026-10-22 那七张码卡撤掉后锚点失效，
`/cdkeys/` 的存根改指 `/gift-cards/`**（数字码那一页）。

`/figures/` 2026-10-20 改名 `/sourcing/`（FIGURES → SOURCING，「改为代购」；
中途短暂叫过 `/proxy-buy/`），八张手办卡与 63 张图原样搬过去；`/figures/`、
`/proxy-buy/`、`/gear/`、`/tech/` 四个旧地址都由存根直接指过去，卡片 id 没改，
`/figures/#gear-13` 这类锚点当时仍然落在卡片上。**2026-10-21 那八张卡随整页删掉，
这四条存根改指首页**（见下一条）。

`/sourcing/` 2026-10-21 换成 Gift Cards（用户：「将 /sourcing/ 改为 Gift Cards，
包括链接」）：URL 改回 `/gift-cards/`（这个地址 09-24 到 10-13 之间正是礼品卡的
正式地址），六张礼品卡从 `/topup/` **复制**过来 —— `/topup/` 原样保留，两页的
档位价都由 `prices.json` + `games-prices.js` 按 `data-game` 填，改价不用改标记，
改卡上的静态文案才要改两处。原来的八张手办卡随页面删掉，63 张图仍留在
`docs/assets/gallery/gear/`；`/sourcing/` 由存根指 `/gift-cards/`。首页的
SOURCING 那一排换成六张礼品卡，总数仍是 17 张。

`/games/` 2026-10-21 新增（用户：「增加一个Game类目」）：问过之后选的是「游戏代储
汇总页」—— `/topup/` 开头 5 张游戏代储卡（PUBG Mobile UC / PUBG G-COIN /
Honor of Kings / Arena Breakout / 燕云十六声）整块搬过去，卡片 id 与 `data-game`
没改，价格仍由 `prices.json` + `games-prices.js` 填；`/topup/` 只剩 6 张礼品卡
+ 7 张充值卡，标题跟着改成「礼品卡与充值卡价格参考」。`/topup/#pubg-mobile`
这类锚点因此失效，五个游戏详情页、`games/honor-of-kings` 与 `games/topup-prices`
的存根都改指 `/games/`（锚点落在新页同名卡上）。首页因此多一排 GAME 5 张，
从 17 张回到 **22 张**。

`/games/` 2026-10-21 同日晚些从 **5 张扩到 30 张**（用户：「将
https://topuplist.com/category/game-top-up 页中的商品以 /games/ 页中的样式为
模板，复刻到 /games/ 页中」；问过之后选「精选 30 款」「品牌字标」「现有 5 款各自
保留」）。**新增的 25 款**按 topuplist 分类页自己的顺序取，跳过 `/topup/` 已上架的
同款；卡片版式一字未改（`--picker` + `--wordmark`），仍由 `prices.json` +
`games-prices.js` 填档位价。数据链：`scripts/capture_topuplist_game.py`（同源
fetch 它的 JSON API，lang=en + user_currency=USD，不换汇）→
`scripts/merge_game_prices.py`（区服重名取无后缀/档位最多的那套，同名取最低价，
档位名英文化，写 `prices.json`）→ `scripts/build_games_page.py`（从同一张
`GAMES` 表生成卡片与 JSON-LD）。**卡片区有 `GAMES:CARDS` 标记，Product 列表没有**
—— 它在一个 `ld+json` 脚本块里，HTML 注释不是合法 JSON，带标记的那版会让整个
`@graph` 解析失败，所以脚本改成按 `"@type": "ItemList"` 后面那
`"itemListElement": [ … ]` 的形状就地重写。价格口径：原有 5 张仍是多来源区间，
新卡是 topuplist 单一来源换算后的三个相同数字。品牌图走 `_tmp_ocr/brand_img`
（一款一进程抓，Bing 连抓会降级成无关图；Steam 的 `logo_2x.png`、Wikipedia、
Logopedia 三路兜底），`prep_brands.py --safe` 出 2400×500 透明横幅 ——
**`--safe` 是必须的**：卡片的 `object-fit: cover` 只画中段 52%，没加 safe 的
旧图（PSN、eShop）字尾就是这样被切掉的。首页 GAME 那排 5 → 6 张（第六张是
Free Fire），总数 **18 → 19 张**（TOP-UP 6 / GAME 6 / GIFT CARDS 6 / BLOG 1）。

2026-10-22 整页换成**资讯列表**（用户：「模仿
https://www.topuplive.com/news/ 页中的排版，并将第一页的内容添到 /blog/
（把内容改成符合自己网站的），并去掉 Haruo the Alien …… 卡片」）。问过之后定
两件事：来源站第一页的内容**全部改写进来**、首页 BLOG **仍只取 1 张**。结果是
**九行**横排卡（第十条是对方自家 2024 年的招商稿，没收：正文通篇是对方的平台，
图上也印满对方品牌）：缩略图 16:9 在左，标题（句首大写 22px）、`日期 · 游戏`、
两三行导语、"Read article" 在右。
每条一张 `docs/assets/news/<slug>/cover.jpg`（1000×563，`_tmp_ocr/news_covers.py`
从来源站列表缩略图裁出来；ZZZ 3.3 那张原图 2.47:1、标题横贯整幅，改用模糊底
+ 整图居中的画法）。CSS 是 `uncrate.css` 的 `.ab-newsfeed` / `.ab-card--row`；
Haruo 那张卡、文中 2×2 图集、`.ab-news-shot` 与 `photo-wall.js` 里两处特判、
`docs/assets/news/haruo/` 一起撤掉。首页仍 **19 张**：`gen_home.py` 新增
`CATEGORY_LIMIT_BY_LABEL = {"BLOG": 1}`，否则九行横卡会把首页压满。

同一天第二版（用户：「blog每篇文章点击Read article后应该是跳到独立的详情页」）：
行内折叠撤掉，九条正文各自成为独立页 `docs/blog/<slug>/index.md`（地址
`/blog/<slug>/`，slug 就是原来那一行的 id），行里只留一个 `Read article` 链接。
正文、封面、标题、摘要一字未改 —— 由 `_tmp_ocr/blog_split_pages.py` 从列表页
那一行整段搬过去，此后就是普通源文件。详情页版式是 `uncrate.css` 新的一组
`.ab-article`（34px 句首大写 H1、`日期 · 游戏` 小字、19px 导语、16:9 封面、
18px/30 正文、文末 Source 与 "All stories" 回链），文末照惯例一排 Related；
每页带自己的 `NewsArticle` + `BreadcrumbList` JSON-LD，列表页的 `ItemList`
改指九个独立地址。首页那张横卡随 `gen_home.py` 整行搬过去，因此链接写的是
根绝对地址。这九个页面**不进 nav**（与 `/games/gpu-deals/` 同一种，只靠列表页
内链和 sitemap），build 时那串 `not included in nav` 的 INFO 是预期的。
探针 `_tmp_ocr/blog_feed_probe.py` 也随之从「折叠开合」改成「点进去是独立页」，
共 63 项；先拿 HEAD（还带着折叠的旧站）跑一遍，25 项报红，再在新站上全绿。

`/news/` 2026-10-20 接替 nav 第一格的 HOME（用户：「将 /card-test/ 改名为
news并将它替代home导航」）。它前一版是 `/card-test/` 的排版测试页，那个地址从未
进过 nav、也从未推送，所以没有存根。首页 `/` **没有删**：它仍是 `gen_home.py`
跑出来的「最近更新」流，只是不再占 nav 一格，入口是页头的字标 ACEBASE。反过来，
`/news/` 成了 nav 类目，资讯卡会经 `gen_home.py` 出现在首页。

2026-10-21 改名 **BLOG**（用户：「将News改为blog」，问过之后选的是标签与地址
都改）：nav 标签 `BLOG`、目录 `docs/news/` → `docs/blog/`、地址 `/news/` →
`/blog/`，`/news/` 由 `redirect_maps` 出存根指过来（带锚点）。页面标题、正文、
卡片一字未动，只把 JSON-LD 里写死的绝对地址同步成 `/blog/`；图片仍在
`docs/assets/news/`。同一天导航重排，这一格从第一格挪到最后一格。

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
之后 BOOSTING（+4）、SERVICES（+6）与 NEWS（+1）各加一排，首页一度到
**23 张**；SERVICES 2026-10-21 整页撤掉，又回到 **17 张**；同日再新增 GAME
（`/games/`，5 张游戏代储卡），现在是 **22 张**。从 2026-10-21 起
`gen_home.py` 还按卡片 id 去重 —— 同一天 GIFT CARDS 从 `/topup/` 复制了六张
礼品卡，同一张卡在一份首页 HTML 里出现两次会重复 id、并让第二张的规格选择器
填不上价。**重复卡归卡片更少的那个类目**（即更专门的页），nav 顺序只在张数
相同时用来打破平局 —— 这条规则是同一天导航重排时改的：原先「nav 里靠前的
类目保留卡片」，TOP-UP 排到 GIFT CARDS 前面后会把六张礼品卡全占掉，GIFT
CARDS 一格都上不了首页（22 → 16）。当时 TOP-UP 上的是 6 张充值卡（Fortnite、Apex、PSN、Switch Online、eShop、Steam），六张礼品卡由
GIFT CARDS 那一排负责，5 款游戏由 GAME 那一排负责；2026-10-22 那七张码卡撤掉后，
TOP-UP 那六张换成了 30 款娱乐代储里的前六张（Douyin、Kuaishou、Bigo、MICO、
Poppo、Tango），规则本身没动。

`/services/` 2026-10-21 删除（用户：「将 /services/ 页去掉，包括导航」）：六张
电脑调试卡（每项 $9.9）连同 nav 的 SERVICES 一格一起下线，没有搬到别的页，
所以 `/services/` 由 `redirect_maps` 出一张指回首页的存根（和 `/style/`、
`/wellness/` 同一种处置）；图片留在 `docs/assets/services/`，卡片样式
`ab-card--service` 仍被 `/boosting/` 使用。

`/faq/` 2026-10-21 删除（用户：「删除FAQ」，问过之后选的是导航和页面一起删）：
`docs/faq/` 连页面删除，`/faq/` 由 `redirect_maps` 出一张指回首页的存根（同
`/services/`）；每个页面页尾「相关」云里的「购买指南」一并去掉。旧存根
`/shop/faq-and-updates/` 原先指 `/faq/`，改指首页，免得两跳。

同一天导航重排为 **TOP-UP · GAME · GIFT CARDS · BOOSTING · BLOG**（用户：「将
导航按 top-up , game,gift cards,BOOSTING,news进行排序」）。

## 部署

推送 `main` 后由 `.github/workflows/deploy-mkdocs.yml` 构建并发布到 GitHub Pages（`acebase.cc`）。
