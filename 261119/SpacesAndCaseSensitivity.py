# ====== 문자열의 대소문자 ======
word = "python"
sentence = "I Love python"

# upper(), lower() -> 전체 변경
# capitalize(), title() -> 앞글자만 대문자로 변경
print(word.upper())  # PYTHON
print(sentence.upper())  # I LOVE PYTHON
print(word.count("p"))  # 1, 원본 문자열은 변경되지 않음.

print("normal".upper())  # NORMAL
print("WARNING".lower())  # warning
print("WARNING 경고".lower())  # warning 경고 (한글이나 특수문자는 그대로 유지)
print(
    "python is good. i have an apple.".capitalize()
)  # Python is good. i have an apple.
print("python is good. i have an apple.".title())  # Python Is Good. I Have An Apple.
print("hong gil-dong".title())  # Hong Gil-Dong
print("apple".lower() == "Apple".lower())  # True

# isupper(), islower()
print("Apple".islower(), "Apple".isupper())  # False False
print("apple".islower())  # True
print("APPLE".isupper())  # True

# 실습
# 1번
"ready".upper()
# 2번
"WARNING".lower()
# 3번
"kim chul soo".title()
# 4번
print("fault" == "FAULT".lower())
# 5번
print("ABC".isupper(), "ABC".islower())
print("abc".isupper(), "abc".islower())
print("Abc".isupper(), "Abc".islower())
# 6번
word = "Sensor_LOG.CSV".lower()
print(word.startswith("sensor"), word.endswith(".csv"))

# ====== 문자열 공뱍 처리 ======
# strip(): 왼쪽/오른쪽 공백 제거, lstrip(): 왼쪽 공백 제거, rstrip(): 오른쪽 공백 제거
sentence = "  안녕하세요. 저는 jay입니다.      "
print(sentence + "!!")
print(sentence.strip() + "!!")
print(sentence.lstrip() + "!!")
print(sentence.rstrip() + "!!")

print("====== 절취선 ======".strip("="))

# jay를 대문자로 -> 결과
# 앞뒤 공백 제거
# 문자 개수를 세기
print(sentence.upper())
print(sentence.upper().strip())
print(len(sentence.upper().strip()))

# 실습
"""
7. '  가동중 ' 변수로 저장 후 -> [가동중] 출력해보기
8. ' 대기 ' 변수로 저장 후 -> [대기 ]/[ 대기] 각각 출력
9. ***경고**** 저장 후 * 제거 후 `경고`만 출력
10. '  WARNING ' -> 'warning' 체이닝으로 출력하기
"""
# 7번
sentence = "  가동중 "
print(sentence.strip())
# 8번
sentence = " 대기 "
print(sentence.lstrip())
print(sentence.rstrip())
# 9번
sentence = "***경고****"
print(sentence.strip("*"))
# 10번
sentence = "  WARNING "
print(sentence.strip().lower())
