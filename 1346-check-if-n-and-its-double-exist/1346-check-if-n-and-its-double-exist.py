class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                if arr[j]==arr[i]*2 or arr[i]==arr[j]*2:
                    print(i,j)
                    return True
#         dic={}
#         for i in arr:
#             if i not in dic:
#                 dic[i]=1
#         for j in dic.keys():
            
#             if j!=0 and (j*2 in dic or j/2 in dic ):
#                 return True
            
        return False
    