class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = {}
        for n in nums:
            if n not in store:
                store[n]=1
            else:
                return True
        return False
        