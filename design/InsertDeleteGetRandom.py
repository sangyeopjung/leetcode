# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
# tags: design, hashmap, random

class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        
        self.map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        
        self.map[self.list[-1]] = self.map[val]
        self.list[self.map[val]] = self.list[-1]
        self.list.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        i = random.randint(0, len(self.list)-1)
        return self.list[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()