'''
One Away: There are three types of edits that can be performed on strings: insert a character, 
remove a character, or replace a character. Given two strings, write a function to check if 
they are one edit (or zero edits) away.
'''

from collections import defaultdict


class Solution():
    def oneAway(self, u: str, v: str) -> bool:
        if abs(len(u) - len(v)) > 1:
            return False
        _map = defaultdict(int)
        for c in u:
            _map[c] += 1
        for c in v:
            _map[c] -= 1
        u_more, v_more = True, True
        for k in _map:
            if _map[k] == 0:
                continue
            if _map[k] == 1:
                if u_more:
                    u_more = False
                else:
                    return False
            if _map[k] == -1:
                if v_more:
                    v_more = False
                else:
                    return False
        return (u_more or v_more) or (not u_more and not v_more)


s = Solution()
print("pale pale =>", s.oneAway("pale", "pale"))
print("pale ple =>", s.oneAway("pale", "pal"))
print("pal pale =>", s.oneAway("pal", "pale"))
print("plad pale =>", s.oneAway("plad", "pale"))
print("plad able =>", s.oneAway("plad", "able"))
