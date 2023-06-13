# clase Comentario
#  id, id_articulo, id_usuario, contenido, fecha_hora, estado
from datetime import datetime

class Comentario:
    def __init__(self, id, id_articulo, id_usuario, contenido):
        self.id = id
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = datetime.now() #no la espesifico arriba para que de esta forma tome la fecha y hora en la que se ejecuta
        self.estado = "activo"

    def mostrar_atributos(self):
        fecha_hora_formateada = self.fecha_hora.strftime("%Y-%m-%d %H:%M")
        print("id de comentario: ", self.id)
        print("id de articulo: ", self.id_articulo)
        print("id de usuario: ", self.id_usuario)
        print("comentario: ", self.contenido)
        print("fecha y hora del comentario: ", fecha_hora_formateada)
        print("estado: ", self.estado)

    def cambiar_estado(self, nuevo_estado): #para cambiar de estado de arctivo a inactivo
        self.estado = nuevo_estado


#prueba
mi_comentario = Comentario(1, 1, 1, "este codigo esta masomenos echo, con el resto del codigo de mis compañeros quedaria mas completo")
mi_comentario.mostrar_atributos()
