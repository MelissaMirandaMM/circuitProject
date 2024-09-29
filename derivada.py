from sympy import symbols, laplace_transform, exp, diff

# Definindo as variáveis simbólicas
t, s = symbols('t s')

# Derivada de uma função exponencial
f = exp(-2*t)
deriv_f = diff(f, t)

# Transformada de Laplace da derivada
L_deriv_f = laplace_transform(deriv_f, t, s)

print(L_deriv_f)
