# homepage

油咖喱的个人主页，复刻自 [tfxc.de](https://tfxc.de/) 的简洁风格，配色改为粉调（#fde9e7）。

## 预览

直接双击打开 `index.html`，或在本地起一个静态服务器：

```bash
python -m http.server 8000
```

然后访问 http://localhost:8000

## 自定义

- 名字 / 副标题 / 简介：修改 `index.html` 里的 `h1`、`.subtitle` 和 `.bio`
- 邮箱 / 微信 / QQ：改对应 `href` 里的联系方式（微信用 `weixin://` 唤起，QQ 用 `tencent://message/` 唤起）
- GitHub：`https://github.com/Sakimmoe`
- 浏览器标签图标：替换根目录的 `favicon.ico`
- 链接图标（从左到右）：邮箱、微信（ri-wechat-2-line）、QQ（ri-qq-line）、GitHub、Bilibili（ri-bilibili-line）、监测（ri-cloud-line），均为内联 SVG，改 `aria-label` 和 `href` 即可

## 技术栈

单文件 HTML + 内联 CSS，零依赖。

## 部署（Vercel）

- 线上地址：https://www.noyu.moe（备用：https://homepage-tawny-psi.vercel.app）
- 源码仓库：https://github.com/Sakimmoe/homepage
- 项目：Vercel 上的 `homepage` 项目（已绑定 www.noyu.moe、已连接 GitHub 仓库，推送 `main` 分支即自动部署）

更新后重新部署：

```bash
git push
```
