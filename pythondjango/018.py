# 참조 불변

x = [100, 200, 300]
t = (x, 200, 300, 400)
print(t)
x[0] = 1000
print(t)