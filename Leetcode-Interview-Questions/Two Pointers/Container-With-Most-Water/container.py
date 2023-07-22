def maxArea(height):
    n = len(height)
    left = 0
    right = n - 1
    maxArea = 0

    while left < right:
        currentArea = min(heigth[left], height[right]) * (right - left)
        maxArea = max(maxArea, currentArea)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxArea
