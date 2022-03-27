asia = ["한국", "중국", "일본"]
europe = ["영국", "프랑스", "독일"]
america = ["미국", "캐나다", "멕시코"]

inp = input("나라를 입력해주세요: ")

if inp in asia:
    print("아시아입니다")
elif inp in europe:
    print("유럽입니다")
elif inp in america:
    print("아메리카입니다")
else:
    print("데이터베이스에 없습니다")
#조건식을 이용해 입력값이 어느곳에 속하는지 판단하는 코드를 작성해주세요. 
#"아시아입니다", "유럽입니다", "아메리카입니다"의 출력값을 가지면 됩니다.

