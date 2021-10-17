import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def MergeSort(start, end):
    global swap, arr

    size = end - start
    mid = (start + end) // 2
    if size <= 1:
        return

    # divide
    MergeSort(start, mid)
    MergeSort(mid, end)

    # merge
    new_arr = []
    idx1, idx2 = start, mid

    cnt = 0
    while idx1 < mid and idx2 < end:
		# 왼쪽이 큰 경우
        if arr[idx1] > arr[idx2]:
            new_arr.append(arr[idx2])
            idx2 += 1
            cnt += 1

		# 오른쪽이 큰 경우
        # arr[idx1] < arr[idx2]
        else:
            new_arr.append(arr[idx1])
            idx1 += 1
            # 오른쪽 배열에서 merge 될 때 왼쪽 배열에 큰 값의 수를 합쳐 줌
            swap += cnt

	# 남은 원소 처리
    while idx1 < mid:
        new_arr.append(arr[idx1])
        idx1 += 1
        swap += cnt
    while idx2 < end:
        new_arr.append(arr[idx2])
        idx2 += 1

    # 반영
    for t in range(len(new_arr)):
        arr[start+t] = new_arr[t]

n = int(input())
# array 생성
arr = list(map(int, input().split()))
swap = 0

MergeSort(0, n)
print(swap)

'''
# 버블 소트
https://www.acmicpc.net/problem/1517
-> 주어진 수열에 대해서 버블 소트를 수행할 때, Swap이 총 몇 번 발생하는지 알아내는 프로그램 작성하기

[느낀점 정리]
1. range의 범위를 정하는게 생각보다 머리가 빠르게 안돌아갔다.
2. 백준에서는 N의 범위가 500000까지 주어져 있으므로 O(N^2)인 버블소트로는 사실상 구할 수 없는 문제다.
-> 시간복잡도 O(NlogN)인 합병정렬을 활용해서 풀 수 있다.

버블소트에서는 인덱스 i, j에 대해서 i < j일때 a[i] > a[j]일 경우 두 수를 바꾸어주는 알고리즘을 의미한다.
따라서, 이를 합병정렬로 생각하면 두 그룹을 합쳐줄 때 버블소트에서 두 수를 바꾸어주는 swap의 카운트를 세어줄 수 있다.
=> 특정 수가 swap 되는 수 : 자기 기준 왼쪽에 큰 수의 개수만큼 swap이 일어난다.

참고) https://velog.io/@leehe228/boj1517
'''
'''
[기본 버블소트 구현 -> 시간초과]
def bubblesort(li):
    global swap
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
    # for i in range(len(li)-1, 0, -1):
    #   for j in range(i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                swap += 1

# n개의 수로 이루어진 수열
n = int(input())
li = list(map(int, input().split()))

# 버블 소트 = 서로 인접해 있는 두 수를 바꿔가며 정렬하는 방법
# swap 횟수
swap = 0
bubblesort(li)
print(swap)
'''
