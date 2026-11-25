"""
다음과 같이 구구단을 작성하시오

2*1=2    3*1=3  4*1=4  5*1=5

....

2*9=18   3*9=27 4*9=36  5*9=45
"""

for i in range(1, 10):
    for j in range(2, 6):
        print(f"{j}*{i}={j * i}", end="\t")
    print("\n")

"""
숫자를 입력받아서  해당 구구단을 작성하시오

첫단  2   5   7       aaa  => 숫자오류!

끝단  3   7    5

2~ 3 

5~7 단
"""
n1 = input("첫단: ")
n2 = input("끝단: ")
if not n1.isnumeric() or not n2.isnumeric():
    print("숫자 오류!")
n1 = int(n1)
n2 = int(n2)
if n1 > n2:
    temp = n1
    n1 = n2
    n2 = temp

for i in range(n1, n2 + 1):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}", end="\t")
    print("\n")

"""
단어별 등장 횟수 세기

apple banana apple orange banana apple

결과

apple : 3개

banana : 2개

orange : 1개
"""
data = ["apple", "banana", "apple", "orange", "banana", "apple"]
data_dict = {}
for item in data:
    if item in data_dict:
        data_dict[item] += 1
    else:
        data_dict[item] = 1

for item in data_dict:
    print(f"{item}: {data_dict[item]}개")

"""
students=[ ( 'hong', 90, 100), 

               ('park',45,40),

               ('kim',80,75)]

#평균이  60 이상인 학생들의 자료를 출력하시오
"""
students = [("hong", 90, 100), ("park", 45, 40), ("kim", 80, 75)]
for student in students:
    avg = ((student[1]) + student[2]) / 2
    if avg >= 60:
        print(f"{student}")
