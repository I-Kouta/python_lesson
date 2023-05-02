# 算数・数学
import sympy

x = sympy.Symbol("x")  # sympy.Symbol()で定義
y = sympy.Symbol("y")
print(type(x), "\n")
expr = x**2 + y + 1
print(expr)
print(expr.subs(x, 1))  # exprにx=1を代入
