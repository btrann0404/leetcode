#Solution 1 & 2: Using sliding window to shift left pointer up until there is valid substring for every case and calculate
#Solution 1 Complexity: Time -> O(n) because every value is ran once, Space -> because of the set worst case it would O(n)
#Solution 2 Complexity: Time -> O(n^2) because of slicing and loop together, Space -> O(n) because of implict slicing worst case
class Solution:
    #alternative solution
    def lengthOfLongestSubstring(self, s: str) -> int:
        #intialize set of unique subset
        charSet = set()
        l = 0
        res = 0

        # have the right keep iterating
        for r in range(len(s)):
            # if there is a value that is not unique, keep removing elements from the beginning
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            #then update the new element for new substring
            charSet.add(s[r])
            # recalculate max value
            res = max(res, r - l + 1)
        return res

    # my first solution
    def lengthOfLongestSubstring2(self, s: str) -> int:
        # have a 2 pointer one ahead of the other
        left, right = 0, 1
        max_length = 0

        # if only contains one return 1
        if len(s) == 1:
            max_length = 1

        # go through until right pointer reaches end
        while right < len(s):
            # if it not in the substring update the right pointer and recalculate max value
            if s[right] not in s[left:right]:
                right+=1
                length = len(s[left:right])
                max_length = max(length, max_length)
            # if it is in the substring move the left pointer up one
            else:
                left += 1

        return max_length

if __name__ == "__main__":
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))
    print(Solution().lengthOfLongestSubstring2(s))
