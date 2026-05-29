#Clase usuario taller 2 Spotify
from lista_reproduccion import ListaReproduccion
from favorito import Favorito
from calificacion import Calificacion
class Usuario():
    """
    Clase abstracta que representa la estructura  de un Usuario en la aplicacion.

    Attributes:
        nombre (str): Nombre del usuario.
        correo (str): Correo electrónico con el que se crea la cuenta.
        contraseña (str): Contraseña 
        lista_reproducción (List[ListaReproducción]): listas de reproducciones creadas por el usuario
        suscripcion (Suscripcion | None) : informacion de la suscripcion
        favorito (list[Favoritos]): lista de canciones favoritas
        
    """
    
    def __init__(self, nombre, correo, contraseña, suscripcion=None):
        """
        Inicializa los atributos base del usuario.

        Args:
            nombre (str): Nombre del usuario.
            correo (str): Correo electrónico con el que se crea la cuenta.
            contraseña (str): Contraseña 
            suscripcion (Suscripcion ! None) : informacion de la suscripcion
            favorito (list[Favoritos]): lista de canciones favoritas
        """
        self.nombre = nombre
        self.__correo = correo
        self.__contraseña = contraseña
        self.lista_reproducción = []
        self.suscripcion = suscripcion
        self.favorito = []

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
            print(f'Bienvenido {self.nombre}')
            return True
        
        return False
    
    def cerrar_sesion(self):
        print(f'Hasta pronto')

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
        """
        Crea un nuevo favorito que se agrega a la lista 


        Args:
            cancion (Cancion): Cancion que se desea agregar a favoritos.

        """
        nuevo_favorito = Favorito(cancion)
        self.favorito.append(nuevo_favorito)

    def quitar_favoritos(self,cancion):
        """
            Crea un nuevo favorito que se compara en la lista para eliminarlo


            Args:
            cancion (Cancion): Cancion que se desea eliminar de favoritos.

        """
        favorito_a_quitar = Favorito(cancion)
        self.favorito.remove(favorito_a_quitar)

    def calificar_cancion(self,cancion, valor):
        """
            Crea una nueva calificacion que se agrega a lista de calificaciones de la cancion


            Args:
                cancion (Cancion): Cancion que se desea eliminar de favoritos.
                valor (float): valor que se le desea poner de calificacion a la cancion

        """
        nueva_calificacion = Calificacion(self, cancion, valor)
        cancion.agregar_calificacion(nueva_calificacion)
        

    def cambiar_suscripcion(self, suscripcion_nueva):
        """
            Cambia la suscripcion que se tiene actualmente


            Args:
            suscripcion_nueva (Suscripcion): suscripcion por la que se desea actualizar.

        """
        self.suscripcion = suscripcion_nueva

    
