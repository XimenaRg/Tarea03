import random

class Pregunta:
    def __init__(self, pregunta:str, opciones:list, respuesta_correcta:int):
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta

class Examen:
    def __init__(self, preguntas):
        self.preguntas = preguntas

    def realizar_examen(self):
       
        print("¡Hola! Bienvenid@ al examen de Programación")
        nombre = input("Ingresa tu nombre completo: ")

        preguntas_seleccionadas = random.sample(self.preguntas, 10)
        puntaje = 0
        respuestas_correctas = []
        respuestas_incorrectas = []

        for i, pregunta in enumerate(preguntas_seleccionadas):
            print(f"\nPregunta {i + 1}:")
            puntaje += self.presentar_pregunta(pregunta)
            if puntaje > sum(respuestas_correctas):
                respuestas_correctas.append(i + 1)
            else:
                respuestas_incorrectas.append(i + 1)

        print("\nNombre del alumno: ", nombre)
        print ("\nResultados:")
        print(f"\nRespuestas correctas: {respuestas_correctas}")
        print(f"\nRespuestas incorrectas: {respuestas_incorrectas}")

        calificacion = int(puntaje)
        print(f"\nTu calificación es: {calificacion}/10.")
                        
    def presentar_pregunta(self, pregunta):
        print(pregunta.pregunta)
        for n, opcion in enumerate(pregunta.opciones):
            print(f"{n + 1}. {opcion}")

        respuesta = input("Ingresa el número de la respuesta correcta: ")

        if respuesta.isnumeric() and int(respuesta) - 1 == pregunta.respuesta_correcta:
            return 1
        else:
            return 0

preguntas = [
    Pregunta("¿Cuál es la sintaxis correcta para imprimir en pantalla en Python?", ["print('texto a imprimir')", "echo('texto a imprimir')", "printf('texto a imprimir')"], 0),
    Pregunta("¿Qué tipo de dato se utiliza para representar un texto en Python?", ["int", "str", "bool"], 1),
    Pregunta("¿Qué es una lista en Python?", ["Un conjunto de elementos ordenados y modificables", "Un conjunto de elementos no ordenados y no modificables", "Un conjunto de elementos ordenados y no modificables"], 0),
    Pregunta("¿Cuál es la sintaxis correcta para imprimir en pantalla en Python?", ["print('texto a imprimir')", "echo('texto a imprimir')", "printf('texto a imprimir')"], 0),
    Pregunta("¿Qué tipo de dato se utiliza para representar un texto en Python?", ["int", "str", "bool"], 1),
    Pregunta("¿Qué es una lista en Python?", ["Un conjunto de elementos ordenados y modificables", "Un conjunto de elementos no ordenados y no modificables", "Un conjunto de elementos ordenados y no modificables"], 0),
    Pregunta("¿Cuál es la sintaxis correcta para imprimir en pantalla en Python?", ["print('texto a imprimir')", "echo('texto a imprimir')", "printf('texto a imprimir')"], 0),
    Pregunta("¿Qué tipo de dato se utiliza para representar un texto en Python?", ["int", "str", "bool"], 1),
    Pregunta("¿Qué es una lista en Python?", ["Un conjunto de elementos ordenados y modificables", "Un conjunto de elementos no ordenados y no modificables", "Un conjunto de elementos ordenados y no modificables"], 0),
    Pregunta("¿Cuál es la sintaxis correcta para imprimir en pantalla en Python?", ["print('texto a imprimir')", "echo('texto a imprimir')", "printf('texto a imprimir')"], 0),
    Pregunta("¿Qué tipo de dato se utiliza para representar un texto en Python?", ["int", "str", "bool"], 1),
    Pregunta("¿Qué es una lista en Python?", ["Un conjunto de elementos ordenados y modificables", "Un conjunto de elementos no ordenados y no modificables", "Un conjunto de elementos ordenados y no modificables"], 0),
]

examen = Examen(preguntas)
examen.realizar_examen()
