#Clase calificacion taller 2 Spotify
from datetime import datetime

class Calificacion():
    """
    Clase abstracta que representa la estructura  de una calificacion en la aplicacion.

    Attributes:
        usuario (Usuario): Usuario que califica.
        cancion (Cancion): Cancion que se califica.
        valor (float): Valor que se le pone al calificar 
        comentario (str): Descripcion del porque la calificacion
        fecha (string) : Fecha en la que se hizo la calificacion
    """
    
    def __init__(self, usuario, cancion, valor, comentario):
        """
        Inicializa los atributos base del usuario.

        Args:
            usuario (Usuario): Usuario que califica.
            cancion (Cancion): Cancion que se va a calificar.
            valor (float): Valor que se le pone al calificar 
            comentario (str): Descripcion del porque la calificacion
            
        """
        self.usuario = usuario
        self.cancion = cancion
        self.valor = valor
        self.comentario = comentario
        self.fecha = datetime.now().strftime("%Y - %m - %d")

    def editar_calificacion(self, valor,comentario):
        """
        Edita una calificacion antes dada


        Args:
            valor (int): nuevo valor del valor
            comentario (str): nuevo comentario de la calificacion
        """
        self.valor = valor
        self.comentario = comentario
    
    def eliminar_calificacion(self):
        """
        Eliminar una calificacion creada anteriormente
        """
        pass
