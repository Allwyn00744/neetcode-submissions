class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers)-1
        res=[]
        sum=0
        while(left<right):
            sum = numbers[left] + numbers[right]
            if (sum == target):
                res.append(left+1)
                res.append(right+1)
                break
            elif(sum < target):
                left += 1
            else:
                right -= 1
        return res

