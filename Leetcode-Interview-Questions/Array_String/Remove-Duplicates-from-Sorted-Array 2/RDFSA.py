def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    writer = 1
    counter = 1

    for reader in range(1, len(nums)):
        if nums(reader) == nums(reader - 1):
            counter += 1
        else:
            counter = 1

        if counter <= 2:
            nums[writer] = nums[reader]
            writer += 1


    return writer
