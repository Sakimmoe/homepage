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
- 邮箱：改 `mailto:` 链接
- GitHub：把 `https://github.com/` 换成你的主页地址
- 链接图标：邮箱、GitHub、监测（status.noyu.moe）、Bilibili，均为内联 SVG 描边风格，改 `aria-label` 和 `href` 即可

## 技术栈

单文件 HTML + 内联 CSS，零依赖。
