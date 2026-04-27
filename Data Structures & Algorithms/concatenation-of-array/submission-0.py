class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for idx, num in enumerate(nums):
            ans.insert(idx, num)
            ans.append(num)

        return ans