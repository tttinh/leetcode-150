# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false


# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.


# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?


def is_subsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)


# ----------------FOLLOW UP----------------------
# from collections import defaultdict
# import bisect


# def preprocess_t(t):
#     # Create a dictionary mapping each character to its indices in t
#     char_indices = defaultdict(list)
#     for i, char in enumerate(t):
#         char_indices[char].append(i)
#     return char_indices


# def is_subsequence(s, char_indices):
#     # Initialize the previous index position to -1 (before the first character of t)
#     prev_index = -1

#     for char in s:
#         if char not in char_indices:
#             return False
#         # Get the list of indices for the current character in s
#         indices = char_indices[char]
#         # Use binary search to find the smallest index greater than prev_index
#         pos = bisect.bisect_right(indices, prev_index)
#         if pos == len(indices):
#             return False
#         prev_index = indices[pos]

#     return True
