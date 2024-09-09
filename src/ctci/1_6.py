'''
String Compression: Implement a method to perform basic string compression using the counts of repeated characters. 
For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller 
than the original string, your method should return the original string. You can assume the string has only uppercase 
and lowercase letters (a - z).
'''
class Solution:
    def compression(self, s: str) -> str:
        result = []
        prev_index = i = 0
        result.append(s[0])
        for i in range(1, len(s)):
            if s[i] != s[prev_index]:
                result.append(str(i - prev_index))
                result.append(s[i])
                prev_index = i
        result.append(str(i - prev_index + 1))
        result = ''.join(result)
        return s if len(s) < len(result) else result


s = Solution()
print(s.compression("abcdef"))
print(s.compression("aabcccccaaa"))
print(s.compression("aabccccca"))
