#used loop in to increment for the 1st value and used "two pointer" in order to find the last the 2 value for threeSum
#Time Complexity: O(n^2) since sorting array take O(nlogn) and two pointer takes O(n^2)
#Space Complexity: O(n^2) since the return array is 2d array and the largest if could be is O(n^2)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        #num being a in a+b+c = threeSum
        for i, num in enumerate(nums):
            #skip the first element and make sure if theres multiple of the same element go to the last one
            if i > 0 and num == nums[i-1]:
                continue

            #intialize pointer to element after "a" being "b" and last element being "c"
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                #sum is too large so decrement right pointer down
                if threeSum > 0:
                    right-=1
                #sum is too small so increament left pointer up
                elif threeSum < 0:
                    left+=1
                #if sum is found increment "a" to search for more threeSums
                elif threeSum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    #update left pointer and make sure its the last common element
                    # also while making sure left and right pointer dont overlap
                    left+=1
                    while nums[left - 1] == nums[left] and left < right:
                        left+=1

        return res

if __name__ == "__main__":
    x1 = [-1,0,1,2,-1,-4]
    x2 = [0,0,0,0]
    print(Solution().threeSum(x1))
    print(Solution().threeSum(x2))
