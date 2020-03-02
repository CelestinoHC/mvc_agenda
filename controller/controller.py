from model.model import Model
from view.view import View

class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View()


    #Contacto methods
    def agregar_contacto(self, id_contacto, nombre, tel, correo, direccion):
        b, c = self.model.agregar_contacto(id_contacto, nombre, tel, correo, direccion)
        if b:
            self.view.agregar_contacto(c)
        else:
            self.view.contacto_ya_existe(c)

    def leer_contacto(self, id_contacto):
        e, c = self.model.leer_contacto(id_contacto)
        if e:
            self.view.mostrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_todos_los_contactos(self):
        c = self.model.leer_todos_los_contactos()
        self.view.mostrar_contactos(c)

    def actualizar_contacto(self, id_contacto = '', n_nombre = '', n_tel = '', n_correo = '', n_direccion = ''):
        e = self.model.actualizar_contacto(id_contacto, n_nombre, n_tel, n_correo, n_direccion)
        if e:
            self.view.actualizar_contacto(id_contacto)
        else:
            self.view.contacto_no_existe(id_contacto)

    def borrar_contacto(self, id_contacto):
        e, c = self.model.borrar_contacto(id_contacto)
        if e:
            self.view.borrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_contactos_letra(self, letra):
        c = self.model.leer_contactos_letra(letra)
        self.view.mostrar_contactos(c)

    #General Methods    

    def insertar_contactos(self):
        self.agregar_contacto(1, 'Juan Perez', '484-285-9323', 'juanp@ugto.mx', 'Obregon #102 Col. Independencia')
        self.agregar_contacto(2, 'Javier Fernandez', '484-397-1086', 'javFp@ugto.mx', 'Hidalgo #162 Col. Margaritas')
        self.agregar_contacto(3, 'Daniel Salinas', '752-469-7236', 'daniS@ugto.mx', 'Zaragoza #175 Col. Revolucion')

    def insertar_citas(self):
        self.agregar_cita(1, 1, 'DICIS', '25/02/2020', '11:00 hrs', 'Proyecto SSP')
        self.agregar_cita(2, 3, 'Plazoleta Salamanca', '13/03/2020', '15:00 hrs', 'Jugar Pokemon GO')
        self.agregar_cita(3, 2, 'ENMSS', '29/02/2020', '10:00 hrs', 'Examen Inglés')

    def start(self):
        #Display welcome message
        self.view.start()
        #Insert data in model
        self.insertar_contactos()
        self.insertar_citas()
        #Show all the contacts in DB
        self.leer_todos_los_contactos()
        self.leer_contactos_letra('j')

    def menu(self):
        self.view.menu()
        o = input('Selecciona una opcion (1-9): ')
        if o == '1':
            id_contacto = input('ID de contacto: ')
            id_contacto = int(id_contacto)
            nombre = input('Nombre: ')
            tel = input('Telefono (xxx-xxx-xxxx): ')
            correo = input('Correo: ')
            direccion = input('Direccion: ')
            self.agregar_contacto(id_contacto, nombre, tel, correo, direccion)
        elif o == '2':
            id_contacto = input('ID de contacto que desea leer: ')
            id_contacto = int(id_contacto)
            self.leer_contacto(id_contacto)
        elif o == '3':
            id_contacto = input('ID de contacto a actualizar: ')
            id_contacto = int(id_contacto)
            n_nombre = input('Nuevo nombre de contacto: ')
            n_tel = input('Nuevo numero de contacto: ')
            n_correo = input('Nuevo correo de contacto: ')
            n_direccion = input('Nueva direccion de contacto: ')
            self.actualizar_contacto(id_contacto, n_nombre, n_tel, n_correo, n_direccion)
        elif o == '4':
            id_contacto = input('ID de contacto a borrar: ')
            id_contacto = int(id_contacto)
            self.borrar_contacto(id_contacto)
        elif o == '5':
            id_cita = input('ID de la cita: ')
            id_cita = int(id_cita)
            id_contacto = input('ID de contacto: ')
            id_contacto = int(id_contacto)
            lugar = input('Lugar: ')
            fecha = input('Fecha (dd/mm/aaaa): ')
            hora = input('Hora (hh:mm hrs): ')
            asunto = input('Asunto: ')
            self.agregar_cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
        elif o == '6':
            id_cita = input('ID de cita que desea leer: ')
            id_cita = int(id_cita)
            # id_contacto = input('ID de contacto relacionado con la cita: ')
            # id_contacto = int(id_contacto)
            self.leer_cita(id_cita)
        elif o == '7':
            id_cita = input('ID de la cita que desea actualizar: ')
            id_cita = int(id_cita)
            n_id_contacto = ('ID de contacto: ')
            n_id_contacto = int(n_id_contacto)
            n_lugar = input('Lugar actualizado: ')
            n_hora = input('Hora actualizada: ')
            n_fecha = input('Fecha actualizada: ')
            n_asunto = input('Asunto actualizado: ')
            self.actualizar_cita(id_cita, n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto) 
        elif o == '8':
            id_cita = input('ID de la cita que desea borrar: ')
            id_cita = int(id_cita)
            self.borrar_cita(id_cita)
        elif o == '9':
            self.view.end()
        else:
            self.view.opcion_no_valida()


    #Cita methods

    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        b, c = self.model.agregar_cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
        if b:
            self.view.mostrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)

    def leer_cita(self, id_cita):
        e, c = self.model.leer_cita(id_cita)
        if e:
            self.view.mostrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)

    def leer_todas_las_citas(self):
        c = self.model.leer_todas_las_citas()
        self.view.mostrar_citas(c)

    def actualizar_cita(self, id_cita, n_id_contacto = '', n_lugar = '', n_fecha = '', n_hora = '', n_asunto = ''):
        e = self.model.actualizar_cita(id_cita, n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto)
        if e:
            self.view.actualizar_cita(id_cita)
        else:
            self.view.cita_no_existe(id_cita)

    def borrar_cita(self, id_cita):
        e, c = self.model.borrar_cita(id_cita)
        if e:
            self.view.borrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)        

    def leer_citas_fecha(self, fecha):
        c = self.model.leer_citas_fecha(fecha)
        self.view.mostrar_citas(c)