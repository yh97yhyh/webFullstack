# Python Built-in Function - 그 외 내장함수

name = ['a', 'b', 'c']
for i in enumerate(name, 100): # 순서 매길 때
    print(i)

x = [(1, 2, (1, 20)), (3, 4, (30, 40)), (5, 6, (50, 60))]
for i, j, (k, z) in x:
    print(i, j, k, z)