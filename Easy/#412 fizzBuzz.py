class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # 1 Line solution
        # return ['Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) + str(i) * (not i % 3 == 0 and not i % 5 == 0) for i in range(1, n + 1)]

        i = 1
        f = b = 0
        res = []

        while i < n + 1:
            f += 1
            b += 1

            if f == 3 and b == 5:
                res.append('FizzBuzz')
                f = b = 0

            elif f == 3:
                res.append('Fizz')
                f = 0

            elif b == 5:
                res.append('Buzz')
                b = 0

            else:
                res.append(str(i))

            i += 1

        return res
