# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

# Exampe:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
#     For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
#     For number 1 in the first array, the next greater number for it in the second array is 3.
#     For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

def nextGreaterElement(findNums, nums):
  """
  :type findNums: List[int]
  :type nums: List[int]
  :rtype: List[int]
  """
  greaterNumbers = []
  for i in range(len(findNums)):
    index = nums.index(findNums[i])
    for x in range(index, len(nums)):
      if nums[x] > findNums[i]:
        greaterNumbers.append(nums[x])
        break
      elif x == (len(nums) - 1):
        greaterNumbers.append(-1)
  return greaterNumbers


findNums = [4,1,2]
nums = [1,2,3,4]
print(nextGreaterElement(findNums, nums))