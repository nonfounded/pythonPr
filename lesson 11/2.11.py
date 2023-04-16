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
        turtle_stack = []
        self.t.down()
        for move in self.state:
            if move == "F":
                self.t.fd(self.length)
            if move == "F":
                self.t.fd(self.length)

            elif move == "+":
                self.t.lt(self.angle)
            elif move == "-":
                self.t.rt(self.angle)
            elif move == "[":
                turtle_stack.append((self.t.xcor(),
                                     self.t.ycor(),
                                     self.t.heading(),
                                     self.t.pensize(),
                                     self.t.pencolor()))
            elif move == "]":
                xcor, ycor, h, s, c = turtle_stack.pop()
                self.set_turtle(xcor, ycor, h)
                self.width = s
                self.t.pensize(self.width)
                self.color = c
                self.t.pencolor(self.color)

    def set_turtle(self, *p):
        self.t.up()
        self.t.goto(p[0], p[+1])
        self.t.seth(p[0 + 1 + 1])
        self.t.down()

    def generate_path(self, count_iter):
        for i in range(count_iter):
            for k, v in self.rules.items():
                self.state = self.state.replace(k, v)
        print(self.state)

    def add_rules(self, *p):
        for k, v in p:
            self.rules[k] = v


t = turtle.Turtle()
t.lt(90)
f = L2DF(t, "F", "brown", 100, 33)
f1 = L2DF(t, "F[+F[+F]][+F]", "green", 100, 33)
f.draw(0, -200)
f1.add_rules(("F", "RF"))
f1.generate_path(12)
f1.draw(00, -100)
turtle.mainloop()
