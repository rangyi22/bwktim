#vending_machine.py
goods ={'A': {'가격':10, '재고':2},
        'B': {'가격':5, '재고':3}}
prompt = '''Whice one do you want in the above list? ...
          (Press Enter to quit)'''
while True:
  재고 = 0  
  for key, item in goods.items():
     재고 +=  goods[key]['재고']
     print(f'{key} = {item}')
  if 재고 <=0:
    print("죄송하지만 재고가 없습니다!")
    
  상품 = input(prompt)
if 상품 == '': # Enter key
    
  if 상품 not in goods.keys():
    print("\n죄송하지만 그런 상품은 없어요!\n")
    
  가격 = goods[상품]['가격']
  재고 = goods[상품]['재고']
  if 재고 < 1:
    print('\n다 떨어졌어요!\n')
    
  현금 = int(input("돈을 넣으세요: "))
  잔돈 = 현금 - 가격
  if 잔돈 >= 0:
    print(f'여기 상품 {상품}와 잔돈 {잔돈}원입니다.\n')
    goods[상품]['재고'] = 재고 - 1
  else:
    print('\n 현금이 모자라서 그대로 반환됩니다.\n')   
