#Maria Eduarda Moretto de Lima
#Leticia Batista Rocha

import random
import time

#***********************************Criação dos vetores****************************************
def criar_vetor_aleatorio(vetor_ordenado):
    vetor_aleatorio = vetor_ordenado[:]
    random.shuffle(vetor_aleatorio)
    return vetor_aleatorio

def criar_vetor_reverso(inc, fim, stp):
    return list(range(fim, inc - 1, -stp))

def criar_vetor_ordenado(inc, fim, stp):
    return list(range(inc, fim + 1, stp))

def criar_vetor_parcialmente_ordenado(vetor_ordenado, percentual_desordem):
    if percentual_desordem <= 0 or percentual_desordem > 100:
        raise ValueError("O percentual de desordem deve estar entre 0 e 100.")
    
    num_elementos = len(vetor_ordenado)
    num_elementos_desordenar = int(num_elementos * percentual_desordem / 100)
    
    if num_elementos_desordenar == 0:
        return vetor_ordenado.copy()
    
    novo_vetor = vetor_ordenado.copy()
    indices_desordenar = random.sample(range(num_elementos), num_elementos_desordenar)
    
    # Desordenar os elementos selecionados
    valores_desordenados = [novo_vetor[i] for i in indices_desordenar]
    random.shuffle(valores_desordenados)
    
    # Inserir de volta os valores desordenados nos índices originais
    for i, indice in enumerate(indices_desordenar):
        novo_vetor[indice] = valores_desordenados[i]
    
    return novo_vetor

#***********************************Algoritimos de ordenação***********************************
def bubble_sort(vetor):
    result = vetor.copy()
    n = len(result)
    for i in range(n):
        for j in range(0, n-i-1):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
    return result

def insertion_sort(vetor):
    result = vetor.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and key < result[j]:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result
def merge_sort(vetor):
    if len(vetor) <= 1:
        return vetor
    mid = len(vetor) // 2
    left_half = merge_sort(vetor[:mid])
    right_half = merge_sort(vetor[mid:])
    return merge(left_half, right_half)


