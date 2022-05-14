# 2. *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя
# ключевое слово yield.

n = 15
a = (s + 1 for s in range(0, n, 2))

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))