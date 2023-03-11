#try_dsolve.py
import sympy as sym

#sym.init_printing() # 혹시 symbolic expression을 보기 좋게 print 할 때
t = sym.symbols('t') # t를 하나의 symbolic variable로 선언
y = sym.Function('y')(t) # y를 t에 관한 하나의 함수로 선언
dydt = y.diff(t)   # y 함수의 t에 관한 1차 미분
d2ydt2 = y.diff(t, 2) # y 함수의 t에 관한 2차 미분
de = d2ydt2 + 3*dydt +2*y - 10*sym.sin(t) # 미분방정식 (9.26)
ics = {y.subs(t, 0):0, dydt.subs(t,0):-3} # 초기조건(initial conditions)
# 초기조건 ics를 가진 미분방정식 de를 y에 대해 푼다.
sol = sym.dsolve(de, y, ics=ics) 
ys = sol.rhs  # solution 식의 우변(RHS)
print(ys) # ys를 print해
# ys를 미분방정식 de에 대입해서 그 결과를 간단하게 정리하면 뭐가 나올까?
print(de.subs(y,ys).simplify()) 
