class MyCircularQueue:
    #创建一个列表
    #front 从队列获取元素
    #rear 获取队尾元素
    queue = []
    count, front, rear = 0, 0, 0

    def __init__(self, k):
        self.queue = [ 0 for i in range(k)]
        print(self.queue)

    def enQueue(self, value):
    #向循环队列插入一个元素。如果成功插入则返回真。
        print(value)
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % len(self.queue)
        self.count += 1
        return True


    def deQueue(self):
    # 向循环队列删除一个元素。如果成功删除则返回真。
        if self.isFull():
            return False
        self.front = (self.front + 1) % len(self.queue)
        self.count -= 1
        print(self.queue)

    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[len(self.queue) - 1] if self.rear == 0 else self.queue[self.rear - 1]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == len(self.queue)

#构造器，设置队列的大小
circularQueue = MyCircularQueue(4)
circularQueue.enQueue(1)
circularQueue.enQueue(2)
circularQueue.enQueue(3)
circularQueue.enQueue(4)

circularQueue.Rear()
circularQueue.isFull()
circularQueue.deQueue()
circularQueue.enQueue(4)
circularQueue.Rear()
