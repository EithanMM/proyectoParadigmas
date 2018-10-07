import os, fnmatch
from tkinter import *
from tkinter import scrolledtext
from tkinter import Menu
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from datetime import datetime


class ventana_principal(Frame):

    global archivo_actual #variable global que alberga la direccion actual del archivo que se esta modificando

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.archivo_actual = ""
        self.init_window()

    def salir(self):
        sys.exit(0)

    def init_window(self):
        self.master.title("Proyecto Paradigmas")
        self.pack(fill=BOTH, expand=1)

        # creamos una instancia del menu
        menu = Menu(self.master)

        self.master.config(menu=menu)

        # creamos un objeto
        item1 = Menu(menu, tearoff=0)
        item2 = Menu(menu, tearoff=0)

        # elementos que va a contener el menu de arriba
        menu.add_cascade(label="Archivo", menu=item1)
        item1.add_command(label="Nueva gramatica", command=self.clear_texts)
        item1.add_command(label="Salvar gramatica", command=self.modify_archive)
        item1.add_command(label="Salir", command=self.salir)

        menu.add_cascade(label="Editar", menu=item2)
        item2.add_command(label="Editar Gramatica", command=self.open_archive)

        # campos de texto
        self.scroll_text = scrolledtext.ScrolledText(self.master, width=97, height=18)
        self.scroll_text.pack()
        self.scroll_text2 = scrolledtext.ScrolledText(self.master, width=97, height=17)
        self.scroll_text2.pack()
        # botones-alfabeto griego
        self.button_a = Button(self.master, text="α", state=ACTIVE, width=4, height=5, command= lambda: self.write_greek_alphabet("α"))
        self.button_a.pack(side=LEFT)

        self.button_b = Button(self.master, text="β", state=ACTIVE, width=4, height=5, command=lambda: self.write_greek_alphabet("β"))
        self.button_b.pack(side=LEFT)

        self.button_c = Button(self.master, text="γ", state=ACTIVE, width=4, height=5, command=lambda: self.write_greek_alphabet("γ"))
        self.button_c.pack(side=LEFT)

        self.button_d = Button(self.master, text="δ", state=ACTIVE, width=4, height=5, command=lambda: self.write_greek_alphabet("δ"))
        self.button_d.pack(side=LEFT)

        self.button_e = Button(self.master, text="ε", state=ACTIVE, width=4, height=5, command=lambda: self.write_greek_alphabet("ε"))
        self.button_e.pack(side=LEFT)

        self.button_f = Button(self.master, text="ζ", state=ACTIVE, width=4, height=5, command=lambda: self.write_greek_alphabet("ζ"))
        self.button_f.pack(side=LEFT)

        self.button_g = Button(self.master, text="η", state=ACTIVE, width=4, height=5, command=lambda: self.write_greek_alphabet("η"))
        self.button_g.pack(side=LEFT)

        self.button_g = Button(self.master, text="θ", state=ACTIVE, width=4, height=5, command=lambda: self.write_greek_alphabet("θ"))
        self.button_g.pack(side=LEFT)

        self.button_g = Button(self.master, text="μ", state=ACTIVE, width=4, height=5, command=lambda: self.write_greek_alphabet("μ"))
        self.button_g.pack(side=LEFT)

        self.button_g = Button(self.master, text="λ", state=ACTIVE, width=4, height=5, command=lambda: self.write_greek_alphabet("λ"))
        self.button_g.pack(side=LEFT)

        self.button_g = Button(self.master, text="ξ", state=ACTIVE, width=4, height=5, command=lambda: self.write_greek_alphabet("ξ"))
        self.button_g.pack(side=LEFT)

        self.button_g = Button(self.master, text="π", state=ACTIVE, width=4, height=5, command=lambda: self.write_greek_alphabet("π"))
        self.button_g.pack(side=LEFT)

        self.button_g = Button(self.master, text="σ", state=ACTIVE, width=4, height=5, command=lambda: self.write_greek_alphabet("σ"))
        self.button_g.pack(side=LEFT)

        self.button_g = Button(self.master, text="φ", state=ACTIVE, width=4, height=5, command=lambda: self.write_greek_alphabet("φ"))
        self.button_g.pack(side=LEFT)

        self.button_g = Button(self.master, text="ψ", state=ACTIVE, width=4, height=5, command=lambda: self.write_greek_alphabet("ψ"))
        self.button_g.pack(side=LEFT)

        self.button_g = Button(self.master, text="ω", state=ACTIVE, width=4, height=5, command=lambda: self.write_greek_alphabet("ω"))
        self.button_g.pack(side=LEFT)

    def write_greek_alphabet(self, temp):
        self.scroll_text.insert(INSERT, temp)

    def open_archive(self):
        filename = askopenfilename(
            initialdir=os.getcwd()+"/Algoritmos/",
            filetypes=(("Text File", "*.txt"), ("XML Files", "*.xml")),
            title= "Elija una gramatica"
        )

        #muestra en el scrolltext de abajo, que tipo de algoritmo se esta usando
        nombre_algoritmo = str(filename)
        nombre_algoritmo = nombre_algoritmo.replace("C:/PycharmProjects/paradigmas/Algoritmos/", "")

        self.archivo_actual = filename #guardamos la direccion
        # vamos a leer lo que contenga el archivo y se imprime en pantalla.
        fo = open(filename, "r", encoding='utf-8')
        self.scroll_text.insert(INSERT, fo.read())
        fo.close()

        message = messagebox.showinfo("Mensaje", "Algoritmo cargado :" + nombre_algoritmo)

    def new_archive(self):
        print("nuevo archivo")

    def modify_archive(self):

        if self.archivo_actual == "": # si no se selecciono "abrir gramatica" antes.
            filename = asksaveasfilename(
                initialdir=os.getcwd()+"/Algoritmos/",
                filetype=(("Text File", "*.txt"), ("XML Files", "*.xml")),
                title="Salvar gramatica"
            )

            if not filename: # si le dio a "cancelar" o la  "x"
                print("archivo no seleccionado")

            else:
                fo = open(filename, "w", encoding='utf-8')
                fo.write(self.scroll_text.get("1.0", END))
                fo.close()
                print("gramatica modificada")

        else: # si se selecciono "abrir gramatica" antes

            fo = open(self.archivo_actual, "w", encoding='utf-8')
            fo.write(self.scroll_text.get("1.0", END))
            fo.close()
            self.archivo_actual = ""  # limpiamos la variable
            mens = messagebox.showinfo("advertencia","gramatica modificada");


    def clear_texts(self):
        res = messagebox.askyesno("Advertencia","Desea guardar el archivo?")
        if res == True:
            filename = asksaveasfilename(
                initialdir=os.getcwd()+"/Algoritmos/",
                filetype=(("Text File", "*.txt"), ("XML Files", "*.xml")),
                title="Salvar gramatica"
            )
            if not filename:
                print("gramatica no guardada")
            else:
                fo = open(filename, "w", encoding='utf-8')
                fo.write(self.scroll_text.get("1.0", END))
                fo.close()
                print("gramatica guardada")
        else:
            self.scroll_text.delete("1.0", END)
            self.scroll_text2.delete("1.0", END)
            print("campos limpiados")