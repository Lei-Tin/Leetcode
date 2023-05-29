class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        left = right = 0

        res = []

        for i in range(n):
            nums1.pop()

        while left < len(nums1) and right < len(nums2):
            if nums1[left] <= nums2[right]:
                res.append(nums1[left])
                left += 1
            else:
                res.append(nums2[right])
                right += 1

        if left >= len(nums1):
            res.extend(nums2[right:])
        else:
            res.extend(nums1[left:])

        nums1[:] = res
