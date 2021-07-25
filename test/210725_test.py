test = int(input())

num = []
for i in range(test):
	num.append(list(map(int, input().split())))

for i in range(test):
  ans = 0
  for j in num[i]:
	  if j % 2 == 1:
		  ans += j
  print('#'+ str(i+1), ans)

'''
# 홀수 더하기 문제

[오류 냈던 부분 정리]
1. list를 2차원으로 받아야하는데 1차원으로 받아서
즉, num = list(map(int, input().split())) 으로 해서
list가 다 덮어 씌워져 마지막 ans에 같은 값만 출력됨
-> num = [], num.append(list(map(int, input().split())))으로 리스트 안에 리스트를 추가하는 방식으로 바꿔주었다.

2. 위와 같은 맥락으로 for j in num: 으로 1차원 리스트로 생각하고
풀어버려서 오류 발생함
1번을 고친 후에 여기서 2차원 리스트에서 for문을 돌리면
한 행씩(가로 한 줄) 가져오기 때문에 j%2에서 오류가 발생하였다.
-> list 한줄씩 가져와서 원소 하나씩 뽑아주기 위해 num[i]로 바꿔주었다.

3. print에서 ,를 사용하면 자동으로 공백을 하나 출력해준다.
처음에는 print('#', i, ' ', ans)로 출력하여 공백을 하나 더 준꼴이 되어 버렸음
-> ' '를 없앤 후에도 문제에서 "#1 ans" 이런 식으로 출력을 해야하기 때문에
#과 i를 붙여야 함을 깨달았고, + 연산자와 str()를 통해 이어주었다.

4. i를 출력하면 0부터 돌기 때문에 #0으로 시작하므로 문제 조건에 맞지 않아 오류가 발생함
-> i+1을 통해 하나씩 올려주었다.
'''
