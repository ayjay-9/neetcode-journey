from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        self.map.move_to_end(key)
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        # 1. Update the key's value if it exists
        # 2. Add new key-value
        # 3. Remove the last used key
        # put() can only do either of the three

        if key in self.map:
            self.map[key] = value
            self.map.move_to_end(key)
            return

        if len(self.map) == self.capacity:
            self.map.popitem(last=False)

        self.map[key] = value

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
