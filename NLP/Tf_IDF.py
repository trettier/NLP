from math import log
# Метод
def Tf_IDF(docs, words, words_count_not_rep):
    words_count = len(words)
    tf_idf = {}
    x = 0
    for doc in docs:
        tf_idf[x] = [0] * words_count
        y = 0
        for word in words:
            if word in doc:
                tf_idf[x][y] = round(1 / len(doc) * (log(len(docs) / words_count_not_rep[y])), 3)
            y += 1
        x += 1
    return tf_idf
