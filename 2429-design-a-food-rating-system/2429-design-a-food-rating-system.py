class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodToCuisine = {}
        self.foodToRating = {}
        self.cuisineToHeap = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.foodToCuisine[f] = c
            self.foodToRating[f] = r
            if c not in self.cuisineToHeap:
                self.cuisineToHeap[c] = []
            heapq.heappush(self.cuisineToHeap[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        self.foodToRating[food] = newRating
        cuisine = self.foodToCuisine[food]
        heapq.heappush(self.cuisineToHeap[cuisine], (-newRating, food))
        

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisineToHeap[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.foodToRating[food]:
                return food
            heapq.heappop(heap)
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)