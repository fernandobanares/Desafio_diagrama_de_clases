class Usuario:
    def __init__(self, correo: str, edad: int, region: str):
        self.correo = correo
        self.edad = edad
        self.region = region

    def modificar_correo(self, nuevo_correo: str):
        self.correo = nuevo_correo

    def modificar_edad(self, nueva_edad: int):
        self.edad = nueva_edad

    def modificar_region(self, nueva_region: str):
        self.region = nueva_region

    def contestar_encuesta(self, encuesta: str, listado_respuestas: str):
        encuesta.agregar_respuestas(listado_respuestas)
