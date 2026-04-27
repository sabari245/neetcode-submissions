class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        before = []
        after = []

        i, j = 0, -1

        l, r = 1, 1

        while i < len(nums) and j >= -1 * len(nums):
            l = l * nums[i]
            r = r * nums[j]
            before.append(l)
            after.append(r)
            i += 1
            j -= 1
            
        for index in range(len(nums)):
            if index == 0:
                res.append(after[-2])
            elif index == len(nums) -1:
                res.append(before[-2])
            else:
                res.append(before[index-1] * after[-1 * (index+2)])

        return res