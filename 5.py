from tkinter import Tk, Menu, messagebox, simpledialog, Text
import pandas as pd

class MenuApp:
    def __init__(self, master):
        self.master = master
        self.create_menu()
        self.nombreArchivo ="/home/b5/Documentos/5B/gonzalo pana/tkinter/0"
        self.estudiantes = pd.read_excel(self.nombreArchivo)

        self.text_area = Text(master,wrap="word", height=20, width=60)
        self.text_area.pack(side="left", fill="both", expand=True)
    def create_menu(self):
        # Crear la barra de menú
        barra_menus = Menu(self.master)

        # Crear el menú "Excel"
        menu_excel = Menu(barra_menus, tearoff=0)
        menu_calc = Menu(barra_menus, tearoff=0)
        
        barra_menus.add_cascade(label="Excel", menu=menu_excel)
        barra_menus.add_cascade(label="Calculos", menu=menu_calc)
        
        menu_calculos=Menu(barra_menus,tearoff=0)
        barra_menus.add_cascade(label="Calculo",menu=menu_calculos)
        
        # Agregar opciones al menú "Excel"
        menu_excel.add_command(label="Todos", command=self.show_all)
        menu_excel.add_command(label="Nombre", command=self.show_name)
        menu_excel.add_command(label="Mayores de 18", command=self.show_over_18)

        menu_calculos.add_command(label="Promedio", command=self.mesi)
        menu_calculos.add_command(label="Mediana", command=self.amen)
        menu_calculos.add_command(label="Moda", command=self.homero)
        # Configurar la barra de menú en la ventana principal
        self.master.config(menu=barra_menus)

    def clear_text_area(self):
        self.text_area.delete(1.0, "end")
            
    def show_all(self):
        self.clear_text_area()
        self.text_area.insert("end",str(self.estudiantes))

    def show_name(self):
        name = simpledialog.askstring("Nombre", "Introduce tu nombre:")
        if name:
            messagebox.showinfo("Nombre ingresado", f"Tu nombre es: {name}")

    def show_over_18(self):
        age = simpledialog.askinteger("Edad", "Introduce tu edad:")
        if age is not None:
            if age >= 18:
                messagebox.showinfo("Acceso permitido", "Eres mayor de 18 años.")
            else:
                messagebox.showwarning("Acceso denegado", "Eres menor de 18 años.")
            if age >= 105:
                messagebox.showinfo("Que?", "WTF tanto?, deberias estar muerto")
    def mesi(self):                
        age = simpledialog.askinteger("promedio", "Ingrese su nota:")
        
    def amen(self):
        age = simpledialog.askinteger("Edad", "Introduce tu edad:")
       
    def homero(self):
        age = simpledialog.askinteger("Edad", "Introduce tu edad:")
    def salir(self):
        while self:
         break
    
class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Aplicación con Menú Excel")
        # Crear el menú
        self.menu_app = MenuApp(self.root)

    def run(self):
        self.root.mainloop()

if __name__== "__main__":
    app = App()
    app.run()