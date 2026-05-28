#Clase Ranking taller 2
from datetime import datetime

class Ranking():
    """
    Clase abstracta que representa la estructura de un ranking en la aplicacion.

    Attributes:
        nombre (str): Nombre del ranking.
        criterio (str): Criterio del ranking (#Masescuchadas, etc).
        canciones (List(Cancion)): lista de las canciones en el ranking
        fecha_actualizacion (str): fecha en la que se actualizo el ranking
    """
    def __init__(self, nombre, criterio):
        """
        Inicializa los atributos base del ranking.

        Args:
            nombre (str): Nombre del ranking.
            criterio (str): Criterio del ranking.
            canciones (List(Cancion)): lista de las canciones en el ranking
            fecha_actualizacion (str): fecha en la que se actualizo el ranking
        """
        self.nombre = nombre
        self.criterio = criterio
        self.canciones = []
        self.fecha_actualizacion = datetime.now().strftime("%Y-%m-%d")

    def actualizar_ranking(self):
        pass

    def obtener_top(self, cantidad):
        """
        retorna una lista con una cantidad de ccanciones necesarias


        Args:
            cantidad(int): cantidad de canciones que se quiere visualizar del ranking



        Returns:
            list[Cancion]: Lista de canciones, con la cantidad previamente indicada
        """
        return self.canciones[0:cantidad+1]