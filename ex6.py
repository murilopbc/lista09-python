import numpy as np

avaliacoes_filmes = np.array([[7, 8, 10],
                              [7, 6, 9],
                              [9, 6, 8]])
medias_filmes = np.mean(avaliacoes_filmes, axis=0)
for i, media_filme in enumerate(medias_filmes):
    print(f"A média de avaliação do filme {i + 1} é {media_filme:.2f}")
