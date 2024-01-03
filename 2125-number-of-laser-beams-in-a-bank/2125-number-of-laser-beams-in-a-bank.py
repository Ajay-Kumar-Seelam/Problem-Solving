class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        '''Ajay
        '''
        ans=0
        pre=0
        for sr in bank:
            cur=0
            for i in sr:
                
                if i=='1':
                    cur+=1
            ans=ans+pre*cur
            
            if cur>0:
                pre=cur
        return ans
                    
            
        