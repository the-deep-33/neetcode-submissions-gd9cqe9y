from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.order = OrderedDict()

    def get(self, key: int) -> int:
        value = self.order.get(key, -1)
        if value != -1:
            self.order.move_to_end(key, last=True)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.order:
            self.order[key] = value
            self.order.move_to_end(key, last=True)
            return
        
        if len(self.order) == self.capacity:
            self.order.popitem(last=False)
            
        self.order[key] = value
