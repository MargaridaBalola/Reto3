# Autor: Margarida Balola
# Version: 0.0.1
# data: 22/03/2022

#Definição de Classe
class Libro():

    #Definição dos atributos

    __Isbn: str
    __Titulo: str
    __Autor: str
    __NPag: int

    #Definição do construtor

    def __init__(self, newISBN, newTit, newAut, newNP):
        self.__Isbn = newISBN
        self.__Titulo = newTit
        self.__Autor = newAut
        self.__NPag = newNP

    #Definição dos métodos

    @property
    def Isbn(self):
        return self.__Isbn

    @property
    def Titulo(self):
        return self.__Titulo

    @property
    def Autor(self):
        return self.__Autor

    @property
    def NumPag(self):
        return self.__NPag

    @Isbn.setter
    def Isbn(self, newISBN):
        self.__Isbn = newISBN

    @Titulo.setter
    def Titulo(self, newTit):
        self.__Titulo = newTit

    @Autor.setter
    def Autor(self, newAut):
        self.__Autor = newAut

    @NumPag.setter
    def NumPag(self, newNP):
        self.__NPag = newNP

    def compara(self, Libro1, Libro2):
        if Libro1.NumPag > Libro2.NumPag:
            print(f'El libro con más páginas es el Libro 1')
        else:
            print(f'El libro con más páginas es el Libro 2')

    def __str__(self):
        return f'El libro {self.__Titulo} con ISBN {self.__Isbn} creado por el autor {self.__Autor} tiene {self.__NPag} páginas'

    def VerNumPag(self):
        if l1.__NPag > l2.__NPag:
            return f'El libro con más páginas es el Libro 1'
        else:
            return f'El libro con más páginas es el Libro 2'













