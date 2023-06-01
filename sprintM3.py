import random
import string

#Creo mi lista de usuarios
usuarios = ["Usuario1", "Usuario2", "Usuario3", "Usuario4", "Usuario5", "Usuario6", "Usuario7", "Usuario8", "Usuario9", "Usuario10"]

#Funcion para generar password con los criterios señalados
def generar_pass():
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits

    # Combinamos los caracteres arrojados anteriormente
    caracteres = mayusculas + minusculas + numeros

    # Elejo al menos 1 caracter de cada tipo de manera aleatoria
    contraseña = random.choice(mayusculas) + random.choice(minusculas) + random.choice(numeros)

    # Genero el resto de la contraseña de forma aleatoria 
    contraseña += ''.join(random.choice(caracteres) for _ in range(8))

    # Código para mezclar los caracteres y que no queden fijos ni sea predecible
    contraseña_lista = list(contraseña)
    random.shuffle(contraseña_lista)
    contraseña = ''.join(contraseña_lista)

    return contraseña

#funcion para obtener numero telefonico
def obtener_numero_telefonico(usuario):
    while True:
        telefono = input(f"Ingrese el número telefónico para {usuario}: ")
        #Verifico que lo que ingresa el usuario son digitos y que el largo sea igual a 8 caracteres
        if telefono.isdigit() and len(telefono) == 8:
            return telefono
        print("El número telefónico debe tener 8 dígitos. Inténtelo nuevamente.")

#Se genera un diccionario para guardar los usuarios, pass y telefono
cuentas = {}

#Guardo pass y telefono en la lista cuenta
for usuario in usuarios:
    #Se llama a la funcion para crear una contraseña
    contraseña = generar_pass()
    #Se llama a la función para obtener el numero telefonico del usuario
    telefono = obtener_numero_telefonico(usuario)
    #se añaden ambos a cuenta
    cuenta = {
        "contraseña": contraseña,
        "telefono": telefono
    }
    cuentas[usuario] = cuenta

''' Pruebas
print(f"lista de usuarios: {usuarios}")
print(f"Cuenta: {cuenta}")
print(f"Cuentas: {cuentas}")
'''


# Se imprimen todas las cuentas y sus detalles
for usuario, detalles in cuentas.items():
    print()
    print(f"Usuario: {usuario}")
    print(f"Contraseña: {detalles['contraseña']}")
    print(f"Número telefónico: {detalles['telefono']}")
    print()