def heapify(result, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and result[left] > result[largest]:
        largest = left
    if right < n and result[right] > result[largest]:
        largest = right
    if largest != i:
        result[i], result[largest] = result[largest], result[i]
        heapify(result, n, largest)

def heap_sort(vetor):
    result = vetor.copy()
    n = len(result)
    for i in range(n // 2 - 1, -1, -1):
        heapify(result, n, i)
    for i in range(n - 1, 0, -1):
        result[i], result[0] = result[0], result[i]
        heapify(result, i, 0)
    return result

def quick_sort(vetor):
    if len(vetor) <= 1:
        return vetor
    pivot = vetor[len(vetor) // 2]
    left = [x for x in vetor if x < pivot]
    middle = [x for x in vetor if x == pivot]
    right = [x for x in vetor if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def counting_sort(arr):
    if len(arr) == 0:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    
    count = [0] * (max_val - min_val + 1)
    output = [0] * len(arr)

    for i in range(len(arr)):
        count[arr[i] - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]
    
    return arr

#***********************************************************************************************
# Função para calcular a média dos tempos
def calcular_media(lista):
    return sum(lista) / len(lista) if lista else 0

# Leitura dos parâmetros de entrada
inc = int(input("Vetor inicial: "))
fim = int(input('Vetor final: '))
stp = int(input('Digite o intervalo entre os valores: '))
rpt = int(input('Digite o número de vezes que o teste RANDOM deve se repetir: '))

#*******************************Inicializando listas de tempo**********************************
vet_tamanhos = []
vet_tempo_bubblesort_aleatorio = []
vet_tempo_bubblesort_reverso = []
vet_tempo_bubblesort_ordenado = []
vet_tempo_bubblesort_quase_ordenado = []

vet_tempo_insertions_aleatorio = []
vet_tempo_insertions_reverso = []
vet_tempo_insertions_ordenado = []
vet_tempo_insertions_quase_ordenado = []

vet_tempo_mergesorts_aleatorio = []
vet_tempo_mergesorts_reverso = []
vet_tempo_mergesorts_ordenado = []
vet_tempo_mergesorts_quase_ordenado = []

vet_tempo_heapsorts_aleatorio = []
vet_tempo_heapsorts_reverso = []
vet_tempo_heapsorts_ordenado = []
vet_tempo_heapsorts_quase_ordenado = []

vet_tempo_quicksorts_aleatorio = []
vet_tempo_quicksorts_reverso = []
vet_tempo_quicksorts_ordenado = []
vet_tempo_quicksorts_quase_ordenado = []

vet_tempo_countingsorts_aleatorio = []
vet_tempo_countingsorts_reverso = []
vet_tempo_countingsorts_ordenado = []
vet_tempo_countingsorts_quase_ordenado = []

media_bubblesort_aleatorio = []
media_insertion_aleatorio = []
media_merge_aleatorio = []
media_heap_aleatorio = []
media_quick_aleatorio = []
media_counting_aleatorio = []

#**************************************Main Loop***********************************************
while inc <= fim:
    vet_tamanhos.append(inc)
    vetor_ordenado = criar_vetor_ordenado(inc, fim, stp)
    vetor_reverso = criar_vetor_reverso(inc, fim, stp)
    vetor_quase_ordenado = criar_vetor_parcialmente_ordenado(vetor_ordenado, 10)  

    # Repetição para vetor aleatório
    for _ in range(rpt):
        vetor_aleatorio = criar_vetor_aleatorio(vetor_ordenado)
        
        # Insertionsort
        inicio_tmp = time.time()
        insertion_sort(vetor_aleatorio)
        fim_tmp = time.time()
        tempo_vetor_aleatorio_insertion = fim_tmp - inicio_tmp
        vet_tempo_insertions_aleatorio.append(tempo_vetor_aleatorio_insertion)
        
        # Bubblesort
        inicio_tmp = time.time()
        bubble_sort(vetor_aleatorio)
        fim_tmp = time.time()
        tempo_vetor_aleatorio_bubble = fim_tmp - inicio_tmp
        vet_tempo_bubblesort_aleatorio.append(tempo_vetor_aleatorio_bubble)
        
        # Mergesort
        inicio_tmp = time.time()
        merge_sort(vetor_aleatorio)
        fim_tmp = time.time()
        tempo_vetor_aleatorio_mergesort = fim_tmp - inicio_tmp
        vet_tempo_mergesorts_aleatorio.append(tempo_vetor_aleatorio_mergesort)

        # Heapsort
        inicio_tmp = time.time()
        heap_sort(vetor_aleatorio)
        fim_tmp = time.time()
        tempo_vetor_aleatorio_heapsort = fim_tmp - inicio_tmp
        vet_tempo_heapsorts_aleatorio.append(tempo_vetor_aleatorio_heapsort)
        
        # Quicksort
        inicio_tmp = time.time()
        quick_sort(vetor_aleatorio)
        fim_tmp = time.time()
        tempo_vetor_aleatorio_quicksort = fim_tmp - inicio_tmp
        vet_tempo_quicksorts_aleatorio.append(tempo_vetor_aleatorio_quicksort)

        # Countingsort
        inicio_tmp = time.time()
        counting_sort(vetor_aleatorio)
        fim_tmp = time.time()
        tempo_vetor_aleatorio_countingsort = fim_tmp - inicio_tmp
        vet_tempo_countingsorts_aleatorio.append(tempo_vetor_aleatorio_countingsort)

    # Executando uma vez para os outros vetores
    # =============================== Insertionsort ===============================
    # Reverso
    inicio_tmp = time.time()
    insertion_sort(vetor_reverso)
    fim_tmp = time.time()
    tempo_vetor_reverso_insertion = fim_tmp - inicio_tmp
    vet_tempo_insertions_reverso.append(tempo_vetor_reverso_insertion)
    
    # Ordenado
    inicio_tmp = time.time()
    insertion_sort(vetor_ordenado)
    fim_tmp = time.time()
    tempo_vetor_ordenado_insertion = fim_tmp - inicio_tmp
    vet_tempo_insertions_ordenado.append(tempo_vetor_ordenado_insertion)
    
    # Quase Ordenado
    inicio_tmp = time.time()
    insertion_sort(vetor_quase_ordenado)
    fim_tmp = time.time()
    tempo_vetor_quase_ordenado_insertion = fim_tmp - inicio_tmp
    vet_tempo_insertions_quase_ordenado.append(tempo_vetor_quase_ordenado_insertion)

    # =============================== Bubblesort ===============================
    # Reverso
    inicio_tmp = time.time()
    bubble_sort(vetor_reverso)
    fim_tmp = time.time()
    tempo_vetor_reverso_bubblesort = fim_tmp - inicio_tmp
    vet_tempo_bubblesort_reverso.append(tempo_vetor_reverso_bubblesort)

    # Ordenado
    inicio_tmp = time.time()
    bubble_sort(vetor_ordenado)
    fim_tmp = time.time()
    tempo_vetor_ordenado_bubblesort = fim_tmp - inicio_tmp
    vet_tempo_bubblesort_ordenado.append(tempo_vetor_ordenado_bubblesort)
    
    # Quase Ordenado
    inicio_tmp = time.time()
    bubble_sort(vetor_quase_ordenado)
    fim_tmp = time.time()
    tempo_vetor_quase_ordenado_bubblesort = fim_tmp - inicio_tmp
    vet_tempo_bubblesort_quase_ordenado.append(tempo_vetor_quase_ordenado_bubblesort)
    
    # =============================== Mergesort ===============================
    # Reverso
    inicio_tmp = time.time()
    merge_sort(vetor_reverso)
    fim_tmp = time.time()
    tempo_vetor_reverso_mergesort = fim_tmp - inicio_tmp
    vet_tempo_mergesorts_reverso.append(tempo_vetor_reverso_mergesort)
    
    # Ordenado
    inicio_tmp = time.time()
    merge_sort(vetor_ordenado)
    fim_tmp = time.time()
    tempo_vetor_ordenado_mergesort = fim_tmp - inicio_tmp
    vet_tempo_mergesorts_ordenado.append(tempo_vetor_ordenado_mergesort)

    # Quase Ordenado
    inicio_tmp = time.time()
    merge_sort(vetor_quase_ordenado)
    fim_tmp = time.time()
    tempo_vetor_quase_ordenado_mergesort = fim_tmp - inicio_tmp
    vet_tempo_mergesorts_quase_ordenado.append(tempo_vetor_quase_ordenado_mergesort)

    # =============================== Heapsort =============================== 
    # Reverso
    inicio_tmp = time.time()
    heap_sort(vetor_reverso)
    fim_tmp = time.time()
    tempo_vetor_reverso_heapsort = fim_tmp - inicio_tmp
    vet_tempo_heapsorts_reverso.append(tempo_vetor_reverso_heapsort)
        
    # Ordenado
    inicio_tmp = time.time()
    heap_sort(vetor_ordenado)
    fim_tmp = time.time()
    tempo_vetor_ordenado_heapsort = fim_tmp - inicio_tmp
    vet_tempo_heapsorts_ordenado.append(tempo_vetor_ordenado_heapsort)

    # Quase Ordenado
    inicio_tmp = time.time()
    heap_sort(vetor_quase_ordenado)
    fim_tmp = time.time()
    tempo_vetor_quase_ordenado_heapsort = fim_tmp - inicio_tmp
    vet_tempo_heapsorts_quase_ordenado.append(tempo_vetor_quase_ordenado_heapsort)

    # =============================== Quicksort ===============================
    # Reverso
    inicio_tmp = time.time()
    quick_sort(vetor_reverso)
    fim_tmp = time.time()
    tempo_vetor_reverso_quicksort = fim_tmp - inicio_tmp
    vet_tempo_quicksorts_reverso.append(tempo_vetor_reverso_quicksort)

    # Ordenado
    inicio_tmp = time.time()
    quick_sort(vetor_ordenado)
    fim_tmp = time.time()
    tempo_vetor_ordenado_quicksort = fim_tmp - inicio_tmp
    vet_tempo_quicksorts_ordenado.append(tempo_vetor_ordenado_quicksort)

    # Quase Ordenado
    inicio_tmp = time.time()
    quick_sort(vetor_quase_ordenado)
    fim_tmp = time.time()
    tempo_vetor_quase_ordenado_quicksort = fim_tmp - inicio_tmp
    vet_tempo_quicksorts_quase_ordenado.append(tempo_vetor_quase_ordenado_quicksort)

    # =============================== Countingsort ===============================
    # Reverso
    inicio_tmp = time.time()
    counting_sort(vetor_reverso)
    fim_tmp = time.time()
    tempo_vetor_reverso_countingsort = fim_tmp - inicio_tmp
    vet_tempo_countingsorts_reverso.append(tempo_vetor_reverso_countingsort)

    # Ordenado
    inicio_tmp = time.time()
    counting_sort(vetor_ordenado)
    fim_tmp = time.time()
    tempo_vetor_ordenado_countingsort = fim_tmp - inicio_tmp
    vet_tempo_countingsorts_ordenado.append(tempo_vetor_ordenado_countingsort)

    # Quase Ordenado
    inicio_tmp = time.time()
    counting_sort(vetor_quase_ordenado)
    fim_tmp = time.time()
    tempo_vetor_quase_ordenado_countingsort = fim_tmp - inicio_tmp
    vet_tempo_countingsorts_quase_ordenado.append(tempo_vetor_quase_ordenado_countingsort)
    
    # Cálculo das médias
    media_bubblesort_aleatorio.append(calcular_media(vet_tempo_bubblesort_aleatorio))
    media_insertion_aleatorio.append(calcular_media(vet_tempo_insertions_aleatorio))
    media_merge_aleatorio.append(calcular_media(vet_tempo_mergesorts_aleatorio))
    media_heap_aleatorio.append(calcular_media(vet_tempo_heapsorts_aleatorio))
    media_quick_aleatorio.append(calcular_media(vet_tempo_quicksorts_aleatorio))
    media_counting_aleatorio.append(calcular_media(vet_tempo_countingsorts_aleatorio))

    inc += stp



#***********************************Impressão dos Resultados**********************************
print()
print("[[RANDOM]]")
print("n   bubblesort   insertions   mergesorts   heapsorts   quicksorts   countingsorts")
print("-------------------------------------------------------------------------------")


for i in range(len(vet_tamanhos)):
    print("{:.0f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}".format(
    vet_tamanhos[i], 
    media_bubblesort_aleatorio[i], 
    media_insertion_aleatorio[i],
    media_merge_aleatorio[i],
    media_heap_aleatorio[i],
    media_quick_aleatorio[i],
    media_counting_aleatorio[i],
    ))

print()
print("[[REVERSE]]")
print("n   bubblesort   insertions   mergesorts   heapsorts   quicksorts   countingsorts")
print("-------------------------------------------------------------------------------")
for i in range(len(vet_tamanhos)):
    print("{:.0f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}".format(
        vet_tamanhos[i], 
        vet_tempo_bubblesort_reverso[i], 
        vet_tempo_insertions_reverso[i], 
        vet_tempo_mergesorts_reverso[i], 
        vet_tempo_heapsorts_reverso[i], 
        vet_tempo_quicksorts_reverso[i], 
        vet_tempo_countingsorts_reverso[i],
    ))

print()
print("[[SORTED]]")
print("n   bubblesort   insertions   mergesorts   heapsorts   quicksorts   countingsorts")
print("-------------------------------------------------------------------------------")
for i in range(len(vet_tamanhos)):
    print("{:.0f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}".format(
        vet_tamanhos[i], 
        vet_tempo_bubblesort_ordenado[i], 
        vet_tempo_insertions_ordenado[i], 
        vet_tempo_mergesorts_ordenado[i], 
        vet_tempo_heapsorts_ordenado[i], 
        vet_tempo_quicksorts_ordenado[i], 
        vet_tempo_countingsorts_ordenado[i],
    ))

print()
print("[[NEARLY SORTED]]")
print("n   bubblesort   insertions   mergesorts   heapsorts   quicksorts   countingsorts")
print("-------------------------------------------------------------------------------")
for i in range(len(vet_tamanhos)):
    print("{:.0f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}".format(
        vet_tamanhos[i], 
        vet_tempo_bubblesort_quase_ordenado[i], 
        vet_tempo_insertions_quase_ordenado[i], 
        vet_tempo_mergesorts_quase_ordenado[i], 
        vet_tempo_heapsorts_quase_ordenado[i], 
        vet_tempo_quicksorts_quase_ordenado[i], 
        vet_tempo_countingsorts_quase_ordenado[i],
    ))