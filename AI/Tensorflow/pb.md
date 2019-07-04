1. 查看节点名字

   ```python
   # 处在调试状态，图已经建立起来后
   graph = tf.get_default_graph().as_graph_def()
   
   with open('graph', 'w', encoding='utf-8') as fgraph:
       f.write(str(g.node))
       
   # 然后根据程序中的节点名字去搜索，在后面生成 pb 文件写结点名字的时候用  
   # saver.save(sess, 'model.ckpt') 里面保存的是变量，并不是所有图的节点  
   ```

   

2. 生成 pb 文件

   ```python
   # output_node_names 为输出节点的名字
   def freeze_graph(path='model.ckpt', output='model.pb'):
       saver = tf.train.import_meta_graph(path+'.meta', clear_devices=True)
       graph = tf.get_default_graph()
       input_graph_def = graph.as_graph_def()
   
       with tf.Session() as sess:
           saver.restore(sess, path)
           output_graph_def = graph_util.convert_variables_to_constants(
                              sess=sess,
                              input_graph_def=input_graph_def,   # = sess.graph_def,
                              output_node_names=['output/scores'])
   
           with tf.gfile.GFile(output, 'wb') as fgraph:
               fgraph.write(output_graph_def.SerializeToString())
               
   # 程序中的输出节点
   # with name_scope('output'):
   #     self.scores = tf.*(..., name='scores')    
   ```

   

3. inference

   ```python
   with tf.gfile.GFile('model.pb', 'rb') as fgraph:
       graph_def = tf.GraphDef()
       graph_def.ParseFromString(fgraph.read())
   
   with tf.Graph().as_default() as graph:
       tf.import_graph_def(graph_def, name='')
   
       input_x = graph.get_tensor_by_name('input_x:0')
       pred = graph.get_tensor_by_name('output/scores:0')
   
       sess = tf.Session(graph=graph)
       scores = sess.run(pred, feed_dict={input_x: x})
   ```

   
   
4. 查看变量名字

   ```python
   from tensorflow.python import pywrap_tensorflow
   reader = pywrap_tensorflow.NewCheckpointReader('model.ckpt')
   var_to_shape_map = reader.get_variable_to_shape_map()
   for key in var_to_shape_map.keys():
   	print("tensor_name: ", key)
   ```

   

