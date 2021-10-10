def preorder(node):
    if node == '.':
        return
    print(node, end="")
    preorder(tree[node][0]) # 왼쪽자식
    preorder(tree[node][1]) # 오른쪽자식

def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0]) # 왼쪽자식
    print(node, end="")
    inorder(tree[node][1]) # 오른쪽자식

def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0]) #왼쪽자식
    postorder(tree[node][1]) #오른쪽자식
    print(node, end="")

# 이진트리의 노드 개수
n = int(input())
# 이진트리(딕셔너리 형태)
tree = {}

for _ in range(n):
    p, l, r = input().split() # 부모, 왼쪽자식, 오른쪽자식
    tree[p] = (l, r)

preorder('A')
print()
inorder('A')
print()
postorder('A')

'''
# 트리 순회
https://www.acmicpc.net/problem/1991
-> 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하기

- 전위순회 : 부모, 왼쪽자식, 오른쪽자식
- 중위순회 : 왼쪽자식, 부모, 오른쪽자식
- 후위순회 : 왼쪽자식, 오른쪽자식, 부모

노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

[느낀점 정리]
1. print문에서 end를 오랜만에 사용해봤다.
2. dictionary 형태를 사용해서 트리를 처음 구현해봤다.
-> 이전에 학교 자료구조시간에 C를 활용해서 이진트리와 트리 순회를 구현했던 적이 있었는데,
파이썬을 활용하니까 훨씬 쉽게 구현할 수 있다는 것이 느껴졌다.
'''
