# while 문: 조건이 True일 동안 반복
count = 1
while count < 4:
    print("안녕", count)
    count += 1

# 1... 5까지
count = 0
while count < 5:
    count += 1
    print("안녕", count)

count = 5
while count >= 1:
    print(count)
    count -= 1

count = 3
while count <= 11:
    print(count)
    count += 2

count = 14
while count > 4:
    count -= 2
    print(count)

# break: 반복문 탈출, 중간에 exit
# continue: 현재 반복문을 건너뛰고 다음 반복
i = 1
while i <= 10:
    if i % 4 == 0:
        break
    print(i)
    i += 1

for item in range(1, 10):
   print(item)
   if item % 3 == 0:
      break

while True:                # 기본은 계속 반복
    x = input("입력 ( q= 종료): ")
    if x == 'q':           # 종료 신호면
        break              # 빠져나옴
    print("입력:", x)