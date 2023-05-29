class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_a = set()
        set_b = set()
        ans = []

        for i in range(len(A)):
            set_a.add(A[i])
            set_b.add(B[i])

            ans.append(len(set_a & set_b))

        return ans
