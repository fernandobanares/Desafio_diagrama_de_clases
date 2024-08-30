from usuario import Usuario

class ListadoRespuestas():
    def __init__(self, usuario: Usuario, respuestas: list) -> None:
        self.__usuario = usuario
        self.__respuestas = respuestas    
    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @property
    def respuestas(self) -> list:
        return self.__respuestas

    def mostrar(self):
        return f"Usuario: {self.usuario.correo}\nRespuestas: {self.respuestas}"
