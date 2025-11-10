class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        while x:
            d = x % 10
            x //= 10
            res = res * 10 + d
        res *= sign
        return res if INT_MIN <= res <= INT_MAX else 0