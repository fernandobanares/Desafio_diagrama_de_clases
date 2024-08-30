from pregunta import Pregunta
from listado_respuestas import ListadoRespuestas

class Encuesta():
    def __init__(self, nombre: str, preguntas: list) -> None:
        self.nombre = nombre
        self.__preguntas = preguntas
        self.__listados_respuestas = []

    def agregar_respuesta(self, listado_respuestas: ListadoRespuestas) -> None:
        self.__listados_respuestas.append(listado_respuestas)

    def mostrar(self) -> None:
        print(f"Encuesta: {self.nombre}")
        for pregunta in self.__preguntas:
            pregunta.mostrar_pregunta()

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, edad_min: int, edad_max: int, preguntas: list) -> None:
        super().__init__(nombre, preguntas)
        self.__edad_min = edad_min
        self.__edad_max = edad_max

    def agregar_respuesta(self, listado_respuestas: ListadoRespuestas) -> None:
        usuario = listado_respuestas.usuario
        if self.__edad_min <= usuario.edad <= self.__edad_max:
            super().agregar_respuesta(listado_respuestas)
        else:
            print(f"Usuario {usuario.correo} no está dentro del rango de edad permitido.")

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre: str, regiones: list, preguntas: list) -> None:
        super().__init__(nombre, preguntas)
        self.__regiones = regiones

    def agregar_respuesta(self, listado_respuestas: ListadoRespuestas) -> None:
        usuario = listado_respuestas.usuario
        if usuario.region in self.__regiones:
            super().agregar_respuesta(listado_respuestas)
        else:
            print(f"Usuario {usuario.correo} no está en una región permitida.")

        
    