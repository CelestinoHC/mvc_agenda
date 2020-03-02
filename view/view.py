class View:
    ##################### Contactos
    def mostrar_contacto(self, contacto):
        print('***** Datos del Contacto *****')
        print('Nombre: ', contacto.nombre)
        print('Teléfono: ', contacto.tel)
        print('Correo: ', contacto.correo)
        print('Direccion: ', contacto.direccion)
        print('******************************')

    def mostrar_contactos(self, contactos):
        print('***** Contactos definidos *****')
        for c in contactos:
            print(c.nombre, c.tel, c.correo, c.direccion)
        print('*******************************')

    def agregar_contacto(self, contacto):
        print(contacto.nombre, 'Se ha agregado a la base de datos!')

    def borrar_contacto(self, contacto):
        print(contacto.nombre, 'Se ha borrado de la base de datos!')

    def actualizar_contacto(self, id_contacto):
        print(id_contacto, 'Se ha modificado correctamente!')

    def contacto_ya_existe(self, contacto):
        print(contacto.id_contacto, 'YA EXISTE EN LA BASE DE DATOS!')

    def contacto_no_existe(self, id_contacto):
        print(id_contacto, 'NO EXISTE EN LA BASE DE DATOS!')

    #General Views

    def start(self):
        print('Esto es un ejemplo de vista sencilla')

    def end(self):
        print('Hasta la vista')

    def opcion_no_valida(self):
        print('Opción no valida')

    def menu(self):
        print('1. Agregar contacto')
        print('2. Leer contacto')
        print('3. Actualizar contacto')
        print('4. Borrar contacto')
        print('5. Agregar cita')
        print('6. Leer cita')
        print('7. Actualizar cita')
        print('8. Borrar cita')
        print('9. Salir')


    ############################# Citas

    def mostrar_cita(self, cita):
        print('***** Datos de la Cita *****')
        print('Lugar: ',  cita.lugar)
        print('Fecha: ',  cita.fecha)
        print('Hora: ',   cita.hora)
        print('Asunto: ', cita.asunto)
        print('******************************')

    def mostrar_citas(self, citas):
        print('***** Citas definidas *****')
        for c in citas:
            print(c.lugar, c.fecha, c.hora, c.asunto)
        print('*******************************')

    def crear_cita(self, cita):
        print(cita.asunto, 'Se ha agregado a la base de datos!')

    def borrar_cita(self, cita):
        print(cita.asunto, 'Se ha borrado de la base de datos!')

    def actualizar_cita(self, id_cita):
        print(id_cita, 'Se ha modificado correctamente!')

    def cita_ya_existe(self, cita):
        print(cita.id_contacto, 'YA EXISTE EN LA BASE DE DATOS!')

    def cita_no_existe(self, id_cita):
        print(id_cita, 'NO EXISTE EN LA BASE DE DATOS!')