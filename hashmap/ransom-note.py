# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.


# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true


# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.


def ransom_note(note: str, magazine: str) -> bool:
    letters = {}
    for c in magazine:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1

    for c in note:
        if c not in letters or letters[c] == 0:
            return False

        letters[c] -= 1

    return True
