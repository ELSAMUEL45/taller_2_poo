#Clase suscripcion taller 2
from datetime import datetime, timedelta

class Suscripcion():
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
        mes = datetime.now().month


        self.plan = plan
        self.precio = precio
        self.metodo_de_pago = metodo_de_pago
        self.estado = "Pendiente"
        self.fecha_inicio = datetime.now().strftime("%Y-%m-%d")
        self.fecha_fin = datetime.now().replace(month= mes+1).strftime("%Y-%m-%d")

    def activar(self):
        """
            Cambia el estado de un plan activo
        """
        self.estado = "Activo"
        

    def cancelar(self):
        """
            Cambia el estado de un plan a Cancelado
        """
        self.estado = "Cancelado"
        pass

    def renovar(self):
        """
         Cambia el estado de un plan a Cancelado
        """
        mes = datetime.now().month

        self.fecha_fin = datetime.now().replace(month=mes+1).strftime("%Y-%m-%d")
        pass
