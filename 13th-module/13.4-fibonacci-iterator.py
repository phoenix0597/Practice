class Fibonacci:
    """ Итератор последовательности Фибоначчи из n элементов """
    
    def __init__(self, number):
        self.counter = 0
        self.cur_val = 0
        self.next_val = 1
        self.number = number
    
    def __iter__(self):
        self.counter = 0
        self.cur_val = 0
        self.next_val = 1
        return self
    
    def __next__(self):
        if self.counter < self.number:
            self.cur_val, self.next_val = self.next_val, self.cur_val + self.next_val
            self.counter += 1
            return self.cur_val
        else:
            raise StopIteration


fib_iterator = Fibonacci(10)
for i_num in fib_iterator:
    print(i_num)
print(8 in fib_iterator)
