def s(key):
    return {
        'one':1,
        'two': 2,
        'three': 3,
        'four': 4,
    }.get(key, 'Not found')

print(s('one'))
print(s('five'))