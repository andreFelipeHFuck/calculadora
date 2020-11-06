from tkinter import *
"""
calc: calculadora
"""
calc = Tk()
calc.title("Calculadora")
calc.geometry("500x500")

button = Button(calc, text='1', font="20", bg= "#999999", width= 5, height= 5, padx = 25).pack()

calc.mainloop()