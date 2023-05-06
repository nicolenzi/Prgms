

"""ventana = Tk()
ventana.geometry("600x600")

estilos = ttk.Style()
estilos.theme_use("clam")
estilos.configure("boton.TButton",background="orange")
estilos.map("boton2.TButton",
			background=[("pressed","blue"),("active","red")])



titulo = Label(ventana,text="clase 21-4",bg="red",fg="white")
titulo.pack()
titulo2 = ttk.Label(ventana,text="programacion 2")
titulo2.pack()

boton = Button(ventana,text="Guardar")
boton.pack()

boton2 = ttk.Button(ventana,text="Guardar2", style="boton.TButton")
boton2.pack()

boton3 = ttk.Button(ventana,text="otro", style="boton2.TButton")
boton3.pack()

ventana.mainloop()
"""

ventana = Tk()
ventana.geometry("400x600")

titulo = Label(ventana,text="JUGANDO")
titulo.place(x=200,y=50)

titulo.after(1000,Lambda:titulo.place(x=20,y=10))
#titulo.after(2000,Lambda:titulo.place(x=20,y=10))

ventana.mainloop()