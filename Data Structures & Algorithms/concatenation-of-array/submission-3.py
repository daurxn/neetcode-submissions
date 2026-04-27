class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [0] * size * 2

        for idx, num in enumerate(nums):
            ans[idx] = num
            ans[idx + size] = num
        
        return ans