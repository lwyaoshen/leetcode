# 9. Palindrome Number
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
# Input: 121
# Output: true

# Example 2:
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:
#
# Coud you solve it without converting the integer to a string?


def reverse_integer(x):
    result = 0
    while x:
        result = result * 10 + x % 10
        x = x // 10
    return result


def palindrome_number(number):
    if number < 0:
        return False
    reverse = reverse_integer(number)
    if reverse == number:
        return True
    return False

print(palindrome_number(122))