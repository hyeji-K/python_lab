def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("아무런 실행 인자도 받지 않음.")

print_two("클라우드", "시대")
print_two_again("4차", "산업혁명")
print_one("인공지능!")
print_none()