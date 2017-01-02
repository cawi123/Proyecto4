import time 
from tkinter import *
tk = Tk()
#Creamos la ventana 
canvas = Canvas(tk, width=400 ,height=200)
canvas.pack()
#El archivo de la imagen 
image=PhotoImage(file="bola.gif")
#Creamos la imagen en la ventana 
canvas.create_image(0,0,anchor=NW,image=image)

def mover(move):
    if move.keysym == 'W':
        canvas.move(1, 0, -5)
        time.sleep(0.05)
    elif move.keysym == 'S':
        canvas.move(1, 0, 5)
        time.sleep(0.05)
    elif move.keysym == 'A':
        canvas.move(1, -5, 0)
        time.sleep(0.05)
    elif move.keysym == 'D':
        canvas.move(1, 5, 0)
        time.sleep(0.05)
canvas.bind_all('<KeyPress-W>', mover)
canvas.bind_all('<KeyPress-S>', mover)
canvas.bind_all('<KeyPress-A>', mover)
canvas.bind_all('<KeyPress-D>', mover)
tk.mainloop()
