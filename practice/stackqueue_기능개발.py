import math

def solution(progresses, speeds):
    answer = []
    deploy = [0] * len(progresses)
    for i in range(len(progresses)): # 배포가능 일자 계산
        deploy[i] = math.ceil((100 - progresses[i]) / speeds[i])
    idx = 0
    for i in range(1, len(progresses)):
        if deploy[idx] < deploy[i]: # 같은 경우에는 따로 배포할 수 있다. (=을 없애야함)
            answer.append(i-idx)
            idx = i
    answer.append(len(progresses)-idx) # 마지막 원소 처리

    return answer

'''
# [스택/큐] 기능개발
https://programmers.co.kr/learn/courses/30/lessons/42586

미리 배포시간을 계산해서 처리하는 식으로 해결했으나,
스택/큐를 활용해서는 문제를 어떻게 풀 수 있는지 확인하기 위해 아래 링크를 통해 학습하였다.

참고) https://huidea.tistory.com/15

# 큐(FIFO) 풀이
def solution(progresses, speeds):
    answer = []
    time = 0 # 시간
    count = 0 # 출시 가능 기능
    
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100: # 100%가 될때까지 시간을 증가
            # 시간이 지났기 때문에 뒤에있는 것들도 100%가 되었다면 함께 출시 가능
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count) # 출시
                count = 0 # count 값 초기화
            time += 1 # 시간을 증가
    answer.append(count) # 마지막 제품까지 출시
    return answer
'''
