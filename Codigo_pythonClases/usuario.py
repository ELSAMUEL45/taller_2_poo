#Clase usuario taller 2 Spotify
from lista_reproduccion import ListaReproduccion

class Usuario():
    """
    Clase abstracta que representa la estructura  de un Usuario en la aplicacion.

    Attributes:
        nombre (str): Nombre del usuario.
        correo (str): Correo electrónico con el que se crea la cuenta.
        contraseña (str): Contraseña 
        lista_reproducción (List[ListaReproducción]): listas de reproducciones creadas por el usuario
        suscripcion (Suscripcion ! None) : informacion de la suscripcion
    """
    
    def __init__(self, nombre, correo, contraseña, suscripcion=None):
        """
        Inicializa los atributos base del usuario.

        Args:
            nombre (str): Nombre del usuario.
            correo (str): Correo electrónico con el que se crea la cuenta.
            contraseña (str): Contraseña 
            suscripcion (Suscripcion ! None) : informacion de la suscripcion
        """
        self.nombre = nombre
        self.__correo = correo
        self.__contraseña = contraseña
        self.lista_reproducción = []
        self.suscripcion = suscripcion

    def iniciar_sesion(self, correo ,contraseña):
        """
        Verifica si las credenciales ingresadas son correctas para iniciar sesion.


        Args:
            correo (str): Correo que se compara con la informacion usada a la hora del registro
            contraseña (str): Contraseña que se comprara con la informacion usada a la hora del registro


        Returns:
            bool: True si tanto el correo como la contraseña son iguales
        """
        if self.__correo == correo and self.__contraseña == contraseña:
            return True
        
        return False
    
    def cerrar_sesion(self):
        pass

    def crear_lista_reproduccion(self, nombre ,descripcion, es_publica=False):
        """
        Crea una nueva lista de reproduccion


        Args:
            nombre (str): Nombre de la nueva lista de reproduccion.
            descripcion (str): Agrega una descripccion a la nueva lista de reproduccion
            es_publica (bool): Identifica si la lista de reproduccion es publica o privada por defecto es privada



        Returns:
            bool: True si la lista se creo correctamente y se agrego correctamente al diccionario
        """
        try:
            lista_rep = ListaReproduccion(nombre, descripcion, self, es_publica)
            self.lista_reproducción.append(lista_rep)         
        except:
            return False

    def agregar_favorito(self,cancion):
        pass

    def quitar_favoritos(self,cancion):
        pass

    def calificar_cancion(self,cancion, valor):
        pass



    
