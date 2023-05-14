class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # a = b ^ c then c = a ^ b and b = a ^ c

        if len(derived) == 1:
            return derived[0] == 0

        orig1 = [0]
        for i in range(1, len(derived)):
            orig1.append(orig1[i - 1] ^ derived[i - 1])

        orig2 = [1]
        for i in range(1, len(derived)):
            orig2.append(orig2[i - 1] ^ derived[i - 1])

        return orig1[0] ^ orig1[-1] == derived[-1] or orig2[0] ^ orig2[-1] == derived[-1]
