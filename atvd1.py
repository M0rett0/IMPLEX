#Maria Eduarda Moretto de Lima
#Leticia Batista Rocha

import random
import time

#criação dos vetores
def criar_vetor_aleatorio(vetor_ordenado):
    vetor_aleatorio = vetor_ordenado[:]
    tam_desordem = int(len(vetor_ordenado))
    indices_desordenados = random.sample(range(len(vetor_ordenado)), tam_desordem)
    numeros_usados = set()
    for idx in indices_desordenados:
        numero_escolhido = random.choice(vetor_ordenado)
        while numero_escolhido in numeros_usados:
            numero_escolhido = random.choice(vetor_ordenado)
        
        numeros_usados.add(numero_escolhido)
        vetor_aleatorio[idx] = numero_escolhido 
    return vetor_aleatorio

def criar_vetor_reverso(inc, fim, stp):
    return list(range(fim, inc - 1, -stp))

def criar_vetor_ordenado(inc, fim, stp):
    vetor_ordenado = [inc]
    valor_atual = inc
    
    while valor_atual + stp <= fim:
        valor_atual += stp
        vetor_ordenado.append(valor_atual)
    return vetor_ordenado

def criar_vetor_parcialmente_ordenado(vetor_ordenado, percentual_desordem):
    if percentual_desordem <= 0 or percentual_desordem > 100:
        raise ValueError("O percentual de desordem deve estar entre 0 e 100.")
    num_elementos = len(vetor_ordenado)
    num_elementos_desordenar = int(num_elementos * percentual_desordem / 100)
    novo_vetor = vetor_ordenado.copy()
    while True:
        indices_desordenar = random.sample(range(num_elementos), num_elementos_desordenar)
        indices_desordenar.sort()
        valores_desordenados = [novo_vetor.pop(i) for i in reversed(indices_desordenar)]
        random.shuffle(valores_desordenados)
        for i, indice in enumerate(indices_desordenar):
            novo_vetor.insert(indice, valores_desordenados[i])
        if novo_vetor != sorted(vetor_ordenado):
            break
    return novo_vetor

