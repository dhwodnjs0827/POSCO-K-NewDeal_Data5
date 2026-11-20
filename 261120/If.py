'''
if 조건:
    조건이 참일 때 실행될 문장1
    조건이 참일 때 실행될 문장1
    조건이 참일 때 실행될 문장1
======
if 조건:
    조건이 참일 때 실행될 문장
else:
    조건이 거짓일 때 실행될 문장
======
if 조건1:
    조건1이 참일 때 실행될 문장
elif 조건2:
    조건1이 거짓이고, 조건2가 참일 때 실행될 문장
else:
    조건1, 조건2 모두 거짓일 때 실행될 문장
'''

score = int(input("점수를 입력해 주세요."))
if score >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")
print("조건문과 관련없이 실행되는 문장입니다.")

# 실습
age = int(input("나이 입력"))
if age >= 20:
    print("성인입니다")
else:
    print("미성년자입니다")

score = int(input("점수를 입력해 주세요."))
if score >= 90:
    print("우수")
elif score >= 70:
    print("보통")
else:
    print("미흡")

score = int(input("점수를 입력해 주세요."))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

temp = 78
vib = 3.5
if temp > 60 and vib > 3:
    print("위험합니다")
elif temp > 60 and vib <= 3:
    print("주의하세요")
elif temp <= 60:
    print("정상입니다.")


# ======
### 삼항 연산자
num = 5
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

result = "짝수" if num % 2 == 0 else "홀수"

### match ~ case 문
color = input("red, yellow, green 중 하나를 작성해주세요.").strip()
match color:
    case "red" | "RED":
        print("퇴장입니다.")
    case "yellow":
        print("경고입니다.")
    case "green":
        print("통과입니다.")
    case _:
        print("잘못되 값이 들어왔습니다.")

# 설비 코드, 온도, 상태
data = ["PUMP-01", 85, "WARNING"]
match data:
    case [name, temp, "WARNING"]:
        print(f"{name}: 온도 {temp}도, 주의상태입니다.")
    case [name, temp, "NORAML"]:
            print(f"{name}: 온도 {temp}도, 정상상태입니다.")

# 실습
id = input("아이디 입력: ")
pw = input("비밀번호 입력: ")
if id == "admin" and pw == "1234":
    print("로그인 성공")
else:
    print("로그인 실패")