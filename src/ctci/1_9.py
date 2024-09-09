'''
String Rotation:Assume you have a method isSubstring which checks if one word is a substring of another. 
Given two strings, sl and s2, write code to check if s2 is a rotation of s1 using only one call to 
isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").
'''


class Solution:
    def isSubstring(self, u: str, v: str) -> bool:
        repeated_u = u * 2
        return v in repeated_u


s = Solution()
print("waterbottle erbottlewat ->", s.isSubstring("waterbottle", "erbottlewat"))
