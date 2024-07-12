from data_access import BCCR
from entities import TipoCambio

class BusinessLogic:
    def __init__(self):
        self.bccr = BCCR()
        
    def tipo_cambio(self, fecha):
        try:
            tipo_cambio_compra = round(float(self.bccr.obtener_tasa_cambio(fecha, '317')), 2)
            tipo_cambio_venta = round(float(self.bccr.obtener_tasa_cambio(fecha, '318')), 2)

            return TipoCambio(fecha, tipo_cambio_compra, tipo_cambio_venta)
        except Exception :
            raise RuntimeError(f"No se pudo obtener el tipo de cambio del {fecha}: {str()}")
