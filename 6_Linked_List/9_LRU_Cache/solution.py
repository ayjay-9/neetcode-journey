class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.rank = 0 # Track the age

    def get(self, key: int) -> int:
        if key in self.map:
            # Increase the rank to be the highest rank
            max_rank = max(self.map.items(), key=lambda item: item[1][0])[1][0]
            self.map[key][0] = max_rank+1 # Update the rank
            self.rank = max_rank+2
            return self.map[key][1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # 1. Update the key's value if it exists
        # 2. Add new key-value
        # 3. Remove the last used key
        # put() can only do either of the three

        if key in self.map or len(self.map) < self.capacity:
            self.map[key] = [self.rank, value]
            self.rank += 1
        else: # Remove the key with the lowest rank -> sort[0][0]
            min_rank_key = min(self.map.items(), key=lambda item: item[1][0])[0]
            del self.map[min_rank_key]
            self.map[key] = [self.rank, value]
            self.rank += 1

if __name__ == "__main__":
    lru_cache = LRUCache(3)
    lru_cache.put(1,1)
    lru_cache.put(2,2)
    lru_cache.put(3,3)
    print(lru_cache.get(1))
    print(lru_cache.get(2))
    print(lru_cache.get(4))

    lru_cache.put(4,4)
    print(lru_cache.get(1))
    print(lru_cache.get(2))
    print(lru_cache.get(3))
    print(lru_cache.get(4))
    print(lru_cache.get(2))

    lru_cache.put(1,8)
    lru_cache.put(3, 7)
    print(lru_cache.get(1))
    print(lru_cache.get(2))
    print(lru_cache.get(3))
    print(lru_cache.get(4))
    print(lru_cache.get(5))
    print(lru_cache.get(2))
    print(lru_cache.get(3))
    print(lru_cache.get(4))

    lru_cache.put(1,9)
    lru_cache.put(6, 6)
    print(lru_cache.get(1))
    print(lru_cache.get(2))
    print(lru_cache.get(3))
    print(lru_cache.get(4))
    print(lru_cache.get(5))
    print(lru_cache.get(6))
