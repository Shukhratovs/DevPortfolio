def add(*args):
    sum_numbers = 0
    for n in args:
        sum_numbers += n
    return sum_numbers


print(add(250, 2, 45, 3, 5))
