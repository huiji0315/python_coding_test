import sys
input = sys.stdin.readline
from collections import deque

tc = int(input())
while tc:
    tc -= 1
    # 문서의 개수, 몇번째로 인쇄되었는지 궁금한 문서
    n, m = map(int, input().split())
    # n개 문서의 중요도(중복가능)
    priority = deque(map(int, input().split()))
    seq = 0
    while priority:
        top = max(priority) # 중요도가 가장 높은 문서
        pop = priority.popleft()
        m -= 1 # 큐에서 하나를 뽑았으므로 문서의 순서도 재배치 필요(앞으로 댕김)

        # 큐에서 뽑은 문서가 중요도가 가장 높은 문서인지 판단
        if top != pop:
            priority.append(pop) # 가장 뒤에 재배치
            if m < 0:
                m = len(priority)-1 # 음수처리(맨뒤로 보냄)
        else:
            seq += 1 # 출력되는 순서 카운팅
            if m == -1: # 원하는 문서가 출력된 경우
                print(seq)
                break
'''
# 프린터 큐
https://www.acmicpc.net/problem/1966
1. 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

ex) (A B C D) 2 1 4 3 : C -> D -> A -> B

-> 각 테스트 케이스에 대해 원하는 문서가 몇번째로 인쇄되는지 출력하기

참고) https://chancoding.tistory.com/38
* 큐에서 문서를 뽑은 후에 '문서의 순서를 재배치' 하는 부분이 중요한 부분인 것 같다.
'''
