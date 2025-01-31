#Using heap to keep order of values (auto approach)
#Time Complexity is O(n * nlogn) and Space Complexity is O(n)
import collections
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        #creates (num: freq) counter for all values
        counter = collections.Counter(nums)
        #swap to make into heap from (freq: num)
        heap = [(v,k) for (k,v) in counter.items()]
        #turn data structure to a valid heap data structure
        heapq.heapify(heap)
        #pop until there is only last values are left (max freq we are looking for)
        while len(heap) > k:
            heapq.heappop(heap)
        #return only the num the structure without the freq
        return [num for (freq, num) in heap]

    #Samething but more manual approach...
    def topKFrequent2(self, nums: list[int], k: int) -> list[int]:
        return_lst = []
        hashmap = {} #(num: count)
        freq_lst = [[] for i in range(len(nums) + 1)] #(freq: list of num)

        #hashmap for sort (num: freq)
        for n in nums:
            hashmap[n] = hashmap.get(n,0) + 1

        #bucket sort w list of list: indexes representing freq and num in each bucket that coorelates
        for n, c in hashmap.items():
            freq_lst[c].append(n)

        #go through bucket sort list backwards (for max)
        for i in range(len(freq_lst) - 1, 0, -1):
            for n in freq_lst[i]:
                return_lst.append(n)
                if len(return_lst) == k:
                    return return_lst

        return return_lst






if __name__ == "__main__":
    lst = [1,1,1,2,2,3]
    k = 2
    test = Solution().topKFrequent(lst, k)
    test2 = Solution().topKFrequent2(lst, k)
    print(test)
    print(test2)
