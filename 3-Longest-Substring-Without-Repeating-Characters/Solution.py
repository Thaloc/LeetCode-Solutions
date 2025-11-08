def lengthOfLongestSubstring(s: str) -> int:
    last = {}
    l = 0
    best = 0
    for r, c in enumerate(s):
        if c in last and last[c] >= l:
            l = last[c] + 1
        last[c] = r
        best = max(best, r - l + 1)
    return best