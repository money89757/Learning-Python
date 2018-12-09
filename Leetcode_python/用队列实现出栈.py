"""
class MyStack:
    def __init__(self):
        self.data_queue = [] #队列
        self.temp_queue = [] #临时队列

    def push(self,item):
        self.data_queue.append(item)

    def pop(self):
        if len(self.data_queue) == 0:
            return None
        while len(self.data_queue) != 1:
            self.temp_queue.append(self.data_queue(0))
        self.data_queue,self.temp_queue = self.temp_queue,self.data_queue
        return self.temp_queue.pop()

    def top(self):
        self.data_queue[-1]

    def empty(self):
        return 0 == len(self.data_queue)
"""

class MyStack():
    def __init__(self):
        self.data_queue = []
        self.temp_queue = []

    def push(self,item):
        self.temp_queue.insert(0,item)
        while self.temp_queue:
            self.data_queue.insert(0,self.temp_queue.pop())
        self.data_queue,self.temp_queue = self.temp_queue,self.data_queue

    def pop(self):
        return self.data_queue.pop()

    def top(self):
        return self.data_queue[-1]

    def empty(self):
        return 0 == len(self.data_queue)

stack = MyStack()
stack.push(1)
stack.push(2)
stack.top()
stack.pop()
stack.empty()
