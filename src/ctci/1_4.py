'''
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words.
'''

class Solution():
    def palindromePermutation(self, s: str) -> bool:
        _set = set()
        for c in s:
            if c == ' ':
                continue
            if c in _set:
                _set.remove(c)
            else:
                _set.add(c)
        return len(_set) < 2


s = Solution()
print("test search", "->", s.palindromePermutation("test search"))
print("tact coa", "->", s.palindromePermutation("tact coa"))
