# Hashing method
class Solution(object):
    def containsDuplicate(self, nums):
        unique_set = set()
        for n in nums:
            if n in unique_set:
                return True
            unique_set.add(n)
        return False
