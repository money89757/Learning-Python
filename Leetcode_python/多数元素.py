class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, cnt = 0, 1

        for i in range(1, len(nums)):
            if nums[idx] == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    idx = i
                    cnt = 1
        print (nums[idx])
        return nums[idx]


if __name__ == "__main__":
    temp = Solution()
    T = [2,3,4,5,5,6]
    temp.majorityElement(T)
