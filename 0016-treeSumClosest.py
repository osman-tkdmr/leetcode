def threeSumClosest(nums, target):
    nums.sort()

    if sum(nums[:3]) >= target:
        return sum(nums[:3])
    if sum(nums[-3:]) <= target:
        return sum(nums[-3:])

    curr = sum(nums[:3])
    for i in range(len(nums) - 2):

        f , l = i + 1, len(nums)-1  

        if i > 0 and nums[i] == nums[i -1]:
            continue

        while f < l:
            s = nums[f] + nums[l] + nums[i]
            if abs(target - s) < abs(target - curr):
                curr = s
            elif s < target:
                f += 1
            elif s > target:
                l -= 1
            else:
                return curr

    return curr