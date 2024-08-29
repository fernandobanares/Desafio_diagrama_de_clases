from usuario import Usuario

class ListadoRespuestas:
    def __init__(self, usuario: str, respuestas: str):
        self.usuario = usuario
        self.respuestas = respuestas

    def mostrar(self):
        return f"Usuario: {self.usuario.correo}\nRespuestas: {self.respuestas}"
