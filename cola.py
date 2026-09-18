class cola:

    def __init__(self):
        self.documentos = []

    def agregar(self, documento):
        self.documentos.append(documento)

    def sacar(self):
        if len(self.documentos) > 0:
            return self.documentos.pop(0)

    def primero(self):
        if len(self.documentos) > 0:
            return self.documentos[0]

    def esta_vacia(self):
        return len(self.documentos) == 0