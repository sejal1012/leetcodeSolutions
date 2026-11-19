class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        case1 = nums[len(nums)-2]  - nums[1]
        case2 = nums[len(nums)-1] - nums[2]
        case3 = nums[len(nums)-3] - nums[0]
        result = min(case1, case2, case3)
        return result
        