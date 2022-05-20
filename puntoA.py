'''
El siguiente programa tiene como finalidad simular la ejecución
de la cafetería de la universidad, solicitando el número de cédula
el rol dentro de la universidad, el código del producto que se
desea comprar, la cantidad de unidades del producto, el precio unitario
y preguntando si es beneficiario de una beca. Al final se imprime una cadena
donde se mencionan el rol, la cédula, el código del product y el total de la
compra sujeto a los respectivos descuentos.
'''

menu = {11:'almuerzo', 22:'gaseosa', 33:'salchipapa', 44:'papas margarita', 55:'pastel', 66:'galleta'}


def cobroAlmuerzos():
    while 1 > 0:    # Se pretende un funcionamiento continuo
        print()
        
        ansBeca = False     # La beca no esta aplicada hasta que se ingrese lo contrario
        cedula = int(input('Ingresa el número de tu cedula: '))
        tipo = input('¿Eres profesor o estudiante? ')

        while tipo != 'profesor' and tipo != 'estudiante':  # Validacion del rol
            tipo = input('Ingresa un rol válido: ')

            
        if tipo == 'estudiante':
            beca = input('¿Haces parte del programa de becas? ')

            while beca != 'Si' and beca != 'No':
                beca = input('¿Haces parte del programa de becas, Si o No? ')   # Validacion de una respuesta valida
            
            if beca == 'Si':
                ansBeca = True
                
        producto = int(input('Ingresa el código del producto: '))

        while producto not in menu:
            print('Ese código no está dentro de nuestro menú')
            producto = int(input('Ingrese un código válido: '))
            
        unidades = int(input('Ingresa la cantidad de unidades: '))
        precio = int(input('Ingresa el precio unitario del producto: '))

        subtotal = unidades * precio

        # aplicacion del descuento
        if tipo == 'profesor':
            total = subtotal * 0.8
        elif tipo == 'estudiante':
            if ansBeca:
                total = subtotal * 0.5
            else:
                total = subtotal * 0.7

        print('El %s con cédula %d, debe pagar %d por el producto %d: %s' %(tipo, cedula, total, producto, menu[producto]))
        print()
        print('########################################################################')
