class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        largest=max(nums)
        m=nums.index(largest)
        for i in nums:
            if i!=largest and largest<i*2:
                return -1
        return m        


        