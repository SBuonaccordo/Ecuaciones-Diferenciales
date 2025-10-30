import numpy as np
import matplotlib.pyplot as plt

# 1. Solución Analítica de una Ecuación Diferencial Separable
print("=== SOLUCIÓN ANALÍTICA ===")
# Ecuación: dy/dt = -2y, con condición inicial y(0) = 1
# Solución exacta: y(t) = e^(-2t)

def exact_solution(t):
    return np.exp(-2*t)

# 2. Método de Euler para Aproximación
print("\n=== MÉTODO DE EULER ===")
# Parámetros
t0 = 0.0      # Tiempo inicial
y0 = 1.0      # Condición inicial
h = 0.2       # Paso
n_steps = 5   # Número de pasos (para llegar a t=1.0)

# Definir la ecuación diferencial
def f(t, y):
    return -2*y

# Aplicar método de Euler
t_values = [t0]
y_values = [y0]
y_euler = y0

print("t \t Euler \t Exacta")
print(f"{t0:.1f}\t {y0:.4f}\t {exact_solution(t0):.4f}")

for i in range(n_steps):
    t = t_values[-1]
    y_euler = y_euler + h * f(t, y_euler)
    t_values.append(t + h)
    y_values.append(y_euler)
    exact_val = exact_solution(t + h)
    print(f"{t+h:.1f}\t {y_euler:.4f}\t {exact_val:.4f}")

# 3. Visualización
plt.figure(figsize=(10, 6))
t_continuous = np.linspace(0, 1, 100)
plt.plot(t_continuous, exact_solution(t_continuous), 'b-', label='Solución Exacta')
plt.plot(t_values, y_values, 'ro--', label='Método de Euler (h=0.2)')
plt.title('Comparación: Solución Exacta vs Método de Euler')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.show()

# 4. Cálculo del Error
print("\n=== ERRORES ===")
for i, (t, y_e) in enumerate(zip(t_values, y_values)):
    y_exact = exact_solution(t)
    error = abs(y_exact - y_e)
    print(f"t={t:.1f}: Error = {error:.6f}")