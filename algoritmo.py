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
            where = self.whereIsRuleApplyWithVariables ( cadena )
            if where == None:
                return cadena
            else:
                return self.ruleApply ( cadena, where )
        else:
            v1 = self.funcionEspecial ( cadena )
            if self.isRuleApply ( v1 ):
                where = self.whereIsRuleApply ( v1 )
                return self.ruleApply ( cadena, where )
            else:
                return cadena
    
    def whereIsRuleApplyWithVariables ( self, cadena ):
        cadenaAuxiliar = cadena
        contador = 0
        while contador < len ( cadena ):
            if contador > ( len ( cadena ) - self.longitud ):
                return None
            v1 = self.funcionEspecial ( cadenaAuxiliar )
            print ( self.marcador )
            print ( cadenaAuxiliar )
            print ( v1 )
            if self.isRuleApplyWithVariables ( v1 ):
                return contador
            else:
                cadenaAuxiliar = cadena [ contador + 1: len ( cadena ) ]
                contador = contador + 1
                self.marcador = self.marcadorOriginal
    
    def isRuleApplyWithVariables ( self, v1 ):
        contador = 0
        while contador < len ( v1 ) and v1 [ contador ] != 0:
            contador = contador + 1
        # print ( contador )
        if contador == self.longitud:
            return True
        else:
            return False
    
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
            # print ( self.marcador [ posicionDeLaRegla ] )
            if self.isVariable ( self.marcador [ posicionDeLaRegla ] ) and not x in self.marcadorOriginal:
                # print ( '¡Una variable!' )
                # self.fixMarker ( self.marcador [ posicionDeLaRegla ], x )
                self.marcador = self.marcador.replace ( self.marcadorOriginal [ posicionDeLaRegla], x )
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
    
    def fixMarker ( self, antes, despues ):
        # print ( antes + '->' + despues )
        auxiliar = ''
        for x in self.marcadorOriginal:
            if x == antes:
                auxiliar = auxiliar + despues
            else:
                auxiliar = auxiliar + x
        self.marcador = auxiliar
        # print ( auxiliar )
    
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

# R1 = Regla ( 'AAA', 'apple' )

# print ( R1.funcionEspecial ( 'ABCABCABCAAA' ) )
# print ( R1.vivaRusia ( 'ABCABCABCAAA' ) )

R2 = Regla ( 'xyA', 'apple' )
C1 = 'BCBCAAABCA'

print ( R2.marcadorOriginal + ' -> ' + R2.regla )
print ( C1 )
print ( R2.vivaRusia ( C1 ) )
print ( C1 )