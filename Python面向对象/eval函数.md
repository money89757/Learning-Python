
### eval函数

> eval()函数将字符串当成有效的表达式来求值并返回计算结构


```python
# 基本的数学计算
eval("1 + 1")
```




    2




```python
#字符串重复
eval("'*' * 10")
```




    '**********'




```python
#将字符串转换成列表
type(eval("[1,2,3,4,5]"))
```




    list




```python
# 将字符串转换成字典
type(eval("{'name':'xiaoming','age':'18'}"))
```




    dict



### 例子


```python
input_str = input("请输入算数题：")
print(eval(input_str))
```

    请输入算数题：(1 + 2 ) * 5
    15
    

#### 在开发时千万不要使用`eval`直接转换`input`的结果


```python
input_str = input("请输入算数题：")
print(eval(input_str))
```

    请输入算数题：__import__('os')
    <module 'os' from 'C:\\Users\\money\\Anaconda3\\lib\\os.py'>
    


```python

```
