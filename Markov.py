# Autores: Justin Vega Madrigal ( 116550095 )
# Diseñador: Justin Vega Madrigal ( 116550095 )

from algoritmo import Regla

class Markov:

    def __init__ ( self, reglas ):
        self.reglas = reglas
        self.reglaSiguiente = 0
    
    def runAlgorithm ( self, cadena ):
        isEnd = False
        count = 0
        cadenaAuxiliar = cadena
        while ( isEnd == False ):
            if count + 1 == len ( self.reglas ):
                print ( self.reglas [ count ].marcadorOriginal + ' -> ' + self.reglas [ count ].regla + ' : ' + self.reglas [ count ].vivaRusia ( cadenaAuxiliar ) )
                return self.reglas [ count ].vivaRusia ( cadenaAuxiliar )
            elif self.reglas [ count ].isEnd:
                print ( self.reglas [ count ].marcadorOriginal + ' -> ' + self.reglas [ count ].regla + ' : ' + self.reglas [ count ].vivaRusia ( cadenaAuxiliar ) )
                return self.reglas [ count ].vivaRusia ( cadenaAuxiliar )
            cadenaAuxiliar = self.reglas [ count ].vivaRusia ( cadenaAuxiliar )
            if cadena == cadenaAuxiliar:
                print ( self.reglas [ count ].marcadorOriginal + ' -> ' + self.reglas [ count ].regla + ' : ' + self.reglas [ count ].vivaRusia ( cadenaAuxiliar ) )
                count = count + 1
            else:
                print ( self.reglas [ count ].marcadorOriginal + ' -> ' + self.reglas [ count ].regla + ' : ' + cadenaAuxiliar )
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

C1 = 'ABBBB'
V1 = ( 'x', 'y', 'z' )
V2 = [ 'x', 'y', 'z' ]
R1 = Regla ( 'A', 'X', None, False, V1, V2 )
R2 = Regla ( 'Xx', 'xX', 2, False, V1, V2 )
R3 = Regla ( 'X', 'Y', None, False, V1, V2 )

M1 = Markov ( [ R1, R2, R3 ] )
print ( M1.runAlgorithm ( C1 ) )

# C1 = M1.algorithmStepByStep ( C1 )
# C1 = M1.algorithmStepByStep ( C1 )
# C1 = M1.algorithmStepByStep ( C1 )