from typing import List


class Solution:
    def addPadding(self, s: str, n: int, lastBucket: bool):
        s = s[:len(s)-1]
        missing = n - len(s)
        spaces = s.count(' ')
        if spaces == 0 or lastBucket:
            return s + (' '*missing)
        if (missing < 1 or spaces < 1):
            return s
        s = s.replace(' ', ' '*(missing // spaces + 1))
        diff = missing % spaces
        i = 0
        while (diff > 0):
            while i < len(s) - 1:
                if s[i] == ' ':
                    s = s[: i] + '  ' + s[i + 1:]
                    while s[i] == ' ':
                        i += 1
                    break
                i += 1
            diff -= 1
        print(s, len(s))
        return s

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        temps = ''
        result = []
        for i in range(len(words)):
            if len(temps + words[i]) > maxWidth:
                result.append(self.addPadding(temps, maxWidth, False))
                temps = (words[i] + ' ')
            else:
                temps += (words[i] + ' ')
        result.append(self.addPadding(temps, maxWidth, True))
        return result


s = Solution()
print(s.fullJustify(
    ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))
print([
    "Science  is  what we",
    "understand      well",
    "enough to explain to",
    "a  computer.  Art is",
    "everything  else  we",
    "do                  "
]
)
