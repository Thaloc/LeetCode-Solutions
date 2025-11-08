from math import inf
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        m, n = len(A), len(B)
        half = (m + n + 1) // 2

        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i

            L1 = -inf if i == 0 else A[i - 1]
            R1 =  inf if i == m else A[i]
            L2 = -inf if j == 0 else B[j - 1]
            R2 =  inf if j == n else B[j]

            if L1 <= R2 and L2 <= R1:
                if (m + n) % 2:
                    return float(max(L1, L2))
                return (max(L1, L2) + min(R1, R2)) / 2.0
            elif L1 > R2:
                hi = i - 1
            else:
                lo = i + 1

        return 0.0