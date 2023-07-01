def rotate(nums, k):
    k = k % len(nums)

    nums[:] = nums[-k:] + nums[:-k]
