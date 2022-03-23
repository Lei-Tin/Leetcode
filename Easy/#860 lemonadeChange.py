class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0, 20: 0}  # This change is the 5 bill, 10 bill, 20 bill

        for payment in bills:
            if payment == 5:
                change[5] += 1

            elif payment == 10:
                change[5] -= 1
                change[10] += 1

            elif payment == 20:
                if change[10] >= 1 and change[5] >= 1:
                    change[10] -= 1
                    change[5] -= 1
                    change[20] += 1

                else:
                    change[5] -= 3
                    change[20] += 1

            if any(change[bill] < 0 for bill in change):
                return False

        return True
