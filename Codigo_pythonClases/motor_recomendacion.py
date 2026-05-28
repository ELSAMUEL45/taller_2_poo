#Clase motorrecomendacion taller 2 Spotify
from datetime import datetime

class Reproductor():
    """
    Clase abstracta que representa del algoritmo de recomendacion en la aplicacion.

    Attributes:
        historial (list[Cancion]): Canciones escuchadas anteriormente.
    """
    
    def __init__(self):
        """
        Inicializa los atributos base de motor de recomendacion.

        Args:
            historial (list[Cancion]): Canciones escuchadas anteriormente, se inicia una vez se crea el perfil.
            
        """
        self.historial = []
    
    def generar_recomendaciones(self, usuario):
        """
        recibe un usuario y retorna una lista de canciones con base en el historial
        Args:
            usuario (Usuario) : usuario al cual se le quiere recomendar
        """
        pass
    
    def recomendacion_por_genero(self, genero):
        """
        recibe un genero y retorna una lista de canciones con base en este genero
        Args:
            genero (string) : el genero del cual se desea crear la recomendacion
        """
        pass
    
    def recomendacion_por_calificaciones(self):
        """
        retorna una lista de canciones mejor valoradas

        """
        pass
