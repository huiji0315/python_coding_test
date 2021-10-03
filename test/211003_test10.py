import sys
input = sys.stdin.readline

# 회원수
n = int(input())

# 회원리스트
member = []
for i in range(n):
    age, name = input().split()
    member.append((int(age), i, name))

member.sort()
for i in range(n):
    print(member[i][0], member[i][2])

'''
# 나이순 정렬
https://www.acmicpc.net/problem/10814

온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다.
이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬

-> 오랜만에 혼자 금방 풀어낸 쉬운 문제였다.

[문제점 정리]
1) 처음에 위의 코드에서 member.append((int(age), name))로 해서 sort를 진행했다.
그랬더니 age로 먼저 정렬된 후 name으로도 정렬이 되어서, 문제와 다르게
나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬이 되지 않았다.
-> 때문에 중간에 가입 순서를 집어 넣어주어 해결했다.

2) sort의 특성과 sort에 lambda를 사용하는 것의 차이가 갑자기 궁금해져 추가로 코드로 실행해보았다.
-> 아래의 코드를 참고해보면 알 수 있듯이,
sort에 key로 설정해준 값인 age로만 정렬을 진행하고, 뒤의 name으로는 정렬을 진행하지 않기 때문에 문제의 조건에 바로 만족시킬 수 있다.
'''
'''
# 회원리스트
member = []
for i in range(n):
    age, name = input().split()
    member.append((int(age), name))

member.sort(key=lambda member:member[0])
for age, name in member:
    print(age, name)
'''
