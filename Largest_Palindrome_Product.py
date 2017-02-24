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
  number = ""
  for x in range(n):
    number += "9"
  number = int(number)
  palindrome = 0
  upper = number + 1
  lower = 0
  for x in range(upper, lower, -1):
    for i in range(upper, lower, -1):
      product = x * i
      if product < palindrome:
        break
      elif isPalindrome(product):
        palindrome = product
        upper = x
        lower = i
        break
  return palindrome % 1337

def isPalindrome(num):
  """ Return True is number is Palindrome, else return False """
  if str(num) == str(num)[::-1]:
    return True
  return False

n = 5
print(largestPalindrome(n))
