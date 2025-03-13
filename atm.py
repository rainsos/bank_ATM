# balance : 통장에 들어있는 기본 금액을 담는 변수

#1.입금, 2.출금, 3.영수증 보기, 4.종료 -> 글자를 입력받을지(입금...출금.....) / 숫자로 입력받을지 (1,2,3....)
# 숫자로 원하는 기능을 입력할수있게 만들어주세요. 그리고 사용자가 입력한 기능은 num 변수에 담아주세요.
# deposit_amount: 
# withdraw_amout:

# 기본 통장 금액
balance = 3000

# 메뉴 출력
print("원하는 기능을 선택하세요:")
print("1. 입금")
print("2. 출금")
print("3. 영수증 보기")
print("4. 종료")

# 사용자의 입력을 숫자로 받아서 num 변수에 저장
# if num =="2":
     # pass를 할경우 지금은 작업은 안하지만 나중에 작업할거다라고 표시되고 진행이됨 

while True:
    num = (input("숫자를 입력해주세요 (1~4): ")) # 초기설정은 문자열로 진행했다.

    if num =="1":
        deposit_amount = input("입금할 금액을 입력해주세요 : ") #"123132.isdigit" -> true ★isdigit활용 추가보충설명필요하다다
        if deposit_amount.isdigit() and int(deposit_amount) > 0: # 첫번째 조건 문자가 입력된건 아닌지 확인 / 0보다 큰금액을 입력했는지 
            balance += int(deposit_amount) # balance = balance + int(deposit_amount)
            print(f"{deposit_amount}원이 입금되었습니다. 현재 잔액은 {balance}원입니다.")

        else:
            print("정신차리고, 제대로된 숫자형태로 입금액을 작성해줘")
        
            
    if num =="2":
        withdraw_amount = input("출금할 금액을 입력해주세요 : ")
        if withdraw_amount.isdigit() and int(withdraw_amount) > 0:
            withdraw_amount = min(balance, int(withdraw_amount))
            balance -= withdraw_amount #balance = balance-withdraw_amout
            print(f"고객님이 출금한 금액은{withdraw_amount}원이고고. 현재 잔액은 {balance}원입니다.")
        else:
            print("정신차리고, 제대로된 숫자형태로 출금액을 작성해줘")

    if num =="3":
        pass
    if num =="4":
        print("서비스를 종료합니다")
        break
    

