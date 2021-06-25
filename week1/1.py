class Solution:
    def getArea(self, height, left, right):
        width = right - left
        height = min(height[left], height[right])
        return width * height

    def maxArea(self, height: List[int]) -> int:
    	if height is None: return 0
    	left, right, area = 0, len(height) - 1, 0
    	while left <= right:
    		area = max(area, self.getArea(height, left, right))
    		if height[left] < height[right]:
    			left += 1
    		else:
    			right-= 1
    	return area
