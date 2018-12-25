# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def traversal(root):
            if root is None:
                return
            list.append(root.val)
            traversal(root.left)
            traversal(root.right)

        list = []
        traversal(root)
        return list

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def traversal(root):
            if root is None:
                return
            traversal(root.left)
            list.append(root.val)
            traversal(root.right)

        list = []
        traversal(root)
        return list

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def traversal(root):
            if root is None:
                return
            traversal(root.left)
            traversal(root.right)
            list.append(root.val)

        list = []
        traversal(root)
        return list