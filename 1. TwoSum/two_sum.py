class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, x in enumerate(nums):
            c = target - x
            if c in seen:
                return [seen[c], i]
            seen[x] = i
        # per constraints, this line is unreachable
        return []