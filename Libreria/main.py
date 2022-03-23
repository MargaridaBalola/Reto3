# Autor: Victoria Muñoz
# Version: 0.0.1
# data: 23/03/2022
from Libreria.Libro import Libro
A = 1
if __name__ == '__main__':
        while A < 3:
                val1 = int(input('Indica el ISBN:'))
                val2 = str(input('Indica el Titulo:'))
                val3 = str(input('Indica el Autor:'))
                val4 = int(input('Indica el Numero de Paginas:'))

                if A < 2:
                        Libro1 = Libro(val1, val2, val3, val4)
                        print(Libro1)
                else:
                        Libro2 = Libro(val1, val2, val3, val4)
                        print(Libro2)
                        Libro2.compara(Libro1.NPag, Libro2.NPag)
                A += 1









