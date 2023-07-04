def trap(height):
    n = len(height)
    left = 0
    right = n - 1
    left_maxim = right_maxim = water_total = 0

    while left <= right:
        if height[left] <= height[right]:
            if height[left] > left_maxim:
                left_maxim = height[left]
            else:
                water_total += left_maxim - height[left]
            left += 1

        else:
            if height[right] > right_maxim:
                right_maxim = height[right]
            else:
                water_total += right_maxim - height[right]
            right -= 1

    return water_total
