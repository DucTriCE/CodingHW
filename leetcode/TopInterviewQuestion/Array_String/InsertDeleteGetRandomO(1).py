class RandomizedSet:

    def __init__(self):
        self.mp = {}
    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False
        else:
            self.mp[val]=val
            return True
    def remove(self, val: int) -> bool:
        if val in self.mp:
            self.mp.pop(val)
            return True
        else:
            return False
    def getRandom(self) -> int:
        return random.choice(list(self.mp.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()