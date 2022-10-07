class Solution:
    def twoSum(self, nums: list, target: int):
        self.nums = nums
        self.target = target
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j] == self.target and i != j:
                    first = self.nums.index(nums[i])
                    second = self.nums.index(nums[j])
                    if first == second:
                        second = self.nums.index(nums[j], first+1)
                    return [first, second]

print(Solution().twoSum([3,3], 6))
