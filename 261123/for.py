# 반복 가능한 객체 Iterable
# 1. 시퀀스 객체: 순서가 있고 인덱스로 접근이 가능한 객체(list, tuple, str, range)
# 2. 맵핑 객체: key-value 구조로 이루어짐(dict)
# 3. Iterator: enxt로 하나씩 자료를 꺼내는 객체(itr, filter, zip, enumerate, generator)
# 4. set 계열: 중복을 허용하지 않고 순서가 없는 자료형(set)

str = "안녕하세요 만나서 반갑습니다"
for ch in str:
    print(ch, end = '')

name_list = ["곽현규", "김수진", "김주영", "신승민"]
for name in name_list:
    print(name)

# 실습
data = [10, 5, 3, 6, 20, 50, 15]
min = data[0]
max = data[0]
for num in data:
    if min > num:
        min = num
    if max < num:
        max = num
print(f"최댓값: {max}\n최솟값: {min}")


# range: 일정 범위의 정수를 생성해서 반복문에서 사용
# range(stop), range(start, stop), range(start, stop, step) # stop: exclusive
for data in range(5):
    print(data)
for num in range(2, 4):
    print(num)
for num in range(1, 11, 2):
    print(num)
for num in range(20, 10, -1):
    print(num)

# 실습
num = int(input("끝 숫자 입력: "))
for n in range(1, num + 1):
    print(n)
for n in range(2, num + 1, 2):
    print(n)
for n in range(num, 0, -1):
    print(n)