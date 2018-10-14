#Autores: Justin Vega Madrigal (116550095)

variables = [ 'x', 'y', 'z' ]

class Regla:
    
    def __init__( self, marcador, regla ):
        self.marcadorOriginal = marcador
        self.marcador = marcador
        self.regla = regla
        self.longitud = len ( marcador )
    
    def vivaRusia ( self, cadena ):
        if self.isVariable ( self.marcadorOriginal [ 0 ] ):
            print ( 'No tengo idea de como resolver esto.' )
            return None
        else:
            v1 = self.funcionEspecial ( cadena )
        if self.isRuleApply ( v1 ):
            where = self.whereIsRuleApply ( v1 )
            return self.ruleApply ( cadena, where )
        else:
            return cadena
    
    def isVariable ( self, otraX ):
        for x in variables:
            if x == otraX:
                return True
        return False
        
    def funcionEspecial ( self, cadena ):
        # cadenaAuxiliar = self.crearCadenaAuxiliar ( cadena )
        auxiliar = self.crearAuxiliar ( cadena )
        posicionDelVector = 0
        posicionDeLaRegla = 0
        for x in cadena:
            if self.isMatch ( x, self.marcador [ posicionDeLaRegla ] ):
            # if x == self.marcador [ posicionDeLaRegla ]:
                posicionDeLaRegla = posicionDeLaRegla + 1
                auxiliar [ posicionDelVector ] = posicionDeLaRegla
            else:
                posicionDeLaRegla = 0
            if posicionDeLaRegla == self.longitud:
                posicionDeLaRegla = 0
            posicionDelVector = posicionDelVector + 1
        return auxiliar
    
    def isMatch ( self, posicionDeLaCadena, posicionDeLaRegla ):
        # print ( posicionDeLaCadena + ' == ' + posicionDeLaRegla )
        if posicionDeLaCadena == posicionDeLaRegla:
            return True
        else:
            return False
    
    def isRuleApply ( self, v1 ):
        for x in v1:
            if x == self.longitud:
                return True
        return False
    
    def whereIsRuleApply ( self, v1 ):
        contador = 0
        for x in v1:
            if x == self.longitud:
                if self.longitud == 0:
                    return contador
                return ( contador - ( self.longitud - 1 ) )
            contador = contador + 1
    
    def ruleApply ( self, cadena, where ):
        nuevaCadena = ''
        contador = 0
        while contador < len ( cadena ):
            if contador == where:
                nuevaCadena = nuevaCadena + self.regla
                contador = contador + ( self.longitud )
            else:
                nuevaCadena = nuevaCadena + cadena [ contador ]
                contador = contador + 1
        return nuevaCadena
    
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

R1 = Regla ( 'AAA', 'apple' )

print ( R1.funcionEspecial ( 'ABCABCABCAAA' ) )
print ( R1.vivaRusia ( 'ABCABCABCAAA' ) )

R2 = Regla ( 'xyA', 'apple' )

print ( R2.funcionEspecial ( 'ABCABCABC' ) )
print ( R2.vivaRusia ( 'ABCABCABC' ) )