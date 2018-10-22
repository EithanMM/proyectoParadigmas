# Autores: Justin Vega Madrigal ( 116550095 )
# Diseñador: Justin Vega Madrigal ( 116550095 )

from algoritmo import Regla

class Markov:

    def __init__ ( self, reglas ):
        self.reglas = reglas
    
    # El método "runAlgorithm" aplica un conjunto de reglas de producción o sustitución a la hilera
    # de entrada (cadena), la forma de aplicar dichas reglas forma un sistema de reescritura o sus-
    # titución llamado Algoritmo de Markov.
    
    def runAlgorithm ( self, cadena ):
        isEnd = 0
        count = 0
        lista = []
        cadenaAuxiliar = cadena
        while ( isEnd <= 100 ): # Detiene la ejecución después de 100 interaciones para evitar cic-
            isEnd = isEnd + 1   # clos infinítos.
            if isEnd == 100:
                return lista
            if count + 1 > len ( self.reglas ):
                return lista
            elif self.reglas [ count ].isEnd:
                otraCadenaAuxiliar = self.reglas [ count ].clearString ( cadenaAuxiliar )
                if cadenaAuxiliar != otraCadenaAuxiliar:
                    temp = self.reglas [ count ].marcadorOriginal + ' -> ' + self.reglas [ count ].reglaOriginal + ' : ' + self.reglas [ count ].clearString ( cadenaAuxiliar )
                    lista.append(temp)
                    return lista
            cadenaAuxiliar = self.reglas [ count ].clearString ( cadenaAuxiliar )
            if cadena == cadenaAuxiliar:
                temp = self.reglas [ count ].marcadorOriginal + ' -> ' + self.reglas [ count ].reglaOriginal + ' : ' + self.reglas [ count ].clearString ( cadenaAuxiliar )
                lista.append(temp)
                count = count + 1
            else:
                temp = self.reglas [ count ].marcadorOriginal + ' -> ' + self.reglas [ count ].reglaOriginal + ' : ' + cadenaAuxiliar
                lista.append(temp)
                cadena = cadenaAuxiliar
                if self.reglas [ count ].etiqueta != None:
                    count = self.reglas [ count ].etiqueta - 1
                else:
                    count = 0
    
    