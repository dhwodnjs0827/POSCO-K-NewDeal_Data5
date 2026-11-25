# 실습1. 여러 줄 문자열 만들기
str1 = """가동 점검표
1. 온도 확인
2. 입력 확인"""

str2 = "가동 점검표\n1. 온도 확인\n2. 압력 확인"

print(str1)
print(str2)

# 실습2. 설비 라벨 이어 붙이기
code = "PUMP_A"
status = "정상"
date = "2025-01-15"
print(code + " / " + status + " / " + date)
print(code, status, date, sep=" / ")
