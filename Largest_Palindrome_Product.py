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
  minNum = int(number[:-1])
  number = int(number)
  palindrome = 0
  for x in range(number, minNum, -2):
    if (x**2) < palindrome:
      break
    for i in range(number, x - 1, -2):
      product = x * i
      if product <= palindrome or product % 11 != 0:
        break
      elif isPalindrome(product):
        palindrome = product
        print(palindrome, palindrome % 1337)
        break
  return (palindrome, palindrome % 1337)


def isPalindrome(num):
  """ Return True is number is Palindrome, else return False """
  numString = str(num)
  if numString == numString[::-1]:
    return True
  return False

n = 8
print(largestPalindrome(n))

# for i in range(upper, int((x*x)**.5), -2):
# 990090099 152 99999 9901 99998 76865