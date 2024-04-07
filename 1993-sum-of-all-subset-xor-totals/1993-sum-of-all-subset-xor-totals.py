class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)
        total = 0

        for mask in range(1 << N):
            current = 0
                

            for x in range(N):
                if (mask & (1 << x)) > 0:
                    current ^= nums[x]

            total += current
        return total                
        