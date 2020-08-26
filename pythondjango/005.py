# 문자열포매팅

name = 'younghyun'
age = 15
n = 888888888888888.8888
# print('제 이름은 %s입니다. 제 나이는 %d입니다.' %(name,age))
print('제 이름은 {}입니다. 제 나이는 {}입니다.'.format(name, age))
print('제 이름은 {0}입니다. 제 나이는 {0}입니다.'.format(name, age)) #몇번째값
s = '제 이름은 {name}입니다. 제 나이는 {age}입니다.'
print(s.format(name='younghyun', age=15))
print('{0:4} X {1:4} = {2:4}'.format(2, 3, 6)) #네 칸
print('{0:<4} X {1:<4} = {2:<4}'.format(2, 3, 6)) #왼쪽정렬
print('{0:.3f}'.format(1/4.0))
print('{0:,.3f}'.format(n))