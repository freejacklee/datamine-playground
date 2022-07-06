# deepl web api (unofficial)

![img.png](assets/cover.png)

## features

- [x] language translation powered by DeepL between ZH, EN, JA, EN, etc.
- [x] SUPER terminology support （由于deepl只支持部分语言比如德英日等的术语表，而不支持中文，因此本程序在deepl内置术语表架构上增加了一层预处理，使之可以实现提前预替换，最终达到支持任意语言的术语表，实测下来效果很ok！） 

## global guide

[readme](../readme.md)

## project guide

### run

```shell
cd src
python main.py "Are You OK?"
# 你还好吗？
```

### possible problems

如果返回 `Too many requests` 的错误，最好的做法是换个proxy。

比如我的vpn是基于 clashx 的，所以可以切换欧美、日韩等不同的线路，从而保证大多数情况下可用。

目前还没有集成自动更换代理，需要一段时间观察网站实际表现。

## hack manual

[hack-manual](./hack-manual.md)
