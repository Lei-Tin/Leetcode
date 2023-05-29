class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Solution 1
        # return sorted([num ** 2 for num in nums])

        # Solution 2
        # Using two pointers
        left_ptr = 0
        right_ptr = len(nums) - 1

        squared = []

        # Loop condition
        while left_ptr <= right_ptr:
            # Comparing the item at nums[left_ptr] and nums[right_ptr]
            if abs(nums[left_ptr]) > abs(nums[right_ptr]):
                squared.append(nums[left_ptr] ** 2)
                left_ptr += 1

            else:
                squared.append(nums[right_ptr] ** 2)
                right_ptr -= 1

        return reversed(squared)
