import heapq

n = int(input())
left = [] # 최대힙
right = [] # 최소힙

for _ in range(n):
    num = int(input())
    # 짝수개
    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    # 홀수개
    else:
        heapq.heappush(right, (num, num))
    # 두 힙의 top을 비교해 최대힙의 top이 최소힙의 top보다 큰 경우에는 전체 대소관계가 무너지므로, 그때의 top을 서로 swap해준다.
    if right and left[0][1] > right[0][1]:
        max_value = heapq.heappop(left)[1]
        min_value = heapq.heappop(right)[1]
        heapq.heappush(left, (-min_value,min_value))
        heapq.heappush(right, (max_value, max_value))
    # 중간값은 최대힙의 top (최대힙부터 원소가 들어가므로)
    print(left[0][1])

# https://kimmeh1.tistory.com/260 참고 코드
'''
# 가운데를 말해요
https://www.acmicpc.net/problem/1655

백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다.
만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.
-> 한 줄에 하나씩 N줄에 걸쳐 백준이의 동생이 말해야 하는 수를 순서대로 출력하기

[문제점 정리]
1. 입력 예시와 출력 예시를 그냥 대충 보고,
중간값이 그냥 말한 수의 순서대로 중간에 있는 값(전체 길이의 가운데)인줄알고 아래와 같이 바로 코드를 작성했다.
하지만, 여기서 말하고 있는 중간값은 숫자를 크기순으로 나열했을 때, 중간에 있는 값을 출력하라는 것이다.
-> 즉, 아래의 코드에서 idx를 계산하기 전에 num_list.sort()만 작성하면 된다.

n = int(input())

num_list = []
for _ in range(n):
  num = int(input())
  num_list.append(num)
  idx = (len(num_list) // 2)
  # 홀수개
  if len(num_list) % 2 != 0:
    print(num_list[idx])
  # 짝수개
  else:
    print(min(num_list[idx-1], num_list[idx]))

2. sort() 함수의 시간복잡도는 O(nlogn)으로 전체 시간복잡도가 n^2logn이 된다.
그런데 문제에서 1<=n<=100,000 이므로 시간제한이 0.1초여서 시간초과가 발생하게 된다.
(파이썬에서 1억까지를 1초로 생각하면 된다. 2000만 = 1초)
https://velog.io/@jehjong/Python-알고리즘-요구사항-분석-시간-복잡도

* 파이썬 주요 함수, 메소드의 시간복잡도
https://wayhome25.github.io/python/2017/06/14/time-complexity/

* 시간 제한이 1초인 문제를 만났을 때, 일반적인 기준은 다음과 같다.
  1) N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계하면 문제를 풀 수 있다.
  2) N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계하면 문제를 풀 수 있다.
  3) N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계하면 문제를 풀 수 있다.
  4). N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계하면 문제를 풀 수 있다.

 * 공간 제한은 보통 128~256MB 이므로 리스트의 크기를 1000만 이상을 넘지 않도록 주의하자.

 3. 따라서 이 문제는 우선순위큐를 활용하는 문제라고 할 수 있다.
 heappush(heap, item) 함수는 O(logn)의 시간복잡도를 가지고,
 heappop(heap) 함수는 O(nlogn)의 시간복잡도를 가진다.
 * list를 즉각적으로 heap으로 변환하는 heapify(list) 함수는 O(n)의 시간복잡도를 가진다.
 -> 파이썬에서 제공하는 heapq 모듈은 이진트리기반의 최소힙(min heap)의 형태로 원소를 정렬한다.
 : 힙에 원소를 추가할 때 (-item, item)의 튜플 형태로 넣어주면, 튜플의 첫번째 원소를 우선순위로 힙을 구성하게 된다.
 이때 원소 값의 부호를 바꿨기 때문에, 최소 힙으로 구현된 heapq 모듈을 최대 힙 구현에 활용할 수 있게 되는 것이다.
 https://littlefoxdiary.tistory.com/3

4. 이 문제에 필요한 로직을 그림으로 잘 표현한 블로그 페이지다.
https://blog.naver.com/PostView.nhn?blogId=sjy263942&logNo=222233717647
-> 이 블로그에서는 코드를 튜플 형태로 넣어주지 않고, 마이너스 부호를 붙여서 다 해결하였다.
'''
