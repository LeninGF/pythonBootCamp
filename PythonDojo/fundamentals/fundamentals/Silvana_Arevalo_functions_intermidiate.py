"""
    Funciones Intermedias
    Silvana Arevalo
"""

# datos a utilizar
x = [ [5,2,3], [10,8,9] ] 

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Actualizar valores diccionarios y listas
# 1. Cambia el valor 10 en x a 15
x[1][0] = 15
print(x)

# 2. Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)

# 3. En el directorio_deportes, cambia "Messi" por "Andrés"
directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)

# 4. Cambia el valor 20 en z a 30
z[0]['y'] = 30
print(z)

# 2. Iterar a traves de lista de diccionarios

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(lista_dicts):
    for dict_i in lista_dicts:
        print(f"first_name - {dict_i['first_name']}, last_name - {dict_i['last_name']}") 

print(iterateDictionary(estudiantes))

# 3. Obtener valores de una lista de diccionarios

def iterateDictionary2(key_name, some_list):
    for dict_i in some_list:
        print(dict_i[key_name])
    return 0
print(iterateDictionary2('first_name', estudiantes))
print(iterateDictionary2('last_name', estudiantes))

# 4. Iterar a través de un diccionarios con valores de lista
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(adictionary):
    for key in adictionary.keys():
        print(f"{key} de longitud {len(adictionary[key])}")
        for elem in adictionary[key]:
            print(elem)
            
print_info(dojo)
