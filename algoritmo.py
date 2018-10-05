#Autores: Justin Vega Madrigal (116550095)

marcadores=['A', 'B', 'C', 'D', "theshop"]
reglas = [ 'apple', 'bag', 'shop', "the", "mybrother"]
cadenaDeEntrada = 'DC'

class Regla:
    
    def __init__( self, etiqueta, regla ):
        self.etiqueta = etiqueta
        self.regla = regla
        self.longitud = len ( etiqueta )
        
    def funcionEspecial ( self, cadena ):
        auxiliar = self.crearAuxiliar ( )
        contador = 0
        contadorDeEtiqueta = 0
        for x in cadena:
            if x == self.etiqueta [ contadorDeEtiqueta ]:
                auxiliar [ contadorDeEtiqueta ] = bool ( 1 )
                contadorDeEtiqueta = contadorDeEtiqueta + 1
        contador = contador + 1
        return self.cantidadDeMatches ( auxiliar )
    
    def crearAuxiliar ( self ):
        auxiliar = [ ]
        for x in self.etiqueta:
            auxiliar.append ( bool ( 0 ) )
        return auxiliar

    def cantidadDeMatches ( self, lista ):
        matches = 0
        for x in lista:
            if x == bool ( 1 ):
                matches = matches = 1
        if self.longitud == matches:
            return bool ( 1 )
        else:
            return bool ( 0 )

R1 = Regla ( 'A', 'apple' )

print ( R1.funcionEspecial ( 'A' ) )
print ( R1.etiqueta )
print ( R1.regla )
print ( R1.longitud )