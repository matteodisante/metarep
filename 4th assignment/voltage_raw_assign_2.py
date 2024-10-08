from dataclasses import dataclass

from loguru import logger
import numpy as np

#OLD VERSION
#
# file_path = 'voltage.txt'
#
# def adc_to_voltage(adc):
#     """ Convert ADC counts to a physical voltage (in V)
#     """
#     return 1.653*adc + 0.456
#
#
# input_file = open(file_path)
# for line in input_file.readlines():
#     timestamp, adc = line.split()
#     timestamp = float(timestamp)
#     adc = int(adc)
#     print(timestamp, adc, type(timestamp), type(adc))


############################################################################################################################################

################################### New VERSION ##################################


# # Questa classe è un classico esempio di anti-pattern
# class Reading:
#     """ Small container class representing a single voltage reading
#     """
#     def __init__(self, timestamp, adc):
#         self.timestamp = timestamp
#         self.adc = adc
#
#     def voltage(self):
#         """ Convert ADC counts to a physical voltage (in V)
#         """
#         return 1.653*self.adc + 0.456
#
#     def __str__(self):
#         return f'Reading at {self.timestamp} s: {self.adc} ADC counts ({self.voltage()}) V'





@dataclass # <--- IMPORTANTE. DA GUARDARE BENE. Usando il decoratore @dataclass ci siamo evitati __init__ e __str__
class Reading:

    """ Small container class representing a single voltage reading
    """

    # ci pensa in automatico a fare il costruttore. Basta che do nome : tipo.
    # Il tipo va messo solo per indicare in modo non ambiguo per indicare che questi sono i membri della classe che voglio.
    # Python non ci fa niente con il tipo che do.
    timestamp: float #nome : tipo
    adc: int


    def voltage(self):
        """ Convert ADC counts to a physical voltage (in V)
        """
        return 1.653*self.adc + 0.456




class VoltageData:

    """Simple interface to a set of voltage readings.
    """

    def __init__(self, file_path):
        logger.info(f'Reading voltage data from {file_path}...')
        with open(file_path) as input_file:
            self._readings = [self._parse_line(line) for line in input_file.readlines()]
        logger.info(f'Done, {len(self._readings)} values read.')
        self._iterator = iter(self._readings)

    @classmethod # <-- Classmethod mi da anche la referenza al tipo. Nel codice del prof: "cls" è come scrivere VoltageData
    def from_arrays(cls, timestamps, adcs):
        logger.info(f'Initialilizing {cls.__name__} from arrays...')
        self._readings = [Reading(timestamp, adc) for (timestamp, adc) in zip(timestamps, adcs)]
        print(timestamp, adcs)




    @staticmethod #<-- E' uno static method. E' comune a tutte le classi. Si può chiamare senza un'istanza della classe. E' spesso usato quando ho una funzione che è un metodo di una classe ma non usa niente della specifica classe
    def _parse_line(line): # N.B. _parse_line è la funzione candidata ad essere sottoposta a unit test
        """Parse  a single line form a text file and return Reading object
        """
        timestamp, adc = line.split()
        timestamp = float(timestamp)
        adc = int(adc)
        return Reading(timestamp, adc)


    def __iter__(self): #iter trasforma un iterabile in un iteratore
        ##logger.debug(f'Calling {self.__class__.__name__}.__iter__')
        return self

    def __next__(self):
        return next(self._iterator)

    def __getitem__(self, index):
        self._readings[index]




if __name__ == '__main__':
#    r = Reading(1.,2345)
#    print(r)
    #data = VoltageData('voltage.txt')
    t = np.linspace(1., 10., 10)
    a = np.full(t.shape, 127)
    print(t)
    print(a)
    data = VoltageData.from_arrays(t,a)
    # for reading in data:
    #     print(reading, reading.timestamp, reading.adc, reading.voltage())
    #
    # print('Done.')
    # print(data[3])
    #
    # print(data._parse_line('1. 2345'))
    # print(VoltageData._parse_line('1. 2345'))
