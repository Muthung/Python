def find_ranges(nums):
    if not nums:
        return []

    ranges = []
    start_range = nums[0]
    end_range = nums[0]

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            # Extend the current range
            end_range = nums[i]
        else:
            # Create a new range
            if start_range == end_range:
                ranges.append(str(start_range))
            else:
                ranges.append("{}->{}".format(start_range, end_range))
            start_range = nums[i]
            end_range = nums[i]

    # Add the last range
    if start_range == end_range:
        ranges.append(str(start_range))
    else:
        ranges.append("{}->{}".format(start_range, end_range))

    return ranges