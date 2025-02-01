#used two pointer to find largest height comparison while computing the area to find the max
#Time Complexity: O(n) since every element is run once
#Space Complexity: O(1) since no other data structure is used
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            #through every iteration compute the area to see if its the nax
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)

            #move the pointer based on the shorter height
            if height[left] < height[right]:
                left+=1
            else:
                right-=1

        return max_area

if __name__ == "__main__":
    x = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(x))
