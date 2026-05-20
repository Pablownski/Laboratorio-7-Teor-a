# Laboratorio 7 — Simulación Monte Carlo: Álbum Panini

Simulación del problema del coleccionista de cupones (*coupon collector problem*) aplicado al álbum Panini, usando Monte Carlo.

## Contenido

| Archivo | Descripción |
|---|---|
| `ej_completo.py` | Script Python completo con Etapa 1 y Etapa 2 |
| `Lab7 (1).ipynb` | Notebook Jupyter con las mismas simulaciones y análisis teórico |

## Requisitos

- Python 3.8 o superior
- NumPy
- Matplotlib
- Jupyter (solo para el notebook)

Instalar dependencias:

```bash
pip install numpy matplotlib jupyter
```

## Ejecutar el script Python

```bash
python ej_completo.py
```

El script imprime en consola los resultados de ambas etapas y muestra dos gráficos:

1. Histograma de la distribución del número de sobres necesarios para completar el álbum.
2. Gráfico de barras con la probabilidad de completar el álbum según la cantidad de sobres comprados.

## Ejecutar el Notebook

```bash
jupyter notebook "Lab7 (1).ipynb"
```

O con JupyterLab:

```bash
jupyter lab "Lab7 (1).ipynb"
```

Luego ejecutar todas las celdas con **Kernel → Restart & Run All**.

## Parámetros de la simulación

| Parámetro | Valor | Descripción |
|---|---|---|
| `N` | 100 | Total de estampas en el álbum |
| `S` | 7 | Estampas distintas por sobre |
| `R` | 10 000 | Número de simulaciones Monte Carlo |
| Semilla | 2026 | `np.random.seed(2026)` para reproducibilidad |

## Descripción de las etapas

### Etapa 1 — Simulación básica

Simula el proceso de llenar el álbum comprando sobres hasta completarlo. Calcula:

- Media y desviación estándar del número de sobres necesarios.
- Media y desviación estándar de estampas repetidas.
- `P(T > 30)`: probabilidad de necesitar más de 30 sobres.
- Mínimo teórico: `⌈N/S⌉ = 15` sobres.
- Valor esperado teórico con la fórmula del coleccionista: `E[T] ≈ (N/S) · H_N ≈ 74`.

### Etapa 2 — Probabilidad de completar con M sobres fijos

Para distintos valores de M `[20, 25, 30, 35, 40, 45, 50, 60, 70, 80]`, estima la probabilidad de completar el álbum comprando exactamente M sobres. También calcula una cota superior teórica usando la desigualdad de unión:

```
P(falta al menos una) ≤ N · e^(-M·S/N)
```

## Resultados esperados (semilla 2026)

```
Media de sobres:         72.25
Desviación estándar:     17.47
Media de repetidas:     405.72
Valor esperado teórico:  74.11

M = 70  -->  primera vez que supera 50%
Cota superior (M=50):    3.019738  (mayor que 1, no útil como probabilidad)
```
