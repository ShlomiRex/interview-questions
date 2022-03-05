# Find second minimum in exactly one pass with O(1) space
from typing import List

def findSecondMinimum(nums: List[int]) -> int:
	if nums is None or len(nums) < 2:
		raise "Invalid input"
	# Min 1 is the minimum value
	# Min 2 is the second minimum value
	min1 = nums[0]
	min2 = float('inf')
	for i in range(1, len(nums)):
		num = nums[i]
		if num < min1:
			# Switch min1 and min2
			min2 = min1
			min1 = num
		elif num < min2 and num != min1:
			# Switch min2 only
			min2 = num
	return min2

if __name__ == "__main__":
	nums = [1,2,3,4,5]
	res = findSecondMinimum(nums)
	print(res)
	assert res == 2

	nums = [5,4,3,2,1]
	res = findSecondMinimum(nums)
	print(res)
	assert res == 2

	nums = [1,2]
	res = findSecondMinimum(nums)
	print(res)
	assert res == 2
 
	nums = [0,1,0,1,0,1,0,1]
	res = findSecondMinimum(nums)
	print(res)
	assert res == 1