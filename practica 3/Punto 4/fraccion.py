from fractions import Fraction

class Fraccion:

    __numerador = 0
    __denominador = 0

    def __init__(self, numerador, denominador):
        self.__numerador = int(numerador)
        self.__denominador = int(denominador)

    def setNumerador(self, numerador):
        self.__numerador = numerador

    def setDenominador(self, denominador):
        self.__denominador = denominador

    def getNumerador(self):
        return self.__numerador

    def getDenominador(self):
        return self.__denominador

    def ConvertirAFraccion(self, f1):
        if(type(f1) is not Fraccion):
            f1 = Fraccion(f1 , 1)
        return f1

    def mcd(self):
        u = abs(self.getNumerador());
        v = abs(self.getDenominador());
        if(v==0):
            return u;
        while(v!=0):
            r=u%v;
            u=v;
            v=r;
        return u;
    

    def simplificar(self):
        dividir=self.mcd()
        self.setNumerador(round(self.getNumerador()/dividir))
        self.setDenominador(round(self.getDenominador()/dividir))
        if(self.getDenominador() == self.getNumerador()):
            return 1
        else:
            return self

    def __str__(self):
        return str("{}/{}".format(self.getNumerador(), self.getDenominador()))

    def __add__ (self, f1):
        f1 = self.ConvertirAFraccion(f1)
        numerador = (self.__numerador * f1.getDenominador()) + (f1.getNumerador() * self.__denominador)
        denominador = (self.__denominador * f1.getDenominador())
        return Fraccion(numerador, denominador)

    def __sub__ (self, f1):
        f1 = self.ConvertirAFraccion(f1)
        numerador = (self.__numerador * f1.getDenominador()) - (f1.getNumerador() * self.__denominador)
        denominador = (self.__denominador * f1.getDenominador())
        return Fraccion(numerador, denominador)

    def __div__(self, f1):
        f1 = self.ConvertirAFraccion(f1)
        numerador = (self.__numerador * f1.getDenominador())
        denominador = (self.__denominador * f1.getNumerador())
        return Fraccion(numerador, denominador)

    def __mul__ (self, f1):
        f1 = self.ConvertirAFraccion(f1)
        numerador = (self.__numerador * f1.getDenominador()) - (f1.getNumerador() * self.__denominador)
        denominador = (self.__denominador * f1.getDenominador())
        return Fraccion(numerador, denominador)

    def __radd__ (self, f1):
        f1 = self.ConvertirAFraccion(f1)
        numerador = (f1.getNumerador() * self.__denominador) + (self.__numerador * f1.getDenominador())
        denominador = (self.__denominador * f1.getDenominador())
        return Fraccion(numerador, denominador)

    def __rsub__ (self, f1):
        f1 = self.ConvertirAFraccion(f1)
        numerador = (f1.getNumerador() * self.__denominador) - (self.__numerador * f1.getDenominador())
        denominador = (self.__denominador * f1.getDenominador())
        return Fraccion(numerador, denominador)

    def __rdiv__(self, f1):
        f1 = self.ConvertirAFraccion(f1)
        numerador = (self.__denominador * f1.getNumerador())
        denominador = (self.__numerador * f1.getDenominador())
        return Fraccion(numerador, denominador)

    def __rmul__ (self, f1):
        f1 = self.ConvertirAFraccion(f1)
        numerador = (self.__numerador * f1.getDenominador()) - (f1.getNumerador() * self.__denominador)
        denominador = (self.__denominador * f1.getDenominador())
        return Fraccion(numerador, denominador)

