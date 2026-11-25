# 문자열 검색 종합실습
word = "NORMAL-WARNING-NORMAL-ERROR-WARNING"
# 1번
print(word.count("WARNING"))  # 2
# 2번
print(word.count("NORMAL"))  # 2
# 3번
print(word.count("ERROR"))  # 1
# 4번
print(word.find("WARNING"))  # 7
# 5번
first_warning = word.find("WARNING")
second_warning = word.find("WARNING", first_warning + 1)
print(second_warning)  # 28
# 6번
length = len("WARNING")
print(len(word[first_warning + length : second_warning]))  # 14
# 7번
print(word[first_warning + length : second_warning])  # -NORMAL-ERROR-
# 8번
substr = word[first_warning + length : second_warning]
print("ERROR" in substr)  # True

# 실습1. 사칙연산 계산기
a = 17
b = 5
print(a + b, a - b, a * b, a / b, a % b, a**b, sep="·")

# 실습2. 평균과 도형 계산
x = 3
y = 4
z = 5
print((x + y + z) / 3)
print(x * y * z)

# 실습5. 설비 지표 계산
total = 500
error = 23
run_time = 21
total_time = 24
print(error / total * 100)
print(run_time / total_time * 100)

# 실습6. 시간 변환
time = 500
hour = 500 // 60
minute = time % 60
print(str(hour) + "시간" + str(minute) + "분")

# 실습7. 프로그램 실행시간 계산해보기 (NN초를 시간으로)
run_time = 98765
day = 98765 // (60 * 60 * 24)
hour = (98765 % (60 * 60 * 24)) // (60 * 60)
minute = ((98765 % (60 * 60 * 24)) % (60 * 60)) // 60
second = ((98765 % (60 * 60 * 24)) % (60 * 60)) % 60
print(str(day) + "일" + str(hour) + "시간" + str(minute) + "분" + str(second) + "초")

# 실습8. 정상범위와 다중센서 판정
temp = 85
is_temp_normal = temp >= 60 and temp <= 90
press = 5
is_press_normal = press >= 3 and press <= 7
print(
    "온도 정상"
    + str(is_temp_normal)
    + "·"
    + "압력정상"
    + str(is_press_normal)
    + "·"
    + "모두정상"
    + str(is_temp_normal and is_press_normal)
)

# 최종 실습
auth_code = input("인증 코드: ")

condition1 = auth_code.startswith("SEC-")
print("1번 조건:" + str(condition1))

condition2 = len(auth_code) == 15
print("2번 조건:" + str(condition2))

condition3 = auth_code[4:8] == "2026"
print("3번 조건:" + str(condition3))

condition4 = (
    auth_code[len(auth_code) - 1] == "X" or auth_code[len(auth_code) - 1] == "Y"
)
print("4번 조건:" + str(condition4))

condition5 = int(auth_code[9:13]) >= 1000 and int(auth_code[9:13]) <= 9999
print("5번 조건:" + str(condition5))

condition6 = auth_code.count("-") == 3
print("6번 조건:" + str(condition6))

all_condition = (
    condition1
    and condition2
    and condition3
    and condition4
    and condition5
    and condition6
)
print("모든 조건 만족: " + str(all_condition))
