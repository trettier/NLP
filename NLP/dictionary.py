import json
import pandas as pd
from Tf_IDF import  Tf_IDF
from knn import compute_distance
data = open(r"sample.json", encoding='utf-8')
sample = json.load(data)
selection = []

# создадим список со списками слов по каждому предложению
for i in sample:
    selection.append(i["text"][:-1].split(" "))

# selection_dist = {"слово": "сколько раз встречается"}
selection_dist = {}
for i in selection:
    for j in i:
        if j not in selection_dist:
            selection_dist[j] = [1]
        else:
            selection_dist[j][0] += 1

words_count = len(selection_dist)
embedding = [0] * words_count

# selection_dist = {"слово": ["сколько раз встречается", "one-hot embedding"]}
for i in range(len(selection_dist)):
    embedding[i] += 1
    selection_dist[list(selection_dist)[i]].append(embedding)
    embedding[i] -= 1

# Создадим датафрейм, потому что с ним удобнее работать
df = pd.DataFrame(selection_dist, index=["count", "emb"]).transpose()

# Реализация метода Tf-IDF
words_count_rep = sum(df["count"])
words_count_not_rep = list(df['count'])


Tf_IDF_dist = Tf_IDF(selection, list(selection_dist), words_count_not_rep)
# Создание матрицы расстояний и поиск ближайших соседей
matrix = compute_distance(Tf_IDF_dist)


matrix_df = pd.DataFrame(matrix)
list_of_similar = []

for i in range(len(sample)):
    t = True
    for j in list_of_similar:
        if i in j:
            t = False

    if t:
        list_of_similar.append([i])
        distances = matrix_df[i].sort_values()

        for j in range(len(sample)):
            if i != j:
                if distances[j] <= 2:
                    list_of_similar[-1].append(j)

list_of_similar.sort(key=len, reverse=True)

for i in list_of_similar:
    for j in i:
        print(sample[j]["text"])
    print()

# Финальный ответ в list_of_similar
