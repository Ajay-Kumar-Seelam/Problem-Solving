
class RandomizedSet:

    def __init__(self):
        self.items={}

    def insert(self, val: int) -> bool:
        if self.items.get(val):
            return False
        self.items[val]=True
        return True

    def remove(self, val: int) -> bool:
        if self.items.get(val):
            self.items.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.items.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()