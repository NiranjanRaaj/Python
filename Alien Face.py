import turtle

cursor = turtle.Turtle()
cursor.speed(1)
cursor.pensize(3)
cursor.color("black", "green")

def h_curve():
    cursor.begin_fill()
    cursor.left(140)
    #cursor.stamp()
    cursor.forward(75)
    #cursor.stamp()
    for i in range(280):
        cursor.right(1)
        cursor.forward(2)
    cursor.forward(75)
    #cursor.stamp()
    for i in range (41):
        cursor.right(2.3)
        cursor.forward(1)
    cursor.end_fill()
    cursor.hideturtle()

def dr_e():
    em = turtle.Turtle()
    em.color("black", "gray")
    em2 = turtle.Turtle()
    em2.color("black", "gray")
    em.penup()
    em2.penup()
    em.goto(-6, 120)
    em2.goto(40, 120)
    em.begin_fill()
    em2.begin_fill()
    em.left(120)
    em2.left(60)
    em.pendown()
    em2.pendown()
    em.forward(30)
    em2.forward(30)
    for j in range (100):
        em.left(2.3)
        em2.right(2.3)
        em.forward(1)
        em2.forward(1)
    em.forward(30)
    em2.forward(30)
    for k in range (27):
        em.left(5.2)
        em2.right(5.2)
        em.forward(1)
        em2.forward(1)
    em.end_fill()
    em2.end_fill()
    em.hideturtle()
    em2.hideturtle()

def mou():
    em3 = turtle.Turtle()
    em3.pensize(2.5)
    em3. penup()
    em3.goto(-6,50)
    em3.right(20)
    em3.pendown()
    for k in range(60):
        em3.left(0.8)
        em3.forward(1)
    em3.hideturtle()

h_curve()
dr_e()
#right_e()
mou()

turtle.mainloop()
