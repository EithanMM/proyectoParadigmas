import os, fnmatch
from tkinter import *
from tkinter import scrolledtext
from tkinter import Menu
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from paradigmas.algoritmo import Regla
from paradigmas.Markov import Markov

from datetime import datetime


class ventana_principal(Frame):
    global archivo_actual  # variable global que alberga la direccion actual del archivo que se esta modificando
    global lista_reglas
    global marcadores  # aqui se guardaran todos los simbolos romandos que hay en el programa
    global simbolos  # aqui se guardaran

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.archivo_actual = ""
        self.lista_reglas = []
        self.marcadores = "αβγδεζηθμλξπσφψωABCDEFGHIJKLMNOPQRSTUWXYZ"
        self.simbolos = "abcdefghijklmnopqrstuvwxyz0123456789|"
        self.init_window()

    def salir(self):
        sys.exit(0)

    def init_window(self):
        self.master.title("Proyecto Paradigmas")
        # self.pack(fill=BOTH, expand=1)

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

        # CAMPOS DE TEXTO
        self.scroll_text = scrolledtext.ScrolledText(self.master)
        self.scroll_text.place(x=0, y=0, width=300, height=300)

        self.scroll_text2 = scrolledtext.ScrolledText(self.master)
        self.scroll_text2.place(x=0, y=300, width=600, height=270)

        # INPUT PARA EL USUARIO
        self.user_input = Entry(self.master)
        self.user_input.place(x=300, y=0, width=290, height=50)

        # BOTONES PARA EVALUAR
        self.btn_paso_paso = Button(self.master, text="Evaluar paso a paso", state=ACTIVE, width=15, height=1, bd=2,
                                    bg="chartreuse2", fg="firebrick1")
        self.btn_paso_paso.place(x=298, y=60)

        self.btn_eval_golpe = Button(self.master, text="Evaluar", state=ACTIVE, width=15, height=1, bd=2,
                                     bg="chartreuse2", fg="firebrick1",command=self.mostrar_resultado)
        self.btn_eval_golpe.place(x=470, y=60)

        # BOTONES LETRAS GRIEGAS
        self.button_a = Button(self.master, text="α", state=ACTIVE, width=3, height=1,
                               command=lambda: self.write_greek_alphabet("α"))
        self.button_b = Button(self.master, text="β", state=ACTIVE, width=3, height=1,
                               command=lambda: self.write_greek_alphabet("β"))
        self.button_c = Button(self.master, text="γ", state=ACTIVE, width=3, height=1,
                               command=lambda: self.write_greek_alphabet("γ"))
        self.button_d = Button(self.master, text="δ", state=ACTIVE, width=3, height=1,
                               command=lambda: self.write_greek_alphabet("δ"))
        self.button_e = Button(self.master, text="ε", state=ACTIVE, width=3, height=1,
                               command=lambda: self.write_greek_alphabet("ε"))
        self.button_f = Button(self.master, text="ζ", state=ACTIVE, width=3, height=1,
                               command=lambda: self.write_greek_alphabet("ζ"))
        self.button_g = Button(self.master, text="η", state=ACTIVE, width=3, height=1,
                               command=lambda: self.write_greek_alphabet("η"))
        self.button_h = Button(self.master, text="θ", state=ACTIVE, width=3, height=1,
                               command=lambda: self.write_greek_alphabet("θ"))
        self.button_i = Button(self.master, text="μ", state=ACTIVE, width=3, height=1,
                               command=lambda: self.write_greek_alphabet("μ"))
        self.button_j = Button(self.master, text="λ", state=ACTIVE, width=3, height=1,
                               command=lambda: self.write_greek_alphabet("λ"))
        self.button_k = Button(self.master, text="ξ", state=ACTIVE, width=3, height=1,
                               command=lambda: self.write_greek_alphabet("ξ"))
        self.button_l = Button(self.master, text="π", state=ACTIVE, width=3, height=1,
                               command=lambda: self.write_greek_alphabet("π"))
        self.button_m = Button(self.master, text="σ", state=ACTIVE, width=3, height=1,
                               command=lambda: self.write_greek_alphabet("σ"))
        self.button_n = Button(self.master, text="φ", state=ACTIVE, width=3, height=1,
                               command=lambda: self.write_greek_alphabet("φ"))
        self.button_o = Button(self.master, text="ψ", state=ACTIVE, width=3, height=1,
                               command=lambda: self.write_greek_alphabet("ψ"))
        self.button_p = Button(self.master, text="ω", state=ACTIVE, width=3, height=1,
                               command=lambda: self.write_greek_alphabet("ω"))

        # POSICIONES LETRAS GRIEGAS

        self.button_a.place(x=0, y=570)
        self.button_b.place(x=25, y=570)
        self.button_c.place(x=50, y=570)
        self.button_d.place(x=75, y=570)
        self.button_e.place(x=100, y=570)
        self.button_f.place(x=125, y=570)
        self.button_g.place(x=150, y=570)
        self.button_h.place(x=175, y=570)
        self.button_i.place(x=200, y=570)
        self.button_j.place(x=225, y=570)
        self.button_k.place(x=250, y=570)
        self.button_l.place(x=275, y=570)
        self.button_m.place(x=300, y=570)
        self.button_n.place(x=325, y=570)
        self.button_o.place(x=350, y=570)
        self.button_p.place(x=375, y=570)

    def write_greek_alphabet(self, temp):
        self.scroll_text.insert(INSERT, temp)

    def open_archive(self):
        filename = askopenfilename(
            initialdir=os.getcwd() + "/Algoritmos/",
            filetypes=(("Text File", "*.txt"), ("XML Files", "*.xml")),
            title="Elija una gramatica"
        )

        # muestra en el scrolltext de abajo, que tipo de algoritmo se esta usando
        nombre_algoritmo = str(filename)
        nombre_algoritmo = nombre_algoritmo.replace("C:/PycharmProjects/paradigmas/Algoritmos/", "")

        self.archivo_actual = filename  # guardamos la direccion
        # vamos a leer lo que contenga el archivo y se imprime en pantalla.
        fo = open(filename, "r", encoding='utf-8')
        self.analyze_text(filename)
        print(self.lista_reglas)
        self.scroll_text.insert(INSERT, fo.read())
        fo.close()

        mensa = messagebox.showinfo("", nombre_algoritmo + " cargado")

    def new_archive(self):
        print("nuevo archivo")

    def analyze_text(self, filename):

        with open(filename, "r", encoding='utf-8') as fo:
            while True:
                line = fo.readline()
                if line == '':
                    break
                if line.startswith('%'):
                    continue
                else:
                    line.replace('\\n', '')
                    a = line.split("->")
                    if -1 != a[1].find('.'):
                        a[1].replace('.', '')
                    else:
                        print(a[0])
                        print(a[1])

    def modify_archive(self):

        if self.archivo_actual == "":  # si no se selecciono "abrir gramatica" antes.
            filename = asksaveasfilename(
                initialdir=os.getcwd() + "/Algoritmos/",
                filetype=(("Text File", "*.txt"), ("XML Files", "*.xml")),
                title="Salvar gramatica"
            )

            if not filename:  # si le dio a "cancelar" o la  "x"
                print("archivo no seleccionado")

            else:
                fo = open(filename, "w", encoding='utf-8')
                fo.write(self.scroll_text.get("1.0", END))
                fo.close()
                print("gramatica modificada")

        else:  # si se selecciono "abrir gramatica" antes

            fo = open(self.archivo_actual, "w", encoding='utf-8')
            fo.write(self.scroll_text.get("1.0", END))
            fo.close()
            self.archivo_actual = ""  # limpiamos la variable
            mensaje2 = messagebox.showinfo("Mensaje", "gramatica guardada")

    def clear_texts(self):
        res = messagebox.askyesno("Advertencia", "Desea guardar el archivo?")
        if res == True:
            filename = asksaveasfilename(
                initialdir=os.getcwd() + "/Algoritmos/",
                filetype=(("Text File", "*.txt"), ("XML Files", "*.xml")),
                title="Salvar gramatica"
            )

            if not filename:
                print("algoritmo no salvado")
            else:
                fo = open(filename, "w", encoding='utf-8')
                fo.write(self.scroll_text.get("1.0", END))
                fo.close()
                print("gramatica guardada")
        else:
            self.scroll_text.delete("1.0", END)
            self.scroll_text2.delete("1.0", END)
            print("campos limpiados")
    def mostrar_resultado(self):
        marvov = Markov
        C1 = '101'
        V1 = ('x', 'y', 'z')
        V2 = ['x', 'y', 'z']
        R1 = Regla("|0", "0||", None, False, V1, V2)
        R2 = Regla("1", "0|", None, False, V1, V2)
        R3 = Regla("0", "", None, False, V1, V2)
        R4 = Regla("A", "apple", None, False, V1, V2)
        M1 = Markov([R1, R2, R3, R4])
        res = M1.runAlgorithm ( C1 )
        for x in res:
            self.scroll_text2.insert(INSERT, x+"\n")




# Este es el nuevo Main
if __name__ == "__main__":
    root = Tk()
    root.geometry("600x600")
    root.resizable(0, 0)
    app = ventana_principal(root)
    root.mainloop()
