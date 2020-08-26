# Python Built-in Function - max, min, sum

x = [100, 200, 300, 400]
print(max(x))
print(min(x))
print(sum(x))
print('=============')
a = [1, 2, 3]
b = 'DEF'
c = 'GHI'
print(list(zip(a, b)))
print(list(zip(a, b, c)))
for i in zip(a, b):
    print(i)

def younghyun(x):
    return x ** 2
print(list(map(younghyun, [1, 2, 3])))
print(list(map(lambda x : x ** 2, [1, 2, 3])))