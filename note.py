# 算数・数学
import sympy

x = sympy.Symbol("x")  # sympy.Symbol()で定義
y = sympy.Symbol("y")
print(type(x), "\n")
expr = x**2 + y + 1
print(expr)
print(f"xに1を代入:{expr.subs(x, 1)}")
print(f"xにyを代入:{expr.subs(x, y)}")
