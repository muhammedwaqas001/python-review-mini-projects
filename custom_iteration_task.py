class CountDown:
    def __init__(self, start):
        self.number = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.number > 0:
            current_number = self.number
            self.number -= 1
            return current_number

        raise StopIteration

countdown = CountDown(5)

for count in countdown:
    print(count)
