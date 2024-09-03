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
narysuj_kwadrat(powolniak)
maruda.right(45)
narysuj_kwadrat(maruda)

turtle.mainloop()
