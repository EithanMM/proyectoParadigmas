import os, fnmatch
from tkinter import *
from tkinter import scrolledtext
from tkinter import Menu
import fileinput
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
    global VG
    global vars
    global isChecked

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.archivo_actual = ""
        self.isChecked = False
        self.vars = "wxyz"
        self.lista_reglas = []
        self.marcadores = "αβγδεζηθμλξπσφψωABCDEFGHIJKLMNOPQRSTUWXYZ"
        self.simbolos = "abcdefghijklmnopqrstuvwxyz0123456789|"
        self.VG = []
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
        item2.add_command(label="Cargar Gramatica", command=self.open_archive)

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
                                    bg="chartreuse2", fg="firebrick1", command=self.obtener_reglas_de_consola)
        self.btn_paso_paso.place(x=298, y=60)

        self.btn_eval_golpe = Button(self.master, text="Evaluar", state=ACTIVE, width=15, height=1, bd=2,
                                     bg="chartreuse2", fg="firebrick1", command=self.mostrar_resultado)
        self.btn_eval_golpe.place(x=470, y=60)

        self.var = IntVar()
        self.btn_radio = Radiobutton(self.master, text="evaluar regla de panel izquierdo", variable=self.var, value=1, command=self.check_option)
        self.btn_radio.place(x=298, y=250)

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
        #si la lista de reglas no esta vacia, osea que cargaron otro algoritmo antes.
        if len(self.lista_reglas) != 0:

            self.scroll_text.delete("1.0", END)
            self.scroll_text2.delete("1.0", END)

            del self.lista_reglas[:] #eliminamos cualquier la totalidad de los elementos
            del self.VG[:] #eliminamos las variables viejas de la lista de variables.

            nombre_algoritmo = str(filename)
            nombre_algoritmo = nombre_algoritmo.replace("C:/PycharmProjects/paradigmas/Algoritmos/", "")

            self.archivo_actual = filename  # guardamos la direccion
            fo = open(filename, "r", encoding='utf-8')
            self.analyze_text(filename)
            print(self.lista_reglas)
            self.scroll_text.insert(INSERT, fo.read())
            fo.close()
            mensa = messagebox.showinfo("", nombre_algoritmo + " cargado")

        else:
            self.scroll_text.delete("1.0", END)
            self.scroll_text2.delete("1.0", END)
            # muestra en el scrolltext de abajo, que tipo de algoritmo se esta usando
            nombre_algoritmo = str(filename)
            nombre_algoritmo = nombre_algoritmo.replace("C:/PycharmProjects/paradigmas/Algoritmos/", "")

            self.archivo_actual = filename  # guardamos la direccion
            # vamos a leer lo que contenga el archivo y se imprime en pantalla.
            fo = open(filename, "r", encoding='utf-8')
            self.analyze_text(filename)
            print(self.VG)
            # print(self.lista_reglas)
            self.scroll_text.insert(INSERT, fo.read())
            fo.close()

            mensa = messagebox.showinfo("", nombre_algoritmo + " cargado")

    def new_archive(self):
        print("nuevo archivo")

    def analyze_text(self, filename):
        bandera = False

        with open(filename, "r", encoding='utf-8') as fo:
            while True:
                line = fo.readline()
                if line == '': #si es fin de linea
                    if bandera == False: # sino encontro '#vars'
                        break
                    else: # si encontro '#vars'
                        break

                elif line.startswith('%') or line.startswith('#symbols') or line.startswith('#markers') or line.startswith('\n'):
                    continue
                else:
                    # temp tendra el identificador '#vars'
                    temp = line[1:6]
                    print(len(temp))
                    if temp == "#vars": #si '#vars' se encuentra dentro del documento.
                       bandera = True
                       x = line.rsplit(' ', -1)[-1]
                       self.recorrer_string_vars(x) #aguegue las variables a VG.

                    else: #  si '#vars' no se ecuentra en el documento.
                        c = 0
                        a = ""
                        c_numero = ""
                        if line.startswith('P'): # si nos encontramos lineas que poseean etiquetas
                            for x in line:
                                if x == ":":
                                    c = c + 2
                                    break
                                else:
                                    c = c + 1
                        # se agregaran las reglas a  la variable a
                        while  c < len(line) and line[c] != ' ':
                            a = a + line[c]
                            print(a)
                            c = c + 1

                        # este while busca si en la linea, encuentra un valor numerico,
                        # si lo hace corresponde a la etiqueta de la regla
                        while c < len(line)-1:
                            if self.RepresentsInt(line[c]):
                                c_numero = c_numero + line[c]
                                print(c_numero)
                            c = c + 1

                        # si el archivo posee etiquetas y variables
                        if c_numero != '' and a != '':

                            # si  no se encontraron variables en el archivo, agregue las que estan por defecto
                            if len(self.VG) == 0:
                                self.recorrer_string_vars(self.vars)


                            obj = a.split('->')
                            if "\n" in obj[1]:
                                obj[1] = obj[1].partition('\n')[0]
                            elif ' ' in obj[1]:
                                obj[1] = obj[1].partition(' ')[0]

                            if '.' in obj[1]:
                                obj[1].replace('.', '')
                                R = Regla(obj[0], obj[1], int(c_numero), True, self.VG)
                                self.lista_reglas.append(R)

                            else:
                                R = Regla(obj[0], obj[1], int(c_numero), False, self.VG)
                                self.lista_reglas.append(R)

                        # sino posee atiquetas
                        elif c_numero == '' and a != '':

                            # si  no se encontraron variables en el archivo, agregue las que estan por defecto
                            if len(self.VG) == 0:
                                self.recorrer_string_vars(self.vars)



                            obj = a.split('->')
                            if "\n" in obj[1]:
                                obj[1] = obj[1].partition('\n')[0]
                            elif ' ' in obj[1]:
                                obj[1] = obj[1].partition(' ')[0]


                            if '.' in obj[1]:
                                obj[1].replace('.', '')
                                R = Regla(obj[0], obj[1], None, True, self.VG)
                                self.lista_reglas.append(R)

                            else:
                                R = Regla(obj[0], obj[1], None, False, self.VG)
                                self.lista_reglas.append(R)


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
        #Una vez que se cargue el algoritmo, vamos a obtener la entrada del usuario.
        text = self.user_input.get()
        if text == '':
            messagebox.showinfo("Mensaje", "Digite una cadena a evaluar")
        else:

            if self.var.get() == 1:
                if len(self.VG) != 0:
                    del self.VG[:]
                if len(self.lista_reglas) != 0:
                    del self.lista_reglas[:]

                bandera = False
                temp = str(self.scroll_text.get("1.0", "end-1c"))
                temp = temp.split('\n')
                for line in temp: # va  a leer cada linea
                    print(line)
                    if line == '':
                        continue

                    elif line.startswith('%') or line.startswith('#symbols') or line.startswith('#markers') or line.startswith('\n'):
                        continue
                    else:
                        temp2 = line[:5]
                        print(temp2)
                        if temp2 == '#vars':
                            bandera = True
                            x = line.rsplit(' ', -1)[-1]
                            self.recorrer_string_vars(x)
                        else:
                            c = 0
                            a = ""
                            c_numero = ""
                            if line.startswith('P'):
                                for x in line:
                                    if x == ":":
                                        c = c + 2
                                        break
                                    else:
                                        c = c + 1

                            while c < len(line) and line[c] != ' ':
                                a = a + line[c]
                                print(a)
                                c = c + 1

                            while c < len(line)-1:
                                if self.RepresentsInt(line[c]):
                                    c_numero = c_numero + line[c]
                                    print(c_numero)
                                c = c + 1

                            if c_numero != '' and a != '':
                                if len(self.VG) == 0:
                                    self.recorrer_string_vars(self.vars)

                                obj = a.split('->')
                                if ' ' in obj[1]:
                                    obj[1] = obj[1].partition(' ')[0]

                                if '.' in obj[1]:
                                    obj[1].replace('.', '')
                                    R = Regla(obj[0], obj[1], None, int(c_numero), self.VG)
                                    self.lista_reglas.append(R)

                                else:
                                    R = Regla(obj[0], obj[1], int(c_numero), False, self.VG)
                                    self.lista_reglas.append(R)

                            elif c_numero == '' and a != '':
                                if len(self.VG) == 0:
                                    self.recorrer_string_vars(self.vars)

                                obj = a.split('->')
                                if ' ' in obj[1]:
                                    obj[1] = obj[1].partition(' ')[0]

                                if '.' in obj[1]:
                                    obj[1].replace('.', '')
                                    R = Regla(obj[0], obj[1], None, False, self.VG)
                                    self.lista_reglas.append(R)

                                else:
                                    R = Regla(obj[0], obj[1], None, False, self.VG)
                                    self.lista_reglas.append(R)

                #nos salimos del for
                M1 = Markov(self.lista_reglas)
                res = M1.runAlgorithm(text)
                self.scroll_text2.insert(INSERT, "\nReglas - Resultado\n")
                for x in res:
                    print(x)
                    self.scroll_text2.insert(INSERT, x + "\n")

                x = str(res[-1])
                x = x.replace('""', '')
                self.scroll_text2.insert(INSERT, "Resultado Final: " + x.rsplit(':', -1)[-1])

            else:
                M1 = Markov(self.lista_reglas)
                res = M1.runAlgorithm ( text )
                self.scroll_text2.insert(INSERT, "\nReglas - Resultado\n")
                for x in res:
                    print(x)
                    self.scroll_text2.insert(INSERT, x+"\n")
                    self.scroll_text2.see(END)

                x =str(res[-1])
                x = x.replace('""', '')
                self.scroll_text2.insert(INSERT, "Resultado Final: " + x.rsplit(':', -1)[-1])

    def recorrer_string_vars(self, x):
        for val in x:
            if val != "\n":
                self.VG.append(val)
                print(self.VG)
            else:
                continue

    def RepresentsInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False


    def obtener_reglas_de_consola(self):


        conttador = 0
        text = self.user_input.get()
        if text == '':
            messagebox.showinfo("Mensaje", "Digite una cadena a evaluar")
        else:

            if self.var.get() == 1:
                if len(self.VG) != 0:
                    del self.VG[:]
                if len(self.lista_reglas) != 0:
                    del self.lista_reglas[:]

                bandera = False
                temp = str(self.scroll_text.get("1.0", "end-1c"))
                temp = temp.split('\n')
                for line in temp: # va  a leer cada linea
                    print(line)
                    if line == '':
                        continue

                    elif line.startswith('%') or line.startswith('#symbols') or line.startswith('#markers') or line.startswith('\n'):
                        continue
                    else:
                        temp2 = line[:5]
                        print(temp2)
                        if temp2 == '#vars':
                            bandera = True
                            x = line.rsplit(' ', -1)[-1]
                            self.recorrer_string_vars(x)
                        else:
                            c = 0
                            a = ""
                            c_numero = ""
                            if line.startswith('P'):
                                for x in line:
                                    if x == ":":
                                        c = c + 2
                                        break
                                    else:
                                        c = c + 1

                            while c < len(line) and line[c] != ' ':
                                a = a + line[c]
                                print(a)
                                c = c + 1

                            while c < len(line)-1:
                                if self.RepresentsInt(line[c]):
                                    c_numero = c_numero + line[c]
                                    print(c_numero)
                                c = c + 1

                            if c_numero != '' and a != '':
                                if len(self.VG) == 0:
                                    self.recorrer_string_vars(self.vars)

                                obj = a.split('->')
                                if ' ' in obj[1]:
                                    obj[1] = obj[1].partition(' ')[0]

                                if '.' in obj[1]:
                                    obj[1].replace('.', '')
                                    R = Regla(obj[0], obj[1], None, int(c_numero), self.VG)
                                    self.lista_reglas.append(R)

                                else:
                                    R = Regla(obj[0], obj[1], int(c_numero), False, self.VG)
                                    self.lista_reglas.append(R)

                            elif c_numero == '' and a != '':
                                if len(self.VG) == 0:
                                    self.recorrer_string_vars(self.vars)

                                obj = a.split('->')
                                if ' ' in obj[1]:
                                    obj[1] = obj[1].partition(' ')[0]

                                if '.' in obj[1]:
                                    word = str(obj[1])
                                    word = word.replace('.', '')
                                    obj[1] = word

                                    R = Regla(obj[0], obj[1], None, False, self.VG)
                                    self.lista_reglas.append(R)

                                else:
                                    R = Regla(obj[0], obj[1], None, False, self.VG)
                                    self.lista_reglas.append(R)

                #aqui estamos fuera del for
                print(self.VG)
                M1 = Markov(self.lista_reglas)
                res = M1.runAlgorithm(text)

                self.scroll_text2.insert(INSERT, "\nReglas - Resultado\n")
                for x in res:
                    result = messagebox.askquestion("Siguiente paso", "siguiente paso?")
                    if result == 'yes':
                        self.scroll_text2.insert(INSERT, x + "\n")
                        self.scroll_text2.see(END)
                    else:
                        break

                x = str(res[-1])
                x = x.replace('""', '')
                self.scroll_text2.insert(INSERT, "Resultado Final: " + x.rsplit(':', -1)[-1])

            else: # si el radio button no esta clickeado

                M1 = Markov(self.lista_reglas)
                res = M1.runAlgorithm(text)
                self.scroll_text2.insert(INSERT, "\nReglas - Resultado\n")
                for x in res:
                    result = messagebox.askquestion("Siguiente paso", "siguiente paso?")
                    if result == 'yes':
                        self.scroll_text2.insert(INSERT, x + "\n")
                        self.scroll_text2.see(END)
                    else:
                        break

                x = str(res[-1])
                x = x.replace('""', '')
                self.scroll_text2.insert(INSERT, "Resultado Final: " + x.rsplit(':', -1)[-1])


    def check_option(self):
        if self.isChecked == False:
            self.isChecked = True

            print("checkbox seleccionado " + str(self.var.get()))
        else:
            self.isChecked = False
            self.var.set(0)
            print("checkbox deseleccioando "+ str(self.var.get()))


# Este es el nuevo Main
if __name__ == "__main__":
    root = Tk()
    root.geometry("600x600")
    root.resizable(0, 0)
    app = ventana_principal(root)
    root.mainloop()
