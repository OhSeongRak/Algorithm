import turtle as t
t.shape("turtle")
t.speed(10)
t.right(10)
t.color("green")
t.pensize("6")
for i in range(2):
    for i in range(9):
        t.forward(15)
        t.left(10)
    t.left(90)
t.left(120)
for i in range(2):
    for i in range(9):
        t.forward(15)
        t.left(10)
    t.left(90)
t.right(20)
t.forward(160)
t.color("purple")
t.pensize("4")
for i in range(7):
    for i in range(2):
        for i in range(9):
            t.forward(15)
            t.left(10)
        t.left(90)
    t.left(50)