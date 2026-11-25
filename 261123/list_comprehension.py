# List Comprehension(내포 함수)
# 반복문과 조건문을 한 줄로 작성해서 새로운 리스트를 만드는 방법
# for문보다 간결하게 사용
# [표현식 for 변수 in Iterable]

numbers = []  # 1, 2, 3, 4, 5

for item in range(1, 6):
    numbers.append(item)
print(numbers)

numbers = [item for item in range(1, 6)]
print(numbers)

# 1, 3, 5, 7, 9
odd = [n for n in range(1, 10, 2)]
print(odd)

data = [1, 2, 3, 4, 5]
double3_data = []  # 3배씩 증가하여 저장 3, 6, 9, 12, 15
double3_data = [n * 3 for n in data]
print(double3_data)

data = [10, 12, 13, 41, 25, 46, 17]
double_data = []  # 2의 배수만 추려서 가져오기
double_data = [item for item in data if item % 2 == 0]
print(double_data)

data = [10, 12, 13, 41, 25, 46, 17]
result = [item + 10 for item in data]
print(data)

# list comprehension의 if else 사용

# 짝수이면 5를 곱해서, 홀수이면 그대로 저장
numbers = [1, 2, 3, 4, 5]  # 1, 10, 3, 20, 5
list = [num * 5 if num % 2 == 0 else num for num in numbers]
print(list)
