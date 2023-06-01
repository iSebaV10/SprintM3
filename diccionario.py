mi_agenda = {
    "Alicia" : 222,
    "Roberto" : 111,
    "Lucía" : 333,
    "Andrés" : 555
}

'''
#Forma de recorrer un diccionario donde clave hace referencia a la key
for clave in mi_agenda:
    print(clave , ": ", mi_agenda[clave])
'''

for clave, valor in mi_agenda.items():
    print(clave, ":", valor)
