n = int(input())
stack = []

def push(x):
  stack.append(x)

def pop():
  if len(stack) == 0:
    print(-1)
  else:
    num = stack.pop()
    print(num)

def size():
  print(len(stack))

def empty():
  if len(stack) == 0:
    print(1)
  else:
    print(0)

def top():
  if len(stack) == 0:
    print(-1)
  else:
    print(stack[len(stack)-1])

for _ in range(n):
  a = input().split()
  if a[0] == 'push':
    push(a[1])
  elif a[0] == 'pop':
    pop()
  elif a[0] == 'size':
    size()
  elif a[0] == 'empty':
    empty()
  elif a[0] == 'top':
    top()

'''
# 명령에 따른 스택 구현하기

- push X: 정수 X를 스택에 넣는 연산이다.
- pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- size: 스택에 들어있는 정수의 개수를 출력한다.
- empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
- top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

* 입력 예시)
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top

[문제점 정리]
1. for문으로 같은 개수의 input만 입력을 반복적으로 받아 봤지, 입력 예시와 같이 push의 경우에만 두 개의 인자를 받기 때문에 이를 어떻게 해야할지 당황했다.
-> 그냥 input().split()을 이용하면 된다.
입력받을 때 아무 생각 없이 그냥 기계적으로 input().split()을 썼던 폐해인것 같다.
-> split() 함수는 input()으로 받아온 데이터를 특정 기준을 통해 분리하는 역할을 한다.
일반적인 split()은 공백(Space Bar)을 기준으로 분리하는 데, 특정 문자를 기준으로 분리하고 싶다면 split() 인자로 특정 문자를 지정하면 된다.
ex) input().split('p')
-> 즉, 엔터(enter)를 기준으로 사용자 입력이 진행된다.
-> 직접 print로 찍어보니

n = int(input())
stack = []

for _ in range(n):
  a = input().split()
  print(a)

['push', '1']
['push', '2']
['top']
['size']
['empty']
['pop']
...

이런 식으로 list 안에 입력값이 구분되어서 잘 들어가는 것을 볼 수 있다.

2. stack의 top 함수(리스트의 마지막 원소)는 stack[len(stack)-1]을 통해 구현을 했는데 stack[-1]로 간단하게 구할 수 있다.

 '''
