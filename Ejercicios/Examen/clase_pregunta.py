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
