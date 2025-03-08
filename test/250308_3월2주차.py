'''
[2025.03.08]
1. DB : https://school.programmers.co.kr/learn/courses/30/lessons/59410 (NULL 처리하기)
2. https://school.programmers.co.kr/learn/courses/30/lessons/12945 (피보나치 수)
3. https://school.programmers.co.kr/learn/courses/30/lessons/42842 (카펫)
'''

#1. NULL 처리하기
SELECT ANIMAL_TYPE, NVL(NAME, 'No name') AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

#2. 피보나치 수
'''
재귀 호출을 하면 n이 50 이상일 때
시간 초과가 나거나
Python이나 JavaScript 등 일부 언어에서는 런타임 에러가 납니다.
런타임 에러가 나는 이유: 일부 언어는 재귀 호출을 할 수 있는 횟수가 정해져 있고, 횟수를 넘어 재귀 호출을 하면 런타임 에러를 내도록 설계되어 있습니다.
--> 중복계산을 제거하는 메모이제이션(Memoization)을 활용한 동적계획법(Dynamic Programming) 활용 필요
'''

#1.
def solution(n):
    dp = [0]*100001
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n] % 1234567

#2.
def solution(n):   
    pre = 0
    current = 1
    
    for i in range(2, n+1):
        current, pre = current + pre, current
  
    return current % 1234567

#3. 카펫
'''
큰 사각형의 넓이 (카펫의 넓이)
= 갈색 격자의 개수 + 노란색 격자의 개수
= 카펫의 너비 x 카펫의 높이

작은 사각형의 넓이
= 노란색 격자의 개수
= (카펫의 너비 - 2) x (카펫의 높이 - 2)
'''

def solution(brown, yellow):
    area = brown + yellow
    # 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다. --> 높이가 최소 3
    # 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다. --> 높이는 최대 h*h=area의 제곱근
    for height in range(3, int(area**0.5) + 1):
        if area % height == 0:
            width = area // height
            if (width - 2) * (height - 2) == yellow:
                return [width, height]
