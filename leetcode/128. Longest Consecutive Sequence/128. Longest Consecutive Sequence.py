#first solution and second solution:
#used set to identify unqiue nums and identfied to values that could start a sequence to count
#time and space time complexity is O(N) since it goes through the number n amount of TimeoutError
class Solution:
    # my second more simple solution
    def longestConsecutive(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        longest = 0

        for n in unique_nums:
            # look for a starting number
            if n - 1 not in unique_nums:
                #start the count with loop to see if it the new longest consecutive num ref the first num
                length = 0
                while n + length in unique_nums:
                    length += 1
                longest = max(length, longest)

        return longest

    #my first solution
    def longestConsecutive2(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        sorted_nums = sorted(nums)
        max = 1

        count = 1
        for i in range(1, len(sorted_nums)):
            #if the number is the same continue the loop with no change
            if sorted_nums[i - 1] == sorted_nums[i]:
                continue

            #if the next sorted num is the num we are looking for add to the count
            if sorted_nums[i - 1] == sorted_nums[i] - 1:
                count+=1
                # replace max if the count is bigger
                if count > max:
                    max = count
            else:
                count = 1

        return max


if __name__ == "__main__":
    x = [100,4,200,1,3,2]
    print(Solution().longestConsecutive(x))
    print(Solution().longestConsecutive2(x))
