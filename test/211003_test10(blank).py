a = input().split('-')
num = []
for i in a:
    ## 작성 부분 ##
    if '+' not in i:
        num.append(int(i))
    else:
        b = i.split('+')
        sum = 0
        for j in b:
            sum += int(j)
        num.append(sum)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)

'''
# 잃어버린 괄호 (빈칸 채우기 문제)
https://www.acmicpc.net/problem/1541
-> 괄호를 적절히 쳐서 식의 최솟값 구하기

ex) 55-50+40 -> 55-(50+40) = -35
: 덧셈들을 먼저 더해서 가장 큰 수로 만들고 뺄셈을 진행하면 최솟값을 구할 수 있다.

[문제점 정리]
# 틀린 코드 -> +가 여러 개일 경우에 대해 고려하지 않음 (결과: 런타임에러)
a = input().split('-')
num = []
for i in a:
    ## 작성 부분 ##
    if '+' not in i:
        num.append(int(i))
    else:
        a, b = i.split('+')
        num.append(int(a) + int(b))
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)

* split의 결과가 list로 나온다는 것을 까먹지 말자.(멈칫했었음)
'''
