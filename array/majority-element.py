# https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109


# Follow-up: Could you solve the problem in linear time and in O(1) space?


def majority_element(nums: list[int]) -> int:
    """
    Boyer–Moore majority vote algorithm
    """
    m, c = 0, 0
    for n in nums:
        if c == 0:
            m = n
            c = 1
        elif m == n:
            c += 1
        else:
            c -= 1
    return m
