class Solution:

    def binary_search(self, nums, start, end, target) -> int:

        if target > nums[end] or target < nums[start]:
            return -1

        index = (end + start) // 2

        if target == nums[index]:
            return index

        elif target > nums[index]:
            return self.binary_search(nums, index + 1, end, target)

        else:
            # targe < nums[index]
            return self.binary_search(nums, start, index - 1, target)

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complement = 0

        for i in range(len(numbers)):
            complement = target - numbers[i]

            index_2 = self.binary_search(numbers, i + 1, len(numbers) - 1, complement)

            if index_2 != -1:
                return [i + 1, index_2 + 1]

#         left = 0
#         right = len(numbers) - 1


#         while left < right:
#             if numbers[left] + numbers[right] == target:
#                 return [left + 1, right + 1]  # Doing the +1 because it is 1-indexed for some reasons

#             elif numbers[left] + numbers[right] < target:
#                 left += 1

#             else:
#                 right -= 1
