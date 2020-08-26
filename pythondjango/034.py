# 매직 메서드, 연산자 오버로딩
'''
init : 생성자
del : 소멸자
add : +
or : bit단위 or 연산
repr, str : class를 프린트 했을 경우 출력해주는 문자열
call : 함수를 호출
getattr : 속성 가져오기
setattr : 속성 할당하기
delattr : 속성 제거
dataattribute : 속성 가져오기
getitem : 인덱싱, 슬라이싱, 반복을 위해 사용
setitem : 인덱스와 슬라이스된 값을 가져오기 위해 사용
delitem : 인덱스와 슬라이스된 값을 삭제하기 위해 사용
bool
len
lt, gt le, ge, eq, ne : >, <, <=, >=, ==, !=
radd : 오른쪽 기준 연산자
iadd : +=, -=
iter, next : 반복을 위해 사용
coontains : in
index : 정숫값
enter, exit : with
get, set, delete
new : init
'''

class Car(object):
    def __init__(self):
        print('인스턴스가 생성되었습니다.')
    def addkinds(self, name):
        self.kinds = []
        self.kinds.append(name)
    maxSpeed = 300
    maxPeople = 5
    def move(self, x):
        print(x, '의 스피드로 움직이고 있습니다.')
    def stop(self):
        print('멈췄습니다.')

k3 = Car()