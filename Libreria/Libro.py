# Autor: Victoria Muñoz
# Version: 0.0.1
# data: 23/03/2022

class Libro():
    __Isbn: int
    __Titulo: str
    __Autor: str
    __NPag: int

    def __init__(self, NewIsbn, NewTitulo, NewAutor, NewNPag):
        self.__Isbn = NewIsbn
        self.__Titulo = NewTitulo
        self.__Autor = NewAutor
        self.__NPag = NewNPag

    @property
    def Isbn(self):
        return self.__Isbn

    @Isbn.setter
    def Isbn(self, NewIsbn):
        self.__Isbn = NewIsbn

    @property
    def Titulo(self):
        return self.__Titulo

    @Titulo.setter
    def Titulo(self, NewTitulo):
        self.__Titulo = NewTitulo

    @property
    def Autor(self):
        return self.__Autor

    @Autor.setter
    def Autor(self, NewAutor):
        self.__Autor = NewAutor

    @property
    def NPag(self):
        return self.__NPag

    @NPag.setter
    def NPag(self, NewNPag):
        self.__NPag = NewNPag

    def compara(self, Libro1, Libro2):
        if Libro1 > Libro2:
            print('El Libro1 tiene más páginas')
        else:
            print('El Libro2 tiene más páginas')

    def __str__(self):
        return f'"El libro con ISBN {self.__Isbn} creado por el autor {self.__Autor} tiene {self.__NPag} páginas"'