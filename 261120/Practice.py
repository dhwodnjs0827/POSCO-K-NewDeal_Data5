# 실습4. 세 값으로 설비 종합 상태 판정하기
temp = float(input("온도 입력: "))
vib = float(input("진동 입력: "))
curr = float(input("전류 입력: "))
if temp > 80 or vib > 4.0:
    print("위험: 즉시 정지")
elif curr > 60 and temp > 70:
    print("주의: 부하 점검")
elif vib > 2.5:
    print("주의: 진동 관찰")
else:
    print("정상")

# 실습1. 두 번째로 큰 숫자 찾기
list = input("공백으로 구분하여 정수 5개 입력: ")
list = list.split(" ")
numbers = [int(list[0]), int(list[1]), int(list[2]), int(list[3]), int(list[4])]
numbers.sort()
max = list[-1]
max_index = list.index(max)
print(f"두 번째로 큰 숫자: {list[max_index - 1]}")

# 실습 2. 사칙연산 계산디 만들기
num1 = float(input("첫 번째 숫자 입력: "))
num2 = float(input("두 번째 숫자 입력: "))
op = input("연산자 입력: ")
result = 0.0
match op:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = num1 / num2
print(f"계산 결과: {result}")

# 실습 3. ATM 출금 가능 여부 판정
current_balance = int(input("현재 잔액: "))
withdrawal_amount = int(input("출금 금액: "))
if withdrawal_amount % 1000 != 0:
    print("출금 단위 불일치")
elif withdrawal_amount < 1000 or withdrawal_amount > 100000:
    print("출금 가능 범위 벗어남")
elif withdrawal_amount > current_balance:
    print("잔액을 넘길 수 없음")
else:
    print(f"출금 성공!\n남은 잔액: {current_balance - withdrawal_amount}원")

# 실습 4. 숫자 5개의 중앙값 찾기
list = input("숫자 5개 입력: ")
list = list.split(" ")
numbers = [int(list[0]), int(list[1]), int(list[2]), int(list[3]), int(list[4])]
numbers.sort()
print(f"정렬 결과: {numbers}")
print(f"중앙값: {numbers[2]}")
