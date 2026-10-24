class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_nums = {}
        for i in nums:
            if i in dict_nums:
                dict_nums[i] += 1
            else:
                dict_nums[i] = 1

        for k, v in dict_nums.items():
            if v > 1:
                return True

        return False
            

