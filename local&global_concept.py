def change():
    val = 20  # global 선언 필요
    lst[1] = 0
    print(val, lst) // 20 [1, 0, 3]

val = 10
lst = [1, 2, 3]
change()
print(val, lst)  # 10 [1, 0, 3]

'''
변수가 선언되고 그 값을 바꿀 수 있는 경우를 mutable이라고 하고
반대의 경우를 immutable이라고 한다.
Python에서 immutable 변수로 대표적인 것이 튜플이 있다.
튜플의 원소 값을 바꾸려고 하면 오류가 나는 것을 확인할 수 있을 것이다.
하지만 튜플말고도 숫자, 문자열 등의 변수도 모두 immutable이다.

그러면 이미 선언한 변수를 a += 1이나 a = 10과 같이 바꾸는건 어떻게 된거냐고 물을 수 있는데,
이것은 새로운 a 객체를 생성하여 해당 값을 할당하는 것이다.

이와 달리 리스트 변수는 mutable로 값을 선언 이후에도 바꿀 수 있기 때문에
값을 바꿔줬을때 새로운 객체를 생성하지 않는다.

예시 코드에서 보면 val은 전역 namespace에 선언된 변수가 있지만
지역 namespace에서 새로 선언한 것으로 취급하여 다른 객체를 가리키는 것이다.
반대로 lst의 경우 mutable한 전역객체의 값을 바꾸는 것이기 때문에
전역 namespace에 있는 lst의 값을 바꾸는 것이 되는 것이다.

[Python 지역변수, 전역변수 관련 개념](https://medium.com/@dltkddud4403/python-%EC%A7%80%EC%97%AD%EB%B3%80%EC%88%98-%EC%A0%84%EC%97%AD%EB%B3%80%EC%88%98-%EA%B4%80%EB%A0%A8-%EA%B0%9C%EB%85%90-4ea2a1865071)
'''
