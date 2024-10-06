# s = "abc"
# t = "ahbgdc"
# # Pointer for string `s`
# index = 0

# # Iterate through string `t`
# for char in t:
#     # If the current character matches the one we're looking for in `s`
#     if index < len(s) and char == s[index]:
#         index += 1  # Move to the next character in `s`

# # If we've matched all characters in `s`, it is a subsequence
# is_subsequence = index == len(s)

# print(is_subsequence)  # Output: False


# #2. optimal
# # Two pointers, one for each string
# i, j = 0, 0

# # Traverse both strings
# while i < len(s) and j < len(t):
#     # If characters match, move the pointer for `s`
#     if s[i] == t[j]:
#         i += 1
#     # Always move the pointer for `t`
#     j += 1

# # Check if all characters in `s` were matched
# is_subsequence = i == len(s)