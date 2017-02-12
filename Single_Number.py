# Given an array of integers, every element appears twice except for one. Find that single one.

def singleNumber(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  dict = {}
  for number in nums:
    dict[number] = dict.get(number, 0) + 1
  for number in dict.keys():
    if dict[number] == 1:
      return number

nums = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,8,9]
print(singleNumber(nums))