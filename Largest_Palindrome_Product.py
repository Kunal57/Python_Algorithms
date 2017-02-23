# Find the largest palindrome made from the product of two n-digit numbers.

# Since the result could be very large, you should return the largest palindrome mod 1337.

# Example:
# Input: 2
# Output: 987
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

# Note:
# The range of n is [1,8].

def largestPalindrome(n):
  """
  :type n: int
  :rtype: int
  """
  number1 = ""
  number2 = ""
  for x in range(n):
    number1 += "9"
    number2 += "9"
  number1 = int(number1)
  number2 = int(number2)
  palindrome = 0
  for x in range(number1 + 1):
    for i in range(number2 + 1):
      product = x * i
      if (str(product) == str(product)[::-1]) and product > palindrome:
        palindrome = product
  return palindrome % 1337



n = 2
print(largestPalindrome(n))