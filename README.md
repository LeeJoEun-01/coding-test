# Python 문법 정리

<!-- 토글 코드 -->
<!-- <details>
<summary>제목</summary>
<div>

내용

</div>
</details> -->

### 목차
###### 입력받는 법
- [1차원 배열 입력받기](#1차원-배열-입력받기)
- [한줄에 정수형 변수 여러개 입력받기](#한줄에-정수형-변수-여러개-입력받기)
- [한줄에 문자열 변수 여러개 입력받기](#한줄에-문자열-변수-여러개-입력받기)
###### 메소드&함수.Zip
- [정렬 (sort(), sorted)](#정렬)
- [파라미터 key 값 이용하기](#파라미터-key-값-이용하기)
- [순서 뒤집기](#순서-뒤집기)
###### 시간초과 해결방안
- [Deque](#Deque)


# 입력받는 법
### 1차원 배열 입력받기

```python
#값 2개 입력받기\n
n, k = map(int, input().split())

# 값 3개 입력받기 똑같음 \n
a, b, v = map(int,input().split())

#여러개의 값을 공백으로 나누어 입력받을때 리스트에 집어넣기
arr = list(map(int, input().split()))

#16진수를 10진수로\nn = int(input(), 16)
a = sys.stdin.readline().strip()

# 정수 여러줄\n
# 1
# 2
# 3
# 4
# 5
a = [int(input()) for _ in range(5)]

#문자열 여러줄
s = [input() for _ in range(3)]

#111
#222
#333
s = [list(map(int, input())) for _ in range(3)]

#2차원 배열 입력
#1 1 1 1 1
#2 2 2 2 2
arr = [list(map(int, input().split())) for _ in range(2)]
```

### 한줄에 정수형 변수 여러개 입력받기

```python
a, b, c, d = map(int, input().split())

# 입력
1, 2, 3, 4

# 출력
>> print(a)
1
>> print(b)
2
```

### 한줄에 문자열 변수 여러개 입력받기

```python
a, b = input().split()

# 입력
123 321

# 출력
>> print(a, b)
123 321

>> print(type(a))
<class 'str'>
```

<details>
<summary>문자열 여러줄 입력받기 - v.1</summary>
<div>

```python
graph = [input() for _ in range(a)]

# 입력
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW

# 출력
>> print(graph)
['WLLWWWL', 'LLLWLLL', 'LWLWLWW', 'LWLWLLL', 'WLLWLWW']
```

</div>
</details><br>

<details>
<summary>문자열 여러줄 입력받기 - v.2</summary>
<div>

```python
maze = [list(map(int, input())) for _ in range(n)]

# 입력
101111
101010
101011
111011

# 출력
[[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]
```

</div>
</details><br>

<details>
<summary>2차원 배열 입력받기</summary>
<div>

```python
arr = [list(map(int, input().split())) for _ in range(n)]

# 입력
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3

# 출력
>> print(arr)
[[1, 3, 3, 6, 7], [8, 13, 9, 12, 8], [4, 16, 11, 12, 6], [2, 4, 1, 23, 2], [9, 13, 4, 7, 3]]
```

</div>
</details><br>

# 메소드&함수.Zip

> ### 정렬

sort() 메서드: 본체를 변화시킨다.

```python
# sort()
a = [7,4,6,3,2,0]
a.sort()
print(a)

#[0, 2, 3, 4, 6, 7]

a.sort(reverse=True)
print(a)

#[7, 6, 4, 3, 2, 0]

```

sorted 함수: 정렬한 사본을 만들어 낸다.

```python
# sorted
b = sorted(a)
print(b)
print(a)

#[0, 2, 3, 4, 6, 7]
#[7, 6, 4, 3, 2, 0]
b = sorted(a, reverse=True)
print(b)

#[7, 6, 4, 3, 2, 0]

```

#### 파라미터 key 값 이용하기

```python
gender = ['man', 'woman', 'girl', 'boy']
gender.sort(key=len)
print(gender)

#['man', 'boy', 'girl', 'woman']
```

### 순서 뒤집기

**reverse** <br>
: list 타입에서 제공하는 함수로 리스트 값을 반환하는 것이 아니라 변환시켜준다.
(list가 아닌 tuple, dictionary, string에서 사용하면 에러 발생 ❗️)

```python
list.reverse()
```

**reversed** <br>
: 내장함수로, list에서 제공하는 함수가 아니다.
(dictionary는 순서가 있는 타입이 아님으로 지원하지 않는다. string을 변환하기 위해서는 다른 방법이 필요하다.)

```python
reverse(list)

l = ['a', 'b', 'c']
t = ('a', 'b', 'c')

list_1 = list(reversed(l))  # ['c', 'b', 'a']
tuple_1 = tuple(reversed(t))  # ('c', 'b', 'a')
```

# 시간초과 해결방안

> ### list 보다 deque를 사용하자

- list에서 `pop(0)` 연산의 시간 복잡도는 **O(N)**이어서 N이 커질 수록 연산이 매우 느려진다. <br><br>

### Deque

: double-ended queue의 약자로 데이터를 양방향에서 추가하고 제거할 수 있는 자료구조

- `popleft()`라는 메서드를 사용하면 list의 `pop(0)` 메서드와 같은 효과를 가진다!

```python
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)
# deque[1, 2, 3, 4]

queue.popleft()
# 1

queue.popleft()
# 2

queue
# deque[3, 4]
```

- deque은 Queue와 다르게 `appendleft(x)`라는 메서드가 있는데, 이 메서드를 사용하면 데이터를 앞에서 삽입할 수 있다.
- deque의 `popleft()`와 `appendleft(x)`메서드는 모두 **O(1)**의 시간 복잡도를 가지기 때문에, 자료 구조보다 성능이 훨씬 뛰어나다!
- 단점: 무작위 접근의 시간 복잡도가 O(N)이고, 내부적으로 linked list를 사용하기 때문에 N번째 데이터에 접근하려면 N번 순회가 필요하다.
