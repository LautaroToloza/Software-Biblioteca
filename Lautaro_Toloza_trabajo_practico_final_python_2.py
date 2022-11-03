import sys

import base_datos
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st


class Biblioteca:
    def __init__(self):
        self.connection = base_datos.ConnectDB()
        self.connection.crear()
        self.connection.crear_dos()
        self.ventana = tk.Tk()
        self.menu_opciones()
        self.ventana.title("Biblioteca")
        self.ventana.geometry("820x450")
        self.cuaderno = ttk.Notebook(self.ventana)
        self.cuaderno.grid(column=0, row=0, padx=20, pady=20)
        self.cargar_libro()
        self.consultar_libro()
        self.borrar_libro()
        self.modificar_libro()
        self.mostrar_libros()
        self.mostrar_datos()
        self.condicion_prestamo()
        self.terminar_prestamo()
        self.reclamar_prestamo()
        self.ventana.mainloop()

    """Métodos"""

    def cargar_label(self, ubicacion, texto, fila):
        label = ttk.Label(ubicacion, text=texto)
        label.grid(column=0, row=fila, padx=4, pady=4)
        return label

    def cargar_entry(self, ubicacion, variable, fila):
        entry = ttk.Entry(ubicacion, textvariable=variable)
        entry.grid(column=1, row=fila, padx=4, pady=4)
        return entry

    def consultar_entry(self, variable, fila):
        entry = ttk.Entry(self.label_frame, textvariable=variable, state="readonly")
        entry.grid(column=1, row=fila, padx=7, pady=4)
        return entry

    """Interfaz Libros"""

    def cargar_libro(self):
        self.pagina_uno = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina_uno, text="Cargar libros")
        self.label_frame = ttk.LabelFrame(self.pagina_uno, text="Libro")
        self.label_frame.grid(column=0, row=0, padx=10, pady=10)
        self.label_uno = self.cargar_label(self.label_frame, "Título:", 0)
        self.titulo = tk.StringVar()
        self.entry_uno = self.cargar_entry(self.label_frame, self.titulo, 0)
        self.label_dos = self.cargar_label(self.label_frame, "Autor:", 1)
        self.autor = tk.StringVar()
        self.entry_dos = self.cargar_entry(self.label_frame, self.autor, 1)
        self.label_tres = self.cargar_label(self.label_frame, "Edición:", 2)
        self.edicion = tk.StringVar()
        self.entry_tres = self.cargar_entry(self.label_frame, self.edicion, 2)
        self.label_cuatro = self.cargar_label(self.label_frame, "Lugar de impresión:", 3)
        self.lugar_impresion = tk.StringVar()
        self.entry_cuatro = self.cargar_entry(self.label_frame, self.lugar_impresion, 3)
        self.label_cinco = self.cargar_label(self.label_frame, "Editorial:", 4)
        self.editorial = tk.StringVar()
        self.entry_cinco = self.cargar_entry(self.label_frame, self.editorial, 4)
        self.label_sies = self.cargar_label(self.label_frame, "Es una traducción:", 5)
        self.es_traduccion = tk.StringVar()
        self.entry_sies = self.cargar_entry(self.label_frame, self.es_traduccion, 5)
        self.label_siete = self.cargar_label(self.label_frame, "Cantidad de páginas:", 6)
        self.cantidad_paginas = tk.StringVar()
        self.entry_siete = self.cargar_entry(self.label_frame, self.cantidad_paginas, 6)
        self.label_ocho = self.cargar_label(self.label_frame, "Condición:", 7)
        self.condicion = tk.StringVar()
        self.opcion_uno = ttk.Radiobutton(self.label_frame, text="Disponible", variable=self.condicion,
                                          value="Disponible")
        self.opcion_uno.grid(column=1, row=7)
        self.opcion_dos = ttk.Radiobutton(self.label_frame, text="En restauración", variable=self.condicion,
                                          value="En restauración")
        self.opcion_dos.grid(column=1, row=8)
        self.boton = tk.Button(self.label_frame, text="Agregar", command=self.agregar)
        self.boton.grid(column=1, row=9, padx=4, pady=4)

    def consultar_libro(self):
        self.pagina_dos = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina_dos, text="Consultar libro")
        self.label_frame = ttk.LabelFrame(self.pagina_dos, text="Buscar Libro")
        self.label_frame.grid(column=0, row=0, padx=10, pady=10)
        self.label_uno = self.cargar_label(self.label_frame, "Título:", 0)
        self.titulo_consulta = tk.StringVar()
        self.entry_uno = self.cargar_entry(self.label_frame, self.titulo_consulta, 0)
        self.label_dos = self.cargar_label(self.label_frame, "Autor:", 1)
        self.autor_consulta = tk.StringVar()
        self.entry_dos = self.consultar_entry(self.autor_consulta, 1)
        self.label_tres = self.cargar_label(self.label_frame, "Edición:", 2)
        self.edicion_consulta = tk.StringVar()
        self.entry_tres = self.consultar_entry(self.edicion_consulta, 2)
        self.label_cuatro = self.cargar_label(self.label_frame, "Lugar de impresión:", 3)
        self.lugar_impresion_consulta = tk.StringVar()
        self.entry_cuatro = self.consultar_entry(self.lugar_impresion_consulta, 3)
        self.label_cinco = self.cargar_label(self.label_frame, "Editorial:", 4)
        self.editorial_consulta = tk.StringVar()
        self.entry_cinco = self.consultar_entry(self.editorial_consulta, 4)
        self.label_sies = self.cargar_label(self.label_frame, "Es una traducción:", 5)
        self.es_traduccion_consulta = tk.StringVar()
        self.entry_sies = self.consultar_entry(self.es_traduccion_consulta, 5)
        self.label_siete = self.cargar_label(self.label_frame, "Cantidad de páginas:", 6)
        self.cantidad_paginas_consulta = tk.StringVar()
        self.entry_siete = self.consultar_entry(self.cantidad_paginas_consulta, 6)
        self.label_ocho = self.cargar_label(self.label_frame, "Condición:", 7)
        self.condicion_consulta = tk.StringVar()
        self.entry_ocho = self.consultar_entry(self.condicion_consulta, 7)
        self.boton = tk.Button(self.label_frame, text="Buscar", command=self.consultar)
        self.boton.grid(column=1, row=8, padx=4, pady=4)

    def borrar_libro(self):
        self.pagina_tres = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina_tres, text="Borrar libro")
        self.label_frame = ttk.LabelFrame(self.pagina_tres, text="Borrar libro")
        self.label_frame.grid(column=0, row=0, padx=10, pady=10)
        self.label_uno = self.cargar_label(self.label_frame, "Título:", 0)
        self.titulo_borrar = tk.StringVar()
        self.entry_uno = self.cargar_entry(self.label_frame, self.titulo_borrar, 0)
        self.boton = ttk.Button(self.label_frame, text="Borrar", command=self.borrar)
        self.boton.grid(column=1, row=1, padx=4, pady=4)

    def modificar_libro(self):
        self.pagina_cuatro = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina_cuatro, text="Modificar datos")
        self.label_frame = ttk.LabelFrame(self.pagina_cuatro, text="Dato actual")
        self.label_frame.grid(column=0, row=0, padx=10, pady=10)
        self.label_uno = self.cargar_label(self.label_frame, "Título:", 0)
        self.titulo_actual = tk.StringVar()
        self.entry_uno = self.cargar_entry(self.label_frame, self.titulo_actual, 0)
        # Parte dos.
        self.label_frame_dos = ttk.LabelFrame(self.pagina_cuatro, text="Dato a modificar")
        self.label_frame_dos.grid(column=0, row=1, padx=10, pady=10)
        self.label_dos = self.cargar_label(self.label_frame_dos, "Título:", 1)
        self.titulo_modificar = tk.StringVar()
        self.entry_dos = self.cargar_entry(self.label_frame_dos, self.titulo_modificar, 1)
        self.label_tres = self.cargar_label(self.label_frame_dos, "Autor:", 2)
        self.autor_modificar = tk.StringVar()
        self.entry_tres = self.cargar_entry(self.label_frame_dos, self.autor_modificar, 2)
        self.label_cuatro = self.cargar_label(self.label_frame_dos, "Edición:", 3)
        self.edicion_modificar = tk.StringVar()
        self.entry_cuatro = self.cargar_entry(self.label_frame_dos, self.edicion_modificar, 3)
        self.label_cinco = self.cargar_label(self.label_frame_dos, "Lugar de impresión:", 4)
        self.lugar_impresion_modificar = tk.StringVar()
        self.entry_cinco = self.cargar_entry(self.label_frame_dos, self.lugar_impresion_modificar, 4)
        self.label_seis = self.cargar_label(self.label_frame_dos, "Editorial:", 5)
        self.editorial_modificar = tk.StringVar()
        self.entry_seis = self.cargar_entry(self.label_frame_dos, self.editorial_modificar, 5)
        self.label_siete = self.cargar_label(self.label_frame_dos, "Es una traducción:", 6)
        self.es_traduccion_modificar = tk.StringVar()
        self.entry_siete = self.cargar_entry(self.label_frame_dos, self.es_traduccion_modificar, 6)
        self.label_ocho = self.cargar_label(self.label_frame_dos, "Cantidad de páginas:", 7)
        self.cantidad_paginas_modificar = tk.StringVar()
        self.entry_och = self.cargar_entry(self.label_frame_dos, self.cantidad_paginas_modificar, 7)
        self.label_nueve = self.cargar_label(self.label_frame_dos, "Condición:", 8)
        self.condicion_modificar = tk.StringVar()
        self.opcion_uno = ttk.Radiobutton(self.label_frame_dos, text="Disponible", variable=self.condicion_modificar,
                                          value="Disponible")
        self.opcion_uno.grid(column=1, row=8)
        self.opcion_uno = ttk.Radiobutton(self.label_frame_dos, text="En restauración",
                                          variable=self.condicion_modificar, value="En restauración")
        self.opcion_uno.grid(column=1, row=9)
        self.boton = ttk.Button(self.label_frame_dos, text="Modificar", command=self.modificar_datos)
        self.boton.grid(column=1, row=10, padx=4, pady=4)

    def mostrar_libros(self):
        self.pagina_cinco = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina_cinco, text="Mostrar Libros")
        self.titulo_mostrar = tk.StringVar()
        self.autor_mostrar = tk.StringVar()
        self.edicion_mostrar = tk.StringVar()
        self.lugar_impresion_mostrar = tk.StringVar()
        self.editorial_mostrar = tk.StringVar()
        self.es_traduccion_mostrar = tk.StringVar()
        self.cantidad_paginas_mostrar = tk.StringVar()
        self.condicion_mostrar = tk.StringVar()
        self.scroll = st.ScrolledText(self.pagina_cinco, width=95, height=23)
        self.scroll.grid(column=0, row=0, padx=10, pady=10)

    """Libros + Base de datos"""

    def agregar(self):
        datos = (
            self.titulo.get(), self.autor.get(), self.edicion.get(), self.lugar_impresion.get(), self.editorial.get(),
            self.es_traduccion.get(), self.cantidad_paginas.get(), self.condicion.get())
        flag = self.connection.alta(datos)
        if flag:
            mb.showinfo("Información", "El libro ya fue cargado con éxito!!")
        else:
            mb.showerror("Información", "El título del libro ingresado ya existe!!")

    def generico_modificar(self, atributo, nombre_parametro_tabla):
        datos = (atributo, self.titulo_actual.get())
        flag = False
        if atributo != "":
            self.connection.modificar(datos, nombre_parametro_tabla)
            flag = True
        return flag

    def modificar_datos(self):
        flag_uno = self.generico_modificar(self.titulo_modificar.get(), "titulo")
        flag_dos = self.generico_modificar(self.autor_modificar.get(), "autor")
        flag_tres = self.generico_modificar(self.edicion_modificar.get(), "edicion")
        flag_cuatro = self.generico_modificar(self.lugar_impresion_modificar.get(), "lugar_impresion")
        flag_cinco = self.generico_modificar(self.editorial_modificar.get(), "editorial")
        flag_seis = self.generico_modificar(self.es_traduccion_modificar.get(), "es_traduccion")
        flag_siete = self.generico_modificar(self.cantidad_paginas_modificar.get(), "paginas")
        flag_ocho = self.generico_modificar(self.condicion_modificar.get(), "condicion")

        if flag_uno is True or flag_dos is True or flag_tres is True or flag_cuatro is True:
            mb.showinfo("Información", "Se modificó correctamente!!")
        elif flag_cinco is True or flag_seis is True or flag_siete is True or flag_ocho is True:
            mb.showinfo("Información", "Se modificó correctamente!!")

    def borrar(self):
        datos = (self.titulo_borrar.get(),)
        self.connection.baja("libros", "titulo", datos)
        mb.showinfo("Información", "Libro dado de baja!!")

    def consultar(self):
        datos = (self.titulo_consulta.get(),)
        respuesta = self.connection.consulta(datos)

        if len(respuesta) > 0:
            self.autor_consulta.set(respuesta[0][0])
            self.edicion_consulta.set(respuesta[0][1])
            self.lugar_impresion_consulta.set(respuesta[0][2])
            self.editorial_consulta.set(respuesta[0][3])
            self.es_traduccion_consulta.set(respuesta[0][4])
            self.cantidad_paginas_consulta.set(respuesta[0][5])
            self.condicion_consulta.set(respuesta[0][6])
        else:
            self.autor_consulta.set("")
            self.edicion_consulta.set("")
            self.lugar_impresion_consulta.set("")
            self.editorial_consulta.set("")
            self.es_traduccion_consulta.set("")
            self.cantidad_paginas_consulta.set("")
            self.condicion_consulta.set("")
            mb.showinfo("Información", "No existe un libro con el título ingresado!!")

    def consulta_prestamo(self):
        datos = (self.titulo_prestamo.get(),)
        condicion = self.connection.consulta_prestamo(datos)
        estado = str(condicion[0])
        if estado.lower() == "disponible":
            mb.showinfo("Información", "El libro ingresado esta disponible, puede hacer el prestamo!!")
            self.cargar_prestamo()
            self.libro.set(self.titulo_prestamo.get())
        else:
            mensaje = "El libro ingresado, se encuentra: " + str(condicion[0]) + "!!"
            mb.showerror("Información", mensaje)

    """Interfaz Prestamo"""

    def condicion_prestamo(self):
        self.pagina_seis = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina_seis, text="Prestamo")
        self.label_frame = ttk.LabelFrame(self.pagina_seis, text="Libro a prestar")
        self.label_frame.grid(column=0, row=0, padx=10, pady=10)
        self.label_uno = self.cargar_label(self.label_frame, "Título:", 0)
        self.titulo_prestamo = tk.StringVar()
        self.entry_uno = self.cargar_entry(self.label_frame, self.titulo_prestamo, 0)
        self.boton = ttk.Button(self.label_frame, text="Ver condición", command=self.consulta_prestamo)
        self.boton.grid(column=1, row=1, padx=5, pady=4)

    def cargar_prestamo(self):
        self.label_frame_dos = ttk.LabelFrame(self.pagina_seis, text="Datos del prestamo")
        self.label_frame_dos.grid(column=0, row=2, padx=10, pady=10)
        self.label_uno = self.cargar_label(self.label_frame_dos, "Nombre completo:", 2)
        self.nombre = tk.StringVar()
        self.entry_uno = self.cargar_entry(self.label_frame_dos, self.nombre, 2)
        self.label_dos = self.cargar_label(self.label_frame_dos, "Teléfono:", 3)
        self.telefono = tk.StringVar()
        self.entry_dos = self.cargar_entry(self.label_frame_dos, self.telefono, 3)
        self.label_tres = self.cargar_label(self.label_frame_dos, "Mail:", 4)
        self.mail = tk.StringVar()
        self.entry_tres = self.cargar_entry(self.label_frame_dos, self.mail, 4)
        self.label_cuatro = self.cargar_label(self.label_frame_dos, "Fecha inicio:", 5)
        self.inicio = tk.StringVar()
        self.entry_cuatro = self.cargar_entry(self.label_frame_dos, self.inicio, 5)
        self.label_cinco = self.cargar_label(self.label_frame_dos, "Fecha devolución:", 6)
        self.fin = tk.StringVar()
        self.entry_cinco = self.cargar_entry(self.label_frame_dos, self.fin, 6)
        self.label_seis = self.cargar_label(self.label_frame_dos, "Libro a prestar:", 7)
        self.libro = tk.StringVar()
        self.entry_seis = ttk.Entry(self.label_frame_dos, textvariable=self.libro, state="readonly")
        self.entry_seis.grid(column=1, row=7, padx=4, pady=4)
        self.boton = ttk.Button(self.label_frame_dos, text="Agregar prestamo", command=self.agregar_prestamo)
        self.boton.grid(column=1, row=8, padx=4, pady=4)

    def terminar_prestamo(self):
        self.pagina_siete = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina_siete, text="Terminar prestamo")
        self.label_frame = ttk.LabelFrame(self.pagina_siete, text="Libro prestado")
        self.label_frame.grid(column=0, row=0, padx=10, pady=10)
        self.label_uno = self.cargar_label(self.label_frame, "Título:", 0)
        self.titulo_terminar = tk.StringVar()
        self.entry_uno = self.cargar_entry(self.label_frame, self.titulo_terminar, 0)
        self.boton = ttk.Button(self.label_frame, text="Finalizar prestamo", command=self.borrar_prestamo)
        self.boton.grid(column=1, row=1, padx=4, pady=4)

    def reclamar_prestamo(self):
        self.pagina_ocho = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina_ocho, text="Reclamar prestamo")
        self.label_uno = self.cargar_label(self.pagina_ocho, "Fecha actual:", 0)
        self.fecha = tk.StringVar()
        self.entry_uno = self.cargar_entry(self.pagina_ocho, self.fecha, 0)
        self.boton = ttk.Button(self.pagina_ocho, text="Ver datos", command=self.reclamos)
        self.boton.grid(column=1, row=1, padx=4, pady=4)

    """Prestamo + Base de datos"""

    def agregar_prestamo(self):
        datos = (
            self.telefono.get(), self.nombre.get(), self.mail.get(), self.inicio.get(), self.fin.get(),
            self.libro.get())
        self.connection.alta_prestamo(datos)
        # Modificar condición del libro.
        dato = ("Préstamo en proceso", self.libro.get())
        self.connection.modificar_estado_prestamo(dato)
        mb.showinfo("Información", "Prestamo realizado correctamente!!")

    def borrar_prestamo(self):
        datos_uno = ("Disponible", self.titulo_terminar.get())
        datos_dos = (self.titulo_terminar.get(),)
        self.connection.modificar_estado_prestamo(datos_uno)
        self.connection.baja("prestamo", "libro", datos_dos)
        msj = "El libro " + self.titulo_terminar.get() + " ya se encuentra: Disponible."
        mb.showinfo("Información", msj)

    def reclamos(self):
        self.scroll_dos = st.ScrolledText(self.pagina_ocho, width=95, height=23)
        self.scroll_dos.grid(column=0, row=0, padx=10, pady=10)
        fecha_ingresada = self.fecha.get()
        lista_devolver = self.connection.mostrar_prestamo(fecha_ingresada)
        self.scroll_dos.delete("1.0", tk.END)
        self.scroll_dos.insert("1.0", lista_devolver)

    """Parte del menú"""

    def menu_opciones(self):
        menuOp = tk.Menu(self.ventana)
        self.ventana.config(menu=menuOp)
        opciones = tk.Menu(menuOp, tearoff=0)
        opciones.add_command(label="Actualizar lista libros", command=self.mostrar_datos)
        opciones.add_separator()
        opciones.add_command(label="Cerrar ventana", command=self.salir)
        menuOp.add_cascade(label="Opciones", menu=opciones)

    def mostrar_datos(self):
        lista = self.connection.mostrar()
        if lista != "":
            self.scroll.delete("1.0", tk.END)
            self.scroll.insert("1.0", lista)

    def salir(self):
        sys.exit()


def test():
    Biblioteca()


if __name__ == '__main__':
    # Script principal
    test()
