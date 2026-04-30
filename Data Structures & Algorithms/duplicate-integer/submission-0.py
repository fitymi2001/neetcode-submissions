class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = set()
        for i in nums:
            if i not in num:
                num.add(i)
            else:
                return True
        return False