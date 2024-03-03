def infinite_generator():
    cur_val = 0
    while True:
        yield cur_val
        cur_val += 1


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes():
    cur_val = 0
    while True:
        if is_prime(cur_val):
            yield cur_val
        cur_val += 1

        if cur_val > 10 ** 2:
            return


# my_gen = infinite_generator()
# for i_num in my_gen:
#     print(i_num, end=" ")

my_gen = primes()
for i_num in my_gen:
    print(i_num, end=" ")
