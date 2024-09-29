from sympy import symbols, inverse_laplace_transform

# Definindo as variáveis simbólicas
t, s = symbols('t s')

# Função no domínio de Laplace
F_s = 1/(s+1)

# Calculando a transformada inversa de Laplace
f_t = inverse_laplace_transform(F_s, s, t)

print(f_t)
