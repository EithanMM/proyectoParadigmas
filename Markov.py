# Autores: Justin Vega Madrigal ( 116550095 )

from algoritmo import Regla

class Markov:

    def __init__ ( self, reglas ):
        self.reglas = reglas
        self.reglaSiguiente = 0
    
    def runAlgorithm ( self, cadena, cadenaAuxiliar, isEndRule, count ):
        ideaDeEithan = cadenaAuxiliar
        if isEndRule:
            return ideaDeEithan
        elif count == len ( self.reglas ):
            return ideaDeEithan
        elif cadena == cadenaAuxiliar:
            return self.runAlgorithm ( cadenaAuxiliar, self.reglas [ count ].vivaRusia ( cadenaAuxiliar ), self.reglas [ count ].isEnd, count + 1 )
        else:
            return self.runAlgorithm ( cadenaAuxiliar, self.reglas [ 0 ].vivaRusia ( cadenaAuxiliar), self.reglas [ 0 ].isEnd, 0 )

C1 = 'ABBABB'
R1 = Regla ( 'xyA', 'apple', False )
print ( R1.vivaRusia ( C1 ) )
print ( R1.marcador + ' -> ' + R1.regla )
R2 = Regla ( 'B', 'banana', True )
print ( R2.marcadorOriginal + ' -> ' + R2.regla )

M1 = Markov ( ( R1, R2 ) )
Aux = M1.runAlgorithm ( C1, C1, False, 0 )
print ( Aux )