def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    #Calculate the prefix product
    prefix_product = 1
    for i in range(n):
        result[i] *= prefix_product
        prefix_product *= nums[i]

    #Calculate the suffix product and multiply with the prefix product
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix_product
        suffix_product *= nums[i]

    return result
