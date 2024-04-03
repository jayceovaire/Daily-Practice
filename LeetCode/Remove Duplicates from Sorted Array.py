class Solution:
    def removeDuplicates(self, nums: []) -> int:

        if not nums:
            return 0

        idx = 0

        for i in range(1,len(nums)):
            if nums[i] != nums[idx]:
                idx += 1
                nums[idx] = nums[i]
        del nums[idx + 1:]

        return len(nums)


newT = Solution()
testA = [1,1,2,3]

print(newT.removeDuplicates(testA))