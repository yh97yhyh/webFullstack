# 함수

# def plus(x, y):
#     z = x + y
#     return z
# print(plus(3, 7))

# def printNum():
#     print('one')
#     print('two')
#     print('three')
# printNum()

# def empty():
#     pass
# empty()

# def f(n):
#     if n > 1:
#         return n * f(n-1)
#     else:
#         return 1
# print(f(5))

# 함수의 클로저
# def f():
#     x = 10
#     def xPlus():
#         nonlocal x
#         x += 10
#         return x
#     return xPlus()
# f1 = f()
# f2 = f()
# print(f1())
# print(f1())
# print(f1())