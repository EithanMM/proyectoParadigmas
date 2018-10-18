# Autores: Justin Vega Madrigal ( 116550095 )
# Diseñador: Justin Vega Madrigal ( 116550095 )

from algoritmo import Regla

class Markov:

    def __init__ ( self, reglas ):
        self.reglas = reglas
        self.reglaSiguiente = 0
    
    def runAlgorithm ( self, cadena ):
        return self.algorithm ( cadena, cadena )
    
    def algorithm ( self, cadena, cadenaAuxiliar , isEndRule = False, count = 0 ):
        ideaDeEithan = cadenaAuxiliar
        if isEndRule:
            return ideaDeEithan
        elif count == len ( self.reglas ):
            return ideaDeEithan
        elif cadena == cadenaAuxiliar:
            print ( self.reglas [ count ].marcadorOriginal + ' -> ' + self.reglas [ count ].regla + ' : ' + self.reglas [ count ].vivaRusia ( cadenaAuxiliar ) )
            return self.algorithm ( cadenaAuxiliar, self.reglas [ count ].vivaRusia ( cadenaAuxiliar ), self.reglas [ count ].isEnd, count + 1 )
        else:
            print ( self.reglas [ count ].marcadorOriginal + ' -> ' + self.reglas [ count ].regla + ' : ' + self.reglas [ count ].vivaRusia ( cadenaAuxiliar ) )
            return self.algorithm ( cadenaAuxiliar, self.reglas [ 0 ].vivaRusia ( cadenaAuxiliar), self.reglas [ 0 ].isEnd, 0 )

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

C1 = 'ABBABB'
R1 = Regla ( 'xyA', 'apple', False )
R2 = Regla ( 'B', 'banana', True )

M1 = Markov ( ( R1, R2 ) )
print ( M1.runAlgorithm ( C1 ) )

C1 = M1.algorithmStepByStep ( C1 )
C1 = M1.algorithmStepByStep ( C1 )
C1 = M1.algorithmStepByStep ( C1 )