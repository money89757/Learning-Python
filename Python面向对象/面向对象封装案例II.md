
## 封装案例-01-需求分析-属性可以是另外一个类创建的对象


```python
class Gun:
    def __init__(self,model):
        #1.枪的型号
        self.model = model
        #2.子弹数量
        self.bullet_count = 0
        
    def add_bullet(self,count):
        self.bullet_count += count
    
    def shoot(self):
        # 1.判断子弹数量
            if self.bullet_count <= 0:
                print("[%s]没有子弹了..." % self.model)
        # 2.发射子弹
            self.bullet_count -= 1
        # 3. 提示发射信息
            print("[%s] 突突...[%d]" % (self.model, self.bullet_count))
        
#1.创建枪对象
ak47 = Gun("ak47")
ak47.add_bullet(5)
ak47.shoot()
```

    [ak47] 突突...[4]
    

## 026-封装案例-030创建士兵类-完成初始化方法

定义没有初始值的属性，可以设置为None
* None关键字表示什么都没有
* 表示一个空对象，没有方法和属性，是一个特殊的常量
* 可以将None赋值给任何一个变量


```python
class Soldier:
    def __init__(self, name):
        #1.姓名
        self.name = name
        
        #2.枪属性 - 新兵没有枪
        self.gun = None

XuShanDuo = Soldier("许三多")

XuShanDuo.gun = ak47
#不允许直接外部赋值的方法添加属性，需要在方法中将不确定的属性设置为None
print(XuShanDuo.gun)
```

    <__main__.Gun object at 0x000001B436083438>
    

## 封装案例-04-完成开火方法


```python

```


```python
class Gun:
    def __init__(self,model):
        #1.枪的型号
        self.model = model
        #2.子弹数量
        self.bullet_count = 0
        
    def add_bullet(self,count):
        self.bullet_count += count
    
    def shoot(self):
        # 1.判断子弹数量
            if self.bullet_count <= 0:
                print("[%s]没有子弹了..." % self.model)
        # 2.发射子弹
            self.bullet_count -= 1
        # 3. 提示发射信息
            print("[%s] 突突...[%d]" % (self.model, self.bullet_count))

class Soldier:
    def __init__(self, name):
        #1.姓名
        self.name = name
        
        #2.枪属性 - 新兵没有枪
        self.gun = None

        
    def fire(self):
        # 1.判读士兵是否有枪
        if self.gun == None:
            print("[%s] 还没有枪..." % self.name)
            return
        # 2.高喊口号
            print("冲啊...[%s]" % self.name)
        
        # 3.让枪装填子弹
            self.gun.add_bullet(50)
        # 4. 让枪发射子弹
            self.gun.shoot()
        
ak47 = Gun('AK47')
Jess = Soldier("Jess")
Jess.gun = ak47
Jess.fire()
#print(Jess.gun)

```


```python

```


```python

```
