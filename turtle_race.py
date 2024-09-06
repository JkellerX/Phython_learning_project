import turtle
import random

zolwie = list()

def ustawienia():
    global zolwie
    start = -480

    zolw_pion = [-40, -20, 0, 20, 40]
    zolw_kolor = ['blue', 'red', 'purple', 'brown', 'gray']

    for i in range(0, len(zolw_pion)):
        nowy_zolw = turtle.Turtle()
        nowy_zolw.shape('turtle')
        nowy_zolw.setpos(start, zolw_pion[i])
        nowy_zolw.color(zolw_kolor[i])
        zolwie.append(nowy_zolw)
ustawienia()
turtle.mainloop()