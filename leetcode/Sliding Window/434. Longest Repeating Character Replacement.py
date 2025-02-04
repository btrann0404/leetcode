# Using sliding window and hashmap to calculate the all substring's length considering the highest frequency char
# Time Complexity: O(n) all elements are ran once
# Space Comexplity: O(26) because the hashmap could be at most 26 long (alphabet)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #account for char: freq
        count = {}
        res = 0

        #left pointer from the start with moving right
        left = 0
        for right in range(len(s)):
            #for every value update the freq to hashmap
            count[s[right]] = 1 + count.get(s[right], 0)

            # if current valid length - highest freq char > k (substring isn't valid)
            # then move pointer and left and decrement from the hashmap
            # aka make the window smaller
            while right - left + 1 - max(count.values()) > k:
                count[s[left]] -= 1
                left+=1

            #recalculate the max for every window
            res = max(res, right - left + 1)

        return res

if __name__ == "__main__":
    s = "ABABBA"
    k = 2
    print(Solution().characterReplacement(s, k))
