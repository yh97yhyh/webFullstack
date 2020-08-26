# 파일 입출력


file = open('sample.txt', 'r')
'''
file.write('hello world')
file.write('\n')
file.write('hello world')
'''

# print(dir(file))
print(file.readlines())
print(file.read())

file.close()