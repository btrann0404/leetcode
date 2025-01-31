# Hashing method
# O(N) Time and Space Complexity
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #keep track of the integer and index it was not part of the sum
        hashmap = {}
        for i, n in enumerate(nums):
            element = target - n
            #if the element we are searching for has gone over before return
            if element in hashmap:
                return [hashmap[element], i]
            hashmap[n] = i
        return []
