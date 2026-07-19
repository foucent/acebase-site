# AceBase

硬核玩家基地：**MkDocs Material** 版（框架与风格对齐 [MyGear Guide](https://guide.mygear.top/)）。

## 本地预览

```powershell
cd c:\1Work\acebase.cc
..\penv\Scripts\pip.exe install -r requirements.txt
..\penv\Scripts\mkdocs.exe serve
```

打开：http://127.0.0.1:8000/

## 部署

推送 `main` 后由 `.github/workflows/deploy-mkdocs.yml` 构建并发布到 GitHub Pages（`acebase.cc`）。

## 目录

| 路径 | 说明 |
| --- | --- |
| `docs/` | 站点正文（guides / players）与图片 |
| `docs/stylesheets/` | MyGear 风格样式 + 选手配置卡片 CSS |
| `overrides/` | Material 主题覆盖 |
