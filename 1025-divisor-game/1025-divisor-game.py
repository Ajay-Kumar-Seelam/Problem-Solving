class Solution:
    def divisorGame(self, n: int) -> bool:
        
        def fun(n:int,t:int):
            if n<1:
                return False
            elif n==1 and t%2==0:
                return True
            elif n==1 and t%2!=0:
                return False
            
            for i in range(1,n):
                
                if i==1:
                    return fun(n-1,t+1)
                elif i>1 and n%i==0:
                    fact1=i
                    
                    fact2=n/i
                    if fun(n-fact1,t+1) or fun(n-fact2,t+1):
                        return True
                    else:
                        return False
        return fun(n,1)
                    
            
        
        
        