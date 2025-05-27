# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Given a string s, find the length of the longest substring without duplicate characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


def length_of_longest_substring_without_repeating_chars(s: str) -> int:
    """
    Use a dict to track the latest indices of characters.
    Update the window size at each step by deciding whether or not a character
    can be selected into the window.
    """
    letters = {}
    start, longest = 0, 0

    for i, c in enumerate(s):
        if c not in letters or letters[c] < start:
            longest = max(longest, i - start + 1)
        else:
            start = letters[c] + 1
        letters[c] = i
    return longest