#bubblesort
def bubble_sort(vetor):
    result = vetor.copy()
    n = len(vetor)
    for i in range(n):
        for j in range(0, n-i-1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
    return result

#insertionsort
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

#mergesort
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
    result = vetor.copy()
    if len(result) <= 1:
        return result
    mid = len(result) // 2
    left_half = result[:mid]
    right_half = result[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)

#heapsort
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

#quicksort
def quick_sort(vetor):
    result = vetor.copy()
    if len(result) <= 1:
        return result
    else:
        pivot = result[len(result) // 2]
        left = [x for x in result if x < pivot]
        middle = [x for x in result if x == pivot]
        right = [x for x in result if x > pivot]
        
        return quick_sort(left) + middle + quick_sort(right)

#countingsort
def counting_sort(vetor):
    aux = vetor.copy()
    max_val = max(aux)
    count = [0] * (max_val + 1)
    result = [0] * len(aux)
    
    for num in aux:
        count[num] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    for num in aux:
        result[count[num] - 1] = num
        count[num] -= 1
    
    return result

print ('O valor inicial do teste será 0')
inc = 0
fim = int(input('Digite o valor final do teste: '))
stp = int(input('Digite o intervalo entres os valores: '))
rpt = int(input('Digite o número de vezes que o teste deve se repetir: '))

#===============================inicializando vetores de tempo===============================
#bubblesort
vet_tempo_bubblesort_aleatorio = []
vet_tempo_bubblesort_reverso = []
vet_tempo_bubblesort_ordenado = []
vet_tempo_bubblesort_quase_ordenado = []

#insertionsort
vet_tempo_insertions_aleatorio = []
vet_tempo_insertions_reverso = []
vet_tempo_insertions_ordenado = []
vet_tempo_insertions_quase_ordenado = []

#mergesort
vet_tempo_mergesorts_aleatorio = []
vet_tempo_mergesorts_reverso = []
vet_tempo_mergesorts_ordenado = []
vet_tempo_mergesorts_quase_ordenado = []

#heapsort
vet_tempo_heapsorts_aleatorio = []
vet_tempo_heapsorts_reverso = []
vet_tempo_heapsorts_ordenado = []
vet_tempo_heapsorts_quase_ordenado = []

#quicksort
vet_tempo_quicksorts_aleatorio = []
vet_tempo_quicksorts_reverso = []
vet_tempo_quicksorts_ordenado = []
vet_tempo_quicksorts_quase_ordenado = []

#countingsort
vet_tempo_countingsorts_aleatorio = []
vet_tempo_countingsorts_reverso = []
vet_tempo_countingsorts_ordenado = []
vet_tempo_countingsorts_quase_ordenado = []

#chamando vetores para cada algoritimo de ordenação
vet_tamanhos = []
for i in range(rpt):
    vet_tamanhos.append(fim)
    vetor_ordenado = criar_vetor_ordenado(inc, fim, stp)
    vetor_aleatorio = criar_vetor_aleatorio(vetor_ordenado)
    vetor_reverso = criar_vetor_reverso(inc, fim, stp)
    vetor_quase_ordenado = criar_vetor_parcialmente_ordenado(vetor_ordenado, 30)  

    #=================================insertions========================================
    #aleatorio
    inicio_tmp = time.time()
    result_vetor_aleatorio_insertion = insertion_sort(vetor_aleatorio)
    fim_tmp = time.time()
    tempo_vetor_aleatorio_insertion = fim_tmp - inicio_tmp
    vet_tempo_insertions_aleatorio.append(tempo_vetor_aleatorio_insertion)

    #reverso
    inicio_tmp = time.time()
    result_vetor_reverso_insertion = insertion_sort(vetor_reverso)
    fim_tmp = time.time()
    tempo_vetor_reverso_insertion = fim_tmp - inicio_tmp
    vet_tempo_insertions_reverso.append(tempo_vetor_reverso_insertion)

    #ordenado
    inicio_tmp = time.time()
    result_vetor_ordenado_insertion = insertion_sort(vetor_ordenado)
    fim_tmp = time.time()
    tempo_vetor_ordenado_insertion = fim_tmp - inicio_tmp
    vet_tempo_insertions_ordenado.append(tempo_vetor_ordenado_insertion)

    #quase ordenado
    inicio_tmp = time.time()
    result_vetor_quase_ordenado_insertion = insertion_sort(vetor_quase_ordenado)
    fim_tmp = time.time()
    tempo_vetor_quase_ordenado_insertion = fim_tmp - inicio_tmp
    vet_tempo_insertions_quase_ordenado.append(tempo_vetor_quase_ordenado_insertion)
    
    #==================================bubblesort=======================================
    #aleatorio
    inicio_tmp = time.time()
    result_vetor_aleatorio_bubblesort = bubble_sort(vetor_aleatorio)
    fim_tmp = time.time()
    tempo_vetor_aleatorio_bubble = fim_tmp - inicio_tmp
    vet_tempo_bubblesort_aleatorio.append(tempo_vetor_aleatorio_bubble)

    #reverso
    inicio_tmp = time.time()
    result_vetor_reverso_selection = bubble_sort(vetor_reverso)
    fim_tmp = time.time()
    tempo_vetor_reverso_selection = fim_tmp - inicio_tmp
    vet_tempo_bubblesort_reverso.append(tempo_vetor_reverso_selection)

    #ordenado
    inicio_tmp = time.time()
    result_vetor_ordenado_bubblesort= bubble_sort(vetor_ordenado)
    fim_tmp = time.time()
    tempo_vetor_ordenado_bubble = fim_tmp - inicio_tmp
    vet_tempo_bubblesort_ordenado.append(tempo_vetor_ordenado_bubble)

    #quase ordenado
    inicio_tmp = time.time()
    result_vetor_quase_ordenado_selection = bubble_sort(vetor_quase_ordenado)
    fim_tmp = time.time()
    tempo_vetor_quase_ordenado_selection = fim_tmp - inicio_tmp
    vet_tempo_bubblesort_quase_ordenado.append(tempo_vetor_quase_ordenado_selection)

    #================================mergesorts=========================================
    #aleatorio
    inicio_tmp = time.time()
    result_vetor_aleatorio_mergesort = merge_sort(vetor_aleatorio)
    fim_tmp = time.time()
    tempo_vetor_aleatorio_mergesort = fim_tmp - inicio_tmp
    vet_tempo_mergesorts_aleatorio.append(tempo_vetor_aleatorio_mergesort)

    #reverso
    inicio_tmp = time.time()
    result_vetor_reverso_mergesort = merge_sort(vetor_reverso)
    fim_tmp = time.time()
    tempo_vetor_reverso_mergesort = fim_tmp - inicio_tmp
    vet_tempo_mergesorts_reverso.append(tempo_vetor_reverso_mergesort)

    #ordenado
    inicio_tmp = time.time()
    result_vetor_ordenado_mergesort = merge_sort(vetor_ordenado)
    fim_tmp = time.time()
    tempo_vetor_ordenado_mergesort = fim_tmp - inicio_tmp
    vet_tempo_mergesorts_ordenado.append(tempo_vetor_ordenado_mergesort)

    #quase ordenado
    inicio_tmp = time.time()
    result_vetor_quase_ordenado_mergesort = merge_sort(vetor_quase_ordenado)
    fim_tmp = time.time()
    tempo_vetor_quase_ordenado_mergesort = fim_tmp - inicio_tmp
    vet_tempo_mergesorts_quase_ordenado.append(tempo_vetor_quase_ordenado_mergesort)

    #=================================heapsorts=========================================
    #aleatorio
    inicio_tmp = time.time()
    result_vetor_aleatorio_heapsort = heap_sort(vetor_aleatorio)
    fim_tmp = time.time()
    tempo_vetor_aleatorio_heapsort = fim_tmp - inicio_tmp
    vet_tempo_heapsorts_aleatorio.append(tempo_vetor_aleatorio_heapsort)

    #reverso
    inicio_tmp = time.time()
    result_vetor_reverso_heapsort = heap_sort(vetor_reverso)
    fim_tmp = time.time()
    tempo_vetor_reverso_heapsort = fim_tmp - inicio_tmp
    vet_tempo_heapsorts_reverso.append(tempo_vetor_reverso_heapsort)

    #ordenado
    inicio_tmp = time.time()
    result_vetor_ordenado_heapsort = heap_sort(vetor_ordenado)
    fim_tmp = time.time()
    tempo_vetor_ordenado_heapsort = fim_tmp - inicio_tmp
    vet_tempo_heapsorts_ordenado.append(tempo_vetor_ordenado_heapsort)

    #quase ordenado
    inicio_tmp = time.time()
    result_vetor_quase_ordenado_heapsort = heap_sort(vetor_quase_ordenado)
    fim_tmp = time.time()
    tempo_vetor_quase_ordenado_heapsort = fim_tmp - inicio_tmp
    vet_tempo_heapsorts_quase_ordenado.append(tempo_vetor_quase_ordenado_heapsort)

    #=================================quicksorts=========================================
    #aleatorio
    inicio_tmp = time.time()
    result_vetor_aleatorio_quicksort = quick_sort(vetor_aleatorio)
    fim_tmp = time.time()
    tempo_vetor_aleatorio_quicksort = fim_tmp - inicio_tmp
    vet_tempo_quicksorts_aleatorio.append(tempo_vetor_aleatorio_quicksort)

    #reverso
    inicio_tmp = time.time()
    result_vetor_reverso_quicksort = quick_sort(vetor_reverso)
    fim_tmp = time.time()
    tempo_vetor_reverso_quicksort = fim_tmp - inicio_tmp
    vet_tempo_quicksorts_reverso.append(tempo_vetor_reverso_quicksort)

    #ordenado
    inicio_tmp = time.time()
    result_vetor_ordenado_quicksort = quick_sort(vetor_ordenado)
    fim_tmp = time.time()
    tempo_vetor_ordenado_quicksort = fim_tmp - inicio_tmp
    vet_tempo_quicksorts_ordenado.append(tempo_vetor_ordenado_quicksort)

    #quase ordenado
    inicio_tmp = time.time()
    result_vetor_quase_ordenado_quicksort = quick_sort(vetor_quase_ordenado)
    fim_tmp = time.time()
    tempo_vetor_quase_ordenado_quicksort = fim_tmp - inicio_tmp
    vet_tempo_quicksorts_quase_ordenado.append(tempo_vetor_quase_ordenado_quicksort)

    #=================================countingsorts======================================
    #aleatorio
    inicio_tmp = time.time()
    result_vetor_aleatorio_countingsort = counting_sort(vetor_aleatorio)
    fim_tmp = time.time()
    tempo_vetor_aleatorio_countingsort = fim_tmp - inicio_tmp
    vet_tempo_countingsorts_aleatorio.append(tempo_vetor_aleatorio_countingsort)

    #reverso
    inicio_tmp = time.time()
    result_vetor_reverso_countingsort = counting_sort(vetor_reverso)
    fim_tmp = time.time()
    tempo_vetor_reverso_countingsort = fim_tmp - inicio_tmp
    vet_tempo_countingsorts_reverso.append(tempo_vetor_reverso_countingsort)

    #ordenado
    inicio_tmp = time.time()
    result_vetor_ordenado_countingsort = counting_sort(vetor_ordenado)
    fim_tmp = time.time()
    tempo_vetor_ordenado_countingsort = fim_tmp - inicio_tmp
    vet_tempo_countingsorts_ordenado.append(tempo_vetor_ordenado_countingsort)

    #quase ordenado
    inicio_tmp = time.time()
    result_vetor_quase_ordenado_countingsort = counting_sort(vetor_quase_ordenado)
    fim_tmp = time.time()
    tempo_vetor_quase_ordenado_countingsort = fim_tmp - inicio_tmp
    vet_tempo_countingsorts_quase_ordenado.append(tempo_vetor_quase_ordenado_countingsort)

    #incrementa 5000 no valor para testes seguintes
    fim = fim + 1000

#saidas
print()
print("[[RANDOM]]")
print("n   insertions   bubblesort   mergesorts   heapsorts   quicksorts   countingsorts")
print("-------------------------------------------------------------------------------")
for i in range(rpt):
    print("{:.0f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}".format(
        vet_tamanhos[i], 
        vet_tempo_insertions_aleatorio[i], 
        vet_tempo_bubblesort_aleatorio[i], 
        vet_tempo_mergesorts_aleatorio[i], 
        vet_tempo_heapsorts_aleatorio[i], 
        vet_tempo_quicksorts_aleatorio[i], 
        vet_tempo_countingsorts_aleatorio[i]
    ))

print()
print("[[REVERSE]]")
print("n   insertions   bubblesort   mergesorts   heapsorts   quicksorts   countingsorts")
print("-------------------------------------------------------------------------------")
for i in range(rpt):
    print("{:.0f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}".format(
        vet_tamanhos[i], 
        vet_tempo_insertions_reverso[i], 
        vet_tempo_bubblesort_reverso[i], 
        vet_tempo_mergesorts_reverso[i], 
        vet_tempo_heapsorts_reverso[i], 
        vet_tempo_quicksorts_reverso[i], 
        vet_tempo_countingsorts_reverso[i]
    ))

print("[[SORTED]]")
print("n   insertions   bubblesort   mergesorts   heapsorts   quicksorts   countingsorts")
print("-------------------------------------------------------------------------------")
for i in range(rpt):
    print("{:.0f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}".format(
        vet_tamanhos[i], 
        vet_tempo_insertions_ordenado[i], 
        vet_tempo_bubblesort_ordenado[i], 
        vet_tempo_mergesorts_ordenado[i], 
        vet_tempo_heapsorts_ordenado[i], 
        vet_tempo_quicksorts_ordenado[i], 
        vet_tempo_countingsorts_ordenado[i]
    ))

print()
print("[[NEARLY SORTED]]")
print("n   insertions   bubblesort   mergesorts   heapsorts   quicksorts   countingsorts")
print("-------------------------------------------------------------------------------")
for i in range(rpt):
    print("{:.0f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}".format(
        vet_tamanhos[i], 
        vet_tempo_insertions_quase_ordenado[i], 
        vet_tempo_bubblesort_quase_ordenado[i], 
        vet_tempo_mergesorts_quase_ordenado[i], 
        vet_tempo_heapsorts_quase_ordenado[i], 
        vet_tempo_quicksorts_quase_ordenado[i], 
        vet_tempo_countingsorts_quase_ordenado[i]
    ))