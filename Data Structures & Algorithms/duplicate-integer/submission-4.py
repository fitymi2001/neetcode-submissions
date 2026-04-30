class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True # 중복 발견 즉시 함수 종료!
            seen.add(num)
        return False