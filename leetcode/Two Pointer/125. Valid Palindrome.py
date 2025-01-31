#Used a two pointer to compare the first and last element
#Space complexity is O(1) because there was no extra data structure
#Time complexity is O(N) becausee it checks searches through the element N times
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_index = 0
        right_index = len(s) - 1

        while (left_index < right_index):
            left_val = s[left_index].lower()
            right_val = s[right_index].lower()

            if not left_val.isalnum():
                left_index+=1
                continue

            if not right_val.isalnum():
                right_index-=1
                continue

            if left_val != right_val:
                return False

            if left_val == right_val:
                left_index+=1
                right_index-=1

        return True

if __name__ == "__main__":
    s = "!bHvX!?!!vHbX"
    test = Solution().isPalindrome(s)
    print(test)
