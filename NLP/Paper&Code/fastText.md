# [fastText](<https://github.com/facebookresearch/fastText/tree/master/python>)

1. 训练词向量

   ```python
   import fasttext
   # skip-gram
   # data.txt 每行一个句子，已分词
   model = fasttext.train_unsupervised('data.txt', model='skipgram')
   
   # cbow
   model = fasttext.train_unsupervised('data.txt', model='cbow')
   
   model.words # 词表
   model['king'] # vector of the word 'king'
   ```

2. 保存及加载模型

   ```python
   model.save_model('model.bin')
   model = fasttext.load_model('model.bin')
   ```


3. 文本分类

   ```python
   # data.train.txt 每行一个sample，__label__class , sentence
   # train
   model = fasttext.train_supervised('data.train.txt')
   
   # test
   model.predict(sentence) # 预测单独一个句子的类别及其分类概率
   result = model.test('data.test.txt') # 计算整体的precision/recall
   result = model.test_label('data.test.txt') # 计算每个类别的precision/recall
   ```

   