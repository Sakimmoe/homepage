#!/usr/bin/env python3
"""重新生成首页用的 Resource Han Rounded 网页字体子集。

仓库里只提交「当前页面用到的字」的子集（约 100 KB），所以改了文案之后
如果出现缺字（浏览器会退回系统字体），跑一遍这个脚本即可。

依赖：
    pip install fonttools brotli

需要先下载官方可变字体（Release 里的 RHR-CFF2-CN-*.7z，解压得到
ResourceHanRoundedCN-VF.otf）：
    https://github.com/CyanoHao/Resource-Han-Rounded/releases

用法：
    python scripts/build-font.py /path/to/ResourceHanRoundedCN-VF.otf

也可以指定额外要包含的文字（比如新增的常量文案）：
    python scripts/build-font.py <otf> --extra "预加载图集"
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(REPO, "index.html")
OUTPUT = os.path.join(REPO, "fonts", "resource-han-rounded-cn.woff2")

# 基础 ASCII 可打印字符
ASCII = "".join(chr(c) for c in range(0x20, 0x7F))

# 中文常用标点与排版符号
PUNCTUATION = (
    "、。〃〈〉《》「」『』【】〔〕〖〗！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～"
    "·—…‘’“”※‥′″°¥￥€§¶†‡•\u3000\u00a0"
)


def visible_chars(html_path: str) -> str:
    """收集 index.html 中会被渲染出来的文字（去掉标签、style、script）。"""
    html = open(html_path, encoding="utf-8").read()
    body = re.sub(r"(?is)<(script|style).*?</\1>", " ", html)
    body = re.sub(r"(?s)<head>.*?</head>", " ", body)
    text = re.sub(r"(?s)<[^>]+>", " ", body)
    return "".join(sorted(set(text) - set(" \t\r\n")))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", help="ResourceHanRoundedCN-VF.otf 的路径")
    ap.add_argument("--extra", default="", help="额外需要包含的文字")
    args = ap.parse_args()

    if not os.path.exists(args.source):
        print(f"找不到源字体：{args.source}", file=sys.stderr)
        return 1

    from fontTools import subset
    from fontTools.ttLib import TTFont

    page = visible_chars(INDEX)
    text = page + ASCII + PUNCTUATION + args.extra
    charset = set(text)
    print(f"页面文字 {len(page)} 个，合计 {len(charset)} 个字符")

    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = ["*"]
    opts.name_IDs = ["*"]
    opts.name_legacy = True
    opts.notdef_outline = True
    # 首页用不到竖排表，去掉能省一点体积
    opts.drop_tables += ["BASE", "VORG", "vhea", "vmtx", "VVAR"]

    font = subset.load_font(args.source, opts)
    # 记录子集化之前的 cmap，用来检查源字体本身是否缺字
    source_cmap = set(font.getBestCmap())

    sub = subset.Subsetter(options=opts)
    sub.populate(text=text)
    sub.subset(font)

    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    subset.save_font(font, OUTPUT, opts)

    missing = sorted(c for c in charset if ord(c) not in source_cmap)
    size_kb = os.path.getsize(OUTPUT) / 1024
    print(f"已生成 {os.path.relpath(OUTPUT, REPO)}：{size_kb:.1f} KB，"
          f"{TTFont(OUTPUT)['maxp'].numGlyphs} 个字形")

    if missing:
        print(f"警告：源字体里没有这些字符 -> {''.join(missing)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
