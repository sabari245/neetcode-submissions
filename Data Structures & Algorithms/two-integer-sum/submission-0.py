class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        req = {}

        for index in range(len(nums)):
            if target - nums[index] in req:
                return [req[target - nums[index]],index]
            else:
                req[nums[index]] = index
        