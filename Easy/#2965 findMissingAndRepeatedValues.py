class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        n2 = n * n
        
        expected_sum = (n2 * (n2 + 1)) // 2
        expected_sum_sq = (n2 * (n2 + 1) * (2 * n2 + 1)) // 6
        
        current_sum = 0
        current_sum_sq = 0
        
        # Loop through all values in the grid to calculate current_sum and current_sum_sq
        for row in grid:
            for num in row:
                current_sum += num
                current_sum_sq += num * num
        
        # Calculate the differences
        sum_diff = expected_sum - current_sum
        sum_sq_diff = expected_sum_sq - current_sum_sq
        
        # Now we can solve for the repeating number 'a' and missing number 'b'
        # sum_diff = b - a
        # sum_sq_diff = b^2 - a^2 = (b - a)(b + a)
        # We can express b + a = sum_sq_diff / sum_diff
        sum_plus_diff = sum_sq_diff // sum_diff
        
        # Solve the system of equations:
        # b - a = sum_diff
        # b + a = sum_plus_diff
        b = (sum_diff + sum_plus_diff) // 2
        a = b - sum_diff
        
        return [a, b]