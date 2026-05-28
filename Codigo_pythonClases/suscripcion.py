#Clase Ranking taller 2
from datetime import datetime

class Ranking():
    """
    Clase abstracta que representa la estructura de una suscripcion en la aplicacion.

    Attributes:
        plan (str): Nombre del plan.
        precio (float): Precio del plan.
        metodo_de_pago (str): nombre del metodo de pago.
        estado (str): estado del plan.
        fecha_inicio (str): fecha en la que inicia la suscripcion.
        fecha_fin (str): fecha en la que termina la suscripcion.
    """
    def __init__(self, plan, precio, metodo_de_pago, estado):
        """
        Inicializa los atributos base del ranking.

        Args:
            plan (str): Nombre del plan.
            precio (float): Precio del plan.
            metodo_de_pago (str): nombre del metodo de pago.
            estado (str): estado del plan.
            fecha_inicio (str): fecha en la que inicia la suscripcion.
            fecha_fin (str): fecha en la que termina la suscripcion.
        """
        self.plan = plan
        self.precio = precio
        self.metodo_de_pago = metodo_de_pago
        self.estado = "Activo"
        self.fecha_inicio = datetime.now().strftime("%Y-%m-%d")
        self.fecha_fin = 'fecha_fin'

    def activar(self):
        pass

    def cancelar(self):
        pass

    def renovar(self):
        pass