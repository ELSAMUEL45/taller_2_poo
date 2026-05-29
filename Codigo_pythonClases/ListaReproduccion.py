#Clase listaReproduccion taller 2 Spotify
from datetime import datetime

class ListaReproduccion():
    """
    Clase abstracta que representa la estructura de una Lista de Reroduccion en la aplicacion.

    Attributes:
        nombre (str): Nombre de la lista de reproduccion.
        descripccion (str): Descripccion de la lista.
        portada (str): Base_64 Portada de la lista.
        autor (Usuario): Informacion del usuario que creo la lista
        es_publica (bool): True si la lista es publica por defecto privada (False)
        fecha_creacion (string): Fecha en la que se creo la lista de reproduccion
        canciones (List(Cancion)): Lista de canciones dentro de la lista de reproduccion
    """
    
    def __init__(self, nombre, descripcion, autor, es_publica= False, portada=""):
        """
        Inicializa los atributos base de la cancion.

        Args:
            nombre (str): Nombre de la lista de reproduccion.
            descripccion (str): Descripccion de la lista.
            portada (str): Base_64 Portada de la lista por defecto esta vacia.
            autor (Usuario): Informacion del usuario que creo la lista
            es_publica (bool): True si la lista es publica por defecto privada (False)
            fecha_creacion (string): Fecha en la que se creo la lista de reproduccion
            canciones (List(Cancion)): Lista de canciones dentro de la lista de reproduccion cuando se inicia esta vacia
        """

        tiempo = datetime.now()
        self.nombre = nombre
        self.descripcion = descripcion
        self.portada = portada
        self.autor = autor
        self.es_publica = es_publica
        self.fecha_creacion = tiempo.strftime("%Y - %m - %d")
        self.canciones = []


    def agregar_cancion(self, cancion):
        """
        Recibe una cancion para agregarla a la lista de reproduccion.

        Args:
            cancion (cancion): Objeto cancion que es agregada a la lista de reproduccion



        Returns:
            bool: True si se agrego correctamente

        """
        try:
            self.canciones.append(cancion)
            return True
        except:
            return False
    
    def eliminar_cancion(self, cancion):
        """
        Recibe una cancion para agregarla a la lista de reproduccion.

        Args:
            cancion (cancion): Objeto cancion que va a ser eliminada de la lista de reproduccion



        Returns:
            bool: True si se elimino correctamente

        """
        try:
            self.canciones.remove(cancion)
            return True
        except:
            return False
        
    def ordenar_canciones_por_titulo(self):
        """
        Ordena las canciones en la lista de canciones por titulo de forma alfabetica

        """
        sorted(self.canciones)

    def obtener_duracion_total(self):
        """
        Retorna la duracion de todas las canciones

        Returns:
            int: duracion de la lista en minutos

        """
        segundos = 0
        minutos = 0
        for cancion in self.canciones:
            duracion = cancion.split(':')
            minutos += int(duracion[0])
            segundos += int(duracion[1])

        de_seg_min = segundos // 60
        segundos = segundos%60
        minutos += de_seg_min

        return minutos
