# 算数・数学
import sympy

x = sympy.Symbol("x")  # sympy.Symbol()で定義
y = sympy.Symbol("y")
print(type(x), "\n")
expr = x**2 + y + 1
print(expr)
print(f"xに1を代入:{expr.subs(x, 1)}")
print(f"xにyを代入:{expr.subs(x, y)}")
del expr

expr = (x - 3) ** 2
expr_ex = sympy.expand(expr)
print(f"{expr} を展開：{expr_ex}")

expr_factor = sympy.factor(expr_ex)
print(f"{expr_ex} を因数分解：{expr_factor}")
print(f"{expr_ex}=0の解:{sympy.solve(expr_ex)}")

expr1 = x + y - 7
expr2 = 3 * x + 5 * y - 29
print(sympy.solve([expr1, expr2]))  # {x: ?, y: ?}
