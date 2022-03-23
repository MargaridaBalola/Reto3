from Libreria.Libro import Libro

if __name__ == '__main__':
    '''valor1 = input('Introduce el ISBN')
    valor2 = input('Introduce el Titulo')
    valor3 = input('Introduce el Autor')
    valor4 = input('Introduce el Numéro de Páginas')'''

    l1 = Libro('1856043754', 'The library in the twenty-firsty century: new services for the information age', 'BROPHY, Peter', 150 )
    l2 = Libro('972-33-0781-2', 'O Jardim das Hespérides', 'PEREIRA, Maria Helena da Rocha', 200)
    print(l1, l2)


