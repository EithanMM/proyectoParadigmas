#Autores: Justin Vega Madrigal (116550095)

# variables = [ 'x', 'y', 'z' ]

class Regla:
    
    def __init__( self, marcador, regla, etiqueta, isEnd, variables ):
        self.marcadorOriginal = marcador
        self.marcador = marcador
        self.reglaOriginal = regla
        self.regla = regla
        self.etiqueta = etiqueta
        self.longitud = len ( marcador )
        self.isEnd = isEnd
        self.variablesOriginales = variables
    
    def vivaRusia ( self, cadena ):
        if self.isVariable ( self.marcadorOriginal [ 0 ] ):
            where = self.whereIsRuleApplyWithVariables ( cadena )
            if where == None:
                return cadena
            else:
                self.regla = self.reglaOriginal
                self.fixRule ( )
                return self.ruleApply ( cadena, where )
        else:
            v1 = self.funcionEspecial ( cadena )
            if self.isRuleApply ( v1 ):
                where = self.whereIsRuleApply ( v1 )
                # self.regla = self.reglaOriginal
                self.regla = self.fixRule ( )
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
            # print ( self.marcador )
            # print ( cadenaAuxiliar )
            # print ( v1 )
            if self.isRuleApplyWithVariables ( v1 ):
                return contador
            else:
                cadenaAuxiliar = cadena [ contador + 1: len ( cadena ) ]
                contador = contador + 1
                self.marcador = self.marcadorOriginal
    
    def isRuleApplyWithVariables ( self, v1 ):
        contador = 0
        while v1 [ contador ] != 0 and contador + 1 == v1 [ contador ]:
            contador = contador + 1
        # print ( contador )
        if contador == self.longitud:
            return True
        else:
            return False
    
    def isVariable ( self, otraX ):
        for x in self.variablesOriginales:
            if x == otraX:
                return True
        return False
        
    def funcionEspecial ( self, cadena ):
        # cadenaAuxiliar = self.crearCadenaAuxiliar ( cadena )
        auxiliar = self.crearAuxiliar ( cadena )
        posicionDelVector = 0
        posicionDeLaRegla = 0
        while posicionDelVector < len ( cadena ):
            # print ( self.marcador [ posicionDeLaRegla ] )
            if self.isVariable ( self.marcador [ posicionDeLaRegla ] ) and not x in self.marcador:
                # print ( '¡Una variable!' )
                # self.fixMarker ( self.marcador [ posicionDeLaRegla ], x )
                self.marcador = self.marcador.replace ( self.marcadorOriginal [ posicionDeLaRegla], x )
            if self.isMatch ( cadena [ posicionDelVector ], self.marcador [ posicionDeLaRegla ] ):
            # if x == self.marcador [ posicionDeLaRegla ]:
                posicionDeLaRegla = posicionDeLaRegla + 1
                auxiliar [ posicionDelVector ] = posicionDeLaRegla
            else:
                posicionDeLaRegla = 0
                if auxiliar [ posicionDelVector - 1 ] != 0:
                    posicionDelVector = posicionDelVector - 1
            if posicionDeLaRegla == self.longitud:
                posicionDeLaRegla = 0
            posicionDelVector = posicionDelVector + 1
        print ( auxiliar )
        return auxiliar
    
    def crearVariablesAuxiliares ( self ):
        v1 = []
        for x in self.variablesOriginales:
            v1.append ( x )
        return v1
    
    def fixRule ( self ):
        reglaAuxiliar = ''
        variablesAuxiliares = self.crearVariablesAuxiliares ( )
        contador = 0
        for x in self.marcadorOriginal:
            if x in self.variablesOriginales:
                otroContador = 0
                for y in variablesAuxiliares:
                    if x == y:
                        variablesAuxiliares [ otroContador ] = self.marcador [ contador ]
                    otroContador = otroContador + 1
            contador = contador + 1
        contador = 0
        for x in self.reglaOriginal:
            if x in self.variablesOriginales:
                otroContador = 0
                for y in self.variablesOriginales:
                    if x == y:
                        reglaAuxiliar = reglaAuxiliar + variablesAuxiliares [ otroContador ]
                otroContador = otroContador + 1
            else:
                reglaAuxiliar = reglaAuxiliar + self.reglaOriginal [ contador ]
            contador = contador + 1
        return reglaAuxiliar
    
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

# R2 = Regla ( 'xyA', 'apple' )
# C1 = 'BCBCAAABCA'

# print ( R2.marcadorOriginal + ' -> ' + R2.regla )
# print ( C1 )
# print ( R2.vivaRusia ( C1 ) )
# print ( C1 )