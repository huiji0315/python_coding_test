# 사람의 수
n = int(input())

# 각 사람이 돈을 인출하는 데 걸리는 시간
time = list(map(int, input().split()))
time.sort()

# 각 사람이 돈을 인출하는 데 걸리는 시간의 최소합
tot = [0] * n

tot[0] = time[0]
for i in range(1, n):
    tot[i] = tot[i-1] + time[i]

# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값
ans = 0
for i in range(n):
    ans += tot[i]

print(ans)

'''
# 그리디 문제

문제에서 예시로 설명을 해둔 것을 읽어보니 이해가 쉽게 되었고,
종이에 예시를 적어두고 생각을 해보니 오름차순으로 정렬 후 합을 구하면 된다는 것을 바로 알 수 있었다.
저번에 처음 test에서는 오히려 출력 형식이나 2차원 배열 등을 생각하느라 오래 걸렸던 것 같다.

'''
