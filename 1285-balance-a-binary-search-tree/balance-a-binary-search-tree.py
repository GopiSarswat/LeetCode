# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        def build(l, r):
            if l > r: return None
            m = (l + r) // 2
            node = TreeNode(arr[m])
            node.left = build(l, m - 1)
            node.right = build(m + 1, r)
            return node
        inorder(root)
        return build(0, len(arr) - 1)
