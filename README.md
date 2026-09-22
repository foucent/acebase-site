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
| `/topup/` | 代储与礼品卡价格参考（游戏代储 / 礼品卡 / 直播代储） |
| `/tech/` | 电竞房与桌搭（九套实拍，73 张） |
| `/sim-gear/` | STYLE（穿搭写真 8 套 18 张 + 汽车实拍 6 套 91 张，同一个网格） |
| `/faq/` | 购买指南（下单流程 / 付款 / 费用 / 常见问题） |
| `/gallery/` | 相册（手办 / 模型照片墙） |
| `/pc-components/` | 电脑组件 |
| `/games/gpu-deals/` | 显卡好价参考 |

## 部署

推送 `main` 后由 `.github/workflows/deploy-mkdocs.yml` 构建并发布到 GitHub Pages（`acebase.cc`）。
