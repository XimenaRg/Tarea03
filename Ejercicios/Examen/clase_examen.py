import random
from clase_pregunta import Pregunta

class Examen:
    """
    Clase que representa un examen
    Args:
    __preguntas (list): Una lista de preguntas que se incluirán en el examen
    """
    
    def __init__(self, preguntas:list):
        """
        Constructor de la clase Examen.
        Args:
        preguntas (list): Una lista de preguntas que se incluirán en el examen
        """

        self.preguntas = preguntas

    def realizar_examen(self):
        """
        Método que realiza un examen para el esudiante y muestra su calificación al final
        así como sus respuestas correctas e incorrectas.
        
        Args:
        None
        Returns:
        None
        
        """

        """
        Consideren que en sí, el examen simplemente es la instancia de una serie de preguntas y respuestas.
        Y una forma de evaluarse.

        La parte de aplicarlo, o de mostrarlo al usuario lo dejamos como un script usando métodos de aquí.

        Hay que cambiarlo de modo a que en la interfaz tenga los métodos necesarios para ir creándolo.
        """
        
        print("Hola! Bienvenid@ al examen de Programación")
        nombre = input("Por favor, ingresa tu nombre completo: ")

        #La función random.sample() garantiza que no se seleccionen elementos repetidos.
        preguntas_aleatorias = random.sample(self.preguntas, 10)
        puntaje = 0
        respuestas_correctas = []
        respuestas_incorrectas = []

        for i, pregunta in enumerate(preguntas_aleatorias): 
            print(f"\nPregunta {i + 1}:")
            #manda a llamar a la función y suma 0 o 1 al puntaje.

            """
            Primero muestren las preguntas, al final que exista un método para calificar.
            Todo esto se va a tener que editar ya que en la interfaz no va ser posible hacerlo de esta forma.
            """
            puntaje += self.mostrar_pregunta(pregunta)

            if puntaje > len(respuestas_correctas):
                respuestas_correctas.append(i + 1)
            else:
                respuestas_incorrectas.append(i + 1)

        print("\nNombre del alumno: ", nombre)
        print(f"\nRespuestas correctas: {respuestas_correctas}")
        print(f"\nRespuestas incorrectas: {respuestas_incorrectas}")

        calificacion = int(puntaje)
        print(f"\nTu calificación es: {calificacion}/10.")
                        
    def mostrar_pregunta(self, pregunta):
        """
        Método que muestra una pregunta al usuario y verifica si su respuesta es correcta
        Args:
        pregunta (Pregunta): La pregunta a mostrar
        Returns:
        int: 1 si la respuesta es correcta, 0 si es incorrecta
        """
        """
        Con métodos get. Así puede ser confuso porque es el mismo identificador
        """
        print(pregunta.pregunta)
        for i, opcion in enumerate(pregunta.opciones):
            print(f"{i + 1}. {opcion}")

        respuesta = input("Ingresa el número de la respuesta correcta: ")

        #verifica si la respuesta dada es un número y si es un entero. Valida si es correcta o no.
        if respuesta.isnumeric() and int(respuesta) - 1 == pregunta.respuesta_correcta:
            return 1
        else:
            return 0

