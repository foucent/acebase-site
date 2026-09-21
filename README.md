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
| `/` | Home（本周推荐，由 `scripts/gen_home.py` 生成，勿手改） |
| `/topup/` | 代储与礼品卡价格参考（游戏代储 / 礼品卡 / 直播代储） |
| `/tech/` | 显卡价格参考（RTX 全系） |
| `/sim-gear/` | STYLE（球拍与器材） |
| `/wellness/` | 健康生活（筹备中） |
| `/faq/` | 购买指南（下单流程 / 付款 / 费用 / 常见问题） |
| `/gallery/` | 相册（手办 / 模型照片墙） |
| `/pc-components/` | 电脑组件 |
| `/games/gpu-deals/` | 显卡好价参考 |

## 部署

推送 `main` 后由 `.github/workflows/deploy-mkdocs.yml` 构建并发布到 GitHub Pages（`acebase.cc`）。
