# Autores: Justin Vega Madrigal ( 116550095 )
# Diseñador: Justin Vega Madrigal ( 116550095 )

from algoritmo import Regla

class Markov:

    def __init__ ( self, reglas ):
        self.reglas = reglas
        self.reglaSiguiente = 0
    
    def runAlgorithm ( self, cadena ):
        isEnd = 0
        count = 0
        lista = []
        cadenaAuxiliar = cadena
        while ( isEnd <= 100 ):
            isEnd = isEnd + 1
            if isEnd == 100:
                return lista
            if count + 1 > len ( self.reglas ):
                # print ( self.reglas [ count ].marcadorOriginal + ' -> ' + self.reglas [ count ].regla + ' : ' + self.reglas [ count ].vivaRusia ( cadenaAuxiliar ) )
                # return self.reglas [ count ].vivaRusia ( cadenaAuxiliar )
                return lista
            elif self.reglas [ count ].isEnd and cadena != cadenaAuxiliar:
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
    
    def algorithmStepByStep ( self, cadena ):
        auxiliar = self.reglaSiguiente
        if self.reglaSiguiente == None:
            return cadena
        elif self.reglas [ auxiliar ].isEnd or auxiliar >= len ( self.reglas ):
            self.reglaSiguiente = None
            print ( self.reglas [ auxiliar ].marcadorOriginal + ' -> ' + self.reglas [ auxiliar ].regla + ' : ' + self.reglas [ auxiliar ].vivaRusia ( cadena ) )
            return self.reglas [ auxiliar ].vivaRusia ( cadena )
        else:
            self.reglaSiguiente = self.reglaSiguiente + 1
            print ( self.reglas [ auxiliar ].marcadorOriginal + ' -> ' + self.reglas [ auxiliar ].regla + ' : ' + self.reglas [ auxiliar ].vivaRusia ( cadena ) )
            return self.reglas [ auxiliar ].vivaRusia ( cadena )
    
    def restart ( self ):
        self.reglaSiguiente = 0


# C1 = 'Aabc'
# V1 = ( 'x', 'y', 'z' )
# R1 = Regla ( 'Ax', 'xBxA', 1, False, V1 )
# R2 = Regla ( 'Bx', 'xB', None, False, V1 )
# R3 = Regla ( '0', '', None, False, V1 )
# R4 = Regla ( 'J', 'justin', None, False, V1 )

# M1 = Markov ( [ R1 ] )
# print ( M1.runAlgorithm ( C1 ) )


# C1 = M1.algorithmStepByStep ( C1 )
# C1 = M1.algorithmStepByStep ( C1 )
# C1 = M1.algorithmStepByStep ( C1 )