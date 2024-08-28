class Alternativa:
    def __init__(self, contenido, ayuda=None):
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar(self):
        if self.ayuda:
            return f"{self.contenido} (Ayuda: {self.ayuda})"
        return self.contenido

    def modificar_contenido(self, nuevo_contenido):
        self.contenido = nuevo_contenido

    def modificar_ayuda(self, nueva_ayuda):
        self.ayuda = nueva_ayuda
