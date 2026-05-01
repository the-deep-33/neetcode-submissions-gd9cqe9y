class TimeMap:

    def __init__(self):
        self.lookup = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.lookup:
            self.lookup[key] = []
        self.lookup[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:

        if self.lookup.get(key, None) is None:
            return ""
            
        i = 0
        j = len(self.lookup[key]) - 1

        while i <= j:
            print(f"i = {i}")
            print(f"j = {j}")
            mid = (i + j) // 2
            value = self.lookup[key][mid][0]

            if value == timestamp:
                return self.lookup[key][mid][1]

            elif value < timestamp:
                try:
                    if value < timestamp and self.lookup[key][mid+1][0] > timestamp:
                        return self.lookup[key][mid][1]
                except:
                    return self.lookup[key][mid][1]

                i = mid + 1
            
            else:
                if i == j == 0 and value > timestamp:
                    return ""
                j = mid

        
