1. 统计特征

```python
# Series
data.max() / min / mean / median / mode / count / ptp / std
```



2. nunique 

```python
# 相当于是计算集合的长度
df = pd.DataFrame({'A':[0, 1, 2], 'B':[4, 5, 6]})
df.nunique()
# A 3
# B 3
# dtype: int64
```



3. get_dummies

```python
# one-hot
df = pd.DataFrame([['x'], ['y'], ['z']])
d = pd.concat([df, pd.get_dummies(df)], axis=1)
#    0  0_x  0_y  0_z
# 0  x    1    0    0
# 1  y    0    1    0
# 2  z    0    0    1
```



4. 删除重复数据

```python
duplicated
drop_duplicated
```



