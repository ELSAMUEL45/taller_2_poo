#Clase cancion taller 2 Spotify

class Cancion():
    """
    Clase abstracta que representa la estructura de una cancion en la aplicacion.

    Attributes:
        titulo (str): Nombre de la cancion.
        artista (str): Nombre del artista que creo la cancion.
        album (str): Nombre de album en el que se encuentra la cancion, o nombre del EP, si no tiene seria por defecto el nombre de la cancion
        genero (str): Nombre del genero de la cancion
        duracion (str): tiempo de la duracion de la cancion
        año (int): año en el que sale la cancion 
        reproducciones (int): numero de reproducciones de la cancion, cuando se inicializa el objeto es 0
        calificacion (float): entre el 1-5  que tanta calificacion tiene la cancion
        creditos (str): creditos a las personas que trabajaron en la cancion 
    """
    
    def __init__(self, titulo, artista, genero, duracion, año, creditos, album=""):
        """
        Inicializa los atributos base de la cancion.

        Args:
            titulo (str): Nombre de la cancion.
            artista (str): Nombre del artista que creo la cancion.
            album (str): Nombre de album en el que se encuentra la cancion, o nombre del EP, si no tiene seria por defecto el nombre de la cancion
            genero (str): Nombre del genero de la cancion
            duracion (str): tiempo de la duracion de la cancion
            año (int): año en el que sale la cancion 
            reproducciones (int): numero de reproducciones de la cancion, cuando se inicializa el objeto es 0
            creditos (str): creditos a las personas que trabajaron en la cancion
        """
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.duracion = duracion
        self.año = año
        self.reproducciones = 0
        self.calificancion = 0
        self.creditos = creditos


    def incrementar_reproducciones(self):
        """
        Cada vez que se reproduce la cancion aumenta el contador de las reproducciones.

        """
        self.reproducciones += 1
    
    def actualizar_calificacion(self, nueva_calificacion):
        """
        Actualiza el valor de la calificacion que existia antes


        Args:
            nueva_calificacion (float): Calificacion que reemplaza la anterior 



        Returns:
            bool: True si la actualizacion se realizo correctamente 
        """
        try:
            self.calificancion = nueva_calificacion
            return True
        except:
            return False
        
    def obtener_datos(self):
        """
        Retorna los datos de la cancion

        Returns:
            diccionario: {Artista: self.artista,
                            duracion: self.duracion,
                            album: self.album,
                            año: self.año,
                            creditos: self.creditos}

        """
        informacion = {'Artista': self.artista,
                       'Duracion': self.duracion,
                       'Album': self.album,
                       'Año': self.año,
                       'Creditos':self.creditos}
        
        return informacion

    def __eq__(self, otra_cancion):
        """
        Compara 2 canciones para saber si son iguales, compara titulo, año y artista


        Args:
            otra_cancion (Cancion): Otra cancion con la que se desea comparar



        Returns:
            bool: True si ambas canciones son iguales en sus atributos artista, titulo y año 
        """
        return self.artista == otra_cancion.artista and self.titulo == otra_cancion.titulo and self.año == otra_cancion.año

    def __lt__(self, otra_cancion):
        """
        Compara 2 canciones para saber cual es menor con el titulo de la cancion


        Args:
            otra_cancion (Cancion): Otra cancion con la que se desea comparar



        Returns:
            bool: True si cancion_1 es menor a la cancion_2 
        """
        return self.titulo < otra_cancion.titulo


    
