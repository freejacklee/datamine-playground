# deepl web api (unofficial)

![img.png](assets/cover.png)

## global guide

[readme](../readme.md)

## features

- [x] language translation powered by DeepL between ZH, EN, JA, EN, etc.
- [x] SUPER terminology support （由于deepl只支持部分语言比如德英日等的术语表，而不支持中文，因此本程序在deepl内置术语表架构上增加了一层预处理，使之可以实现提前预替换，最终达到支持任意语言的术语表，实测下来效果很ok！） 

### Usage

```shell
cd src

# 1. basic usage
python main.py "Are You OK?"
# output: 你还好吗？

# 2. specific return format as json
python main.py "Are You OK?" -f json
# output: {'jsonrpc': '2.0', 'id': 76070001, 'result': {'translations': [{'beams': [{'sentences': [{'text': '你还好吗？', 'ids': [0]}], 'num_symbols': 6}], 'quality': 'normal'}], 'target_lang': 'ZH', 'source_lang': 'EN', 'source_lang_is_confident': False, 'detectedLanguages': {}}}

# 3. specific languages
python main.py "你好吗" --from_lang "ZH" --target_lang "FR"
# output: Comment allez-vous ?

# 4. specific terminology from text
python main.py "SLAM is hard to learn" --terminology "SLAM\t大傻逼"
# output: 大傻逼很难学。

# 5. normal scene, translate a paragraph and using a terminology file
python main.py "As with its predecessors, the algorithm is divided into three main threads: tracking, local mapping, loop closing and map merging. This algorithm can be used with monocular, stereo, and RGB-D cameras, and implements global optimiza- tions and loop closures techniques. However, authors in [76] demonstrated signiﬁcant errors results of ORB-SLAM3 online performance."  --terminology "terminology.txt"
# output with    terminology: 与其前身一样，该算法分为三个主线：跟踪、建图、回环检测和地图合并。该算法可用于单目、双目和RGB-D相机，并实现了全局优化和循环闭合技术。然而，作者在[76]中证明了ORB-SLAM3在线性能的显著错误结果。
# output without terminology: 与其前身一样，该算法分为三个主线：跟踪、局部映射、循环关闭和地图合并。该算法可用于单眼、立体和RGB-D相机，并实现了全局优化和循环闭合技术。然而，作者在[76]中证明了ORB-SLAM3在线性能的显著错误结果。
```

## possible problems

如果返回 `Too many requests` 的错误，最好的做法是换个proxy。

比如我的vpn是基于 clashx 的，所以可以切换欧美、日韩等不同的线路，从而保证大多数情况下可用。

目前还没有集成自动更换代理，需要一段时间观察网站实际表现。

## hack manual

[hack-manual](./hack-manual.md)
