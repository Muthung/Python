def majority_element(nums):
    storage = nums[0]
    steps = 1

    for i in range(1, len(nums)):
        if nums[i] == storage:
            steps += 1

        else:
            steps -= 1
            if steps == 0:
                storage = nums[i]
                steps = 1
    return storage
