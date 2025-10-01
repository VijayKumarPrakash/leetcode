class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {-i:-1 for i in range(capacity)}

    def get(self, key: int) -> int:
        try:
            # Fetch result by removing key from dictionary
            result = self.cache.pop(key)
            # Add it back to the dictionary
            # This ensures most recently accessed value is at the end
            self.cache[key] = result
        except KeyError:
            result = -1
        
        print(result)
        return result        

    def put(self, key: int, value: int) -> None:
        # put() is inevitable - it has to go through
        # Calling get() helps us make this key the "most recent"
        existing_value = self.get(key)

        if existing_value == -1:
            # Evict oldest item
            oldest_key = next(iter(self.cache.keys()))
            self.cache.pop(oldest_key)
            self.cache[key] = value
        else:
            # Override existing value
            self.cache[key] = value
        
        print(self.cache)


# Driver code
capacity = 2
obj = LRUCache(capacity)
print(obj.cache)
obj.put(1, 1)   # cache is {1=1}
obj.put(2, 2)   # cache is {1=1, 2=2}
obj.get(1)      # return 1
obj.put(3, 3)   # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
obj.get(2)      # returns -1 (not found)
obj.put(4, 4)   # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
obj.get(1)      # return -1 (not found)
obj.get(3)      # return 3
obj.get(4)      # return 4
