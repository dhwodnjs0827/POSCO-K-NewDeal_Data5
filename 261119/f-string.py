name = "홍길동"
age = 25
# 홍길동님은 25살입니다.
print(name + "님은 " + str(age) + "살입니다.")
print(f"{name}님은 {age}살입니다.")

code = "EQP-001"
print(f"설비 코드 {code} 점검 완료: 온도 {25}도")
hours = 3
print(f"총 가동 시간(분): {hours * 60}분")

value = 3.141592
print(f"PI 소수점 둘째 자리까지: {value:.2f}")
print(f"PI 소수점 넷째 자리까지: {value:.4f}")

# 실습
'''
# ① 설비명·온도를 변수로 저장 → ② f-string을 사용해서 예상 결과와 같이 출력

# ① 세 점수를 변수로 저장 → ② f-string을 사용하여 평균을 구하는 계산식을 사용해 출력

# ① 측정값 87.456 저장 → ② 소수점 첫 번째 자리와 두 번째 자리까지 각각 출력

# ① 문자열 '  5 , sensor_2 , WARNING , 0.78912  ' 저장
# ② strip·split 후 각 조각 정리, 소수점은 두 번째 자리까지

'''
# 1번
name = "EQP-001"
temp = 36.5
print(f"설비 {name} 온도: {temp}도")
# 2번
score1 = 10
score2 = 20
score3 = 30
print(f"평균: {(score1 + score2 + score3) / 3}")
# 3번
num = 87.456
print(f"{num:.1f}")
print(f"{num:.2f}")
# 4번
str = "  5 , sensor_2 , WARNING , 0.78912  "
str = str.strip().split(" , ")