# 문자열.split(생략 가능 구분자)
list = [10, 20, 30, "hello", False]
print(list[3]) # hello
print(list[1]) # 20

coffee = "에스프레소 카페라떼 아메리카노"
print(coffee.split()) # ["에스프레소", "카페라떼", "아메리카노"]
coffee_list = coffee.split()
print(coffee_list[2])

print("사과,배,감".split(','))
print("사과,배,감".split(',')[2])

date = "2025-01-15"
day = date.split('-')[2]

# 실습
'''
#① '설비 정상 가동' 저장 → ② '정상'을 '점검'으로 바꿔 출력
#① 'PUMP A 03' 저장 → ② 공백 기준 분리하여 리스트 출력
#① 'a,b,c,d' 저장 → ② ','을 기준으로 분리
#① 'a,b,c,d' 저장 → ② 첫 번째 ','을 기준으로 한 번만 나누기
'''

# 1번
print("설비 정상 가동".replace("정상", "점검"))
# 2번
print("PUMP A 03".split())
# 3번
print("a,b,c,d".split(','))
# 4번
print("a,b,c,d".split(',', 1))

# 구분자가 될 문자열.join([리스트])
list1 = ["2026", "11", "19"]
# 2026-11-19, 2026.11.19
print('-'.join(list1))
print('.'.join(list1))

# 실습
'''
#1. ① ['2025','01','15'] 준비 → ② '-'으로 연결하여 합치기

#2. 2025·1·15 를 '-' 와 ','로 총 2가지 방법을 사용해 이어서 출력

# 3. ① '2025/01/15' 저장 → ② '/'을 기준으로 나눈 후 '-' 으로 합치기

#4. ① '1, NORMAL ,25.3' 저장
② ',' 기준으로 나누어 1번 인덱스를 공백 제거와 소문자로 변환해 출력
'''

# 1번
'-'.join(["2025", "01", "15"])
# 2번
"2025·1·15".replace('·', '-')
"2025·1·15".replace('·', ',')
# 3번
list = "2025/01/15".split('/')
'-'.join(list)
# 4번
sentence = "1, NORMAL ,25.3"
list = sentence.split(',')
print(list[1].strip().lower())

'''
1. text = "   PyThOn   " ->"python"

2. phone = "  010 - 1234 - 5678  " -> "01012345678"

3. name = "   kIM    cHUL   sOO   " -> "Kim Chul Soo"

4. filename = "  Sensor Data 2026.CSV  " -> "sensor_data_2026.csv"

5. data = "TEMP----PRESSURE----STATUS" -> "TEMP-PRESSURE-STATUS"
'''

# 1번
text = "   PyThOn   "
text.strip().lower()
# 2번
phone = "  010 - 1234 - 5678  "
phone.strip().replace(" - ", '')
# 3번
name = "   kIM    cHUL   sOO   "
name = name.split()
name = ' '.join(name).title()
# 4번
filename = "  Sensor Data 2026.CSV  "
filename.strip().replace(' ', '_').lower()
# 5번
data = "TEMP----PRESSURE----STATUS"
data.replace("----", '-')