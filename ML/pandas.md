### 文件

1. read_csv

   ```python
   df = pd.read.csv(filename, header=0, names=['a', 'b'])
   # header 使用文件的某一行作为数据列的名字
   # header=None, 默认自动从第一行推断列的名字
   # header=0, 使用第 0 行作为列的名字
   # 若提供了 name, 则使用 name 作为列的名字
   # header=0, 且也给了 name， 则使用 name，且忽略文件第一行
   ```



### Dataframe

1. Dataframe

   ```python
   df=pandas.Dataframe(columns=[],index=[],data=[])  # 创建一个Dataframe
   df.head(n=10)  # 显示前n行的数据
   df.tail(n=10)  # 显示尾n行的数据
   ```

2. 查看索引名，列名，values

   ```python
   df.index      # 返回df的行索引值，是一个array
   df.columns    # 返回df的列名，是一个array
   df.values     # 返回df的所有值，是一个2D array
   ```

3. 查看 dataframe 的一些统计特性

   ```python
   df.describe('all')  # 统计每列的min, max, mean, std, quantile
   df.dtypes  # 返回每列数据的类型
   df.T  # 转置数据框
   df.sort_index(axis=1,ascending=False) # 按索引排序所有列，升序或者降序
   ```

   

### 切片

1. 取指定列数据

   ```
   df['column_name']     # 利用列名直接取某一列
   df[df.columns[index]] # 适合于不知道列名，但是知道它在第几列
   ```

   

2. 取指定行数据

3. 