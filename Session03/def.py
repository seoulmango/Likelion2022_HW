#함수를 '1개만' 작성해 공백으로 구분되어 입력받은 두 정수의 합, 차, 곱, 몫, 나머지를 한 줄씩 순서대로 출력하세요

# a, b = map(int, input().split())

def cal(x, y):
    return (x+y, x-y, x*y, x//y, x%y)

# x = int(input("x값 입력: "))
# y = int(input("y값 입력: "))

a, b = map(int, input("두 정수를 공백으로 구분해주세요 >> ").split())

for i in cal(a, b):
    print(i)