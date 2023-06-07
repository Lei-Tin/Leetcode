class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        diff = (a | b) ^ c  # Shows the different bits, each different bits require at least 1 flip.

        # a b c
        # 1 1 0
        # Require 2 flips

        # 1 0 1
        # Require 0 flip

        # 0 0 1
        # Require 1 flip

        return bin(diff).count('1') + bin(diff & a & b).count('1')
