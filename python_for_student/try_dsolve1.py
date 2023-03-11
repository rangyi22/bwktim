#try_dsolve1.py
import sympy as sym

t = sym.symbols('t') # t를 하나의 symbolic variable로 선언
y = sym.Function('y')(t) # y를 t에 관한 하나의 함수로 선언
dydt = y.diff(t)   # y 함수의 t에 관한 1차 미분
d2ydt2 = y.diff(t,2) # y 함수의 t에 관한 2차 미분
de = d2ydt2 + 2*dydt +2*y - sym.exp(-t) # 미분방정식 (9.47)
ics = {y.subs(t,0):0, dydt.subs(t,0):1} # 초기조건(initial conditions)
sol = sym.dsolve(de, y, ics=ics) # 미분방정식의 풀이
ys = sol.rhs  # solution equation의 우변(RHS)
print('y(t) =', ys) # print the solution ys 
