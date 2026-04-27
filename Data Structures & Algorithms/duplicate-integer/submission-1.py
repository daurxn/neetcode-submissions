class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        
        for num in nums:
            if num in counts:
                return True
            
            counts[num] = 0

        return False
        
