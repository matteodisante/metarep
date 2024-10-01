import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

"""
class PDF:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._spline = InterpolatedUnivariateSpline(x, y) #_spline con _ perchè non volgio esporla ma tenerla privata


#    def evaluate(self, x):
#        return self._spline(x)

    def __call__(self, x):  # Rende l'oggetto _spline chiamabile. __call_ è un metodo speciale
        return self._spline(x)


    def plot(self):
        plt.plot(self._x, self._y, 'o')
        x = np.linspace(self._x.min(), self._x.max(), 250)
        plt.plot(x, self(x))


    def integral(self, x1, x2):
        return self._spline.integral(x1, x2)

    def normalization(self):
        return self.integral(self._x.min(), self._x.max())
"""


# Col codice di di seguito EREDITO i metodi dalla classe Spline senza riscrivere tutti i metodi come fatto sopra

class PDF(InterpolatedUnivariateSpline):

    def __init__(self, x, y):
        spline = InterpolatedUnivariateSpline(x, y)
        norm = spline.integral(x.min(), x.max())
        self._x = x
        self._y = y / norm
        super().__init__(self._x, self._y)

    def plot(self):
        plt.plot(self._x, self._y, 'o')
        x = np.linspace(self._x.min(), self._x.max(), 250)
        plt.plot(x, self(x))


    def normalization(self):
        return self.integral(self._x.min(), self._x.max())


### WARNING: Nonostante la classe PDF sia ambiata NOTEVOLEMNTE la parte dell' " if __name__ == '__main__': " NON è CAMBIATA!!!!!!


# Il codice qui sotto è come la gente usa il codice. Si parte dalle interfacce
if __name__ == '__main__':
    x = np.linspace(0., 1., 4)
    y = np.exp(x)
    pdf = PDF(x,y) #pdf è un'istanza della classe PDF
    print(id(pdf))
    x0 = 0.5
    print(np.exp(x0), pdf(x0))
    print(pdf.integral(0., 1.))
    print(pdf.normalization())
    pdf.plot()
    plt.show()
