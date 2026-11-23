# 1번
num = int(input("입력값: "))
tot = 0
for n in range(1, num + 1):
    tot += n
    print(n, end = '')
    if n != num:
        print('+', end = '')
    else:
        print('=', end = '')
print(tot)

# 2번
num = int(input("입력값: "))
answer = 0
for n in range(1, num):
    if n % 2 == 0:
        answer += n
    else:
        answer -= n
print(answer)

# 3번
data = [1, 4, 2, 6, 50, 40, 32]
new_data = []
tot = 0
for i in data:
    if i % 4 == 0:
        new_data.append(i)
        tot += i
print(f"{new_data}\n합계: {tot}")

# 4번
ages = [10, 20, 31, 11, 21, 9, 15]
adult_list = [age for age in ages if age >= 20]
child_list = [age for age in ages if age < 20]