#Autores: Justin Vega Madrigal (116550095)

marcadores=['A', 'B', 'C', 'D', "theshop"]
reglas = [ 'apple', 'bag', 'shop', "the", "mybrother"]
cadenaDeEntrada = 'DC'

class Regla:
    
    def __init__( self, marcador, regla ):
        self.marcador = marcador
        self.regla = regla
        self.longitud = len ( marcador )
    
    def vivaRusia ( self, cadena ):
        v1 = self.funcionEspecial ( cadena )
        if self.isRuleApply ( v1 ):
            return True
        else:
            return False
        
    def funcionEspecial ( self, cadena ):
        # cadenaAuxiliar = self.crearCadenaAuxiliar ( cadena )
        auxiliar = self.crearAuxiliar ( cadena )
        posicionDelVector = 0
        posicionDeLaRegla = 0
        for x in cadena:
            if x == self.marcador [ posicionDeLaRegla ]:
                posicionDeLaRegla = posicionDeLaRegla + 1
                auxiliar [ posicionDelVector ] = posicionDeLaRegla
            else:
                posicionDeLaRegla = 0
            if posicionDeLaRegla == self.longitud:
                posicionDeLaRegla = 0
            posicionDelVector = posicionDelVector + 1
        return auxiliar
    
    def isRuleApply ( self, v1 ):
        for x in v1:
            if x == self.longitud:
                return True
        return False
    
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

R1 = Regla ( 'AA', 'apple' )

print ( R1.funcionEspecial ( 'ABCABCABCAAA' ) )
print ( R1.vivaRusia ( 'ABCABCABCAAA' ) )

R2 = Regla ( 'BB', 'apple' )

print ( R2.funcionEspecial ( 'ABCABCABCAAA' ) )
print ( R2.vivaRusia ( 'ABCABCABCAAA' ) )