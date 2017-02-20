# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

# Example -
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

def findComplement(num):
  """
  :type num: int
  :rtype: int
  """
  binList = list(bin(num))
  for i in range(2, len(binList)):
    if binList[i] == "0":
      binList[i] = "1"
    else:
      binList[i] = "0"
  binString = "".join(binList)
  return int(binString, 2)


num = 5
print(findComplement(num))