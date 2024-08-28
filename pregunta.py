from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado, ayuda=None, es_requerida=False, alternativas=None):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.es_requerida = es_requerida
        self.alternativas = alternativas if alternativas else []

    def mostrar(self):
        resultado = f"{self.enunciado}\n"
        if self.ayuda:
            resultado += f"Ayuda: {self.ayuda}\n"
        resultado += "Alternativas:\n"
        for alternativa in self.alternativas:
            resultado += f" - {alternativa.mostrar()}\n"
        return resultado

    def modificar_enunciado(self, nuevo_enunciado):
        self.enunciado = nuevo_enunciado

    def modificar_ayuda(self, nueva_ayuda):
        self.ayuda = nueva_ayuda
