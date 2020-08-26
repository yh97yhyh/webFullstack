name = 'younghyun'
age = 15

print('{0:^15}'.format(name)) #15자리에 맞춰 중앙정렬
print('{0:<15}'.format(name)) #15자리에 맞춰 왼쪽정렬
print('{0:>15}'.format(name)) #15자리에 맞춰 오른쪽정렬
print('{0:#^15}'.format(name))
print('{0:0<15}'.format(name))
print('{0:!>15}'.format(name))

print(f'제 이름은 {name}입니다. 제 나이는{age}입니다.')