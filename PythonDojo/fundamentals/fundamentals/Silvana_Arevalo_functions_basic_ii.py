"""
Funciones basicAS II
Silvana Arévalo

"""
# Cuenta regresiva
def countdown(number):
    output = []
    for i in range(number, -1, -1):
        output.append(i)
    return output

print(countdown(10))

# Imprimir y Devolver
def imprimier_devolver(lista):
    print(f"el primer valor es {lista[0]}") # imprime el primer valor
    return lista[1] # devuelve el segundo valor

print(imprimier_devolver([-10,2,5,6,7]))


# primero mas longitud:
def primero_mas_longitud(lista):
    return lista[0]+len(lista)

print(primero_mas_longitud([5,1,2,8,3]))


# mayores que segundo
#  cree una nueva que contenga solo los valores de la lista original que 
# sean mayores que su segundo valor. Imprime cuántos valores son y luego 
# devuelve la lista nueva. Si la lista tiene menos de 2 elementos, 
# has que la función devuelva False

def mayores_segundoval(lista):
    nueva_lista = []
    if len(lista) < 2:
        return False
    for val in lista:
        if val > lista[1]:
            nueva_lista.append(val)
    print(f"Existen {len(nueva_lista)} Valores mayores que {lista[1]}")
    return nueva_lista
    
print(mayores_segundoval([5,2,3,2,1,4]))
print(mayores_segundoval([3]))


# esta longitud
def length_and_value(tamanio, valor):
    return [valor for i in range(tamanio)]

print(length_and_value(4,7))
print(length_and_value(6,2))
