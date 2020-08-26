# 리스트 메서드

l = [100, 200, 300, 400]
print(type(l))
print(dir(l))
l.append(500)
print(l)
l.append(500)
print(l)
print(l.count(500)) # 500의 갯수
l.extend([100, 200, 10, 20]) # 확장
print(l)
print(l.index(200)) # 첫번째 만나는 값의 index만 출력
l.insert(3, 10000)
print(l)
l.pop() # 마지막에 있는 것 삭제
print(l)
l.pop(2) # index값
print(l)
l.remove(200) #값 (처음 만나는 200만 삭제)
print(l)
l.reverse()
print(l)
l.sort()
print(l)

# l.clear()