class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = []
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.window) == self.size:
            prev = self.window.pop(0)
            self.total -= prev
        
        self.window.append(val)
        self.total += val
        return self.total / len(self.window)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)