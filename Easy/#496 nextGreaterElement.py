class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        mapping = {}
        stack = [nums2[0]]

        for i in range(1, len(nums2)):
            while len(stack) > 0 and stack[-1] < nums2[i]:
                mapping[stack[-1]] = nums2[i]
                stack.pop()

            stack.append(nums2[i])

        for num in nums1:
            ans.append(mapping.get(num, -1))

        return ans
