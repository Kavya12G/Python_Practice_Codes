class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
    def __next__(self):
        if self.count < self.limit:
            self.count = self.count+1
            return self.count

c = Counter(5)
print(c.__next__())