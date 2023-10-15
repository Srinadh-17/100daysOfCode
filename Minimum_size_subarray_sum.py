class Solution(object):
    def minSubArrayLen(self, target, nums):
        l, r, total = 0, 0, 0
        min_len = len(nums) + 1
        while r < len(nums):
            total += nums[r]
            r += 1
            while total >= target:
                min_len = min(min_len, r - l)
                total -= nums[l]
                l += 1
        if min_len == len(nums) + 1:
            return 0
        else:
            return min_len
        