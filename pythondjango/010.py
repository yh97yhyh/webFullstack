# 반복문

# x = 1
# while x < 10:
#     print(x)
#     x += 1

# x = 1
# while x < 10:
#     print(x)
#     x += 1
#     y = 1
#     while y < 10:
#         print(y, end=' ')
#         y += 1

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in x:
#     print(i)
# print(10 in x)

# for i in 'younghyun':
#     print(i)

# for i in x:
#     for j in y:
#         print('{} X {} = {}'.format(i, j, i*j))


# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # range(start:stop:step)
# print(list(range(10)))
# print(list(range(1, 10, 1)))
# print(list(range(0, 10, 2)))
# print(list(range(1, 10, 2)))
# print(list(range(5, -5, -1)))
# print(list(range(10, 20)))
# '''
# 1. 많은 데이터를 준비하지 않아도 된다.
# 2. 필요한 시점에만 데이터 사용
# '''
# x = iter(range(10))
# print(next(x))
# print(next(x))
# print(next(x))

# result = 0
# for i in range(101):
#     result += i
# print(result)

# x = 1
# while x < 10:
#     if x == 5:
#         break
#     print('good job')
#     x += 1
# print('end')

# for i in range(10):
#     if i == 5:
#         break
#     print('good job')
# print('for end')

# for i in range(101):
#     if i % 2 == 0:
#         continue
#     print(i)

# Ctrl+c 눌러야 무한루프 탈출
x = 0
while True:
    txt = input('제곱할 숫자를 입력하세요: ')
    if txt == 'exit':
        break
    try:
        int(txt)
    except:
        print('숫자를 입력해주세요!')
    else:
        print(int(txt) ** 2)
