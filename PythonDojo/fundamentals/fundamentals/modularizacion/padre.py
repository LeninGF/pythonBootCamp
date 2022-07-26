def square(x):
    return x * x


class Usuario:
    def __init__(self, name):
        self.name = name
    def di_hola(self):
        return "hola"

# en el mismo archivo, agrega lo siguiente debajo de la clase Usuario

print(__name__)

if __name__ == "__main__":
    print("el archivo se esta ejecutando directamente")
    local_val = "unicornios mágicos"
    print(square(5))
    usuario = Usuario("Anna")
    print(usuario.name)
    print(usuario.di_hola())

else:
    print("el archivo se esta ejecutando importado desde otro. El archivo se llama:", __name__)