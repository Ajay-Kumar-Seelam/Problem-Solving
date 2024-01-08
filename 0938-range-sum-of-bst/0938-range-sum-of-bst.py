# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def sum(root):
            if root == None:
                return 0
            ans = 0
            if low <= root.val <= high:
                ans += root.val
                ans += sum(root.left)
                ans += sum(root.right)
            elif root.val < low: 
                ans += sum(root.right)
            elif root.val > low: 
     
                ans += sum(root.left)

            return ans

        return sum(root)
                
            
        