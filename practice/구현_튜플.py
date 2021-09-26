def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = len) # 원소의 순서가 다르면 서로 다른 튜플
    for i in s:
        ii = i.split(',')
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
    return answer

# 참고) https://hazung.tistory.com/103
'''
# [구현] 튜플
https://programmers.co.kr/learn/courses/30/lessons/64065

ex) "{{2},{2,1},{2,1,3},{2,1,3,4}}"	-> [2, 1, 3, 4]

1) 맨앞 '{{'와 맨뒤 '}}'를 잘라준다. 그리고 '},{'을 기준으로 split하면 괄호문자가 모두 사라진다.
s는 현재 ','를 포함한 문자열 원소들이다. -> [ '1', '1,2', '1,2,3' ]

2) 반복문에 들어오는 원소마다 ','을 기준으로 split해준다.
-> [ '1, 2' ]가 들어온다면 [ '1', '2' ]로 만든다.

3) answer 배열에 차례대로 append해준다.
'''
