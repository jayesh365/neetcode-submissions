class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # iterate list, if not seen before add to dupes
        # if seen in list then return true
        dupes = []
        for i in nums:
            if i not in dupes: dupes.append(i)
            elif i in dupes: return True
        return False
        