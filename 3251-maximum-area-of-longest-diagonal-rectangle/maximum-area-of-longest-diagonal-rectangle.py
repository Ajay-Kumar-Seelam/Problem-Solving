class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxArea, Mdia2=0, 0
        for w, h in dimensions:
            dia2=w*w+h*h
            if Mdia2<dia2:
                Mdia2=dia2
                maxArea=0
            if dia2==Mdia2:
                maxArea=max(maxArea, w*h)
        return maxArea
        