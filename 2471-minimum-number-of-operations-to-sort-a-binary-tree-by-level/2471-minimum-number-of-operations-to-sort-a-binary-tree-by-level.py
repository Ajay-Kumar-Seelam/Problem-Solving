# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        def count_swaps(nums):
            swaps=0
            sorted_nums=sorted(nums)
            
            ind_map={n:i for i,n in enumerate(nums)}
            for i in range(len(nums)):
                if nums[i]!=sorted_nums[i]:
                    swaps+=1
                    
                    j=ind_map[sorted_nums[i]]
                    nums[i],nums[j]=nums[j],nums[i]
                    ind_map[nums[j]]=j
                    
            return swaps
        dq=deque([root])
        res=0
        while dq:
            level=[]
            for _ in range(len(dq)):
                
                temp=dq.popleft()
                level.append(temp.val)
                
                if temp.left:
                    dq.append(temp.left)
                if temp.right:
                    dq.append(temp.right)
            
            res+=count_swaps(level)
            
        return res
            
            
        
        
        