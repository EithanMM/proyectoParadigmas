#Autores: Justin Vega Madrigal (116550095)

marcadores=['A', 'B', 'C', 'D', "theshop"]
reglas = [ 'apple', 'bag', 'shop', "the", "mybrother"]
cadenaDeEntrada = 'DC'

class Regla:
    
    def __init__( self, marcador, regla ):
        self.marcador = marcador
        self.regla = regla
        self.longitud = len ( marcador )
        
    def funcionEspecial ( self, cadena ):
        cadenaAuxiliar = self.crearCadenaAuxiliar ( cadena )
        auxiliar = self.crearAuxiliar ( cadena )
        posicionDelVector = 0
        posicionDeLaRegla = 0
        for x in cadenaAuxiliar:
            if x == self.marcador [ posicionDeLaRegla ]:
                posicionDeLaRegla = posicionDeLaRegla + 1
                auxiliar [ posicionDelVector ] = posicionDeLaRegla
            else:
                posicionDeLaRegla = 0
            if posicionDeLaRegla == self.longitud:
                posicionDeLaRegla = 0
            posicionDelVector = posicionDelVector + 1
        print ( auxiliar )
    
    def crearCadenaAuxiliar ( self, cadena ):
        cadenaAuxiliar = [ ]
        x = 0
        while x < len ( cadena ):
            cadenaAuxiliar.append ( cadena [ x ] )
            x = x + 1
        return cadenaAuxiliar
    
    def crearAuxiliar ( self, cadenaDeEntrada ):
        auxiliar = [ ]
        x = 0
        while x < len ( cadenaDeEntrada ):
            auxiliar.append ( 0 )
            x = x + 1
        return auxiliar

R1 = Regla ( 'A', 'apple' )

#R1.funcionEspecial ( 'A' )
#R1.funcionEspecial ( 'AB' )
R1.funcionEspecial ( 'ABC' )