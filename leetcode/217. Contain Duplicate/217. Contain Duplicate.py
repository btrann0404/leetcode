# Hashing method
# O(N) Time and Space Complexity
class Solution(object):
    def containsDuplicate(self, nums):
        #hashing of unique char that is went over
        unique_set = set()
        for n in nums:
            #if it is went over already return true
            if n in unique_set:
                return True
            unique_set.add(n)
        return False
