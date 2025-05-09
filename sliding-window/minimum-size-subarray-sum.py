# https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104


# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).


def min_size_subarray_sum(target: int, nums: list[int]) -> int:
    """
    Using sliding window technique from left to right. This is because the list only
    contains positive elements. If the list has negative numbers, we should use
    another approach.
    """
    ans = len(nums) + 1
    agg, left, right = nums[0], 0, 0
    while left <= right:
        if agg >= target:
            ans = min(right - left + 1, ans)
            agg -= nums[left]
            left += 1
        else:
            right += 1
            if right >= len(nums):
                break

            agg += nums[right]

    return ans if ans <= len(nums) else 0
