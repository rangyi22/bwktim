# 9만원 이상: 매도, 8~9만원: 대기 중, 8만원 미만: 매수
stock_price = int(input("Enter the current price of Samsung Electronics. >>> "))

if stock_price >= 90000:
    print("I'd like to sell the stock.")
elif stock_price >= 80000:
    print("It's pending.")
else:
    print("I'd like to buy the stock.")