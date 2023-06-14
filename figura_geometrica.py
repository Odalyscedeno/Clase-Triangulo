from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):

    def _init_(self, ancho:float=0.0, alto:float=0.0):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho= ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    def _str_(self):
        return f'Figura Geometrica [{self._dict.str_()}]'

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


if _name_ == '_main_':
    pass
    # fg1 = FiguraGeometrica(2,4)
    # print(fg1)
