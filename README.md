# AceBase

国际服电竞玩家入口（MkDocs Material）：下单 · 礼品卡 · 加速。

当前为 **Demo 骨架站**（占位数据，非实时报价）。

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
| `/shop/how-to-order/` 等 | 下单 / 价格 / FAQ / 发货（「关于与政策」分组） |
| `/topup/pubg-mobile-direct/` | PUBG Mobile UC 直充（Global） |
| `/topup/pubg-gcoin/` 等 | BitTopup 风格商品页（G-COIN / 暗区 / 三角洲 / HOK / MLBB） |
| `/figure-wall/` | 图片墙（手办 / 模型照片墙 Demo） |

## 部署

推送 `main` 后由 `.github/workflows/deploy-mkdocs.yml` 构建并发布到 GitHub Pages（`acebase.cc`）。
