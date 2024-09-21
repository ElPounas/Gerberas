import turtle

# Configuración inicial
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)

# Función para dibujar un pétalo
def draw_petal():
    pen.color("yellow")
    pen.begin_fill()
    pen.circle(35, 60)  
    pen.left(120)
    pen.circle(35, 60)
    pen.end_fill()

# Función para dibujar una gerbera
def draw_gerbera(x, y, num_petals):
    # Dibujar el tallo
    pen.penup()
    pen.goto(x, y - 10)  
    pen.pendown()
    pen.color("green")
    pen.pensize(3)
    pen.right(90)
    pen.forward(90)  
    pen.left(90)
    pen.pensize(1)
    
    # Dibujar los pétalos
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    for _ in range(num_petals):
        draw_petal()
        pen.left(360 / num_petals)
    
    # Dibujar el centro
    pen.penup()
    pen.goto(x, y - 10) 
    pen.pendown()
    pen.color("orange")
    pen.begin_fill()
    pen.circle(10)  
    pen.end_fill()

# Función para dibujar una maceta con mensaje
def draw_pot_with_message():
    pen.penup()
    pen.goto(-250, -100)
    pen.pendown()
    pen.color("brown")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(500)
        pen.right(90)
        pen.forward(100)
        pen.right(90)
    pen.end_fill()
    
    # Agregar el mensaje
    pen.penup()
    pen.goto(-200, -150)
    pen.color("black")
    pen.write("Gerberas amarillas les desea ...)", font=("Arial", 12, "normal"))

# Dibujar la maceta con mensaje
draw_pot_with_message()

# Dibujar seis gerberas más pequeñas en la maceta con tallos
draw_gerbera(-220, 0, 18)  # Primera gerbera con 18 pétalos
draw_gerbera(-132, 0, 18)  # Segunda gerbera con 18 pétalos
draw_gerbera(-44, 0, 18)     # Tercera gerbera con 18 pétalos
draw_gerbera(44, 0, 18)   # Cuarta gerbera con 18 pétalos
draw_gerbera(132, 0, 18)   # Quinta gerbera con 18 pétalos
draw_gerbera(220, 0, 18)   # Sexta gerbera con 18 pétalos

# Finalizar
pen.hideturtle()
turtle.done()
