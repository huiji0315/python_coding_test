a = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0)]

# 인자없이 그냥 sorted()만 쓰면, 리스트 아이템의 각 요소 순서대로 정렬을 한다.
b = sorted(a)
# b = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

# key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬한다.
c = sorted(a, key = lamda x : x[0])
# c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]
d = sorted(a, key = lamda x : x[1])
# d = [(3, 0), (0, 1), (5, 1), (1, 2), (5, 2)]

# 아이템 첫번째 인자를 기준으로 오름차순으로 먼저 정렬하고,
# 그 안에서 다음 두번째 인자를 기준으로 내림차순으로 정렬하는 방법
e = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)]
f = sorted(e, key = lamda x : (x[0], -x[1]))
# f = [(0, 3), (0, 1), (1, 5), (1, 4), (1, 3), (2, 4)]

'''
1. sort()
- 리스트를 정렬된 상태로 변경
- 리스트만을 위한 메소드
- 오름차순 정렬 = sort()
- 내림차순 정렬 = sort(reverse=True)

2. sorted()
- 기존의 리스트를 변경하는 것이 아니라 정렬의 새로운 리스트를 반환
- 어떤 이터러블 객체도 받을 수 있다.
(ex. 딕셔너리 객체도 받을 수 있음)
- 오름차순 정렬 = sorted()
- 내림차순 정렬 = sorted(reverse=True)

3. key 매개변수
- key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하며 순서대로 정렬한다.
- 오름차순 정렬 = sorted(a, key = lambda x : x[0])
- 내림차순 정렬 = sorted(a, key = lambda x : -x[0])
- 요소가 여러개일 경우 각 요소마다 정렬기준을 정해줄 수 있다. sorted(a, key=lambda x: (x[0], -x[1])

참고) https://velog.io/@aonee/Python-%EC%A0%95%EB%A0%AC-sort-sorted-reverse

4. dictionary 정렬
 1) 키를 기준으로 오름차순 정렬
 - sorted(dict.keys()) : keys 만 정렬된 값을 반환
 - sorted(dict.items()) : 키(key)를 기준으로 정렬하되 키와 값을 튜플로 묶어서 정렬된 값을 반환
 - sorted(dict.items(), key=lambda item: len(item[0])) : 키의 길이(length)를 기준으로 오름차순 정렬
 2) 키를 기준으로 내림차순 정렬
 : reverse=True를 추가해주면 된다.

 3) 값을 기준으로 오름차순 정렬
 - sorted(dict.items(), key=lambda item: item[1])
 4) 값을 기준으로 내림차순 정렬
 - sorted(dict.items(), reverse=True, key=lambda item: item[1])

참고) https://rfriend.tistory.com/473

[같이 참고하면 좋은 파일]
- 211003 #10. 나이순 정렬
- list&tuple&dictionary.py
'''
