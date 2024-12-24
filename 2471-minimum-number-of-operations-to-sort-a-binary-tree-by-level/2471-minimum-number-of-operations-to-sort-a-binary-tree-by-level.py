# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def count_swap(nums):
            swap=0
            sorted_nums=sorted(nums)
            
            ind={n:i for i,n in enumerate(nums)}
            
            for z in range(len(nums)):
                
                if sorted_nums[z]!=nums[z]:
                    temp=ind[sorted_nums[z]]
                    ind[nums[z]],ind[sorted_nums[z]]=temp,z
                    nums[temp]=nums[z]
                    nums[z]=sorted_nums[z]
                    
                    swap+=1
            return swap
                    
            
        res=0
        
        
        q=deque([root])
        while q:
            
            level=[]
            
            for _ in range(len(q)):
                node=q.popleft()
                level.append(node.val)
                print(node.val,end=" ")
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            # q=level
            res+=count_swap(level)
        return res
            
        
        
        
            
            
        
        
        