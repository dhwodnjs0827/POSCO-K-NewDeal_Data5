# +(문자열 이어주기) *(문자열 반복)
print("설비" + "점검")  # 설비점검
print("설비" + " " + "점검")  # 설비 점검
line = "=" * 20  # 구분선 만들어주기
print(line)

#### 문자열과 관련된 함수
# len(문자열): 문자열의 길이를 반환
print(len("PYTHON"))  # 6
print(len("Strawberry Moon ~!"))  # 18
phone = "01012341234"
phoneLength = len(phone)
print(phoneLength)  # 11

# in, not in -> 함수는 아님
hasWord = "고장" in "설비 고장을 예측하는 ~~"
hasWord2 = "고장" not in "설비 고장을 예측하는 ~~"
print(hasWord)  # True
print(hasWord2)  # Fasle

# 실습. 포함 확인하기
message = "설비 고장 발생"
print("고장" in message)  # True
print("정상" in message)  # False

# count(), find(), index()
# 문자열A.count(문자열B): 문자열A에 문자열B가 몇 개나 들어 있는지 -> 숫자값 반환
# 문자열A.find(문자열B): 문자열A에 문자열B가 언제 처음 등장하는지 -> 인덱스 반환, 등장하지 않으면 -1 반환
# 문자열A.index(문자열B): 문자열A에 문자열B가 언제 처음 등장하는지 -> 인덱스 반환, 문자열B가 등장하지 않으면 Error!
print("banana".count("a"))  # 3
print("banana".count("na"))  # 2

email = "hong@company.com"
print("@의 인덱스 번호", email.find("@"))  # 4
print("@의 인덱스 번호", email.find("!"))  # -1 (찾고자 하는 문자열이 존재하지 않음)

print("@의 인덱스 번호", email.index("@"))  # 4
# print("@의 인덱스 번호", email.index('!')) # ValueError: substring not found

# 실습문제 1. ① 'sensor-01-temp' 저장 → ② count('-') 로 하이픈 개수 출력
print("sensor-01-temp".count("-"))  # 2

# 실습문제 2. ① 'temp_2024' 저장 → ② find('_') 로 첫 위치, 없는 글자(z)는 -1 확인
print("temp_2024".find("_"))  # 4
print("temp_2024".find("z"))  # -1

# startswith / endswith
# 문자열A.startswith(문자열B): 문자열A가 문자열B로 시작하는지 검사 -> True/False
# 문자열A.startswith(문자열B): 문자열A가 문자열B로 끝나는지 검사 -> True/False
print("EQP-001".startswith("EQP"))  # True
print("data.csv".endswith(".csv"))  # True
print("" == " ")  # False
print("normal" == "NORMAL")  # False
print("AAaaBB" == "AAaaBB")  # True
