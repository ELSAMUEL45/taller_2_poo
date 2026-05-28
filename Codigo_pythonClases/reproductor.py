#Clase reproductor taller 2 Spotify
from datetime import datetime

class Reproductor():
    """
    Clase abstracta que representa la estructura  del reproductor en la aplicacion.

    Attributes:
        cancion_actual (Cancion | None): Cancion que esta sonando actualmente.
        cola (list(Canciones)): lista de canciones.
        volumen (int): valor en el que se encuentra el volumen de la aplicacion 
        estado (str): estado en el que se encuentra la aplicacion, si esta sonando o esta pausado
        modo_aleatorio (bool) : Si esta en modo aleatorio elige cualquier cancion al azar de la cola
        modo_repetecion (bool) : si se encuentra en modo repeticion
        temporizador (int) ; para que tenga un limite de tiempo y luego se apague
    """
    
    def __init__(self, cancion_actual, cola=[], volumen=50, estado="Pausado", modo_aleatorio=False, modo_repeticion=False, temporizador=0):
        """
        Inicializa los atributos base del reproductor.

        Args:
            cancion_actual (Cancion | None): Cancion que esta sonando actualmente.
            cola (list(Canciones)): lista de canciones.
            volumen (int): valor en el que se encuentra el volumen de la aplicacion 
            estado (str): estado en el que se encuentra la aplicacion, si esta sonando o esta pausado
            modo_aleatorio (bool) : Si esta en modo aleatorio elige cualquier cancion al azar de la cola
            modo_repetecion (bool) : si se encuentra en modo repeticion
            temporizador (int) ; para que tenga un limite de tiempo y luego se apague
            
        """
        self.cancion_actual = cancion_actual
        self.cola = cola
        self.volumen = volumen
        self.estado = estado
        self.modo_aleatorio = modo_aleatorio
        self.modo_repeticion = modo_repeticion
        self.temporizador = temporizador

    def reproducir_cancion(self, cancion):
        """
        Asigna una cancion a la variable del reproductor y llama a la funcion incrementar_reproducciones de la cancion


        Args:
            cancion (Cancion) : cancion que se desea reproducir
        """
        self.cancion_actual = cancion
        cancion.incrementar_reproducciones()
    
    def pausar_cancion(self):
        """
        Cambia el estado del reproductor a pausa
        """
        self.estado = "Pausado"
    
    def siguiente_cancion(self):
        """
        Avanza a la siguiente cancion que esta en la cola

        """
        pass

    def anterior_cancion(self):
        """
        Retrocede a la cancion anterior que esta en la cola

        """
        pass

    def subir_volumen(self):
        """
        Aumenta la variable volumen con un +5

        """
        self.volumen +=5
        return self.volumen
    
    def bajar_volumen(self):
        """
        Disminuye la variable volumen con un -5

        """
        self.volumen -=5
        return self.volumen
    
    def agregar_a_la_cola(self, cancion):
        """
        Asigna una cancion nueva a la cola del reproductor


        Args:
            cancion (Cancion) : cancion que se desea agregar a la cola
        """
        self.cola.append(cancion)

