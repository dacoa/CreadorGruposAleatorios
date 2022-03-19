#Este va ser el mejor programa para organizar de forma aleatoria personas en distintos grupos

from random import shuffle

print("Bienvenido al Creador de Grupos Aleatorios :)")

# Lista de personas: Andrés Camayo, Camilo Camayo, Diana, Jhonny, Ximena, Jair, Josue, Yazmin, Juan Manuel, Juan David, Óscar, Andrés Caicedo, Jhonatan Sierra, Luz Adriana
# print(cantPersonas)
cantPersonas = ['Andrés Camayo', 'Camilo Camayo', 'Diana', 'Jhonny', 'Ximena', 'Jair', 'Josue', 'Yazmin', 'Juan Manuel', 'Juan David', 'Óscar', 'Andrés Caicedo', 'Jhonatan Sierra', 'Luz Adriana']

#Ingresa los nombres separados por comas ( , )
personas = input("> Ingresa los nombres separados por comas ( , ): ")

#Separar y almacenar en una lista 
if len(personas) < 1:
    personas = cantPersonas
else:
#Uso comprensión de lista https://docs.python.org/es/3/tutorial/datastructures.html#list-comprehensions
    personas = [x.strip() for x in personas.split(',')]
#Manera no simplificada 
# resultado = []
# for x in personas.split(','):
#     resultado.append(x.strip())

print(len(personas),'personas agregadas con éxito')
while True:
    cantGrupos = int(input('Ingrese la cantidad de grupos '))
    if len(personas)%cantGrupos !=0:
        print("Ingrese un número de grupos equitativo entre la cantidad de personas")
    else:
        break
print("===============================")

#Mezclo los items de la lista
shuffle(personas)

personasxGrupo = int(len(personas)/cantGrupos)

grupos = dict()

while cantGrupos > 0:
    grupos[cantGrupos] = personas[:personasxGrupo]
    del personas[:personasxGrupo]
    cantGrupos -=1
for grupo in sorted(grupos):
    print("Grupo %s: %s" % (grupo,grupos[grupo]))



