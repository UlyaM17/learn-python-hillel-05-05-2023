# 1. Fibonacci generator
def fibonacci_generator_function(n: int):
    # starting values 0 and 1
    a, b = 0, 1
    for i in range(n):
        yield a
        # every next number is the sum of 2 previous numbers
        a, b = b, a + b
        # number position in sequence
        print(f'sequence number {i+1}\n')


if __name__ == '__main__':
    generator = fibonacci_generator_function(n=100)
    for number in range(100):
        # get 100 first numbers in Fibonacci sequence
        # printing sequence in given range
        print(generator.__next__())
