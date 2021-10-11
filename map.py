# map은 리스트의 요소를 지정된 함수로 처리해주는 함수
# 원본 리스트를 변경하지 않고 새 리스트를 생성한다.
# 리스트뿐만 아니라 모든 반복 가능한 객체를 넣을 수 있다.

a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a)) # map에 int와 리스트를 넣으면 리스트의 모든 요소를 int를 사용해서 변환해준다.
print(a)
# [1, 2, 3, 4]

b = list(map(str, range(10)))
print(b)
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

c = map(int, input().split())
# 입력 : 10 20
print(c)
# map 객체
print(list(c))
# [10, 20]

c = map(int, input().split())
# 입력 : 10 20
# map이 반환하는 맵 객체는 이터레이터라서 변수 여러 개에 저장하는 언패킹(unpacking)이 가능하다.
# iterable 객체 - 반복 가능한 객체
# 대표적으로 iterable한 타입 - list, dict, set, str, bytes, tuple, range
num1, num2 = c
print(num1, num2)
# 10 20

# 참고) https://dojang.io/mod/page/view.php?id=2286

# 중첩 for loop를 map 함수로 표현해보기
# 1.
for x in range(2,10):
    for y in range(1,10):
        print("(%s, %s)" % (x,y))

# 2.
for tuple in [(x,y) for x in range(2,10) for y in range(1,10)]:
# 수식으로 나타내면 `{ x ∈ [2,9], y ∈ [1,9] | print((x,y)) }` 와 동일
    print(tuple)

# 3.
list(map(lambda x: list(map(lambda y:print("(%s, %s)" % (x,y)), range(1,10))), range(2,10)))
# 클라이언트에게 소스코드를 넘겨줘야될 때는 map함수를, (난독화기능도 가능)
# 오픈소스로 풀 때에는 가독성이 좋은 for loop을 사용하는게 좋다.

# 참고) https://steemit.com/kr-dev/@tmkor/for-loop-map
