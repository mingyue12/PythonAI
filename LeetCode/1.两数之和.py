class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = {}  # 创建一个空哈希表（字典）
        for j, x in enumerate(nums):  # 需要先把所有数及其下标都加到哈希表中
            idx[x] = j  # 直接覆盖，相同元素的下标取最靠右的
        print(idx)
        for i, x in enumerate(nums):  # x=nums[i]
            if idx[x] == i:  # 右边没有 x 了，必须删除
                del idx[x]
            if target - x in idx:  # 在右边找 nums[j]，满足 x+nums[j]=target
                return [i, idx[target - x]]  # 返回两个数的下标



Nums = [2, 7, 11, 15]
Target = 9
S1 = Solution()
Result = S1.twoSum(Nums, Target)
print(Result)
