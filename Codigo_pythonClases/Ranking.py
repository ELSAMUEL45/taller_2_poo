#Clase Ranking taller 2
from datetime import datetime
from cancion import Cancion

class Ranking():
    """
    Clase abstracta que representa la estructura de un ranking en la aplicacion.

    Attributes:
        nombre (str): Nombre del ranking.
        criterio (str): Criterio del ranking (#Masescuchadas, etc).
        canciones (List(Cancion)): lista de las canciones en el ranking
        fecha_actualizacion (str): fecha en la que se actualizo el ranking
    """
    organizada = []
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
    def organizar_por_reproducciones(self, lista):
        cancion = lista[0]
        reproducciones = lista[0].reproducciones
        for i in lista:
            if i.reproducciones > cancion.reproducciones:
                cancion = i
                reproducciones = i.reproducciones
        Ranking.organizada.append(cancion)
        nueva_lista = lista.remove(cancion)
        self.organizar_por_reproducciones(nueva_lista)
        
    def generar_ranking(self, criterio):
        if criterio == "#Masescuchadas":
            todas_canciones = Cancion.todas_las_canciones()
            self.organizar_por_reproducciones(todas_canciones)
        return Ranking.organizada
            
