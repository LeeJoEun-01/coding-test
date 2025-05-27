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
- [문자열 자르기](#문자열-자르기)
- [순서 뒤집기](#순서-뒤집기)
- [Range 매개변수](#Range-매개변수)

###### 시간초과 해결방안

- [빠른 입력](#빠른-입력)
- [Deque](#Deque)
- [Counter](#Counter)

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
![image](https://github.com/LeeJoEun-01/coding-test/assets/78733700/5c72bd3f-8eff-4b1d-a9cc-c9dde59cce38)

![image](https://github.com/LeeJoEun-01/coding-test/assets/78733700/5c72bd3f-8eff-4b1d-a9cc-c9dde59cce38)

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
![image](https://github.com/LeeJoEun-01/coding-test/assets/78733700/c5d670a0-6af0-448a-9209-45ed4d0ea00f)

![image](https://github.com/LeeJoEun-01/coding-test/assets/78733700/c5d670a0-6af0-448a-9209-45ed4d0ea00f)

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

![image](https://github.com/LeeJoEun-01/coding-test/assets/78733700/abc2a64b-f129-40ef-ba4f-31d57414e7df)

### Range 매개변수

- range(start, end, step)

<br><br>

# 메소드&함수.Zip

### 정렬

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
![image](https://github.com/LeeJoEun-01/coding-test/assets/78733700/fc0f4df2-a7df-47d8-8b8d-4e7c08071d75)

![image](https://github.com/LeeJoEun-01/coding-test/assets/78733700/fc0f4df2-a7df-47d8-8b8d-4e7c08071d75)

#### 파라미터 key 값 이용하기

```python
gender = ['man', 'woman', 'girl', 'boy']
gender.sort(key=len)
print(gender)

#['man', 'boy', 'girl', 'woman']
```
![image](https://github.com/LeeJoEun-01/coding-test/assets/78733700/b73b71b7-4c85-49dd-8fa1-a6ba1e7d7131)

##### 정렬 조건 lambda 사용

```python
a = [(4,0), (4,3), (4,2), (3,2), (2,1), (1,0)]

# 인자 없이 sorted()를 사용하면 리스트 아이템의 각 요소 순서대로 정렬
# 첫 번째 요소가 같으면 두 번째 요소로 비교
b = sorted(a)
print(b)    # [(1, 0), (2, 1), (3, 2), (4, 0), (4, 2), (4, 3)]

# key인자에 lambda 함수를 넘겨주면 반환값을 가지고 비교해 정렬
# 이 때, key로 전달되지 않은 요소에 대해선 정렬하지 않음
c = sorted(a, key=lambda x : x[0])
print(c)    # [(1, 0), (2, 1), (3, 2), (4, 0), (4, 3), (4, 2)]
d = sorted(a, key=lambda x : x[1])
print(d)    # [(4, 0), (1, 0), (2, 1), (4, 2), (3, 2), (4, 3)]
```

##### 정렬 조건 여러개

```python
# 정렬 기준으로 다중 조건을 넘겨줄 수도 있다
# 첫 번째 인자를 기준으로 오름차순 정렬을 먼저 한다.
# 그 결과를 가지고 두 번째 인자를 기준으로 내림차순 정렬(-를 붙이면 내림차순 정렬)
e = sorted(a, key = lambda x : (x[0], -x[1]))
print(e)    # [(1, 0), (2, 1), (3, 2), (4, 3), (4, 2), (4, 0)]
```

![image](https://github.com/LeeJoEun-01/coding-test/assets/78733700/b73b71b7-4c85-49dd-8fa1-a6ba1e7d7131)

### 문자열 자르기

#### Slicing

- string[start:end]는 start를 포함하고, end를 포함하지 않는 문자열을 추출
- step을 생략하면 기본적으로 1로 설정되며, 문자열을 자를 때는 1을 사용하면 됨

##### [ 앞에서부터 문자열 자르기 ]

```python
my_str = "This is a substring tutorial..!"

result = my_str[0:7]
print(result) # This is
```

> 여기서 0은 생략이 가능하여 string[:num]처럼 사용할 수 있습니다.

##### [ 뒤에서부터 문자열 자르기 ]

```python
my_str = "This is a substring tutorial..!"

result = my_str[-5:]
print(result) # al..!
```

![image](https://github.com/LeeJoEun-01/coding-test/assets/78733700/0b12362d-0968-4d18-8709-2658aa6fe063)

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

<br><br>

# 시간초과 해결방안

### 빠른 입력

: Python의 input() 함수는 상대적으로 느린 편이기 때문에, 대량의 데이터를 입력받을 때는 `sys.stdin.readline()`을 사용하는 것이 효율적이다.

- 빠른 입력 개행문자 없애기 -> `.strip()` 사용

```python
words = [sys.stdin.readline() for _ in range(n)]
print(words)
# ['a\n', 'ab\n', 'abc\n', 'abcd\n', 'abcde\n', 'abcdef\n']

words = [sys.stdin.readline().strip() for _ in range(n)]
print(words)
# ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']
```

![image](https://github.com/LeeJoEun-01/coding-test/assets/78733700/32b96c0b-477b-4c6b-b386-817bcb2dd09f)

### Deque

: double-ended queue의 약자로 데이터를 양방향에서 추가하고 제거할 수 있는 자료구조

#### list 보다 deque를 사용하자

> list에서 `pop(0)` 연산의 시간 복잡도는 **O(N)**이어서 N이 커질 수록 연산이 매우 느려진다.

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

![image](https://github.com/LeeJoEun-01/coding-test/assets/78733700/a06cb2f7-2e18-476f-86c5-37de6cabb8c5)

### Counter

: 데이터의 개수를 셀 때 매우 유용한 파이썬의 collections 모듈의 Counter 클래스 (Hash와 같이 알고리즘 문제를 풀 때에도 유용하게 사용할 수 있다.)

- Counter 생성자는 여러 형태의 데이터를 인자로 받는다. 먼저 중복된 데이터가 저장된 배열을 인자로 넘기면 각 원소가 몇 번씩 나오는지가 저장된 객체를 얻게 된다.

  ```python
  from collections import Counter

  counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
  # counter({'blue': 3, 'red': 2, 'green': 1})
  ```

- Counter를 사전(Dictionary)처럼 사용

  - items()와 values()로 접근 가능

  ```python
  max_count = max(counter.values())
  many_color_arr = [color for color, count in counter.items() if count == max_count]

  # 키로 값을 읽을 수 있다.
  counter["blue"], counter["red"]
  # (3, 2)

  # 특정 키에 해당하는 값을 갱신할 수 있다.
  counter["blue"] += 100
  # 103

  # in 키워드를 이용하여 특정 키가 카운터에 존재하는지 확인할 수 있다.
  red in counter
  # True
  ```

- **가장 흔한 데이터 찾기**
  가장 흔한 데이터 찾는 작업을 좀 더 쉽게 할 수 있도록, 데이터의 개수가 많은 순으로 정렬된 배열을 리턴하는 `most_common()`이라는 메서드를 제공하고 있다.

  ```python
  from collections import Counter

  Counter('hello world').most_common()
  # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
  Counter('hello world').most_common(2)
  # [('l', 3), ('o', 2)]

  ```
