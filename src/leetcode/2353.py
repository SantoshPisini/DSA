from collections import defaultdict
import heapq
from typing import List


class FoodRatings_BAD:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine_dict = defaultdict(list)
        self.food_dict = defaultdict(str)
        self.cuisine_max = defaultdict(list)
        for i in range(len(foods)):
            self.food_dict[foods[i]] = cuisines[i]
            if cuisines[i] in self.cuisine_dict:
                self.cuisine_dict[cuisines[i]].append([foods[i], ratings[i]])
                if self.cuisine_max[cuisines[i]][1] < ratings[i]:
                    self.cuisine_max[cuisines[i]] = [foods[i], ratings[i]]
                elif self.cuisine_max[cuisines[i]][1] == ratings[i]:
                    if self.cuisine_max[cuisines[i]][0] < foods[i]:
                        self.cuisine_max[cuisines[i]] = [foods[i], ratings[i]]
            else:
                self.cuisine_max[cuisines[i]] = [foods[i], ratings[i]]
                self.cuisine_dict[cuisines[i]] = [[foods[i], ratings[i]]]
        print(self.cuisine_max)

    def changeRating(self, food: str, newRating: int) -> None:
        _max = ["_PLACEHOLDER_", 0]
        for item in self.cuisine_dict[self.food_dict[food]]:
            if item[0] == food:
                item[1] = newRating
            if item[1] > _max[1]:
                _max = item
            elif item[1] == _max[1]:
                if _max[0] > item[0]:
                    _max = item
        self.cuisine_max[self.food_dict[food]] = _max

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_max[cuisine][0]


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.mp = {}
        self.data = defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.mp[food] = (cuisine, rating)
            heapq.heappush(self.data[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.mp[food]
        self.mp[food] = cuisine, newRating
        heapq.heappush(self.data[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.data[cuisine] and -self.data[cuisine][0][0] != self.mp[self.data[cuisine][0][1]][1]:
            heapq.heappop(self.data[cuisine])
        return self.data[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
f = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], [
                "korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7])
print(f.highestRated("korean"))
print(f.highestRated("japanese"))
f.changeRating("sushi", 16)
print(f.highestRated("japanese"))
f.changeRating("ramen", 16)
print(f.highestRated("japanese"))
