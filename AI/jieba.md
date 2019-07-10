1. 分词

   ```python
   '''
   jieba.cut 方法接受三个输入参数: 需要分词的字符串；cut_all 参数用来控制是否采用全模式；HMM 参数用来控制是否使用 HMM 模型
   jieba.cut_for_search 方法接受两个参数：需要分词的字符串；是否使用 HMM 模型。该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细，待分词的字符串可以是 unicode 或 UTF-8 字符串、GBK 字符串。注意：不建议直接输入 GBK 字符串，可能无法预料地错误解码成 UTF-8
   jieba.cut 以及 jieba.cut_for_search 返回的结构都是一个可迭代的 generator，可以使用 for 循环来获得分词后得到的每一个词语(unicode)，或者用
   jieba.lcut 以及 jieba.lcut_for_search 直接返回 list
   jieba.Tokenizer(dictionary=DEFAULT_DICT) 新建自定义分词器，可用于同时使用不同词典。jieba.dt 为默认分词器，所有全局分词相关函数都是该分词器的映射。
   '''
   
   import jieba
   
   seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
   print("Full Mode: " + "/ ".join(seg_list))  # 全模式
   
   seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
   print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
   
   seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
   print(", ".join(seg_list))
   
   seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
   print(", ".join(seg_list))
   ```

   

2. tfidf/textrank

   ```python
   # tf-idf
   jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
       sentence 为待提取的文本
       topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
       withWeight 为是否一并返回关键词权重值，默认值为 False
       allowPOS 仅包括指定词性的词，默认值为空，即不筛选
   
   from jieba import analyse
   tfidf = analyse.extract_tags
   
   text = "线程是程序执行时的最小单位"
   keywords = tfidf(text)
   print(list(keywords)) # python3
   
   # textrank
   from jieba import textrank
   textrank = analyse.textrank
   ...
   ```

   

