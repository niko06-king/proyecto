class Agrotech:
    def __init__(self,humedadi, humedadf, phi, phf, temperaturai, temperaturaf):
        self.humedad = {'semana_anterior': humedadi, 'semana_actual': humedadf}
        self.ph = {'semana_anterior': phi, 'semana_actual': phf}
        self.temperatura = {'semana_anterior': temperaturai, 'semana_actual': temperaturaf}
        self.cambios = {}

    def variacion(self):
        self.cambios = {
            'humedad': self.comparaciones_(self.humedad),
            'ph': self.comparaciones_(self.ph),
            'temperatura': self.comparaciones_(self.temperatura)
        }
        return self.cambios

    def comparaciones_(self, datos):
        if datos['semanafinal'] > datos['semanainicial']:
            return 'aumento'
        elif datos['semanafinal'] < datos['semanainicial']:
            return 'disminuyó'
        else:
            return 'estable'

class Dueño_fundo:
    def __init__(self, nombre_completo, id, imail, cultivo, hectareas, empresa=None, idempresa=None):
        self.nombre_copleto = nombre_completo
        self.id=id
        self.imail=imail
        self.cultivo=cultivo
        self.hectareas=hectareas
        self.empresa = empresa
        self.idempresa = idempresa
        self.empresa_agricola()

    def empresa_agricola(self):
        if self.hectareas > 20 and (self.empresa is None or self.idempresa is None):
            raise ValueError("porfavor diligencie la informacion de la empresa agricola a la cual te encuentras asociado")

    def nuevos_datos(self, informacion, nuevo_valor):
        if hasattr(self, informacion):
            setattr(self, informacion, nuevo_valor)
            if informacion == "hectareas":
                self.empresa_agricola()
        else:
            raise AttributeError("verifique tu informacion e intente nuevamente")

    def soporte(self):
        return self.cultivo.lower() == "frutal" and self.hectareas > 15

class LoteAgricola( Agrotech, Dueño_fundo):
    def __init__(self, humedadi, humedadf, phi, phf, temperaturai, temperaturaf,
                 nombre_completo, identificacion, imail, cultivo, hectareas, empresa=None, idempresa=None):
        Agrotech.__init__(self, humedadi, humedadf, phi, phf, temperaturai, temperaturaf)
        Dueño_fundo.__init__(self, nombre_completo, identificacion, imail, cultivo, hectareas, empresa, idempresa)

    def promedio(self):
        return {
            'semana_anterior': {
                'humedad': self.humedad['semanainicial'],
                'ph': self.ph['semanainicial'],
                'temperatura': self.temperatura['semanainicial']
            },
            'semanafinal': {
                'humedad': self.humedad['semanafinal'],
                'ph': self.ph['semana_actual'],
                'temperatura': self.temperatura['semana_actual']
            }
        }

    def variacion_porcentual(self):
        def calcular_porcentaje(final,inicial ):
            if anterior == 0:
                return None
            return ((inicial - final) / inicial) * 100

        return {
            'humedad': calcular_porcentaje(self.humedad['semana_actual'], self.humedad['semana_anterior']),
            'ph': calcular_porcentaje(self.ph['semana_actual'], self.ph['semana_anterior']),
            'temperatura': calcular_porcentaje(self.temperatura['semana_actual'], self.temperatura['semana_anterior']),
        }

print("datos recolectados por agrotech:")
humedadi = float(input("Humedad semana anterior (%): "))
humedadf = float(input("Humedad semana actual (%): "))
phi = float(input("pH semana anterior: "))
phf = float(input("pH semana actual: "))
temperaturai = float(input("Temperatura semana anterior (°C): "))
temperaturaf = float(input("Temperatura semana actual (°C): "))

print("\nInformacion del dueño del fundo:")
nombre = input("Nombre completo: ")
identificacion = input("Identificación: ")
correo = input("Correo electrónico: ")
cultivo = input("Tipo de cultivo: ")
hectareas = float(input("Número de hectáreas: "))

empresa = None
codigo_empresa = None
if hectareas > 20:
    empresa = input("Nombre de la empresa agrícola a la que te encuentras asocciado: ")
    codigo_empresa = input("Código de identificación de la empresa: ")

