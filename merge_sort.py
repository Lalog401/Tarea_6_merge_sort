def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr

    mitad = len(arr) // 2
    izquierda = arr[:mitad]
    derecha = arr[mitad:]

    izquierda_ordenada = merge_sort(izquierda)
    derecha_ordenada = merge_sort(derecha)

    arr_fusionado = []
    i = 0
    j = 0

    while i < len(izquierda_ordenada) and j < len(derecha_ordenada):
        if izquierda_ordenada[i] < derecha_ordenada[j]:
            arr_fusionado.append(izquierda_ordenada[i])
            i += 1
        else:
            arr_fusionado.append(derecha_ordenada[j])
            j += 1

    arr_fusionado.extend(izquierda_ordenada[i:])
    arr_fusionado.extend(derecha_ordenada[j:])
        
    return arr_fusionado

#Pruebas 
lista_desordenada = [15,7,401,777,25,45,5]
print(f"Lista original: {lista_desordenada}")

lista_ordenada = merge_sort(lista_desordenada)
print(f"Lista ordenada: {lista_ordenada}")