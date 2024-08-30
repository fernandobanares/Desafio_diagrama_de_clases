# usuario.py
from typing import Union
from encuesta import Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion
from listado_respuestas import ListadoRespuestas

class Usuario:
    def __init__(self, correo: str, edad: int, region: int):
        self.correo = correo
        self.edad = edad
        self.region = region

    @property
    def correo(self) -> str:
        return self.__correo

    @correo.setter
    def correo(self, correo: str) -> None:
        self.__correo = correo

    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self, edad: int) -> None:
        self.__edad = edad

    @property
    def region(self) -> int:
        return self.__region

    @region.setter
    def region(self, region: int) -> None:
        self.__region = region

    def contestar_encuesta(self, encuesta: Union[Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion], respuestas: list) -> None:
        listado_respuestas = ListadoRespuestas(self, respuestas)
        encuesta.agregar_respuesta(listado_respuestas)

