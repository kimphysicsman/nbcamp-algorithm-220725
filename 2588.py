# 문제
# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
#
#
#
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
#
# 출력
# 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.


def resolve_num(a):
    a_100 = a // 100
    a_10 = (a % 100) // 10
    a_1 = (a % 100) % 10
    return a_100, a_10, a_1


def multiply():
    a = int(input("input : "))
    b = int(input("input : "))

    if not 100 <= a <= 999 or not 100 <= b <= 999:
        print("input is incorrect. 100 <= input <= 999")
        return

    b_100, b_10, b_1 = resolve_num(b)

    idx_3 = a * b_1
    idx_4 = a * b_10
    idx_5 = a * b_100
    idx_6 = a * b

    print(idx_3)
    print(idx_4)
    print(idx_5)
    print(idx_6)


multiply()
