#Using hashing to help sort
#Time complexity is O(n * klogk) and Space complexity is O(n*k)
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #hashmap to have the unique_pattern as the key and index as the key
        hashmap = {}
        #list of list to return group of anagrams
        return_lst = []
        for word in strs:
            #sort the word to a unique, alpbetically sorted string
            word_pat = "".join(sorted(list(word)))
            #if exist find index and add to return_lst
            if word_pat in hashmap:
                index = hashmap[word_pat]
                return_lst[index].append(word)
            #if not hash the new pattern/index and create a new list in the return_lst
            else:
                hashmap[word_pat] = len(return_lst)
                return_lst.append([word])
        return return_lst
