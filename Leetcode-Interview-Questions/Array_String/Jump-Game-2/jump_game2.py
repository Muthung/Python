def minJumps(nums):
    n = len(nums)
    jumpGame = [float("inf")] * n
    jumpGame[0] = 0

    for i in range(i, n):
        for j in range(i):
            if j + nums[j] >= i:
                jumpGame[i] = min(jumpGame[i], jumpGame[j] + 1)

    return jumpGame[n - 1]
