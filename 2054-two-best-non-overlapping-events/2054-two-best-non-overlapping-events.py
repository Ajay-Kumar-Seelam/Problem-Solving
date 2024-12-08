class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        line_sweep=[]
        for i in events:
            line_sweep.append([i[0],1,i[2]])
            line_sweep.append([i[1]+1,-1,i[2]])
        print(line_sweep)
        line_sweep.sort()
        max_val=0
        max_seen=0
        print(line_sweep)
        for event in line_sweep:
            point=event[0]
            status=event[1]
            val=event[2]
            if status==1:
                max_val=max(max_val,max_seen+val)
            if status==-1:
                max_seen=max(max_seen,val)
        return max_val
            