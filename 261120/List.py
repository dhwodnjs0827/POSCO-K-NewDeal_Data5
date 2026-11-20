numbers = [25, 89, 30, 50, 11, 12]
machines = ["펌프", "모터", "압축기"]
mixed = [True, False, "문자열", 100, [1, 2, 3]]
print(numbers)
print(machines)
print(mixed)

### len(리스트): 리스트의 요소 개수 확인
print(f"numbers의 요소 개수 확인 {len(numbers)}")
print(f"mixed의 요소 개수 확인 {len(mixed)}")
print(f"list의 요소 개수 확인 {len(['a', 'b', 'c'])}")
print(f"비어있는 리스트 요소 개수 확인 {len([])}") # 0

# 리스트의 인덱싱, 슬라이싱
numbers = numbers = [25, 89, 30, 50, 11, 12]
mixed = [True, False, "문자열", 100, [1, 2, 3]]
print(numbers[3])
print(mixed[-2])
print(mixed[-1][0])

print(numbers[2:5]) # [30, 50, 11]
print(numbers[::-1])
print(numbers) # 슬라이싱 이후에도 리스트의 값은 유지

### 리스트의 데이터 변경하기 (인덱싱을 통해 값 변경)
# 원본 데이터가 변경
numbers = [25, 27, 30, 32, 34, 36]
numbers[2] = 100
print(numbers) # [25, 27, 100, 32, 34, 36]

### in, not in
machines = ["펌프", "모터", "압축기"]
print("펌프" in machines) # True
print("펌프 " in machines) # False
print("실린더" not in machines) # True

# 실습
temps = [22, 21, 27, 23, 24, 23]
print(temps[0])
print(temps[2])
print(temps[-1])

yields = [1, 2, 3, 4, 5, 6]
print((yields[0] + yields[-1]) / 2)

### 리스트의 함수 사용해 보기
# 리스트.index(요소) -> 리스트 안에 요소가 몇 번째 인덱스에서 처음 등장하는지, 요소가 없으면 Error
numbers = [25, 27, 30, 32, 34, 36]
# print(numbers.index(100)) # ValueError: list.index(x): x not in list
print(numbers.index(34)) # 4

### 리스트.append(값) -> 리스트의 맨 뒤에 원하는 값 추가
### 리스트.insert(인덱스, 값) -> 리스트의 특정 인덱스에 원하는 값을 추가
### 리스트1.extend(리스트2) -> 리스트1에 리스트2를 붙여주는 함수
data = [25, 26, 27]
data.append(28)
print(data) # [25, 26, 27, 28]

data.insert(0, 24)
print(data) # [24, 25, 26, 27, 28]

data.extend([29, 30, 31])
print(data) # [24, 25, 26, 27, 28 , 29, 30, 31]

# 실습
list = []
list.append(30)
list.insert(0, 28)
list.extend([31, 32])
print(list)

list.insert(-1, 50)
print(list) # [28, 30, 31, 50, 32]
list.insert(100, 100)
print(list) # [28, 30, 31, 50, 32, 100]

### 리스트.remove(값)
### 리스트.pop(인덱스) -> pop의 반환값이 존재해서 제거되는 값을 따로 저장할 수 있음
### del 리스트[인덱스 or 슬라이싱]
data = [25, 26, 27, 28, 29, 30]
value = data.remove(25)
print(data) # [26, 27, 28, 29, 30]
print(value) # None

value = data.pop(2)
print(data) # [26, 27, 29, 30]
print(value) # 28

del data[2]
print(data) # [26, 27, 30]
del data[1:]
print(data) # [26]

# 실습
temps = [25, 26, 999, 24, 28, 26]
temps.remove(999)
print(temps)
value = temps.pop(1)
print(value)
del temps[0]
print(temps)

### 리스트 탐색, 정렬
### 리스트.sort() -> 기본적으로 오름차순 정렬, 괄화 안에 reverse = True 옵션 작성 시, 내림차순 정렬 가능
### 리스트.reverse() -> 리스트의 순서를 거꾸로 뒤집어 줌. (원본 리스트 변경)
### 리스트.count(값), 리스트.index(값)
data = [27, 24, 30, 22, 26]
data.sort() # 오름차순 정렬
print(data)
data.sort(reverse = True) # 내림차순 정렬
print(data)

data = [27, 24, 30, 22, 26]
data.reverse() # 순서 뒤집기
print(data) # [26, 22, 30, 24, 27]

raw_data = ["정상", "이상", "이상", "정상", "이상"]
print(raw_data.count("정상")) # 2
print(raw_data.index("이상")) # 1