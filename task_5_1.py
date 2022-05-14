# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово
# yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...

def gen_odd_num(n):
    for s in range(1, n, 2):
        yield s
        s += 1
a = gen_odd_num(15)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))