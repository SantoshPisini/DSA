class Solution_BruteForce:
    def kthGrammar(self, n: int, k: int) -> int:
        # 0->01, 1->10
        word = ["0"]
        for _ in range(n):
            t = []
            for c in word:
                if c == "0":
                    t.append("0")
                    t.append("1")
                else:
                    t.append("1")
                    t.append("0")
            word = t
        return word[k-1]  # type: ignore
    
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        

s = Solution()
print(s.kthGrammar(1, 1)) # 0
print(s.kthGrammar(2, 1)) # 0
print(s.kthGrammar(2, 2)) # 1