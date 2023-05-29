def primes(self, n: int) -> set:
    ans = set()
    while n % 2 == 0:
        ans.add(2)
        n //= 2

    i = 3
    while i <= int(sqrt(n)):
        while n % i == 0:
            ans.add(i)
            n //= i
        i += 2
    if n > 2:
        ans.add(n)

    return ans
