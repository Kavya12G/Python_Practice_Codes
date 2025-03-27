class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        return word[0:index+1][::-1] + word[index+1:]
sol = Solution()
word = input()
ch = input()
res = sol.reversePrefix(word, ch)
print(res)