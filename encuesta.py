from pregunta import Pregunta

class Encuesta:
    def __init__(self, nombre, preguntas=None):
        self.nombre = nombre
        self.preguntas = preguntas if preguntas else []
        self.listados_respuestas = []

    def mostrar(self):
        resultado = f"Encuesta: {self.nombre}\n"
        for pregunta in self.preguntas:
            resultado += pregunta.mostrar() + "\n"
        return resultado

    def agregar_respuestas(self, listado_respuestas):
        self.listados_respuestas.append(listado_respuestas)

    def modificar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre, edad_min, edad_max, preguntas=None):
        super().__init__(nombre, preguntas)
        self.edad_min = edad_min
        self.edad_max = edad_max

    def agregar_respuestas(self, listado_respuestas):
        if self.edad_min <= listado_respuestas.usuario.edad <= self.edad_max:
            super().agregar_respuestas(listado_respuestas)
        else:
            print("Usuario fuera del rango de edad permitido.")

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, regiones_permitidas, preguntas=None):
        super().__init__(nombre, preguntas)
        self.regiones_permitidas = regiones_permitidas

    def agregar_respuestas(self, listado_respuestas):
        if listado_respuestas.usuario.region in self.regiones_permitidas:
            super().agregar_respuestas(listado_respuestas)
        else:
            print("Usuario fuera de las regiones permitidas.")
