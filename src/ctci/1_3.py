'''
URLify: Write a method to replace all spaces in a string with '%20'. 
You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string.
'''


class Solution():
    def urlIfy(self, s: str) -> str:
        return s.replace(' ', '%20')


s = Solution()
print("test search", "->", s.urlIfy("test search"))
