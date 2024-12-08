class Solution:
    def calculate_area(self, corners: List[List[int]]) -> int:
        bottom_left = corners[0]
        top_left = corners[1]
        bottom_right = corners[2]
        top_right = corners[3]

        # Check if the rectangle is valid
        if bottom_left[0] != top_left[0] or bottom_right[0] != top_right[0]:
            return -1
        if bottom_left[1] != bottom_right[1] or top_left[1] != top_right[1]:
            return -1

        # Calculate area
        return abs(bottom_left[0] - bottom_right[0]) * abs(top_left[1] - bottom_left[1])

    def has_internal_points(self, all_points: List[List[int]], rectangle: List[List[int]]) -> bool:
        bottom_left = rectangle[0]
        top_left = rectangle[1]
        bottom_right = rectangle[2]
        top_right = rectangle[3]

        for point in all_points:
            if point == bottom_left or point == top_left or point == bottom_right or point == top_right:
                continue
            x, y = point
            if bottom_left[0] <= x <= bottom_right[0] and bottom_left[1] <= y <= top_left[1]:
                return True
        return False
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        max_area = -1
        n = len(points)
        if n < 4:
            return max_area

        from itertools import combinations
        for combination in combinations(points, 4):
            corners = sorted(combination)
            area = self.calculate_area(corners)
            if area == -1 or self.has_internal_points(points, corners):
                continue
            max_area = max(max_area, area)

        return max_area
    
        