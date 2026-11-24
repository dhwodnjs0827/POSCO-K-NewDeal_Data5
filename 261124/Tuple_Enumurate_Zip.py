# 리스트; 변경 가능하고, 순서보장, 중복적으로 저장할 수 있는 자료 타입
# 튜플: 데이터를 중복적으로 순서를 보장해서 저장할 수 있는 자료 타입
list = [10, 20, 10, 10, 10] # 리스트
tuple = (10, 20, 10, 10, 10) # 튜플
print(tuple)
print(type(list), type(tuple))
# tuple[0] = 100 # TypeError: 'tuple' object does not support item assignment

# enumerate: 반복이 가능한 자료를 순회하면서 각 요소의 인덱스와 값을 동시에 가져오는 것
names = ["hong", "kim", "lee"]
for data in enumerate(names):
    print(data)

for index, item in enumerate(names):
    print(index, item)

# zip: 여러 개의 반복 가능한 자료에서 같은 위치에 있는 요소들을 하나로 묶는 것
# 리스트의 길이가 다르면 -> 짧은 리스트의 길이에 맞춤
temps = [25, 32, 28, 35, 19, 31, 27]
result = ["이상" if temp > 30 else "정상" for temp in temps]
for temp, result in zip(temps, result):
    print(f"{temp} 온도는: {result}")

temps = [25, 32, 28, 35, 27]
fahrenheit = [temp * 1.8 + 32 for temp in temps]

for temp, fah in zip(temps, fahrenheit):
    print(f"섭씨{temp}, 화씨{fah}")

# 이중 for 문
for i in range(2):
    for j in range(3):
        print('*', end=' ')
    print('\n')

for  i   in range(3):
   for j in range(1,5):
      print(j, end=' ')
   print('\n')

for i in range(5, 0, -1):
    for j in range(i):
        print('*', end = ' ')
    print('\n') 

# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}", end = '\t')
    print('\n')