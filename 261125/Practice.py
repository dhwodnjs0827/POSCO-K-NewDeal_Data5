'''
memebers=[]  리스트에서 관리한다.

안에 들어갈 자료는 dict로 관리하고 

자료 구성 :  code, name, age, gender로 구성된다. 

code는 자동으로 증가하고  1.2.3 ...

name, age, gender는 직접 입력으로 처리한다.

회원추가 
 번호는 자동을 추가 

 이름 

  나이 

성별 만 입력하도록 
'''
members = []
code = 1
while True:
    name = input("이름: ")
    age = input("나이: ")
    gender = input("성별: ")
    data = {"code": code, "name": name, "age": age, "gender": gender}
    code += 1
    members.append(data)

    if 'N' == input("계속 입력?(Y/N)"):
        break
print(members)

'''
저장되어 있는 리스트의 자료를 전체 출력한다.

전체 보기는 다음과 같이 출력한다. 

  사원번호    이름   나이  성별

   1              hong   20    남

   2              kim     10    여
'''
members = [{"사원번호": 1, "이름": "hong", "나이": 20, "성별": "남"}, {"사원번호": 2, "이름": "kim", "나이": 10, "성별": "여"}]
print("사원번호 이름\t나이\t성별\n")
for member in members:
    for data in member:
        print(f"{member[data]}\t", end = '')
    print('\n')

'''
회원 조회

사원 조회를 위해서 사원번호를 입력 

해당 사원 번호가 없으면 조회할 사원이 없음을 출력!

계속 조회할 것인지 체크  y=> 계속 조회, n=> 종료 

   조회할 사원은 1 

   사원번호:

   이름:

   나이:

   성별 

 만약  사원이 없으면 

  조회할 사원이 없습니다

  계속 조회? y /n 

   

n :  조회가 완료되었습니다. 
'''
members = [{"사원번호": 1, "이름": "hong", "나이": 20, "성별": "남"}, {"사원번호": 2, "이름": "kim", "나이": 10, "성별": "여"}]

while True:
    code = int(input("조회할 사원번호 입력: "))
    found = False

    for member in members:
        if member["사원번호"] == code:
            print(f"\n조회할 사원은 {code}")
            print(f"사원번호: {member['사원번호']}")
            print(f"이름: {member['이름']}")
            print(f"나이: {member['나이']}")
            print(f"성별: {member['성별']}\n")
            found = True
            break

    if not found:
        print("조회할 사원이 없습니다.")

    search_continue = input("계속 조회? y/n")
    if search_continue == 'n':
        print("조회가 환료되었습니다.")
        break

'''
회원 삭제 

삭제할  사원의 회원 번호를 조회하여 해당 사원을 삭제 

삭제 사원의 자료를 확인한후 삭제를 할 것인지에 따라 

삭제 여부 판단 

계속 삭제할 것인지 check 

 삭제할 사원은  :  1 

  삭제할 사원은 다음과 같습니다

  사원이름 hong

  나이 20

   성별 남 

 

   삭제하시겠습니까?  y /n

   삭제완료 

   삭제취소 

    계속 삭제할까요?   

   

종료!

삭제할 사원 :50

해당 사원이 없습니다. 
'''
members = [{"사원번호": 1, "이름": "hong", "나이": 20, "성별": "남"}, {"사원번호": 2, "이름": "kim", "나이": 10, "성별": "여"}]
while True:
    code = int(input("삭제할 사원번호 입력: "))
    found = False

    for member in members:
        if member["사원번호"] == code:
            print(f"삭제할 사원은 다음과 같습니다.\n")
            print(f"이름: {member['이름']}")
            print(f"나이: {member['나이']}")
            print(f"성별: {member['성별']}\n")
            found = True

        break

    if found:
        is_del = input("삭제하시겠습니까? y/n")
        if is_del == 'y':
            members.remove(member)
            print("삭제완료")
        else:
            print("삭제취소")
    else:
        print("해당 사원이 없습니다.")


    search_continue = input("계속 삭제할까요? y/n")
    if search_continue == 'n':
        print("종료!")
        break

'''
수정할 사원은  1

해당 사원의 값을 수정한다. 

 

 이름

 나이 

 성별 

 

수정할 사원은 10

 수정할 사원이 없습니다 

계속 수정할까요? y /n

 종료!
'''
members = [{"사원번호": 1, "이름": "hong", "나이": 20, "성별": "남"}, {"사원번호": 2, "이름": "kim", "나이": 10, "성별": "여"}]
while True:
    code = int(input("수정할 사원번호 입력: "))
    found = False

    for member in members:
        if member["사원번호"] == code:
            print(f"수정할 사원은 다음과 같습니다.\n")
            print(f"이름: {member['이름']}")
            print(f"나이: {member['나이']}")
            print(f"성별: {member['성별']}\n")
            found = True

        break

    if found:
        is_modify = input("수정하시겠습니까? y/n")
        if is_modify == 'y':
            name = input("이름: ")
            age = input("나이: ")
            gender = input("성별: ")
            member["이름"] = name
            member["나이"] = age
            member["성별"] = gender
            print("수정 완료")
        else:
            print("수정 취소")
    else:
        print("해당 사원이 없습니다.")


    search_continue = input("계속 수정할까요? y/n")
    if search_continue == 'n':
        print("종료!")
        break