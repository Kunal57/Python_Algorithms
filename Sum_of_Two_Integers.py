# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

# Example:
# Given a = 1 and b = 2, return 3.


def getSum(a, b):
  """
  :type a: int
  :type b: int
  :rtype: int
  """
  while b != 0:
    c = a & b
    a = a ^ b
    b = c << 1
  return a

a = 100
b = 13
print(getSum(a, b))