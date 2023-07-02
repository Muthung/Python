def canJump(nums):
    n = len(nums)

    # The farthest positioon it can reach
    maximum_index = 0

    for i in range(n):
        if i > maximum_index:

            # It cannont reach the current index
            return False

        # Updating the farthest position
        maximum_index = max(maximum_index, i + nums[i])

        if maximum_index >= n - 1:

            # It cannot reach the last index
            return True

    return False
