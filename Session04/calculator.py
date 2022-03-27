class Calculator:
    # 여기에 코드를 작성해보세요!
    def __init__(self, name):
        self.name = name
        self.result = int(input("Your age: "))

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result
    
    def mul(self, num):
        self.result = self.result * num
        return self.result

    def div(self, num):
        while True:
            if num == 0:
                print("나누기로 0이 아닌 숫자를 적어주세요.")
                num = int(input(">> 나누기 숫자를 다시 써주세요"))
                continue
            else: 
                self.result = self.result / num
                return self.result
                break

calculator1 = Calculator("박채원")

calculator1.add(5)
calculator1.div(0)
print(calculator1.result)