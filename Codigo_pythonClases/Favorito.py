#Clase favorito taller 2 Spotify
from datetime import datetime

class Favorito():
    """
    Clase abstracta que representa la estructura  de un favorito en la aplicacion.

    Attributes:
        cancion (Cancion): Cancion que se agrega a favorito.
        fecha_agregado (str): fecha en la que se agrega una cancion a favoritos 
    """
    
    def __init__(self, cancion):
        """
        Inicializa los atributos base del usuario.

        Args:
            cancion (Cancion): Correo electrónico con el que se crea la cuenta.
            fecha_agregado (str)
            
        """
        self.cancion = cancion
        self.fecha = datetime.now().strftime("%Y - %m - %d")

    def marcar(self):

        pass
    
    def desmarcar(self):
        pass
    
    def __eq__(self, otro_favorito):
        """
        Compara 2 favoritos por medio de las canciones que compara titulo, año y artista


        Args:
            otro_favorito (Favorito): Otro favorito que se desea comparar


        Returns:
            bool: True si ambas canciones de los favoritos coinciden en sus atributos artista, titulo y año 
        """
        return self.cancion == otro_favorito.cancion
