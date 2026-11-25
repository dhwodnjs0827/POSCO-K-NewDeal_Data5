person = {"name": "hong", "age": 20}
user_person = dict(name="hong", age=20)
print(type(person), type(user_person))
print(person)
print(user_person)
print(person["name"])
print(user_person["name"])

person["address"] = "서울"
print(person)

del person["age"]
print(person)

print("address" in person)  # True

person.clear()
print(person)

result = user_person.get("name")  # key 값에 맞는 value 반환
print(result)

result = person.get("score", 50)
print(result)

print("=======")

for data in user_person:
    print(data)

print("=======")

for data in user_person.items():
    print(data)

print("=======")

for key in user_person.keys():
    print(key, user_person[key])

print("=======")

person = {"name": "hong", "age": 20}
user_person = dict(name="hong", age=20)
data = user_person.pop("name")
print(data)
data2 = user_person.pop("age")
print(data2)
print(user_person)

# 실습
sensors = {"모터온도": 78, "진동": 0.5, "압력": 95}
print(len(sensors))
if len(sensors) < 5:
    print("센서 데이터 누락 확인 필요")

students = [{"name": "hong", "age": 20}, {"name": "park", "age": 15}]
for student in students:
    for s in student.items():
        print(s)

names = ["a1", "a2", "a3", "a4"]
ages = [10, 15, 26, 17]
data = list(zip(names, ages))
print(data)
data2 = dict(zip(names, ages))
print(data2)
