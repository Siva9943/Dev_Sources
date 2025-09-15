nums=[2,3,4,5,6]
def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if(nums[i]+nums[j+1]==target):
                return list[i,j+1]
print(twoSum(nums,7))

"""
Solved !------
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j]==target):
                return [i,j] 

"""
