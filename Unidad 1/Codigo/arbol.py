class nodo:
    izq , der, dato = None, None, 0
 
    def __init__(self, dato):
        # crea un nodo
        self.izq = None
        self.der = None
        self.dato = dato
 
class arbolBinario:
    def __init__(self):
        # inicializa la raiz
        self.raiz = None
 
    def agregarNodo(self, dato):
        # crea un nuevo nodo y lo devuelve
        return nodo(dato)
 
    def insertar(self, raiz, dato):
        # inserta un dato nuevo en el �rbol
        if raiz == None:
            # si no hay nodos en el �rbol lo agrega
            return self.agregarNodo(dato)
        else:
            # si hay nodos en el �rbol lo recorre
            if dato <= raiz.dato:
                # si el dato ingresado es  menor que el dato guardado va al sub�rbol izquierdo
                raiz.izq = self.insertar(raiz.izq, dato)
            else:
                # si no, procesa el sub�rbol derecho
                raiz.der = self.insertar(raiz.der, dato)
            return raiz
 
