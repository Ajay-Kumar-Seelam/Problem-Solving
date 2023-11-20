class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ttime=[0]
        ans=0
        for i in range(0,len(travel)):
            ttime.append(travel[i]+ttime[i])
        posG=posP=posM=0
        print(ttime)
        for i in range(0,len(garbage)):
            print("Iter",i)
            strn=garbage[i]
            if 'G' in strn:
                posG=i
            if 'M' in strn:
                posM=i
            if 'P' in strn:
                posP=i
            ans+=len(garbage[i])
            print(posG,posM,posP)
            
        ans=ans+ttime[posG]+ttime[posM]+ttime[posP]
        return ans
            
        