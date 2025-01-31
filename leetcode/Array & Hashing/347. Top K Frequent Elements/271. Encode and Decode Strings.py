#Prefix based encoding using length and "#" as the unique val and key
#O(n) Time and Space Complexity because it only runs through a linear search and insert in n complexity
class Solution:

    def encode(self, strs: list[str]) -> str:
        if not strs:
            return ""

        key = "#"
        res_word = ""

        #encode by having the num as length and "#" as delimiter
        #combing the two will make sure for unqiue and correct spltting
        for word in strs:
            wordToAdd = f"{len(word)}{key}{word}"
            res_word+=wordToAdd

        return res_word

    def decode(self, s: str) -> list[str]:
        if not s:
            return []

        # i stand for starting index added and j stand for ending index added
        res_lst = []
        i = 0
        while i != len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            # j + 1: string after "#"
            res_lst.append(s[j + 1:j + length + 1])
            i = j + length + 1

        return res_lst




if __name__ == "__main__":
    test = Solution()
    val = ["neet","code","love","you"]
    x = test.encode(val)
    y = test.decode(x)
    print(x)
    print(y)
