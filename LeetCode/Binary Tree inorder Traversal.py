# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: [TreeNode]) -> [int]:

        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.val)
                traverse(node.right)

        traverse(root)
        return result

    def inorderTraversalIterative(self, root: [TreeNode]) -> [int]:
        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result



root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(9)

testCase = Solution()
print(testCase.inorderTraversal(root))
print(testCase.inorderTraversalIterative(root))

