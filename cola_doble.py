class ColaDoble:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    # Asumimos que el frente de la Cola Doble corresponde al final de la lista
    def agregarFrente(self, item):
        self.items.append(item)

    # Asumimos que el final de la Cola Doble corresponde al inicio de la lista
    def agregarFinal(self, item):
        self.items.insert(0, item)

    # Devuelve y elimina el item del frente de la lista
    def removerFrente(self):
        return self.items.pop()

    # Devuelve y elimina el item del final de la lista
    def removerFinal(self):
        return self.items.pop(0)

    def tamano(self):
        return len(self.items)

    def inspeccionarFrente(self):
        return self.items[len(self.items) - 1]

    def inspeccionarFinal(self):
        return self.items[0]
