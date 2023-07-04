class MyHash:
    def __init__(self, b):
        self.BUCKET = b
        self.table = [[] for x in range(b)]
    
    def insert(self, x):
        i = x % self.BUCKET
        self.table[i].append(x)

    def search(self, x):
        i = x % self.BUCKET
        return x in self.table[i]

    def delete(self, x):
        i = x % self.BUCKET
        if x in self.table[i]:
            self.table[i].remove(x)

    def view(self):
        print(self.table)

h = MyHash(7)
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)
print(h.search(70))
h.view()
h.delete(56)
h.view()