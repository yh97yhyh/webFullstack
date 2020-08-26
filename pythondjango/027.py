a = 13
print(bin(a))
print(oct(a))
print(hex(a))
print(type(bin(a)))
print(type(oct(a)))
print(type(hex(a)))
x = 0b1101
y = 0o15
z = 0xd
print(type(x), y, z)
print(bin(a)[2:].replace('1', '#').replace('0', '!'))