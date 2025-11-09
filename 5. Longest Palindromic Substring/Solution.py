class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        def expand(l: int, r: int) -> tuple[int, int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r  # half-open [lo, hi)

        best_lo, best_hi = 0, 1
        for i in range(len(s)):
            lo, hi = expand(i, i)          # odd length
            if hi - lo > best_hi - best_lo:
                best_lo, best_hi = lo, hi
            lo, hi = expand(i, i + 1)      # even length
            if hi - lo > best_hi - best_lo:
                best_lo, best_hi = lo, hi

        return s[best_lo:best_hi]