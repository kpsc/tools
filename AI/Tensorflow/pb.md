1. 查看节点名字

   ```python
   # 处在调试状态，图已经建立起来后，用下面的代码将节点写入文件
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
       graph_def.ParseFromString(fgraph.read())		# graph_def.node 可以查看节点信息
   
   with tf.Graph().as_default() as graph:
       tf.import_graph_def(graph_def, name='')
   
       input_x = graph.get_tensor_by_name('input_x:0')
       pred = graph.get_tensor_by_name('output/scores:0')
   
       sess = tf.Session(graph=graph)
       scores = sess.run(pred, feed_dict={input_x: x})
   ```




4. 多个图合并到一起

   ```python
   import tensorflow as tf
   from tensorflow.python.framework import graph_util
   
   output_nodes = ['outputs']
   
   def load_pb(path='model.pb'):
       with tf.gfile.GFile(path, 'rb') as fgraph:
           graph_def = tf.GraphDef()
           graph_def.ParseFromString(fgraph.read())
   
           return graph_def
   
   
   def combined_graph():
       with tf.Graph().as_default() as g_combine:
           with tf.Session(graph=g_combine) as sess:
               graph_a = load_pb('graph_a.pb')
               graph_b = load_pb('graph_b.pb')
   
               tf.import_graph_def(graph_a, name='')
               tf.import_graph_def(graph_b, name='')
   
               g_combine_def = graph_util.convert_variables_to_constants(
                              sess=sess,
                              input_graph_def=sess.graph_def,
                              output_node_names=output_nodes)
               tf.train.write_graph(g_combine_def, './', 'model_combine.pb', as_text=False)
   ```

   

5. 查看变量名字

   ```python
   from tensorflow.python import pywrap_tensorflow
   reader = pywrap_tensorflow.NewCheckpointReader('model.ckpt')
   var_to_shape_map = reader.get_variable_to_shape_map()
   for key in var_to_shape_map.keys():
   	print("tensor_name: ", key)
       
   # 只能查看到变量的名字，无法看到所有节点的名字
   ```

   



