import turtle
t=turtle.Pen()


n=int(input("ingrese un numero de lados "))
a=n/2
b=180/a
c=180-b
#saer si n es par o inpar 
if(n%2==0):
    #numero par de n lados 
    for x in range(n):
#va a delante hasta cuantas veces debe girar a la derecha
        t.forward(108)
        t.left(c)
        t.left(c)
        t.left(c)
else:
    for x in range(n):
#va a delante hasta cuantas veces debe girar a la derecha
        t.forward(108)
        t.left((n-2)*180/n)
        t.left((n-2)*180/n)

   
turtle.getscreen()._root.mainloop()


#365 divido para el numero de lados
