class RandomizedSet:

    def __init__(self):
        self.elems = []
        self.indexes = {}
        
    def insert(self, val: int) -> bool:
        
        if val in self.indexes:
            return False
        self.indexes[val] = len(self.elems)
        self.elems.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.indexes:
            return False

        val_index = self.indexes[val]
        last = self.elems[-1]
        if val_index < len(self.elems)-1:  
            self.elems[val_index] = last
            self.indexes[last] = val_index
        self.elems.pop()
        del self.indexes[val]
        return True    

    def getRandom(self) -> int:
        return random.choice(self.elems)
        