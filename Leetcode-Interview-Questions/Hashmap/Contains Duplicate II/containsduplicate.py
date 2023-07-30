def containsNearbyDuplicate(nums, k):
    num_index_map = {}  # Dictionary to store the element and its last seen index

    for i, num in enumerate(nums):
        if num in num_index_map and abs(i - num_index_map[num]) <= k:
            return True
        num_index_map[num] = i

    return False