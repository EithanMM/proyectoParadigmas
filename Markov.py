# Autores: Justin Vega Madrigal ( 116550095 )

from algoritmo import Regla

class Markov:

    def __init__ ( self, reglas ):
        self.reglas = reglas
        self.reglaSiguiente = 0
    
    def runAlgorithm ( self, cadena, cadenaAuxiliar, isEndRule, count ):
        print ( cadena )
        print ( cadenaAuxiliar )
        print ( isEndRule )
        print ( count )
        print ( '----------')
        if isEndRule:
            return cadenaAuxiliar
        elif count == len ( self.reglas ):
            return cadenaAuxiliar
        elif cadena == cadenaAuxiliar:
            self.runAlgorithm ( cadenaAuxiliar, self.reglas [ count ].vivaRusia ( cadenaAuxiliar ), self.reglas [ count ].isEnd, count + 1 )
        else:
            self.runAlgorithm ( cadenaAuxiliar, self.reglas [ 0 ].vivaRusia ( cadenaAuxiliar), self.reglas [ 0 ].isEnd, 0 )


R1 = Regla ( 'A', 'apple', False )
print ( R1.marcador + ' -> ' + R1.regla )
R2 = Regla ( 'B', 'banana', True )
print ( R2.marcadorOriginal + ' -> ' + R2.regla )

M1 = Markov ( ( R1, R2 ) )
print ( M1.runAlgorithm ( 'AB', 'AB', False, 0 ) )