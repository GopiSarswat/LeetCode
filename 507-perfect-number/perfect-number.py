class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        total = 1
        d = 2
        while d * d <= num:
            if num % d == 0:
                total += d
                if d != num // d:
                    total += num // d
            d += 1
        return total == num