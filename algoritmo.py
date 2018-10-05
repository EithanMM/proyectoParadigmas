#Autores: Justin Vega Madrigal (116550095)

marcadores=['A', 'B', 'C', 'D', "theshop"]
reglas = [ 'apple', 'bag', 'shop', "the", "mybrother"]
cadenaDeEntrada = 'DC'

class Regla:
    
    def __init__( self, etiqueta, regla ):
        self.etiqueta = etiqueta
        self.regla = regla
        self.longitud = len ( etiqueta )
        self.auxiliar = []
        for x in etiqueta:
            self.auxiliar.append ( bool ( 0 ) )

R1 = Regla ( 'A', 'apple' )

print ( R1.etiqueta )
print ( R1.regla )
print ( R1.longitud )
print ( R1.auxiliar )