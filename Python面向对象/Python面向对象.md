

```python
def demo():
    """这是一个测试函数"""
    print("hello world")
```


```python
demo()
```

    hello world
    


```python
dir(demo)
# 内置方法和属性
```




    ['__annotations__',
     '__call__',
     '__class__',
     '__closure__',
     '__code__',
     '__defaults__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__get__',
     '__getattribute__',
     '__globals__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__kwdefaults__',
     '__le__',
     '__lt__',
     '__module__',
     '__name__',
     '__ne__',
     '__new__',
     '__qualname__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__']




```python
demo.__doc__
```




    '这是一个测试函数'



## 0.2 定义简单的类

2.1 定义只包含方法的类

```python
class 类名:
    def 方法1(self,参数列表):
        pass
    
    def 方法2(self,参数列表):
        pass
```
第一个参数必须是`self`

2.2 创建对象

```
对象变量 = 类名()
```


```python
class Cat:
    def eat(self):
        print("小猫爱吃鱼")
        
    def drink(self):
        print("小猫喝水")
        
Tom = Cat()
Tom.drink()
Tom.eat()
```

    小猫喝水
    小猫爱吃鱼
    


```python
print(Tom)
```

    <__main__.Cat object at 0x00000256432BD278>
    


```python
addr = id(Tom) 
print("%x" % addr) #16进制地址
```

    256432bd278
    

## 创建多个猫对象


```python
class Cat:
    def eat(self):
        print("小猫爱吃鱼")
        
    def drink(self):
        print("小猫喝水")

#创建一个对象
Tom = Cat()
Tom.eat()
Tom.drink()
print(Tom)

#创建另一个对象
Lazy_cat = Cat()
Lazy_cat.eat()
Lazy_cat.drink()
print(Lazy_cat)

Lazy_cat2 = Lazy_cat
print(Lazy_cat2)


#面向对象开发，类只有一个，对象可以有很多个
```

    小猫爱吃鱼
    小猫喝水
    <__main__.Cat object at 0x0000025643335A58>
    小猫爱吃鱼
    小猫喝水
    <__main__.Cat object at 0x00000256433355C0>
    <__main__.Cat object at 0x00000256433355C0>
    

## 在类的外部给对象增加属性

只需要在`类的外部的代码`中之间通过`.`设置一个属性即可
> 注意：这种方式虽然简单，但不推荐使用！


```python
class Cat:
    def eat(self):
        print("小猫爱吃鱼")
        
    def drink(self):
        print("小猫喝水")
        
# 可以使用 .属性名 利用赋值语句就可以了
Tom = Cat()
Tom.name = "Tom"

Tom.eat()
Tom.drink()
dir(Tom)

```

    小猫爱吃鱼
    小猫喝水
    




    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     'drink',
     'eat',
     'name']




```python
Lazy_cat.eat()
Lazy_cat.drink()
dir(Lazy_cat)
```

    小猫爱吃鱼
    小猫喝水
    




    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     'drink',
     'eat']



## 利用self在类封装的方法中输出对象属性


```python
class Cat:
    def eat(self):
        print("%s爱吃鱼" % self.name)
        
    def drink(self):
        print("小猫喝水")
        
# 可以使用 .属性名 利用赋值语句就可以了
Tom = Cat()
Tom.name = "Tom"
Tom.eat()
Tom.drink()

Lazy_cat = Cat()
Lazy_cat.name = "大懒猫"
Lazy_cat.eat()
Lazy_cat.drink()
# self 内存地址与 Tom.eat()的地址一致
# 哪一个对象调用的方法，self就是哪一个对象的引用

```

    Tom爱吃鱼
    小猫喝水
    大懒猫爱吃鱼
    小猫喝水
    


```python
class Cat:
    def eat(self):
        print("%s爱吃鱼" % self.name)
        
    def drink(self):
        print("%s爱喝水" % self.name)
        
# 可以使用 .属性名 利用赋值语句就可以了
Tom = Cat()
Tom.name = "Tom"
Tom.eat()
Tom.drink()

Lazy_cat = Cat()
Lazy_cat.name = "大懒猫"
Lazy_cat.eat()
Lazy_cat.drink()
# self 内存地址与 Tom.eat()的地址一致
# 哪一个对象调用的方法，self就是哪一个对象的引用

```

    Tom爱吃鱼
    Tom爱喝水
    大懒猫爱吃鱼
    大懒猫爱喝水
    

> 由*哪个对象*调用的方法,方法内的`self`就是*哪一个对象的引用*
* 类在封装的方法内部,`self`就表示*当前调用方法的对象自己*
* *调用方法时*,程序员不需要传递`self`参数
* 在方法内部
    * 可以通过`self.`访问对象的属性
    * 也可以通过`self.`调用其他的对象方法

## 初始化方法-01-在类的外部给对象增加属性的隐患


