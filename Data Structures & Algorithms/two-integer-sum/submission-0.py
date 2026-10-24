class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i , key in enumerate(nums):
            complement  = target - key
            if complement in seen:
                return [seen[complement],i]
            seen[key]= i
        return []


                

        