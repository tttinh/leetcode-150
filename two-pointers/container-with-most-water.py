# https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


# Example 2:

# Input: height = [1,1]
# Output: 1


# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104


def container_with_most_water(height: list[int]) -> int:
    """
    Use 2 pointers, one from left on from right. Update the max area if possible at
    every loop. Move the pointer that has the lower height.
    """
    max_area = 0
    left, right = 0, len(height) - 1
    while left < right:
        area = (right - left) * min(height[left], height[right])
        if area > max_area:
            max_area = area

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
