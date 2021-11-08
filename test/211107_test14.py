# 정답 풀이
# 출처) https://kdgt-programmer.tistory.com/3

# n= 전체학생의 수
# lost= 체육복을 도난당한 학생들의 번호
# reserve= 여벌의 체육복을 가져온 학생들의 번호
def solution(n, lost, reserve):
    reserve_n = list(set(reserve) - set(lost))
    lost_n = list(set(lost) - set(reserve))
    answer = n - len(lost_n)
    for i in lost_n:
        if i - 1 in reserve_n:
            answer += 1
            reserve_n.remove(i - 1)
        elif i + 1 in reserve_n:
            answer += 1
            reserve_n.remove(i + 1)
    return answer

# 틀린 풀이 1
def solution(n, lost, reserve):
    answer = n - len(lost)
    for i in reserve:
        for j in lost:
            if i == j or i-1 == j or i+1 == j:
                reserve.remove(i)
                lost.remove(j)
                answer += 1

    return answer

# 틀린 풀이 2
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for i in reserve:
        for j in lost:
            if i == j:
                reserve.remove(i)
                lost.remove(j)
    answer = n - len(lost)

    for i in reserve:
        for j in lost:
            if i-1 == j or i+1 == j:
                reserve.remove(i)
                lost.remove(j)
                answer += 1

    return answer

'''
# 체육복
https://programmers.co.kr/learn/courses/30/lessons/42862
-> 체육수업을 들을 수 있는 학생의 최댓값 구하기

* set 자료형
1. 중복을 허용하지 않는다.
2. 순서가 없다.
-> 원소끼리 빼기가 가능하기 때문에 중복을 제거하기 좋다.

[느낀점 정리]
1. remove 함수 = 원본 훼손 주의
ex)
li = [3, 2, 1]
for i in li:
  li.remove(i)
  print(li)

-> [2, 1]
   [2]
: [1]이 남는 것이 아니라 [2]가 남아버리는 문제가 있다.

2. set, list 함수 = set을 적용하면 sort의 효과가 있다.
ex)
a = set([5, 6, 2, 4, 1])
print(a)
b = list(a)
print(b)

-> {1, 2, 4, 5, 6}
   [1, 2, 4, 5, 6]

-> ex) n = 5, lost = [4, 2], reserve = [3, 5]일 경우
sort가 되어있지 않으면 순서대로 체육복을 적절하게 배분할 수 없다.
3번이 2번한테 빌려줘야하는데, 4번에게 빌려주어서 2번이 체육복을 가질 수 없게 되는 문제가 있다.
'''
