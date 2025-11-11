"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true
"""


def is_valid_parentheses(s):
    matches = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for bracket in s:
        if bracket in matches:
            stack.append(bracket)
        else:
            if not stack:
                return False
            candidate = stack.pop()
            return bracket == matches[candidate]
    return not stack


print(is_valid_parentheses("([])"))
