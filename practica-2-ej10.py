import math

nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David', 'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge', 'JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''.replace(',','').replace("'",'').lower().title()

nombres = nombres.split()


notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

def generar_nueva_estructura(nombres, notas1, notas2):  #A GENERA LA NUEVA ESTRUCTURA CON NOMBRES Y LAS DOS NOTAS
    return zip(nombres,notas1,notas2)

def promedio_estudiante(alumnos,nombres):                       #B GENERA DICCIONARIO ,CLAVE:NOMBRE Y VALOR:PROMEDIO
  promedio = list(map(lambda x: (x[1]+ x[2]) /2 ,alumnos))
  return dict(zip(nombres,promedio))

def promedio_general(promedios):                         #C
    return sum(map(lambda x: promedios[x] ,promedios)) / len(promedios)  


def mayor_promedio(promedios):                           #D
    return max(promedios, key=lambda alum: promedios[alum])

def menor_nota(nombres,notas1,notas2):                   #E
  listaMinimos = list(map(lambda x,y: x if(x < y) else y,notas1,notas2))
  diccionario_minimo = dict(zip(nombres,listaMinimos))
  alumno = min(diccionario_minimo, key=lambda alum: diccionario_minimo[alum])
  return alumno,diccionario_minimo[alumno]


alumnos = generar_nueva_estructura(nombres, notas_1, notas_2)
promedios = promedio_estudiante(alumnos,nombres)

print(promedios)


for name in promedios:                                      
   print(f'-Alumno: {name} -Promedio: {promedios[name]}')

print(f'El promedio general de todo el curso es: {promedio_general(promedios):.2f}')
nombre = mayor_promedio(promedios)
print(f'El alumno con mayor promedio es: {nombre} con un promedio de: {promedios[nombre]} ')
nombreMenorNota = menor_nota(nombres,notas_1,notas_2)
print(f'El alumno con menor nota obtenida fue: {nombreMenorNota[0]} con una nota de: {nombreMenorNota[1]} ')