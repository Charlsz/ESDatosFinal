class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

    
    def __repr__(self):
        return str(self.data)

class CircularDoublyLinkedList:
    def __init__(self):
        self.PTR = None
        self.ULT = None

    def AddNode(self,data):
        P = Nodo(data)
        if(self.PTR==None):
            self.PTR = P
            self.PTR = P
        else:
            
            self.ULT.next = P
            P.prev = self.ULT
            self.ULT = P
        self.ULT.next = self.PTR
        self.PTR.prev = self.ULT 
    
    def __repr__(self):
        P = self.ULT
        P = P.prev
        while(P != self.ULT):
              P = P.prev
    
    def mover_siguiente(self):
        self.P = self.P.next
    
    def mover_atras(self):
        self.P = self.P.prev
    """
        
    """
    def Find_And_Change(self, valor, change, posicion):
        P = self.PTR
        sw = 0
        c = 0
        while(sw == 0):
            if (P.data == valor):
                sw = 1
                Q = P.data
                print("valor encontrado, se cambiara por el nodo en la posicion: ", change)
                if(posicion == 1):
                    print("a la derecha")
                    while(c<=change):
                        P = P.next
                        if (c==change):
                            X = P.data
                            
                        c = c + 1
                else:
                    if(posicion==2):
                        print("a la izquierda")
                        while(c<=change):
                            P = P.prev
                            if(c==change):
                                X = P.data
                            c = c + 1
            else:
                    P = P.next
                    