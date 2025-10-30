# Ecuaciones-Diferenciales
## Explicación del Código:
**Ecuación diferencial seleccionada: Se usa dy/dt = -2y con condición inicial y(0) = 1**

## Solución analítica:
y(t) = e^(-2t)

## Método de Euler:
Se itera desde t=0 hasta t=1 con oasi h=0.2
En cada paso se calcula: y_{n+1} = y_n + h*(-2*y_n)

### Resultados:
Se muestra una tabla comparativa entre los valores de solución analítica(exacta) y los de Euler.
Se grafican ambas soluciones.
Se calculan los errores absolutos en cada punto.
