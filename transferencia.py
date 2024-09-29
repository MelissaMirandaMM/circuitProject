import control as ctrl
import matplotlib.pyplot as plt

# Função de transferência: 1 / (s + 1)
num = [1]
den = [1, 1]
system = ctrl.TransferFunction(num, den)

t, y = ctrl.step_response(system)

plt.plot(t, y)
plt.title('Resposta ao Degrau')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
