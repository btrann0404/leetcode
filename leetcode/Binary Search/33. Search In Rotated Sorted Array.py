#using binary search to find the lowest number and shift depending whether to move to left or right boundary
#Time Complexity: O(logn) binary search is always logn
#Space Complexity: O(1) not data structures used
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            #check if the midpoint is the target we're looking for'
            if nums[mid] == target:
                return mid

            #if the right side is sorted based on midpoint...
            if nums[mid] <= nums[right]:
                #if target exist within subset check right boundary by shifting left pointer to left
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                #if not do the opposite
                else:
                    right = mid - 1
            #if the left side is sorted based on midpoint...
            if nums[mid] >= nums[left]:
                #if target exist within subset check left boundary by shifting right pointer to right
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                #if not do the opposite
                else:
                    left = mid + 1

        return -1

if __name__ == "__main__":
    lst, target= [4,5,6,7,0,1,2], 1
    print(Solution().search(lst, target))
