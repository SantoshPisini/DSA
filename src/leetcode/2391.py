from typing import List


class Solution:
    def garbageCollection_Better(self, garbage: List[str], travel: List[int]) -> int:
        result = sum(len(g) for g in garbage)
        G = P = M = False
        for i in range(len(travel), 0, -1):
            G |= 'G' in garbage[i]
            P |= 'P' in garbage[i]
            M |= 'M' in garbage[i]
            result += travel[i-1] * (G + P + M)
        return result

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        g_time = p_time = m_time = 0
        g_pos = p_pos = m_pos = 0
        for _gi in range(len(garbage)):
            for _i in range(len(garbage[_gi])):
                if garbage[_gi][_i] == "G":
                    if g_pos != _gi:
                        g_time += sum(travel[g_pos: _gi])
                        g_pos = _gi
                    g_time += 1
                if garbage[_gi][_i] == "P":
                    if p_pos != _gi:
                        p_time += sum(travel[p_pos: _gi])
                        p_pos = _gi
                    p_time += 1
                if garbage[_gi][_i] == "M":
                    if m_pos != _gi:
                        m_time += sum(travel[m_pos: _gi])
                        m_pos = _gi
                    m_time += 1
        # print("g_time", g_time)
        # print("p_time", p_time)
        # print("m_time", m_time)
        return g_time + p_time + m_time


s = Solution()
print(s.garbageCollection(["G", "P", "GP", "GG"], [2, 4, 3]))
print(s.garbageCollection(["MMM", "PGM", "GP"], [3, 10]))
