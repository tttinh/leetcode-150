# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.


# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


def product_except_self(nums: list[int]) -> list[int]:
    """
    First go from right to left to calculate suffix products. Then go from left to right to calculate prefix
    products, also update the product of current index using the same loop. We just need a variable to store
    the prefix product.
    """
    n = len(nums)
    answers = [1] * n
    product = 1
    for i in range(n - 1, -1, -1):
        answers[i] = product
        product = nums[i] * product

    product = 1
    for i in range(0, n):
        answers[i] = product * answers[i]
        product *= nums[i]

    return answers
