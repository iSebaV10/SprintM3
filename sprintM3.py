import random
import string

#Creo mi lista de usuarios
usuarios = ["Usuario1", "Usuario2", "Usuario3", "Usuario4", "Usuario5", "Usuario6", "Usuario7", "Usuario8", "Usuario9", "Usuario10"]

#Funcion para generar password con los criterios señalados
def generar_pass():
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits

    # Combinamos los caracteres en una lista
    caracteres = letras_mayusculas + letras_minusculas + numeros

    # Elegimos al menos un carácter de cada tipo
    contraseña = random.choice(letras_mayusculas) + random.choice(letras_minusculas) + random.choice(numeros)

    # Generamos el resto de la contraseña aleatoriamente
    contraseña += ''.join(random.choice(caracteres) for _ in range(8))

    # Barajamos la contraseña para que no sea predecible
    contraseña_lista = list(contraseña)
    random.shuffle(contraseña_lista)
    contraseña = ''.join(contraseña_lista)

    return contraseña

#funcion para obtener numero telefonico
def obtener_numero_telefonico(usuario):
    while True:
        telefono = input(f"Ingrese el número telefónico para {usuario}: ")
        if telefono.isdigit() and len(telefono) == 8:
            return telefono
        print("El número telefónico debe tener 8 dígitos. Inténtelo nuevamente.")

#Se genera nueva lista para guardar los usuarios, pass y telefono
cuentas = {}

#Guardo pass y telefono en la lista cuenta
for usuario in usuarios:
    contraseña = generar_pass()
    telefono = obtener_numero_telefonico(usuario)
    cuenta = {
        "contraseña": contraseña,
        "telefono": telefono
    }
    cuentas[usuario] = cuenta

# Imprimir todas las cuentas y sus detalles
for usuario, detalles in cuentas.items():
    print()
    print(f"Usuario: {usuario}")
    print(f"Contraseña: {detalles['contraseña']}")
    print(f"Número telefónico: {detalles['telefono']}")
    print()

