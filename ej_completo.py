# ============================================================
# LABORATORIO 7 - TEORÍA DE PROBABILIDADES
# Simulación Monte Carlo - Álbum Panini
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# ETAPA 1
# Simulación básica con álbum reducido
# ============================================================

# Parámetros
N = 100          # número total de estampas
S = 7            # estampas por sobre
R = 10000        # número de simulaciones

# Semilla
np.random.seed(2026)

# Arreglos para almacenar resultados
sobres_totales = []
repetidas_totales = []

# ============================================================
# SIMULACIÓN
# ============================================================

for _ in range(R):

    # álbum vacío
    album = np.zeros(N, dtype=bool)

    sobres = 0
    repetidas = 0
    distintas = 0

    # continuar hasta completar álbum
    while distintas < N:

        # generar sobre
        sobre = np.random.choice(
            N,
            size=S,
            replace=False
        )

        sobres += 1

        # revisar estampas del sobre
        for estampa in sobre:

            if album[estampa]:
                repetidas += 1
            else:
                album[estampa] = True
                distintas += 1

    sobres_totales.append(sobres)
    repetidas_totales.append(repetidas)

# ============================================================
# CONVERTIR A NUMPY
# ============================================================

sobres_totales = np.array(sobres_totales)
repetidas_totales = np.array(repetidas_totales)

# ============================================================
# ESTADÍSTICAS
# ============================================================

media_sobres = np.mean(sobres_totales)
std_sobres = np.std(sobres_totales)

media_repetidas = np.mean(repetidas_totales)
std_repetidas = np.std(repetidas_totales)

prob_mas_30 = np.mean(sobres_totales > 30)

print("================================================")
print("RESULTADOS ETAPA 1")
print("================================================\n")

print(f"Media de sobres: {media_sobres:.4f}")
print(f"Desviación estándar sobres: {std_sobres:.4f}\n")

print(f"Media de repetidas: {media_repetidas:.4f}")
print(f"Desviación estándar repetidas: {std_repetidas:.4f}\n")

print(f"P(T > 30): {prob_mas_30:.4f}\n")

# ============================================================
# MÍNIMO TEÓRICO
# ============================================================

minimo_teorico = np.ceil(N / S)

print(f"Mínimo teórico de sobres: {minimo_teorico}")

# ============================================================
# TEORÍA DEL COLECCIONISTA
# ============================================================

# Número armónico
H_N = np.sum(1 / np.arange(1, N + 1))

# Valor esperado teórico
E_teorico = (N / S) * H_N

print(f"H_{N} = {H_N:.6f}")
print(f"Valor esperado teórico = {E_teorico:.4f}")

# ============================================================
# HISTOGRAMA
# ============================================================

plt.figure(figsize=(10,6))

plt.hist(
    sobres_totales,
    bins=25
)

plt.axvline(
    media_sobres,
    linestyle='--',
    linewidth=2,
    label='Media muestral'
)

plt.axvline(
    minimo_teorico,
    linestyle='--',
    linewidth=2,
    label='Mínimo teórico'
)

plt.xlabel("Número de sobres")
plt.ylabel("Frecuencia")
plt.title("Distribución del número de sobres necesarios")

plt.legend()

plt.show()

# ============================================================
# PREGUNTAS DE ANÁLISIS
# ============================================================

print("\n================================================")
print("PREGUNTAS DE ANÁLISIS")
print("================================================\n")

# Pregunta 1
print("1. Número mínimo teórico de sobres:")
print(f"ceil(100/7) = {minimo_teorico}\n")

# Pregunta 2
print("2. Valor esperado teórico:")
print(f"E[T] ≈ {E_teorico:.4f}")
print(f"Media simulada ≈ {media_sobres:.4f}\n")

# Pregunta 3
estampas_totales = media_sobres * S
repetidas_teoricas = estampas_totales - N

print("3. Estampas repetidas esperadas:")
print(f"{media_sobres:.2f} * 7 - 100 ≈ {repetidas_teoricas:.2f}\n")

# Pregunta 4
print("4. Interpretación:")
print("La desviación estándar es relativamente grande")
print("porque conseguir las últimas estampas puede")
print("tomar muchos sobres adicionales.\n")

# ============================================================
# ETAPA 2
# Probabilidad de completar el álbum
# ============================================================

print("================================================")
print("RESULTADOS ETAPA 2")
print("================================================\n")

M_values = [20, 25, 30, 35, 40, 45, 50, 60, 70, 80]

probabilidades = []

for M in M_values:

    exitos = 0

    for _ in range(R):

        album = np.zeros(N, dtype=bool)

        for _ in range(M):

            sobre = np.random.choice(
                N,
                size=S,
                replace=False
            )

            album[sobre] = True

        if np.all(album):
            exitos += 1

    prob = exitos / R

    probabilidades.append(prob)

    print(f"M = {M:2d} --> P(completar) = {prob:.4f}")

# ============================================================
# GRÁFICA DE PROBABILIDADES
# ============================================================

plt.figure(figsize=(10,6))

plt.bar(
    M_values,
    probabilidades
)

plt.axhline(
    0.5,
    linestyle='--',
    linewidth=2,
    label='50%'
)

plt.xlabel("Número de sobres")
plt.ylabel("Probabilidad estimada")
plt.title("Probabilidad de completar el álbum")

plt.legend()

plt.show()

# ============================================================
# SUPERA 50% Y 90%
# ============================================================

print("\n================================================")
print("ANÁLISIS DE PROBABILIDADES")
print("================================================\n")

for M, p in zip(M_values, probabilidades):

    if p >= 0.5:
        print(f"Primera vez que supera 50%: M = {M}")
        break

for M, p in zip(M_values, probabilidades):

    if p >= 0.9:
        print(f"Primera vez que supera 90%: M = {M}")
        break

# ============================================================
# COTA SUPERIOR
# ============================================================

print("\n================================================")
print("COTA SUPERIOR")
print("================================================\n")

M = 50

cota = N * np.exp(-(M * S) / N)

print(f"Cota superior para M = 50: {cota:.6f}")

if cota > 1:
    print("La cota no es útil porque excede 1.")
else:
    print("La cota es válida y útil.")