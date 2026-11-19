log = " [WARNing] "
log = log.strip()[1:8].lower()
print(log)

sensors = "temp,pressure,vibration"
sensors = sensors.split(',')
sensors = f"{sensors[2].upper()} / {sensors[1].upper()} / {sensors[0].upper()}"
print(sensors)

data = " EQP-01 , NORMAL , 85.5 "
print(data.split(" , ")[1].strip().lower())

text = " ###[ PUMP-07 ]### "
print(text.strip().strip("###").lstrip('[ ').rstrip(' ]').lower().replace('-', '_'))

data = " TEMP / Pressure | vibration "
print(data.strip().replace(" / ", ',').replace(" | ", ','))

# ======
# 실습1. 두 시점의 센서 데이터 비교 분석
data1 = " pump-07 | 08:30 | TEMP=085.5C | STATUS=normal"
data1 = data1.strip().split(" | ")
code1 = data1[0].upper().replace('-', '_')
time1 = data1[1]
temp1 = float(data1[2].replace("TEMP=",'').rstrip('C'))
status1 = data1[3].lstrip("STATUS=")

data2 = "PUMP_07,09:00,92.0C,WARNING"
data2 = data2.split(',')
code2 = data2[0]
time2 = data2[1]
temp2 = float(data2[2].rstrip('C'))
status2 = data2[3].lower()

print("===== 센서 데이터 비교 =====")
print(f"설비 코드: {code1}")
print(f"최초 측정: {time1} / {temp1}°C / {status1}")
print(f"최근 측정: {time2} / {temp2}°C / {status2}\n")
print(f"동일 설비 여부: {code1 == code2}")
print(f"온도 변화량: {temp2 - temp1}°C")
rate = (temp2 - temp1) / temp1 * 100
print(f"온도 상승률: {rate:.2f}%")
print(f"온도 급상승 여부: {rate >= 6}")

# 실습2. 설비 작업 완료 에정 시간 계산
log = " 2026/11/19 23:58:45 | DELAY=135s | EQP-09 "
log = log.strip().split(' | ')
day = log[0].split()[0]
time = log[0].split()[1]
hour = int(time.split(':')[0])
min = int(time.split(':')[1])
sec = int(time.split(':')[2])
delay = int(log[1].lstrip("DELAY=").rstrip('s'))
code = log[2]

print("===== 설비 작업 정보 =====")
print(f"설비 코드: {code}")
print(f"작업 날짜: {day}")
print(f"작업 시작 시간: {hour}시 {min}분 {sec}초")
print(f"소요 시간: {delay}초\n")
time = hour * 3600 + min * 60 + sec
complete_time = time + delay
complete_hour = (complete_time // 3600) % 24
complete_min = (complete_time % 3600) // 60
complete_sec = complete_time % 60
print(f"완료 시각: {complete_hour}시 {complete_min}분 {complete_sec}초")
print(f"날짜 변경 여부: {complete_time >= 24 * 3600}")

# 실습3. 생산 데이터 통합 및 불량률 분석
line1 = " LOT-A | 1,200 | 36 | 8h "
line2 = "lot_a,850,17,5h"

line1 = line1.strip().split(" | ")
code1 = line1[0].replace('-', '_')
yield1 = int(line1[1].replace(',', ''))
defect1 = int(line1[2])
time1 = int(line1[3].replace('h', ''))

line2 = line2.split(',')
code2 = line2[0].upper()
yield2 = int(line2[1])
defect2 = int(line2[2])
time2 = int(line2[3].replace('h', ''))

print("===== 생산 데이터 분석 =====")
print(f"생산라인 코드: {code1}")
print(f"라인 코드 일치: {code1 == code2}\n")

print(f"[1차 생산] 생산량 {yield1}개 / 불량품 {defect1}개")
rate1 = defect1 / yield1 * 100
print(f"불량률: {rate1:.2f}%")
print(f"[2차 생산] 생산량 {yield2}개 / 불량품 {defect2}개")
rate2 = defect2 / yield2 * 100
print(f"불량률: {rate2:.2f}%\n")

print(f"[통합 분석] 생산량 {yield1 + yield2}개 / 불량품 {defect1 + defect2}개")
print(f"통합 불량률: {(defect1 + defect2) / (yield1 + yield2) * 100:.2f}%")
print(f"시간당 평균 생산량: {(yield1 + yield2) / (time1 + time2):.2f}개\n")
      
print(f"불량률 개선 여부: {rate2 < rate1}")
print(f"최종 판정: {rate2 < rate1}")