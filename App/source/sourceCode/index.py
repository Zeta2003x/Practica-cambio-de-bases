import tkinter as tk
import re
from random import randint
from random import choice

class Application(tk.Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.master.config(bg="#181818")
		self.config(bg="#777777")
		self.master.title("Practica de cambio de bases")
		self.master.resizable(0,0)
		self.pack()
		self.crearWidgets()

	def crearWidgets(self):
		self.base_a = ""
		self.base_b = ""

		self.label1 = tk.Label(self)
		self.label1.grid(row=1, column=1)
		self.label1.config(width=25, background="#777777", padx=20, anchor="w")

		self.valorSalida = tk.StringVar(self)
		self.labelSalida = tk.Label(self, textvariable=self.valorSalida)
		self.labelSalida.grid(row=1, column=2, padx=10, pady=10)
		self.labelSalida.config(bg="#222222",fg="#cccccc", justify="center", width=20)

		self.label2 = tk.Label(self)
		self.label2.grid(row=2, column=1)
		self.label2.config(width=25, background="#777777", padx=20, anchor="w")

		self.valorEntrada = tk.StringVar(self)
		self.entradaRespuesta = tk.Entry(self, textvariable=self.valorEntrada)
		self.entradaRespuesta.grid(row=2, column=2, padx=5, pady=5)
		self.entradaRespuesta.config(bg="#222222", fg="#cccccc", justify="center", width=24)

		self.crearValores()

		self.porcentaje = tk.StringVar(self)

		self.intentos = tk.IntVar(self)
		self.intentos.set(0)

		self.correctas = tk.IntVar(self)
		self.correctas.set(0)
		
		self.botonEnter = tk.Button(self)
		self.botonEnter.grid(row=2, column=3, padx=(0, 30))
		self.botonEnter.config(text="PROBAR", width=6, background="#bbbbbb", command=lambda:self.acciones())

		self.labelPorc = tk.Label(self)
		self.labelPorc.grid(row=3, column=1)
		self.labelPorc.config(text="Porcentaje de aciertos: -", fg="#eeeeee", width=25, pady=10, background="#777777", anchor="w")

		self.labelCantInten = tk.Label(self)
		self.labelCantInten.grid(row=3, column=2)
		self.labelCantInten.config(text="Cantidad de intentos: -", fg="#eeeeee", width=25, background="#777777", anchor="w")


		self.quit = tk.Button(self, text="SALIR", fg="#990000", background="#bbbbbb", command=self.master.destroy)
		self.quit.grid(row=4, column=1, pady=(10,10))

		self.reiniciar = tk.Button(self, text="REINICIAR", fg="#990000", background="#bbbbbb", command=lambda:self.reiniciarValores())
		self.reiniciar.grid(row=4, column=2, pady=(10,10))


	def reiniciarValores(self):
		self.labelPorc["text"] = "Porcentaje de aciertos: -"
		self.labelCantInten["text"] = "Cantidad de intentos: -"
		self.porcentaje.set(0)
		self.correctas.set(0)
		self.intentos.set(0)
		self.botonEnter["bg"] = "#bbbbbb"
		self.crearValores()


	def crearValores(self):
		def crearTipoDeSalida():
			while True:
				base_a = choice(conversiones)
				base_b = choice(conversiones)
				if base_a != base_b:
					return base_a, base_b

		def crearSalida(base_a):
			if base_a == "2":return str(bin(randint(0,255)))[2:]
			elif base_a == "8":return str(oct(randint(0,255)))[2:]
			elif base_a == "16":return str(hex(randint(0,255)))[2:]
			else: return str(randint(0,255))

		def tipoDeSNP(base):
			if base == "2": return "binario"
			elif base == "8": return "octal"
			elif base == "16": return "hexadecimal"
			else: return "decimal"

		self.base_a, self.base_b = crearTipoDeSalida()
		self.valorSalida.set(crearSalida(self.base_a))
		self.label1["text"] = "Este valor está en {}".format(tipoDeSNP(self.base_a))
		self.label2["text"] = "Conviertelo a {}".format(tipoDeSNP(self.base_b))


	def chequearResultado(self):
		try:
			if str(int(self.valorEntrada.get(), int(self.base_b))) == str(int(self.valorSalida.get(), int(self.base_a))): return True
			else: return False
		except ValueError:
			print("Se han ingresado cifras fuera de las utilizadas en el sistema pedido.")
			return False
		

	def acciones(self):
		self.intentos.set(self.intentos.get()+1)
		if self.chequearResultado():
			self.correctas.set(self.correctas.get()+1)
			self.botonEnter["bg"] = "#007700"
		else: self.botonEnter["bg"] = "#990000"
		self.porcentaje.set(str(int((self.correctas.get()/self.intentos.get())*100)))
		self.labelPorc["text"] = "Porcentaje de aciertos: {}%".format(self.porcentaje.get())
		self.labelCantInten["text"] = "Cantidad de intentos: {}".format(self.intentos.get())
		self.entradaRespuesta.delete(0,"end")
		self.crearValores()



conversiones = ["2", "8", "10", "16"]

root = tk.Tk()
app = Application(master=root)
app.mainloop()