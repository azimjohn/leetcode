import math

class Solution:
    def countPrimes(self, n: int) -> int:
        primes = []
        numbers = {i: True for i in range(2, n)}
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if self.isPrime(i):
                primes.append(i)
        
        for prime in primes:
            for i in range(prime*prime, n, prime):
                if i % prime == 0:
                    numbers[i] = False              

        return sum(numbers.values())
    
    def isPrime(self, n):
        if n == 2:
            return True
        
        for i in range(2,  int(math.sqrt(n))+1):
            if n % i == 0:
                return False

        return True
