class Clock:
    def __init__(self):
        self.iter = 0

    def tick(self):
        self.iter += 1

    def time(self):
        return self.iter

