class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        encounters = {}
        for num in nums:
            if num in encounters:
                return True
            encounters[num] = True
        
        return False

# [1, 2, 3, 3]
# [1, 2, 3, 3]