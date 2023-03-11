#generator_expr.py
# generator expression/comprehension을 사용해서 파일을 한 줄 한 줄 읽는다.
gen = (row for row in open("grade.csv"))
for row in gen:
    print(row, end='')
