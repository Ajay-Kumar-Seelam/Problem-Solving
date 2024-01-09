# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a1=[]
        b2=[]
        def dfs(node,temp):
            if node==None:
                return temp
            if node.left==None and node.right==None:
                temp.append(node.val)
            temp=dfs(node.left,temp)
            temp=dfs(node.right,temp)
			
            return temp
        
        r1=dfs(root1,a1)
        r2=dfs(root2,b2)
	 
	    
        if r1==r2:
            return True
        else:
            return False

                
            
        