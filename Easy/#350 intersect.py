class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_one = {}
        nums_two = {}

        for num in nums1:
            if num not in nums_one:
                nums_one[num] = 1
            else:
                nums_one[num] += 1

        for num in nums2:
            if num not in nums_two:
                nums_two[num] = 1
            else:
                nums_two[num] += 1

        ans = []

        for num in nums_one:
            if num in nums_two:
                nums_one[num] = min(nums_one[num], nums_two[num])
            else:
                nums_one[num] = 0

            while nums_one[num] > 0:
                ans.append(num)
                nums_one[num] -= 1

        return ans
