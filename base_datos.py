import sqlite3


class ConnectDB:

    def abrir_cone(self):
        conexion = sqlite3.connect("biblioteca.db")
        return conexion

    """Parte de los libros"""

    def crear(self):
        conexion = self.abrir_cone()
        try:
            conexion.execute("""create table libros(
                            titulo text primary key,
                            autor text,
                            edicion text,
                            lugar_impresion text,
                            editorial text,
                            es_traduccion text,
                            paginas integer,
                            condicion text)""")
            print("Se creó la tabla libros!!")
        except sqlite3.OperationalError:
            print("La tabla libros ya existe!!")

    def alta(self, datos):
        flag = True
        conexion = self.abrir_cone()
        try:
            cursor = conexion.cursor()
            sql = "insert into libros (titulo,autor,edicion,lugar_impresion,editorial,es_traduccion,paginas,condicion) values (?,?,?,?,?,?,?,?)"
            cursor.execute(sql, datos)
            conexion.commit()
        except sqlite3.IntegrityError:
            flag = False
        finally:
            conexion.close()
            return flag

    def consulta(self, datos):
        conexion = self.abrir_cone()
        cursor = conexion.cursor()
        sql = "select autor,edicion,lugar_impresion,editorial,es_traduccion,paginas,condicion from libros where titulo = ?"
        cursor.execute(sql, datos)
        lista = cursor.fetchall()
        conexion.close()
        return lista

    def baja(self, nombre_tabla, atributo_tabla, datos):
        conexion = self.abrir_cone()
        cursor = conexion.cursor()
        sql = "delete from " + nombre_tabla + " where " + atributo_tabla + " = ?"
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()

    def modificar(self, datos, parametro_tabla):
        conexion = self.abrir_cone()
        cursor = conexion.cursor()
        sql = "update libros set " + parametro_tabla + " = ? where titulo = ?"
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()

    def mostrar(self):
        conexion = self.abrir_cone()
        cursor = conexion.cursor()
        sql = "select * from libros"
        cursor.execute(sql)
        libros = cursor.fetchall()
        texto = ""
        for libro in libros:
            for i in range(8):
                if i != 7:
                    texto += str(libro[i]) + ", "
                else:
                    texto += str(libro[i]) + "." + "\n"
        conexion.close()
        return texto

    """Parte del prestamo"""

    def crear_dos(self):
        conexion = self.abrir_cone()
        try:
            conexion.execute("""create table prestamo(
                            telefono integer primary key,
                            nombre text,
                            mail text,
                            fecha_inicio text,
                            fecha_fin text,
                            libro text)""")
        except sqlite3.OperationalError:
            print("La tabla prestamo ya existe!!")

    def consulta_prestamo(self, datos):
        conexion = self.abrir_cone()
        cursor = conexion.cursor()
        sql = "select condicion from libros where titulo = ?"
        cursor.execute(sql, datos)
        condicion = cursor.fetchone()
        conexion.close()
        return condicion

    def alta_prestamo(self, datos):
        conexion = self.abrir_cone()
        try:
            cursor = conexion.cursor()
            sql = "insert into prestamo (telefono,nombre,mail,fecha_inicio,fecha_fin,libro) values (?,?,?,?,?,?)"
            cursor.execute(sql, datos)
            conexion.commit()
        except sqlite3.IntegrityError:
            print("Error con en la base de datos, 'alta_prestamo'")
        finally:
            conexion.close()

    def modificar_estado_prestamo(self, datos):
        conexion = self.abrir_cone()
        cursor = conexion.cursor()
        sql = "update libros set condicion = ? where titulo = ?"
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()

    def mostrar_prestamo(self, fecha_ingresada):

        conexion = self.abrir_cone()
        cursor = conexion.cursor()
        sql = "select * from prestamo"
        cursor.execute(sql)
        listas = cursor.fetchall()
        fecha = deudores = deudores_retraso = ""
        no_poner = "/-"
        # Fecha ingresada
        deudores_retraso += f"La fecha ingresada fue: {fecha_ingresada}\n"
        for ind in range(len(fecha_ingresada)):
            if not fecha_ingresada[ind] in no_poner:
                fecha += str(fecha_ingresada[ind])
        # Fechas a comparar
        for lista in listas:
            num = ""
            for i in range(len(lista[4])):
                if not lista[4][i] in no_poner:
                    num += lista[4][i]
                if i == len(lista[4]) - 1:
                    datos = (lista[5],)
                    if int(num) == int(fecha):
                        datos_modificar = ("Préstamo en proceso", lista[5])
                        self.modificar(datos_modificar, "condicion")
                        deudores += self.texto_deudores(datos, lista)
                    elif int(num) < int(fecha):
                        datos_modificar = ("Retraso", lista[5])
                        self.modificar(datos_modificar, "condicion")
                        deudores_retraso += self.texto_deudores(datos, lista)
        if len(deudores) == 0 and len(deudores_retraso) == 34:
            deudores += "---" * 30
            deudores += "\nNo hay libros por reclamar!!"
        return deudores_retraso + deudores

    def texto_deudores(self, datos, lista):
        conexion = self.abrir_cone()
        cursor = conexion.cursor()
        sql_condicion = "select condicion from libros where titulo = ?"
        deudores = ""
        cursor.execute(sql_condicion, datos)
        condicion = cursor.fetchone()
        deudores += "---" * 30
        deudores += "\nDatos del deudor.."
        deudores += "\nNombre: " + lista[1]
        deudores += "\nMail: " + lista[2]
        deudores += "\nTeléfono: " + str(lista[0])
        deudores += "\nLibro a devolver: " + lista[5]
        deudores += "\nFecha final del prestamo: " + lista[4]
        deudores += "\nCondición del libro: " + str(condicion[0]) + "\n"
        conexion.close()
        return deudores
