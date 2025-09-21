

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.price = {}
        self.available = defaultdict(list)
        self.rented = []
        self.rented_set = set()
        
        for shop, movie, price in entries:
            self.price[(shop, movie)] = price
            heapq.heappush(self.available[movie], (price, shop))
    
    def search(self, movie: int) -> List[int]:
        res = []
        temp = []
        seen = set()
        while self.available[movie] and len(res) < 5:
            price, shop = heapq.heappop(self.available[movie])
            if (shop, movie) not in self.rented_set and (shop, movie) not in seen:
                res.append(shop)
                seen.add((shop, movie))
            temp.append((price, shop))
        for item in temp:
            heapq.heappush(self.available[movie], item)
        return res
    
    def rent(self, shop: int, movie: int) -> None:
        self.rented_set.add((shop, movie))
        heapq.heappush(self.rented, (self.price[(shop, movie)], shop, movie))
    
    def drop(self, shop: int, movie: int) -> None:
        self.rented_set.remove((shop, movie))
    
    def report(self) -> List[List[int]]:
        res = []
        temp = []
        seen = set()
        while self.rented and len(res) < 5:
            price, shop, movie = heapq.heappop(self.rented)
            if (shop, movie) in self.rented_set and (shop, movie) not in seen:
                res.append([shop, movie])
                seen.add((shop, movie))
            temp.append((price, shop, movie))
        for item in temp:
            heapq.heappush(self.rented, item)
        return res

        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()