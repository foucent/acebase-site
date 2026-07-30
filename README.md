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
| `/` | Home（本周推荐） |
| `/shop/faq-and-updates/` 等 | FAQ / 发货与到账 / 关于与政策 |
| `/topup/pubg-mobile-direct/` | PUBG Mobile UC 代充（Global） |
| `/topup/pubg-gcoin/` 等 | 人工代充商品页（G-COIN / 暗区 / 三角洲 / HOK） |
| `/gallery/` | 相册（手办 / 模型照片墙） |

## 部署

推送 `main` 后由 `.github/workflows/deploy-mkdocs.yml` 构建并发布到 GitHub Pages（`acebase.cc`）。
