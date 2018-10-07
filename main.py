import tkinter as tk
from tkinter import *
from paradigmas import interfaz


print (__name__)
if __name__ == "__main__":
 root = Tk()
 root.geometry("600x600")
 app = interfaz.ventana_principal(root)
 root.mainloop()
