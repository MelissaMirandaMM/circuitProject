from sympy import symbols, laplace_transform, exp, sin, Heaviside
t, s = symbols('t s')

# Exemplo de transformada de Laplace para e^(-t), sin(t) e um degrau unitário
f1 = exp(-t)
f2 = sin(t)
f3 = Heaviside(t)

L_f1 = laplace_transform(f1, t, s)
L_f2 = laplace_transform(f2, t, s)
L_f3 = laplace_transform(f3, t, s)

print(L_f1, L_f2, L_f3)

