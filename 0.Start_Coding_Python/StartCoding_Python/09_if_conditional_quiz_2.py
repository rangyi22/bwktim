# 1. 사용자로부터 가방, 시계 금액 입력 받기
# 2. 합계 금액 10만원 이상 할인률 30%, 10만원 이상 할인률 30%, 10만원 이상 할인률 10%

bag_price = int(input("Enter the price of the bag.>>> "))
watch_price = int(input("Enter the price of the watch.>>> "))

total_price = bag_price + watch_price

if total_price >= 100000:
    total_price = total_price * 0.7
elif total_price >= 50000:
    total_price = total_price * 0.8
else:
    total_price = total_price * 0.9

print("Total price: ", total_price)