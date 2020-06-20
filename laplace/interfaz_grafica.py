import tkinter as tk

from laplace import ecuaciones_diferenciales

master = tk.Tk()
tk.Label(master, text="coeficiente derivada").grid(row=0)
tk.Label(master, text="coeficiente de la funcion").grid(row=1)
tk.Label(master, text="funcion t").grid(row=2)
tk.Label(master, text="condicion inicial").grid(row=3)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Label(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)

def show_entry_fields():
    ec = ecuaciones_diferenciales(e1.get(), e2.get(), e3.get(), e4.get())
    resultado = ec.resolver()
    e5.configure(text=resultado)

tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=5,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Show', command=show_entry_fields).grid(row=5,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)

master.mainloop()