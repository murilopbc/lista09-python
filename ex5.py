import numpy as np

consumo_energia = np.array([[7, 8, 10, 8],
                            [5, 4, 5, 6],
                            [4, 5, 4, 9]])
consumo_total_casa = np.sum(consumo_energia, axis=1)
for i, consumo_total in enumerate(consumo_total_casa):
    print(f"O consumo total de energia da casa {i + 1} em KWh é {consumo_total} ")
