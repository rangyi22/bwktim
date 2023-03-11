name = '김영희'
color = '파란색'

print('안녕하세요. 제 이름은 {}이고 좋아하는 색상은 {}입니다.'.format(name, color))

number = 20
greeting = '안녕하세요.'
place = '배랑이식당'
wait = '잠시만 기다려주세요.'

base = '{} {}입니다. 손님의 대기번호는 {}번입니다. {}'
new_way = base.format(greeting, place, number, wait)

print(new_way)