#la lista "preguntas" contiene objetos de la clase "Pregunta"
preguntas = [
    Pregunta("¿Cuál es la sintaxis correcta para imprimir en pantalla en Python?", ["print('texto a imprimir')", "echo('texto a imprimir')", "printf('texto a imprimir')"], 0),
    Pregunta("¿Qué tipo de dato se utiliza para representar un texto en Python?", ["int", "str", "bool"], 1),
    Pregunta("¿Qué es una lista en Python?", ["Un conjunto de elementos ordenados y modificables", "Un conjunto de elementos no ordenados y no modificables", "Un conjunto de elementos ordenados y no modificables"], 0),
    Pregunta("¿Cuál es la sintaxis para crear una lista vacía en python?", ["list()", "[]", "[none]"], 1),
    Pregunta("¿Qué significa el término 'mutable' en relación a las listas en python?", ["Que una lista se puede modificar después de ser creada", "Que una lista no puede contener elementos duplicados", "Que una lista puede pertenecer a otra lista"], 0),
    Pregunta("¿Cuál es la forma correcta de agregar un elemento al final de una lista en python?", ["list.insert(elemento)", "list.add(elemento)", "list.append(elemento)"], 2),
    Pregunta("¿Cuál define mejor a las clases en python?", ["Una estructura de datos que almacena un conjunto de elementos ordenados", "Una función para imprimir en pantalla un mensaje", "Un tipo de objeto que define las propiedades y acciones de un objeto"], 2),
    Pregunta("¿Qué son los métodos de una clase?", ["Definen los objetos que tomará la clase", "Funciones que estan definidas que actuan sobre objetos de una clase", "Variables de tipo list que almacenan los objetos de una clase"], 1),
    Pregunta("Sintaxis correcta de una lista", ["lista = (1,2,3)", "lista = [dona,concha,cuernito]", "lista = {perro,gato,ave}"], 1),
    Pregunta("¿Qué método se usa para agregar un elemento al final de una lista en python?", ["insert()", "shuffle()", "append()"], 2),
    Pregunta("¿Qué es un ciclo for en python?", ["Un ciclo que se ejecuta una cantidad fija de veces", "Un ciclo que se ejecuta mientras se cumple una condición", "Un ciclo que se ejecuta indefinidamente hasta que se cumple una función"], 0),
    Pregunta("¿Cómo se usa el ciclo for en python para iterar sobre una lista?", ["for i in range(lista):", "for x in Lista", "for n in lista:"], 2),
    Pregunta("¿Qué es un ciclo while en python?", ["Un ciclo que se ejecuta una cantidad fija de veces", "Un ciclo que se ejecuta mientras se cumple una condición", "Un ciclo que se ejecuta indefinidamente hasta que se cumple una función"], 1),
    Pregunta("Cuál es la diferencia entre el ciclo for y ciclo while?", ["El ciclo for se ejecuta indefinidamente mientras el ciclo while se ejecuta una cantidad fija de veces", "El ciclo for se utiliza para iterar sobre una lista mientras que el ciclo while se usa para repetir una acción mientras se cumple una condición", "El ciclo for siempre se ejecuta al menos una vez, mientras que el ciclo while solo si se cumple una condición inicial"], 1),
    Pregunta("El comando break:", ["Detiene un ciclo y continua con la siguiente acción", "Detiene el ciclo por completo", "Salta a una iteración especifica"], 1),
    Pregunta("El comando continue", ["Detiene el ciclo por completo", "Salta a una iteración especifica", "Detiene el ciclo y sigue con la iteración posterior"], 2),
    Pregunta("¿Qué es la herencia en POO?", ["Una técnica en la que una clase se divide en varias subclases", "Una técnica en la que una clase se comparte entre varios programas", "Una técnica en la que una clase se basa en otra existente"], 2),
    Pregunta("Para acceder al segundo elemento de una lista", ["list[2]", "list(2)", "list[1]"], 2),
    Pregunta("¿Cuál es la sintaxis correcta para crear un ciclo for que recorra una lista e imprima cada elemento en orden inverso?", ["for i in range(len(lista), 0, -1):", "for i in lista[::-1]:", "for i in range(0, len(lista), -1):"], 1),
    Pregunta("¿Qué hace la función 'shuffle' del módulo random en Python?", ["Ordena de mayor a menor los elementos de una lista", "Ordena aleatoriamente los elementos de una lista", "Ordena sin los elementos repetidos de una lista "], 1),
    Pregunta("¿Qué hace la función enumerate() cuando se usa en un bucle for?", ["Cuenta el número de elementos en una lista", "Devuelve un objeto que permite iterar sobre los índices y valores de una lista", "Crea una lista de tuplas con los índices y valores de una lista"], 1),
    Pregunta("¿Qué imprime el siguiente código:\n\nfor i in range(1, 10):\n   if i % 2 == 0:\n    continue\n   else:\n    print(i)\n", ["2,4,6,8", "ERROR", " 1 3 5 7 9"], 2),
    Pregunta("¿Qué imprime el siguiente código:\n\nfor i in range(3):\n   for j in range(3):\n    if i == j:\n       break:\n    print((i,j))\n", ["ERROR", " (0, 1) (0, 2) (1, 2)", "(0, 1) (0, 2) (1, 0) (2, 0) (2, 1) (2, 2)"], 1),
    Pregunta("¿Qué imprime el siguiente código:\n\nfrom random import shuffle\nx = [1, 2, 3, 4, 5]\nshuffle(x)\nprint(x)\n", ["[1,3,5,4]", "[5,4,3,2,1]", "Una permutación aleatoria de la lista"], 2),
    Pregunta("¿Qué imprime el siguiente código:\n\nmy_list = [2, 4, 6, 8]\nfor i in range(len(my_list)):\n     my_list.insert(i+1, 0)\nprint(my_list)\n", ["[2, 0, 0, 0, 0, 4, 6, 8]", "[0, 2, 4, 6, 8]", "[0, 0, 0, 0, 0, 2, 4, 6, 8]"], 0),
    Pregunta("¿Qué imprime el siguiente código:\n\nmy_list = [3, 6, 9, 12, 15, 18, 21\nfor i in range(2, len(my_list), 3):\n   print(my_list[i])\n", ["15 9", "18 21", "9 18"], 2),
    Pregunta("¿Cuál de las siguientes opciones no es una forma de crear una tupla en Python?\n", ["t = (1, 2, 3)", "t = 1,2,3", "t = [1,2,3]"], 2),
    Pregunta("¿Qué imprime el siguiente código:\n\npalabra = 'Python'\nfor i in range(len(palabra)):\n     print(palabra[i])\n", ["Imprime los caracteres de la cadena en orden ascendente.", " Imprime los caracteres de la cadena en orden descendente.", "Imprime la longitud de la cadena"], 1),
    Pregunta("¿Qué imprime el siguiente código:\n\nlista = ['dona', 'concha', 'cuernito', 'oreja']\nlista.sort()\nprint(lista)\n", ["['concha', 'cuernito', 'dona', 'oreja']", "['oreja', 'dona', 'concha', 'cuernito']", "ERROR"], 0),
    Pregunta("¿Qué imprime el siguiente código:\n\ntupla = (3, 1, 4, 1, 5)\ntupla.sort()\nprint(tupla)\n", ["(1, 1, 3, 4, 5)", "Error", "(3, 1, 4, 1, 5)"], 1)]

examen = Examen(preguntas)
examen.realizar_examen()
