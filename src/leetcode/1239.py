from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for a in arr:
            if len(a) > len(set(a)):
                continue
            a = set(a)
            for aa in dp:
                if a & aa:
                    continue
                dp.append(a | aa)
        return max(len(a) for a in dp)




s = Solution()
print(s.maxLength(["un", "iq", "ue"]))
# print(s.maxLength(["ab", "ba","cd","dc","ef","fe","gh","hg","ij","ji","kl","lk","mn","nm","op","po"]))