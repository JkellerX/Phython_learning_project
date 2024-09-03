import turtle
powolniak = turtle.Turtle()
powolniak.shape('turtle')
powolniak.color('pink')
maruda = turtle.Turtle()
maruda.shape('turtle')
maruda.color('blue')

def narysuj_kwadrat(zolw):
    for i in range(0, 4):
        zolw.forward(100)
        zolw.right(90)

def narusuj_spirale(zolw):
    for i in range(0, 36):
        narysuj_kwadrat(zolw)
        zolw.right(10)

narusuj_spirale(powolniak)
maruda.right(5)
narysuj_kwadrat(maruda)

turtle.mainloop()
