d = {'one':1, 'two':2, 'three':3}
print(type(d))
print(dir(d))

jeju = {'banana':4000}
seoul = jeju.copy()
jeju['banana'] = 6000
print(jeju)
print(seoul)
print(id(seoul))
print(id(jeju))

print(d.items())
print(d.keys())
print(d.values())

print(d.pop('one'))
print(d)
print(d.update({'five':5}))
print(d)