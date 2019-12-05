#这是正常的双指针解法的实现
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        else:
            i=0
            for j in range(len(nums)):
                if nums[i]!=nums[j]:
                    i=i+1
                    nums[i]=nums[j]
        return i+1
#这题用set不能用，因为要求in location。python金手指不能开。如果没有set的要求。python可以两行内解决战斗。