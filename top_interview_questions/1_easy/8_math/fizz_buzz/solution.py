class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(1, n + 1):
            if i % 15 == 0:
                string = "FizzBuzz"
            elif i % 5 == 0:
                string = "Buzz"
            elif i % 3 == 0:
                string = "Fizz"
            else:
                string = str(i)

            result.append(string)

        return result
