1. 模型保存及加载

   ```python
   from sklearn.externals import joblib
   
   # save
   joblib.dump(model, 'model.m')
   
   # load
   model = joblib.load('model.m')
   ```

   