```python
class Cat:
    def eat(self):
        print("%s爱吃鱼" % self.name)
        
    def drink(self):
        print("%s爱喝水" % self.name)

Tom = Cat()
# Tom.name = "Tom"
Tom.eat()
Tom.drink()
Tom.name = "Tom"

#错误方法
# 如果没有找到属性，程序会报错
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-51-aafba88cefdb> in <module>()
          8 Tom = Cat()
          9 # Tom.name = "Tom"
    ---> 10 Tom.eat()
         11 Tom.drink()
         12 Tom.name = "Tom"
    

    <ipython-input-51-aafba88cefdb> in eat(self)
          1 class Cat:
          2     def eat(self):
    ----> 3         print("%s爱吃鱼" % self.name)
          4 
          5     def drink(self):
    

    AttributeError: 'Cat' object has no attribute 'name'


## 初始化方法-02-创建对象是自动调用初始化方法

* 当使用`类名()`创建对象时,会自动执行以下操作
    1. 为对象在内存中分配空间--创建对象
    2. 为对象的属性设置初始值--初始化方法(init)

* 这个初始化方法就是`__init__`方法,`__init__`是对象的*内置方法*
> __init__方法是专门用来定义一个类具有哪些属性的方法！


```python
class Cat:
    def __init__(self):
        print("这是一个初始化方法")
   
#使用类名（）创建对象的时候，会自动调用初始化方法
Tom = Cat()
   
        
```

    这是一个初始化方法
    

## 初始化方法-03-在初始化方法中定义属性

* 在`__init__`方法内部使用`self.属性名 = 属性的初始值`就可以定义属性
* 定义属性之后,再使用类创建的对象,都会拥有该属性


```python
class Cat:
    def __init__(self):
        print("这是个初始化方法")
        
        self.name = "Tom"
        
#使用类名（）创建对象的时候，会自动调用初始化方法
Tom = Cat()
print(Tom.name)
        
        
```

    这是个初始化方法
    Tom
    


```python
class Cat:
    def __init__(self):
        print("这是个初始化方法")   
        self.name = "Tom"
    
    def eat(self):
        print("%s爱吃鱼" % self.name)
        
    def drink(self):
        print("%s爱喝水" % self.name)
        
# 可以使用 .属性名 利用赋值语句就可以了
Tom = Cat()
Tom.eat()
Tom.drink()
```

    这是个初始化方法
    Tom爱吃鱼
    Tom爱喝水
    

## 改造初始化方法-04-使用参数设置属性初始值 


```python
class Cat:
    def __init__(self):
        print("这是个初始化方法")   
        self.name = "Tom"
    
    def eat(self):
        print("%s爱吃鱼" % self.name)
        
    def drink(self):
        print("%s爱喝水" % self.name)
        
# 可以使用 .属性名 利用赋值语句就可以了
Tom = Cat()
Tom.eat()
Tom.drink() 

Lazy_cat = Cat()
Lazy_cat.eat()
```

    这是个初始化方法
    Tom爱吃鱼
    Tom爱喝水
    这是个初始化方法
    Tom爱吃鱼
    


```python
class Cat:
    def __init__(self,new_name):
        print("这是个初始化方法")   
        #self.name = "Tom"
        self.name = new_name
    
    def eat(self):
        print("%s爱吃鱼" % self.name)
        
    def drink(self):
        print("%s爱喝水" % self.name)
        
# 可以使用 .属性名 利用赋值语句就可以了
Tom = Cat("Tom")
Tom.eat()
Tom.drink() 

Lazy_cat = Cat("大懒猫")
Lazy_cat.eat()
```

    这是个初始化方法
    Tom爱吃鱼
    Tom爱喝水
    这是个初始化方法
    大懒猫爱吃鱼
    

1. 把希望设置的属性值,定义成__init__方法的参数
2. 在方法内部使用self.属性 = 形参接收外部传递的参数
3. 在创建对象时，使用类名(属性1,属性2,...)调用

## 内置方法-01-del方法和对象的生命周期


```python
class Cat:
    def __init__(self, new_name):
        self.name = new_name
        
        print("%s 来了" % self.name)
       
    def __del__(self):
        print("%s 去了" % self.name)
#Tom是个全局变量       
tom = Cat("Tom")
print(tom.name)

#del 关键字可以删除一个对象
del tom.name

print("-"*50)
```

    Tom 来了
    Tom
    --------------------------------------------------
    

    Exception ignored in: <function Cat.__del__ at 0x0000025643381C80>
    Traceback (most recent call last):
      File "<ipython-input-72-aafa51aa5d91>", line 8, in __del__
    AttributeError: 'Cat' object has no attribute 'name'
    

## 内置方法-str方法制定变量输出信息


```python
class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 来了" % self.name)
      
#     def __del__(self):
#         print("%s 去了" % self.name)

    def __str__(self):
        return "我是小猫[%s]" % self.name

#Tom是个全局变量       
tom = Cat("Tom")
print(tom)
```

    Tom 来了
    我是小猫[Tom]
    


```python

```


```python

```
