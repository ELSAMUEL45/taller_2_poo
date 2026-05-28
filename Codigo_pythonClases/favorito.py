
#Clase favorito taller 2 Spotify
from datetime import datetime

class Favorito():
    """
    Clase abstracta que representa la estructura  de un favorito en la aplicacion.

    Attributes:
        usuario (Usuario): Usuario que califica.
        cancion (Cancion): Correo electrónico con el que se crea la cuenta.
        fecha_agregado (str): fecha en la que se agrega una cancion a favoritos 
    """
    
    def __init__(self, usuario, cancion):
        """
        Inicializa los atributos base del usuario.

        Args:
            usuario (Usuario): Usuario que califica.
            cancion (Cancion): Correo electrónico con el que se crea la cuenta.
            fecha_agregado (str)
            
        """
        self.usuario = usuario
        self.cancion = cancion
        self.fecha = datetime.now().strftime("%Y - %m - %d")

    def marcar(self):
        pass
    
    def desmarcar(self):
        pass
    
    
