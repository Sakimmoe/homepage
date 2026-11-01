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
- GitHub：`https://github.com/Sakimmoe`
- 浏览器标签图标：替换根目录的 `favicon.ico`
- 链接图标（从左到右）：邮箱、GitHub、Bilibili（ri-bilibili-line）、监测（ri-cloud-line），均为内联 SVG，改 `aria-label` 和 `href` 即可

## 字体

全站使用 [Resource Han Rounded CN（资源圆体）](https://github.com/CyanoHao/Resource-Han-Rounded)，
以可变字体子集的形式自托管在 `fonts/resource-han-rounded-cn.woff2`：一个文件覆盖
200–900 全部字重，圆度轴 `ROND` 取默认值 100（完全圆角）。

完整中文字体有好几 MB，对首页来说太重，所以只打包了 `index.html` 里实际出现的字
加上英文、数字和常用标点，体积约 105 KB。代价是：**改了文案之后，如果出现了子集
里没有的字，这些字会退回系统字体**。补字的方式是重新生成子集：

```bash
pip install fonttools brotli

# 1. 从 Release 下载 RHR-CFF2-CN-*.7z（约 15 MB）并解压出 ResourceHanRoundedCN-VF.otf
#    https://github.com/CyanoHao/Resource-Han-Rounded/releases
# 2. 重新生成（脚本会自动扫描 index.html 的文字，输出同名 woff2）
python scripts/build-font.py /path/to/ResourceHanRoundedCN-VF.otf
```

想换成完整字体（不缺字但首次加载慢），把 `index.html` 的 `@font-face` 指向完整字体文件即可。

## 技术栈

单文件 HTML + 内联 CSS，零 JS 依赖；只有字体是额外的一个静态文件。

## 部署（Vercel）

- 线上地址：https://www.noyu.moe（备用：https://homepage-tawny-psi.vercel.app）
- 源码仓库：https://github.com/Sakimmoe/homepage
- 项目：Vercel 上的 `homepage` 项目（已绑定 www.noyu.moe、已连接 GitHub 仓库，推送 `main` 分支即自动部署）

更新后重新部署：

```bash
git push
```
