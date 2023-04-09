import turtle


class L2DF:

    def __init__(self, t, f, color, length, angle):
        self.axiom = f
        self.state = f
        # self.line_color = color
        self.t = t
        self.t.pencolor(color)
        self.rules = {}
        self.length = length
        self.angle = angle

    def draw(self, start_x, start_y):
        turtle.tracer(1, 0)
        self.t.up()
        self.t.goto(start_x, start_y)
        self.t.down()
        for move in self.state:
            if move == "F":
                self.t.fd(self.length)
            elif move == "+":
                self.t.lt(self.angle)
            elif move == "-":
                self.t.rt(self.angle)


t = turtle.Turtle()
f = L2DF(t, "F+F--F+F--F+F--F+F--F+F--F+F", "#143535234", 120, 60)
f.draw(-100, 100)

f2 = L2DF(t, "F+S-FF+F+FF+FS+FF-S", "magenta", 200, 90 )
f2.draw(10, 50)
turtle.mainloop()
