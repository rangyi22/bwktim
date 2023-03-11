#try_dsolve2.py
import sympy as sym

t = sym.symbols('t')  # t를 하나의 symbolic variable로 선언
x = sym.Function('x')(t) # x를 t에 관한 하나의 함수로 선언
y = sym.Function('y')(t) # y를 t에 관한 하나의 함수로 선언
dxdt = x.diff(t)  # x 함수의 t에 관한 1차 미분
dydt = y.diff(t)  # y 함수의 t에 관한 1차 미분
de = [dxdt -y, dydt +3*y +2*x - 10*sym.sin(t)] # 미분방정식 (9.48)
ics = {x.subs(t,0):0, y.subs(t,0):-3} # 초기조건(initial conditions)
sol = sym.dsolve(de, [x,y], ics=ics) # 미분방정식의 풀이
xs = sol[0].rhs; ys = sol[1].rhs  # solution equation들의 우변(RHS)들
print('x(t) =', xs);  print('y(t) =', ys) 
