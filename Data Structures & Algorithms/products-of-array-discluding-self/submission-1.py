class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProd = rightProd = 1
        prefixProd, postProd = [1] * n, [1] * n

        for i in range(1, n):
            leftProd *= nums[i-1]
            prefixProd[i] = leftProd
        
        for i in range(n - 2, -1, -1):
            rightProd *= nums[i+1]
            postProd[i] = rightProd

        res = []
        for i in range(n):
            res.append(prefixProd[i] * postProd[i])

        return res