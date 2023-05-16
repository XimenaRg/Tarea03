

"""
Bueno esta clase no tiene mucho definido.
Los atributos los trabajamos privados y hacemos uso de gets para poder acceder a ellos.


El problema de definir así la lista de opciones y la opción correcta es que nos limita
a mostrar siempre en el mismo orden las respuestas, y a tener que deordenar manualmente las respuestas al
momento de crearlas.

"""
class Pregunta:
    """
    Clase que representa una pregunta de un examen
    Atributos:
    __pregunta (str): La pregunta a realizar
    __opciones (list): Una lista con las opciones de respuesta
    __respuesta_correcta (int): El índice de la respuesta correcta en la lista de opciones
    """
        
    def __init__(self, pregunta:str, opciones:list, respuesta_correcta:int):
        """
        Constructor de la clase Pregunta.
        Args:
        pregunta (str): La pregunta a realizar
        opciones (list): Una lista con las opciones de respuesta
        respuesta_correcta (int): El índice de la respuesta correcta en la lista de opciones
        """

        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta
