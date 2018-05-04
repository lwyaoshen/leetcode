# 1. Two Sum
# Given an array of integers,
# return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


def two_sum(nums, target):
    dic = {}
    for ind, each in enumerate(nums):
        less = target - nums[ind]
        if less in dic.keys():
            return dic[less], ind
        dic[each] = ind


print(two_sum([2, 7, 11, 15], 13))
