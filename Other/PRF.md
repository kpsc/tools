|               |  positive_predict  |  negative_predict  |
| :-----------: | :----------------: | :----------------: |
| positive_real | TP(正类预测为正类) | FN(正类预测为负类) |
| negative_real | FP(负类预测为正类) | TN(负类预测为负类) |



- precision(精确率)

  针对预测结果而言，预测为正的样本中有多少是真正的样本

$$
P=\frac{TP}{TP+FP}
$$



- recall

  针对原来的样本而言，样本中的正例有多少被预测正确了

$$
R=\frac{TP}{TP+FN}
$$



- F1

$$
\frac{2}{F_1}=\frac{1}{P}+\frac{1}{R}
$$

- accuracy(准确率)

$$
acc = \frac{TP+TN}{TP+TN+FP+FN}
$$



![PRF](./image/prf.jpg)

