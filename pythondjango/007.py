# 변수의 타입

a = 10 #int
b = 10.1 #float
c = 'younghyun' #str
d = True #bool
e = [100, 200, 300] #list
f = (100, 200, 300) #tuple
g = {'one':1, 'two':2} #dict
h = {100, 200, 300, 400} #set

print(type(a), type(b), type(c), type(d), type(e))
print(type(f), type(g), type(h))
print(c.isalpha())

'''
1. 공간활용
2. 용도에 맞게 사용, 유용한 기능 사용
3. 변수와 값은 모두 존재함
'''

print(dir(c))