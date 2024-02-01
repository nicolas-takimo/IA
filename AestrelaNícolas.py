import numpy as np
import time 
from queue import PriorityQueue
from scipy.signal import convolve2d as conv2

class Estado:
    def __init__(self, pai=None, matriz=None):
        self.pai = pai
        self.matriz = matriz
        self.d = 0  # Tamanho do caminho do início ao estado
        self.c = 0  # Custo estimado do estado ao objetivo
        self.p = 0  # Prioridade (d + c)

    def __eq__(self, other):
        return np.array_equal(self.matriz, other.matriz)

    def __lt__(self, other):
        return self.p < other.p

    def mostrar(self):
        for linha in self.matriz:
            print(linha)
        print()

def acoes_permitidas(estado):
    adj = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    blank = estado.matriz == 9
    mask = conv2(blank, adj, 'same') == 1
    return estado.matriz[mask]

def movimentar(s, c):
    matriz = s.matriz.copy()
    idx_branco, idx_c = np.where(matriz == 9), np.where(matriz == c)
    matriz[idx_branco], matriz[idx_c] = matriz[idx_c], matriz[idx_branco]
    return Estado(pai=s, matriz=matriz)

def distancia_manhattan(estado, objetivo):
    distancia = 0
    for valor in range(1, 10):
        pos_atual = np.array(np.where(estado.matriz == valor))
        pos_objetivo = np.array(np.where(objetivo == valor))
        distancia += abs(pos_atual[0] - pos_objetivo[0]) + abs(pos_atual[1] - pos_objetivo[1])
    return distancia.sum()

def hamming(estado, objetivo):
    return np.sum((estado.matriz != objetivo) & (estado.matriz != 9))

def a_star(estado_inicial, objetivo, heuristica):
    Q = PriorityQueue()
    estado_inicial.c = heuristica(estado_inicial, objetivo)
    estado_inicial.p = estado_inicial.d + estado_inicial.c
    Q.put((estado_inicial.p, estado_inicial))

    iteracoes = 0  # Contador de iterações
    start_time = time.time()  # Tempo de início

    while not Q.empty():
        _, estado_atual = Q.get()
        iteracoes += 1  # Incrementa o contador a cada iteração

        if np.array_equal(estado_atual.matriz, objetivo):
            end_time = time.time()  # Tempo de término
            print(f"Número de iterações: {iteracoes}")
            print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
            return reconstruir_caminho(estado_atual)

        for acao in acoes_permitidas(estado_atual):
            novo_estado = movimentar(estado_atual, acao)
            novo_estado.c = heuristica(novo_estado, objetivo)
            novo_estado.d = estado_atual.d + 1
            novo_estado.p = novo_estado.d + novo_estado.c
            Q.put((novo_estado.p, novo_estado))

    end_time = time.time()  # Tempo de término
    print(f"Número de iterações: {iteracoes}")
    print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
    return None


def reconstruir_caminho(estado_atual):
    caminho = []
    while estado_atual is not None:
        caminho.append(estado_atual)
        estado_atual = estado_atual.pai
    return caminho[::-1]

def tem_solucao(matriz):
    arr = matriz.flatten()
    num_inversoes = sum(arr[i] > arr[j] for i in range(len(arr)) for j in range(i + 1, len(arr)) if arr[i] != 9 and arr[j] != 9)
    return num_inversoes % 2 == 0


# Configuração inicial e objetivo do quebra-cabeça
#estado_inicial = Estado(matriz=np.array([[4, 1, 3], [9, 2, 5], [7, 8, 6]]))
#estado_inicial = Estado(matriz=np.array([[9, 1, 3], [4, 2, 5], [7, 8, 6]]))
#estado_inicial = Estado(matriz=np.array([[4, 9, 5], [3, 8, 6], [7, 1, 2]]))
estado_inicial = Estado(matriz=np.array([[5, 3, 2], [7, 6, 4], [8, 1, 9]]))
#estado_inicial = Estado(matriz=np.array([[4, 6, 7], [9, 5, 8], [2, 1, 3]]))
objetivo = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

if tem_solucao(estado_inicial.matriz):
    # Escolha a heurística aqui: hamming ou distancia_manhattan
    caminho_solucao = a_star(estado_inicial, objetivo, hamming)  # hammig ou distancia_manhattan
    for estado in caminho_solucao:
        estado.mostrar()
else:
    print("Estado inicial sem solução.")
