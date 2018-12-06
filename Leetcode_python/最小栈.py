#1.最小值和元素一同入栈
#2. Stack记录差值

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = [] #最小栈

    #将元素x推入栈中
    def push(self,x):
        self.stack.append(x)
        #如果最小栈为空                或新增址小于栈顶值
        if len(self.minStack) == 0 or x <= self.minStack[-1]:
            # x如最小栈
            self.minStack.append(x)

    #删除栈顶元素
    def pop(self):
        #如果栈顶值 == 最小栈顶值
        if not self.isEmpty():
            if self.top() == self.minStack[-1]:
                self.minStack.pop()
            self.stack.pop()

    #获取栈顶元素
    def top(self):
        if not self.isEmpty():
            return self.stack[-1]

    # 获取最小栈
    def getMin(self):
        if not self.isEmpty():
            return self.minStack[-1]

    #判断是否为空
    def isEmpty(self):
        return len(self.stack) < 1
"""
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self,x):
        if x is None:
            pass
        else:
            self.stack.append(x)

    def pop(self):
        if self.stack is None:
            return False
        else:
            self.stack.pop()

    def top(self):
        if self.stack is None:
            return False
        else:
            self.stack[-1]

    def getMin(self):
        if self.stack is None:
            return False
        else:
            return min(self.stack)
"""


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-1)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.pop())
    print(minStack.getMin())
