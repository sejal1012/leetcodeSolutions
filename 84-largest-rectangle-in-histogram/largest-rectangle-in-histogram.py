class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = []
        for i, height in enumerate(heights):
            if len(stack) == 0:
                stack.append([i, height])
            else:
                if(stack[-1][1] > height):
                    popIndex = stack[-1][0]
                    while(len(stack) and stack[-1][1] > height):
                        area = stack[-1][1] * (i - stack[-1][0])
                        if area > maxArea:
                            maxArea = area
                        popIndex = stack[-1][0]
                        stack.pop()
                    stack.append([popIndex, height])
                elif(stack[-1][1] <= height):
                    stack.append([i, height])
        # print("before area calc: ", stack)
        if(len(stack) != 0):
            compareIndex = stack[-1][0]
            while(len(stack)!= 0):
                area = stack[-1][1] * (-stack[-1][0] + i + 1)
                if area > maxArea:
                    maxArea = area
                stack.pop()
        return maxArea


            