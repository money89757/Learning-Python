class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self,root):
        nodeQueue = []
        result = []
        if not root:
            return result
        nodeQueue.append(root)
        while nodeQueue:
            singleLevel = []
            queueLength = len(nodeQueue)
            for i in range(0, queueLength):
                currentNode = nodeQueue.pop(0)
                if currentNode.left:
                    nodeQueue.append(currentNode.left)
                if currentNode.right:
                    nodeQueue.append(currentNode.right)
                singleLevel.append(currentNode.val)
            result.append(singleLevel)
        return result


def createBST(nums):
    root = None
    for num in nums:
        root = insert(root, num)
    return root

def insert(root,val):
    if not root:
        return TreeNode(val)
    if val <= root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

if __name__ == "__main__":
    root = createBST([3,9,20,15,7])
    node = Solution()
    print(node.levelOrder(root))