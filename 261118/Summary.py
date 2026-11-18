'''
0. 아이디, 비밀번호, 이메일을 받아서 계정 검증을 하는 프로그램.
1. 아이디 길이는 6자 이상 12자 이하입니다.
2. 아이디는 user_로 시작해야 합니다.
3. 비밀번호는 8자 이상이어야 합니다.
4. 비밀번호에는 ! 또는 @ 중 하나 이상이 포함되어야 합니다.
5. 비밀번호에 아이디 전체가 포함되어 있으면 안 됩니다.
6. 이메일은 @가 정확히 한 번 등장해야 합니다.
7. 이메일은 .com으로 끝나야 합니다.
모든 조건을 만족해야 최종 회원가입 가능 여부가 True가 됩니다.
'''

ID = input("아이디: ")
password = input("비밀번호: ")
email = input("이메일: ")

# 아이디 조건
# 1. 아이디 길이는 6자 이상 12자 이하입니다.
id_condition1 = len(ID) >= 6 and len(ID) <=12
# 2. 아이디는 user_로 시작해야 합니다.
id_condition2 = ID.startswith("user_")

# 비밀번호 조건
# 1. 비밀번호는 8자 이상이어야 합니다.
password_condition1 = len(password) >= 8
# 2. 비밀번호에는 ! 또는 @ 중 하나 이상이 포함되어야 합니다.
password_condition2 = password.count('!') >= 1 or password.count('@') >= 1
# 3. 비밀번호에 아이디 전체가 포함되어 있으면 안 됩니다.
password_condition3 = ID not in password

# 이메일 조건
# 1. 이메일은 @가 정확히 한 번 등장해야 합니다.
email_condition1 = email.count('@') == 1
# 2. 이메일은 .com으로 끝나야 합니다.
email_condition2 = email.endswith(".com")

is_sign_up = (id_condition1 and id_condition2 
              and password_condition1 and password_condition2 and password_condition3 
              and email_condition1 and email_condition2)

# ======
word = "NORMAL-WARNING-NORMAL-ERROR-WARNING"
print(word.count("WARNING"))
print(word.count("NORMAL"))
print(word.count("ERROR"))
print(word.find("WARNING"))
first_warning_index = word.find("WARNING")
print(word[first_warning_index:].find("WARNING"))
second_warning_index = word[first_warning_index:].find("WARNING")
print(second_warning_index - first_warning_index)