#used sliding window and shifting it to find the smaller substring with the neccesary requirements
#Time Complexity: O(n) because every element is gone over once
#Space Complexity: O(n) because the hashmap could contain n amount of chars depending on s and t
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #default base case
        if t == "":
            return ""

        #countT: freq of needed num of char
        #window: freq of num of char in the window currently
        countT, window = {}, {}

        #intialize the count and variables
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0

        # keep moving the right pointer
        for r in range(len(s)):
            #update window counter
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            #if its a character we care about and they have the same freq we want update have countT
            if c in countT and window[c] == countT[c]:
                have += 1

            #when the substring meets the neccsary need then...
            while have == need:
                #length is of substring is smaller then update
                if (r - l + 1) < resLen:
                    res = l, r
                    resLen = (r - l + 1)

                #update left pointer to the left once and update map
                # and before we update the pointer check if its a character we need
                # if we do decrement from the have counter
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if res != float("inf") else ""


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))
