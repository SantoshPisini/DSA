import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        times_used = [0] * n
        q = [x for x in range(n)]
        heapq.heapify(q)
        current_meetings = []
        for i in range(len(meetings)):
            start, end = meetings[i]
            while current_meetings and current_meetings[0][0] <= start:
                end_time, room = heapq.heappop(current_meetings)
                heapq.heappush(q, room)
            if q:
                unused_room = heapq.heappop(q)
                times_used[unused_room] += 1
                heapq.heappush(current_meetings, (end, unused_room))
            else:
                end_time, room = heapq.heappop(current_meetings)
                times_used[room] += 1
                heapq.heappush(current_meetings,
                               (end_time + end - start, room))
        return times_used.index(max(times_used))


s = Solution()
print(s.mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]))
