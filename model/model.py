from .contacto import Contacto
from .cita import Cita

class Model:

    def __init__(self):
        self.contactos = []
        self.citas = []

    def esta_id(self, id_contacto):
        for c in self.contactos:
            if c.id_contacto == id_contacto:
                return True, c
        return False, 0

    def esta_idD(self, id_cita):
        for d in self.citas:
            if d.id_cita == id_cita:
                return True, d
        return False, 0

    #Contactos methods
    def agregar_contacto(self, id_contacto, nombre, tel, correo, direccion):
        if not self.esta_id(id_contacto)[0]:
            c = Contacto(id_contacto, nombre, tel, correo, direccion)
            self.contactos.append(c)
            return True, c
        return False, c

    def leer_contacto(self, id_contacto):
        e, c = self.esta_id(id_contacto)
        return e, c

    def actualizar_contacto(self, id_contacto, n_nombre, n_tel, n_correo, n_direccion):
        e, c = self.esta_id(id_contacto)
        if e:
            if n_nombre != '':
                c.nombre = n_nombre
            if n_tel != '':
                c.tel = n_tel
            if n_correo != '':
                c.correo = n_correo
            if n_direccion != '':
                c.direccion = n_direccion
            return True
        return False

    def borrar_contacto(self, id_contacto):
        e, contacto = self.esta_id(id_contacto)
        if e:
            self.contactos.remove(contacto)
            lista_temp = [c for c in self.citas if c.id_contacto == id_contacto]
            for c in lista_temp:
                self.citas.remove(c)
            return True, contacto
        return False, 0

        # def borrar_cita(self, id_cita):
        # e, d = self.esta_idD(id_cita)
        # if e:
        #     self.citas.remove(d)
        #     return True
        # return False

    def leer_contactos_letra(self, letra):
        #lista = [c for c in self.contactos if c.nombre.lower().startswith(letra.lower())]
        lista = []
        for c in self.contactos:
            if c.nombre[0].lower() == letra.lower():
            #if c.nombre[0].lower() == c.startswith(letra.lower()):
                lista.append(c)
        return lista

    # def buscar_contactos(self):
    #     ##############Buscar Contactos por inicial#################
    #     findcontacto = False
    #     guess = input('Dame un caracter: ')

    #     for cont in self.contactos:
    #         if guess.lower() == cont.nombre[0].lower():
    #             print(cont.nombre)
    #             findcontacto = True
            
    #     if findcontacto == False:
    #         print('No hay ningun contacto con esa inicial')

    def leer_todos_los_contactos(self):
        return self.contactos

    #Cita methods

    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        if not self.esta_idD(id_cita)[0]:
            if self.esta_id(id_contacto)[0]:
                d = Cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
                self.citas.append(d)
                return True, d
        return False, d

    def leer_cita(self, id_cita):
        e, d = self.esta_idD(id_cita) 
        return e, d

    def leer_todas_las_citas(self):
        return self.citas

    def actualizar_cita(self, id_cita, n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto):
        e, d = self.esta_idD(id_cita)
        if e:
            if n_id_contacto != '':
                d.id_contacto = n_id_contacto
            if n_lugar != '':
                d.lugar = n_lugar
            if n_fecha != '':
                d.fecha = n_fecha
            if n_hora != '':
                d.hora = n_hora
            if n_asunto != '':
                d.asunto = n_asunto
            return True
        return False

    def borrar_cita(self, id_cita):
        e, d = self.esta_idD(id_cita)
        if e:
            self.citas.remove(d)
            return True
        return False

    # def buscar_citas(self):
    #     ##############Buscar Citas por fecha###################    
    #     findfecha = False
    #     guessfecha = input('Dame una fecha (dd/mm/aaaa): ')

    #     for cit in self.citas:
    #         if guessfecha == cit.fecha:
    #             print(cit.asunto)
    #             findfecha = True

    #     if findfecha == False:
    #         print('No hay ninguna cita en esta fecha')

    def leer_citas_fecha(self, fecha):
        #lista = [c for c in self.citas if c.fecha == fecha]
        lista = []
        for c in self.citas:
            if c.fecha == fecha:
                lista.append(c)
        return lista

