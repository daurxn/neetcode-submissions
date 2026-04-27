class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if num1 == num2 and i != j:
                    return True
        
        return False
        
