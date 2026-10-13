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
| `/topup/` | 代储与礼品卡价格参考（18 张卡：5 款游戏代储 / 6 种礼品卡 / 7 种充值卡与充值码） |
| `/figures/` | 手办实拍图集（八套，63 张） |
| `/faq/` | 购买指南（下单流程 / 付款 / 费用 / 常见问题） |
| `/gallery/` | 相册（手办 / 模型照片墙） |
| `/pc-components/` | 电脑组件 |
| `/games/gpu-deals/` | 显卡好价参考 |

`/gift-cards/` 与 `/cdkeys/` 2026-10-13 并回 `/topup/` 后不再是页面，两个 URL 由
`mkdocs.yml` 的 `redirect_maps` 出存根指过去（带锚点，十三张卡的 id 没改，所以
`/cdkeys/#gocash-card` 落得到卡片上）。

首页因此从 23 张缩到 12 张：`scripts/gen_home.py` 按「每个类目取最新 6 张」抓卡，
Gift Cards 与 CDKeys 两个类目没了，那两排随之消失；TOP-UP 现有 18 张卡，按规则
只上前 6 张（5 款游戏 + 第一张礼品卡）。要让首页多露几张价格卡，改的是
`gen_home.py` 里的 `CATEGORY_LIMIT`（全站所有类目一起变）。

## 部署

推送 `main` 后由 `.github/workflows/deploy-mkdocs.yml` 构建并发布到 GitHub Pages（`acebase.cc`）。
