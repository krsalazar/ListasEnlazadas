class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prev = None
        self.next = None

class ListaDobleEnlazada:
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
        nuevo_nodo.prev = ultimo_nodo

    def imprime_adelante(self):
        actual_nodo = self.head
        while actual_nodo:
            print(actual_nodo.dato, end=" -> ")
            actual_nodo = actual_nodo.next
        print("Vacio")

    def imprime_atras(self):
        ultimo_nodo = None
        actual_nodo = self.head
        while actual_nodo:
            ultimo_nodo = actual_nodo
            actual_nodo = actual_nodo.next
        while ultimo_nodo:
            print(ultimo_nodo.dato, end=" -> ")
            ultimo_nodo = ultimo_nodo.prev
        print("Vacio")

# Crear lista doblemente enlazada con valores proporcionados por el usuario
def create_doubly_lista_enlazada():
    lista_enlazada = ListaDobleEnlazada()
    n = int(input("Ingresa la cantidad de nodos: "))
    for i in range(n):
        dato = input(f"Ingresa el valor del nodo {i + 1}: ")
        lista_enlazada.agregar(dato)
    return lista_enlazada

# Ejemplo de uso
if __name__ == "__main__":
    doubly_lista_enlazada = create_doubly_lista_enlazada()
    print("Lista enlazada hacia adelante:")
    doubly_lista_enlazada.imprime_adelante()
    print("Lista enlazada hacia atrás:")
    doubly_lista_enlazada.imprime_atras()
