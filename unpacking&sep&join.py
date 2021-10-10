# unpacking = 패킹된 변수에서 여러개의 값을 꺼내오는 것
# -> 풀어헤치려는 값 앞에 *를 붙여주면 된다. (여러 개의 인자를 넘긴 효과)
a = [0, 1, 2]
print(*a, sep='\n')
'''
0
1
2
'''

b = [[0, 1, 2], [3, 4, 5]]
print(*b, sep='\n')
'''
[0, 1, 2]
[3, 4, 5]
'''

# 리스트 안의 각각의 요소를 하나씩 출력하기
for row in b:
    print(*row)
'''
0 1 2
3 4 5
'''

# sep 옵션 = 여러 요소를 출력하는 경우 sep 인자에 원하는 구분자를 주면
# 해당 구분자를 요소들 사이사이에 출력해준다. (기본적으로는 공백(' '))
print(1, 2, 3)
# 1 2 3
print(1, 2, 3, sep=',')
# 1,2,3
print(1, 2, 3, sep='\n')
# 1
# 2
# 3

# join 함수 = 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수 ('구분자'.join(리스트))
c = ['a', 'b', 'c', 'd']
str = ''.join(c)
print(str)
# abcd

'''
str2 = ''
for ch in c:
    str2 += ch
print(str2)
# abcd
'''

str = '-'.join(c)
print(str)
# a-b-c-d

str = '.\n'.join(c)
print(str)
# a.
# b.
# c.
# d

# 참고) https://blockdmask.tistory.com/468
