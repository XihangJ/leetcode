class Solution:
    #method1. sort then find max h and w. O(nlogn + mlogm). S(1)
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        h_max = 0
        for i in range(len(horizontalCuts) + 1):
            if i == 0:
                height = horizontalCuts[0]
            elif i == len(horizontalCuts):
                height = h - horizontalCuts[i - 1]
            else:
                height = horizontalCuts[i] - horizontalCuts[i - 1]
            h_max = max(height, h_max)
                
        verticalCuts.sort()
        w_max = 0
        for i in range(len(verticalCuts) + 1):
            if i == 0:
                width = verticalCuts[0]
            elif i == len(verticalCuts):
                width = w - verticalCuts[i - 1]
            else:
                width = verticalCuts[i] - verticalCuts[i - 1]
            w_max = max(width, w_max)  
        return (h_max * w_max) % (10 ** 9 + 7)
