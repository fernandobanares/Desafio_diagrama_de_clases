class Usuario:
    def __init__(self, correo, edad, region):
        self.correo = correo
        self.edad = edad
        self.region = region

    def modificar_correo(self, nuevo_correo):
        self.correo = nuevo_correo

    def modificar_edad(self, nueva_edad):
        self.edad = nueva_edad

    def modificar_region(self, nueva_region):
        self.region = nueva_region

    def contestar_encuesta(self, encuesta, listado_respuestas):
        encuesta.agregar_respuestas(listado_respuestas)
