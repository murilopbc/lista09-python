import numpy as np

restaurante = np.array([[2, 3, 6],
                        [5, 4, 5],
                        [4, 3, 4]])

media_restaurante = np.mean(restaurante, axis=1)
indice = np.argmax(media_restaurante)
maior_media = media_restaurante[indice]

print(f"O melhor restaurante é o {indice + 1} com {maior_media:.2f} de média!")
