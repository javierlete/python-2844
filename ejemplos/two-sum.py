# https://leetcode.com/problems/two-sum/
def twoSum(nums, target):
    for a in range(len(nums)-1):
        for b in range(a + 1, len(nums)):
            print(f'{nums[a]}+{nums[b]}={target}?', end=' ')

            if nums[a] + nums[b] == target:
                return [a, b]

    return None

print(twoSum([1, 2, 3, 4, 5, 6], 11))
