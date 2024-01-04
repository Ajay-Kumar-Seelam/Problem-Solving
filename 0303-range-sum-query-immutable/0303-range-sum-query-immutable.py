class NumArray:
    '''Ajay'''

    def __init__(self, nums: List[int]):
        self.obj=[]
        self.obj.append(nums[0])
        if len(nums)>1:
            for i in range(1,len(nums)):
                self.obj.append(self.obj[i-1]+nums[i])
        # print(self.obj)
        return
            
        

    def sumRange(self, left: int, right: int) -> int:
        # print(self.obj)
        
        if left==0:
            # print("works")
            return self.obj[right]
        elif right==0:
            return self.obj[left]
        else:
            # print("doesn't work")
            return self.obj[right]-self.obj[left-1]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)