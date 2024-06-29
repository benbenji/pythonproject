class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num

# 创建迭代器对象
counter = CountDown(3)
print(next(counter))
# 使用迭代器
for num in counter:
    print(num)