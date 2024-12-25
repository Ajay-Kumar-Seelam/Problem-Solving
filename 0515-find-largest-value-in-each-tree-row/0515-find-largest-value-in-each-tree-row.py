# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        
        q=deque([root])
        
        while q:
            
            level=[]
            for _ in range(len(q)):
                node=q.popleft()
                if node:
                    level.append(node.val)
                
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            if len(level)>0:
                maxi=level[0]
                for _ in range(len(level)):
                    maxi=max(maxi,level[_])
                ans.append(maxi)
        return ans
                
        
        