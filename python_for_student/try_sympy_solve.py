#try_sympy_solve.py
import sympy as sym

G,L1,L2,M1,M2 = sym.symbols('G L1 L2 M1 M2') # symbolic 변수 선언
s1, s2, s12, c12, w1, w2, x2, x4 =\
  sym.symbols('s1 s2 s12 c12 w1 w2 x2 x4') # symbolic 변수 선언
s = sym.solve([L1*(M1+M2)*x2 +L2*M2*c12*x4 +L2*M2*s12*w2**2 \
 +G*(M1+M2)*s1, L1*M2*c12*x2+L2*M2*x4-L1*M2*s12*w1**2+G*M2*s2],\
 [x2, x4])  # 식 (P9.14.1)
print(s[x2]); print(s[x4])
A = [[L1*(M1+M2), L2*M2*c12], [L1*M2*c12, L2*M2]] # 식 (P9.14.3)
b = [-L2*M2*s12*w2**2 -G*(M1+M2)*s1, L1*M2*s12*w1**2 -G*M2*s2]
xs = sym.Matrix(A).inv()*sym.Matrix(b)
print(sym.simplify(xs[0]-s[x2]), sym.simplify(xs[1]-s[x4]))
