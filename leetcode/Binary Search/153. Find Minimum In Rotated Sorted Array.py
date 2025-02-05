#using binary search to find the lowest number and shift depending whether to move to left or right boundary
#Time Complexity: O(logn) binary search is always logn
#Space Complexity: O(1) not data structures used

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

if __name__ == "__main__":
    lst = [2,3,1]
    print(Solution().findMin(lst))
