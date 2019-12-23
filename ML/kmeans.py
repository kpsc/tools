import os
import numpy as np
import tensorflow as tf
from tensorflow.contrib.factorization import KMeans
from tensorflow.examples.tutorials.mnist import input_data

cfg = tf.ConfigProto(
    allow_soft_placement=True,
    log_device_placement=False,
    gpu_options=tf.GPUOptions(allow_growth=True))
config = {
    'epochs': 50,
    'batch_size': 1024,
    'k': 100,
    'num_classes': 10,
    'num_features': 784,
    'gpu': -1
}
os.environ['CUDA_VISIBLE_DEVICES'] = ''
if config['gpu'] >= 0:
    os.environ["CUDA_VISIBLE_DEVICES"] = str(config['gpu'])


def load_data():
    mnist = input_data.read_data_sets('./data', one_hot=True)
    data = mnist.train.images  # [55000, 784]   28 x 28

    return data


class Model:
    def __init__(self, args):
        self.k = args.get('k', 10)
        self.num_classes = args.get('num_classes', 10)
        self.num_features = args.get('num_features', 784)

        self._add_op()

        self.device = '/gpu:0' if args['gpu'] >= 0 else '/cpu:0'
        with tf.device(self.device):
            self._build_nn()

    def _add_op(self):
        self.x = tf.placeholder(tf.float32, shape=[None, self.num_features])
        self.y = tf.placeholder(tf.float32, shape=[None, self.num_classes])

    def _build_nn(self):
        self.kmeans = KMeans(inputs=self.x,
                             num_clusters=self.k,
                             distance_metric='cosine',
                             use_mini_batch=True)

        # 构建K-Means的计算图
        training_graph = self.kmeans.training_graph()

        if len(training_graph) > 6:  # tensorflow 1.4及以上版本
            (all_scores, cluster_idx, scores, cluster_cnters_initialized,
             cluster_cnters_var, init_op, train_op) = training_graph
        else:
            (all_scores, cluster_idx, scores, cluster_cnters_initialized,
             init_op, train_op) = training_graph

        self.cluster_idx = cluster_idx[0]  # 每个样本的类别，[0, k)
        self.avg_distance = tf.reduce_mean(scores)

        self.init_op = init_op
        self.train_op = train_op


def train():
    mnist = input_data.read_data_sets('./data', one_hot=True)
    data = mnist.train.images  # [55000, 784]   28 x 28
    with tf.Session(config=cfg) as sess:
        model = Model(config)
        saver = tf.train.Saver(max_to_keep=5)
        sess.run(tf.global_variables_initializer(), feed_dict={model.x: data})
        sess.run(model.init_op, feed_dict={model.x: data})

        for epoch in range(1, config.get('epochs', 2)+1):
            _, loss, idx = sess.run([model.train_op, model.avg_distance, model.cluster_idx],
                                    feed_dict={model.x: data})
            print(f'epoch: {epoch}, loss: {loss}')
            saver.save(sess, f'./model/kmeans_{epoch}.ckpt')

        # 统计每个类中的样本
        counts = np.zeros(shape=(config['k'], config['num_classes']))
        for i in range(len(idx)):
            counts[idx[i]] += mnist.train.labels[i]
        labels_map = [np.argmax(c) for c in counts]
        labels_map = tf.convert_to_tensor(labels_map)

        # evaluate
        cluster_label = tf.nn.embedding_lookup(labels_map, model.cluster_idx)
        correct_prediction = tf.equal(cluster_label, tf.cast(tf.argmax(model.y, 1), tf.int32))
        acc = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        test_x, test_y = mnist.test.images, mnist.test.labels
        print("eval acc：", sess.run(acc, feed_dict={model.x: test_x, model.y: test_y}))


if __name__ == '__main__':
    train()
