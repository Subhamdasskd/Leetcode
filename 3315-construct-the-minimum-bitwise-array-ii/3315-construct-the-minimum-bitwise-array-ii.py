class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        B = 32
        INF = 10 ** 20
        
        """
        101111 - 47

        100111 - 39
        101000 - 40

        """

        def f(x):
            mask = (1 << B) - 1
            best = INF
            for i in range(B):
                """

                11111000

                11111111 ^ 000000111

                """
                #nmask = ((mask >> i) << i)
                nmask = mask ^ ((1 << i) - 1)
                t = (x & nmask)

                if (t | (t - 1)) == x:
                    best = min(best, t - 1)
            if best >= INF:
                return -1
            return best


        ans = []
        for x in nums:
            ans.append(f(x))
        return ans