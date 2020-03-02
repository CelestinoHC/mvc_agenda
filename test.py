from model.contacto import Contacto
from model.cita import Cita
from model.model import Model
from view.view import View
from controller.controller import Controller
"""
contactos = []
find = False

c1 = Contacto(1, 'Juan Perez', '484-285-9323', 'juanp@ugto.mx', 'Obregon #102 Col. Independencia')
c2 = Contacto(2, 'Daniel Salinas', '752-469-7236', 'daniS@ugto.mx', 'Zaragoza #175 Col. Revolucion')
d1 = Cita(1, 1, 'DICIS', '18/02/2020', '11:00 hrs', 'Proyecto SSP')

contactos.append(c1)
contactos.append(c2)

guess = input('Dame un nombre: ')

for c in contactos:
    if guess.lower() == c.nombre.lower():
        print('Si está')
        break
else:
    print('No está')"""

#for i in range (2):
#    if guess == contactos[i].nombre:
#        print('Contacto existe')
#        find = True
    
#if find == False:
#    print('Contacto no existe')

# m = Model()
# v = View()

# m.agregar_contacto(1, 'Juan Perez', '484-285-9323', 'juanp@ugto.mx', 'Obregon #102 Col. Independencia')
# m.agregar_contacto(2, 'Javier Fernandez', '484-397-1086', 'javFp@ugto.mx', 'Hidalgo #162 Col. Margaritas')
# m.agregar_contacto(3, 'Daniel Salinas', '752-469-7236', 'daniS@ugto.mx', 'Zaragoza #175 Col. Revolucion')

# #s = m.leer_contacto(2)
# #print(s.nombre)

# m.agregar_cita(1, 1, 'DICIS', '25/02/2020', '11:00 hrs', 'Proyecto SSP')
# m.agregar_cita(2, 3, 'Plazoleta Salamanca', '13/03/2020', '15:00 hrs', 'Jugar Pokemon GO')
# m.agregar_cita(3, 2, 'ENMSS', '29/02/2020', '10:00 hrs', 'Examen Inglés')

cont = Controller()
cont.insertar_contactos()
cont.insertar_citas()
cont.leer_todas_las_citas()
cont.menu()
cont.leer_todas_las_citas()
#cont.leer_contacto(1)

# s = m.leer_todos_los_contactos()
# v.mostrar_contactos(s)
# c = m.leer_contacto(1)
# v.mostrar_contacto(c)

# f, c = m.borrar_contacto(1)
# if f:
#     v.borrar_contacto(c)
# else:
#     v.contacto_no_existe(1)

# s = m.leer_todos_los_contactos()
# v.mostrar_contactos(s)    

# s = m.leer_todas_las_citas()
# v.mostrar_citas(s)
# c = m.leer_cita(2, 3)
# v.mostrar_cita(c)

#m.borrar_cita(1)

# f, c = m.borrar_cita(1)
# if f:
#    v.borrar_cita(c)
# else:
#    v.cita_no_existe(1)

# s = m.leer_todas_las_citas()
# v.mostrar_citas(s)    

#m.buscar_contactos()
#m.buscar_citas()

"""s = m.leer_cita(1, 1)
print(s.lugar)

m.actualizar_cita(1, 1, 'DCEA', '25/02/2020', '12:00 hrs', 'Proyecto SSP')

a = m.leer_cita(1, 1)
print(a.lugar)"""

##############Buscar Contactos por inicial#################
# findcontacto = False
# guess = input('Dame un caracter: ')

# for c in m.contactos:
#     if guess.lower() == c.nombre[0].lower():
#         print(c.nombre)
#         findcontacto = True
    
# if findcontacto == False:
#     print('No hay ningun contacto con esa inicial')

##############Buscar Citas por fecha###################    
# findfecha = False
# guessfecha = input('Dame una fecha (dd/mm/aaaa): ')

# for c in m.citas:
#     if guessfecha == c.fecha:
#         print(c.asunto)
#         findfecha = True

# if findfecha == False:
#     print('No hay ninguna cita en esta fecha')


