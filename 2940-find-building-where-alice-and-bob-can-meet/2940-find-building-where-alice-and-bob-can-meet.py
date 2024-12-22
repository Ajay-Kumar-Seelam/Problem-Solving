class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        
        @cache
        def recur(idx, target):
            if idx == n:
                return -1
            if heights[idx] > target:
                return idx
            return recur(idx+1, target)
            
        def get_ans(a, b):
            if a == b:
                return a
            if a > b and heights[a] > heights[b]:
                return a
            if a < b and heights[a] < heights[b]:
                return b
            next_idx = max(a, b) + 1
            target = max(heights[a], heights[b])
            return recur(next_idx, target)
        
        return [get_ans(a, b) for a, b in queries]