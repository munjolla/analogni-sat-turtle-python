import time
import turtle


prozor = turtle.Screen()
prozor.bgcolor("black")
prozor.setup(width=600, height=600)
prozor.title("jednostavan anologni sat")
prozor.tracer(0)

#kreiranje olovke za crtanje
olovka = turtle.Turtle()
olovka.hideturtle()
olovka.speed(0)
olovka.pensize(3)

def crtanje_sata(h,m,s,olovka):
    olovka.up()
    olovka.goto(0,210)
    olovka.setheading(180)
    olovka.color("red")
    olovka.pendown()
    olovka.circle(210)
    olovka.penup()
    olovka.goto(0,0)
    olovka.setheading(90)

    for i in range(12):
        olovka.fd(190)
        olovka.pendown()
        olovka.fd(20)
        olovka.penup()
        olovka.goto(0,0)
        olovka.rt(30)
#sati
    olovka.penup()
    olovka.goto(0,0)
    olovka.color("white")
    olovka.setheading(90)
    kut = (h / 12 * 360)
    olovka.rt(kut)
    olovka.pendown()
    olovka.fd(100)

#minute
    olovka.penup()
    olovka.goto(0, 0)
    olovka.color("red")
    olovka.setheading(90)
    kut = (m / 60 * 360)
    olovka.rt(kut)
    olovka.pendown()
    olovka.fd(300)
#sekunde
    olovka.penup()
    olovka.goto(0, 0)
    olovka.color("blue")
    olovka.setheading(90)
    kut = (s / 60 * 360)
    olovka.rt(kut)
    olovka.pendown()
    olovka.fd(244)

while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%s"))

    crtanje_sata(h,m,s,olovka)
    prozor.update()
    time.sleep(1)
    olovka.clear()


prozor.mainloop()
