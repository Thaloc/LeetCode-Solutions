class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        i, n = 0, len(s)
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0

        sign = 1
        if s[i] in '+-':
            sign = -1 if s[i] == '-' else 1
            i += 1

        res = 0
        while i < n and s[i].isdigit():
            d = ord(s[i]) - 48
            # pre-check overflow before push
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and d > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            res = res * 10 + d
            i += 1

        res *= sign
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
        return res