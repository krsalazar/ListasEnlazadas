class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.head is None:
            self.head = nuevo_nodo
            return
        ultimo_nodo = self.head
        while ultimo_nodo.next:
            ultimo_nodo = ultimo_nodo.next
        ultimo_nodo.next = nuevo_nodo

    def imprime_lista(self):
        actual_nodo = self.head
        while actual_nodo:
            print(actual_nodo.dato, end=" -> ")
            actual_nodo = actual_nodo.next
        print("Null")

# Ejemplo de uso
if __name__ == "__main__":
    lista_enlazada = ListaEnlazada()
    lista_enlazada.agregar(1)
    lista_enlazada.agregar(2)
    lista_enlazada.agregar(3)
    lista_enlazada.imprime_lista()
