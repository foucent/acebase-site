# AceBase

硬核玩家基地：**MkDocs Material** 版（框架与风格对齐 [MyGear Guide](https://guide.mygear.top/)）。

原 Hugo 文稿仍保留在 `content/posts/`；站点正文在 `docs/`。

## 本地预览

```powershell
cd c:\1Work\acebase.cc
..\penv\Scripts\pip.exe install -r requirements.txt
..\penv\Scripts\mkdocs.exe serve
```

打开：http://127.0.0.1:8000/

## 从 Hugo 重新导入

若更新了 `content/posts/` 或选手 shortcode：

```powershell
python scripts\migrate_to_mkdocs.py
..\penv\Scripts\mkdocs.exe build
```

## 部署

推送 `main` 后由 `.github/workflows/deploy-mkdocs.yml` 构建并发布到 GitHub Pages（`acebase.cc`）。

## 目录

| 路径 | 说明 |
| --- | --- |
| `docs/` | MkDocs 正文（guides / players） |
| `docs/stylesheets/` | MyGear 风格样式 + 选手配置卡片 CSS |
| `overrides/` | Material 主题覆盖（与 mygear-wiki 同结构） |
| `content/posts/` | 原 Hugo 文章（归档） |
| `layouts/shortcodes/` | 原选手配置 HTML 短代码（迁移脚本会内联进 docs） |
