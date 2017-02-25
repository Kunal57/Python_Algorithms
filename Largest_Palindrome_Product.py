# Find the largest palindrome made from the product of two n-digit numbers.

# Since the result could be very large, you should return the largest palindrome mod 1337.

# Example:
# Input: 2
# Output: 987
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

# Note:
# The range of n is [1,8].

from itertools import product

def largestPalindrome(n):
  """
  :type n: int
  :rtype: int
  """
  number = ""
  for x in range(n):
    number += "9"
  number = int(number)
  palindrome = 0
  for x in range(number, 1, -2):
    if (x*x) < palindrome:
      break
    for i in range(number, x - 1, -2):
      product = x * i
      if product < palindrome:
        break
      elif isPalindrome(product):
        palindrome = product
        break
  return palindrome % 1337

def isPalindrome(num):
  """ Return True is number is Palindrome, else return False """
  return str(num) == str(num)[::-1]


n = 7
print(largestPalindrome(n))