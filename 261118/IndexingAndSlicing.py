word = "PYTHON"
print(word[0], word[2], word[5]) # P T N
print(word[-6], word[-4], word[-1]) # P T N
print("python"[2]) # t

word = "Strawberry Moon ~!"
son = word[0] + word[12] + word[14] + word[17]
print(son) # Son!

word2 = "안녕하세요!"
hello = word2[-6] + word2[-5] + word[-1]
print(hello) # 안녕!

# 실습1. 양수 인덱스로 글자 꺼내기
word = "SIGNAL"
print(word[0], word[2], word[5], sep = '/') # S/G/L
# print(word[6]) # IndexError: string index out of range

#### 슬라이싱
word = "PYTHON"
# 양수 인덱스를 통한 슬라이싱
print(word[0:5]) # PYTHO
print(word[:4]) # PYTH
print(word[1:]) # YTHON
print(word[1:100]) #YTHON # 슬라이싱은 범위 밖 번호를 지정해도 Error 발생x
print(word[:]) # PYTHON

# 음수 인덱스를 통한 슬라이싱
print(word[-3:]) # HON
print(word[:-1]) # PYTHO

# 문자열[시작:끝:간격] - step으로 건너뛰기
print(word[0::2]) # PTO
print(word[::-1]) # NOHYP

# 실습1. 구간 자르기
word = "SIGNAL"
print(word[:3], word[2:5], sep = " / ") # SIG / GNA

# 실습2. ① 'temp_sensor' 저장 → ② 앞 4글자만 추출하기
word = "temp_sensor"[:4]

# 실습3. ① 'temp_sensor' 저장 → ② _(언더바) 이후 모든글자 추출
word = "temp_sensor"[5:]

# 실습4. ① 'icecream' 저장 → ② 슬라이싱만을 이용해서 'crm' 추출
word = "icecream"[1::3]