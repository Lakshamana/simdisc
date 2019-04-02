import statistics as st

def k_quartil(data, k):
    cpy_data = sorted(data)
    if k == 1:
        return st.median(cpy_data[:len(cpy_data) // 2])
    elif k == 2:
        return st.median(cpy_data)
    elif k == 3:
        return st.median(cpy_data[len(cpy_data) // 2:])


dataset = [11 , 5 , 2 , 0 , 9 , 9 , 1 , 5 , 1 , 3 ,3 , 3 , 7 , 4 , 12 , 8 , 5 , 2 , 6 , 1 ,11 , 1 , 2 , 4 , 2 , 1 , 3 ,
           9 , 0 , 10 ,3 , 3 , 1 , 5 , 18 , 4 , 22 , 8 , 3 , 0 ,8 , 9 , 2 , 3 , 12 , 1 , 3 , 1 , 7 , 5 ,14 , 7 , 7 , 28,
           1 , 3 , 2 , 11 , 13 , 2 ,0 , 1 , 6 , 12 , 15 , 0 , 6 , 7 , 19 , 1 ,1 , 9 , 1 , 5 , 3 , 17 , 10 , 15 , 43 , 2 ,6 ,
           1 , 13 , 13 , 19 , 10 , 9 , 20 , 19 , 2 ,27 , 5 , 20 , 5 , 10 , 8 , 2 , 3 , 1 , 1 ,4 , 3 , 6 , 13 , 10 , 9 ,
           1 , 1 , 3 , 9 ,9 , 4 , 0 , 3 , 6 , 3 , 27 , 3 , 18 , 4 ,6 , 0 , 2 , 2 , 8 , 4 , 5 , 1 , 4 , 18 ,1 , 0 , 16 ,
           20 , 2 , 2 , 2 , 12 , 28 , 0 ,7 , 3 , 18 , 12 , 3 , 2 , 8 , 3 , 19 , 12 ,5 , 4 , 6 , 0 , 5 , 0 , 3 , 7 , 0 ,
           8 ,8 , 12 , 3 , 7 , 1 , 3 , 1 , 3 , 2 , 5 ,4 , 9 , 4 , 12 , 4 , 11 , 9 , 2 , 0 , 5 ,8 , 24 , 1 , 5 , 12 , 9 ,
           17 , 728 , 12 , 6 ,4 , 3 , 5 , 7 , 4 , 4 , 4 , 11 , 3 , 8]

print('Medidas de Centralidade:')
print(f"Média: {st.mean(dataset)}")
print(f"Mediana: {st.median(dataset)}")
print(f"Moda: {st.mode(dataset)}")

print('Medidas de Variação:')
min = min(dataset)
max = max(dataset)
print(f"Mínimo: {min}")
print(f"Máximo: {max}")
print(f"Max - Min: {max - min}")
print(f"Desvio padrão: {round(st.stdev(dataset), 3)}")
print(f"Variância: {round(st.variance(dataset), 3)}")
print(f"Coeficiente de variação: {round(st.stdev(dataset) / st.mean(dataset) * 100, 3)}%")
print(f"Coeficiente de assimetria: {round(k_quartil(dataset, 3) , 3)}")
k = 1
print(f"q{k}: {k_quartil(dataset, k)}")
k = 3
print(f"q{k}: {k_quartil(dataset, k)}")
print(f"{k_quartil(dataset, 3) - k_quartil(dataset, 1)}")

