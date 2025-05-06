# https://leetcode.com/problems/3sum/?envType=study-plan-v2&envId=top-interview-150
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105


def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Life is easier if we sort our array. For each step, our first number in the set must
    be different from the previous one. The next 2 numbers must be behind the current choice,
    this makes sure no duplicated work. Use 2 pointers technique to select these numbers.
    This technique also help us avoiding duplicated choices.
    """
    answers = []
    nums.sort()

    for i in range(len(nums)):
        # Make sure we dont select used numbers.
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        first = nums[i]
        second, third = i + 1, len(nums) - 1
        while second < third:
            s = first + nums[second] + nums[third]
            if s > 0:
                third -= 1
            elif s < 0:
                second += 1
            else:
                answers.append([first, nums[second], nums[third]])
                second += 1
                while nums[second] == nums[second - 1] and second < third:
                    second += 1

    return answers
