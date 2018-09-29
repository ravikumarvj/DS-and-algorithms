class Solution:
    def twosum(self, nums, target, start, end):
        i = start
        j = end
        ret = []
        while j > i:
            if nums[i] + nums[j] == target:
                ret.append([nums[i], nums[j]])
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return ret

    def threesum(self, nums, target, start, end):
        for i in range(end, start - 1, -1):
            ret = self.twosum(nums, target - nums[i], start, i - 1)
            if ret:
                for r in ret:
                    r.append(nums[i])
        return ret

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []

        nums.sort()
        start = 0
        end = len(nums) - 1

        for i in range(end, -1, -1):
            ret = self.threesum(nums, target - nums[i], start, i - 1)
            if ret:
                for r in ret:
                    r.append(nums[i])
        s = [set(r) for r in ret]
        s = set(s)

        return s





if __name__ == '__main__':
    s = Solution()
    s.fourSum([1,0,-1,0,-2,2], 0)