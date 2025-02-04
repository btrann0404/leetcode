#Used postfix and prefix method to figure out left and right product of each element
#O(n) Time Complexity because it goes through the list linear search
#O(1) Space complexity because the only data structure involved is the output list
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        #create the return array
        res = [1] * len(nums)

        #have the prefix value of every element
        prefix = 1
        for i in range(0, len(nums)):
            res[i] = prefix #update val
            prefix *= nums[i] #update the new prefix

        #now that res contains every prefix element
        #calc the postfix of the same position and multiply
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix #update val
            postfix *= nums[i] #update the new postfix

        return res

if __name__ == "__main__":
    x = [1,2,3,4]
    test = Solution().productExceptSelf(x)
    print(test)
