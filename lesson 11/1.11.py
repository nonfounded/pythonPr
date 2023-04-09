import turtle

def snejinka_koha(t, line):
    if line > 6:
        snejinka_koha(t,line//3)
        t.lt(60)
        snejinka_koha(t, line//3)
        t.rt(120)
        snejinka_koha(t, line//3)
        t.lt(60)
    else:
        t.fd(line)
        t.lt(60)
        t.fd(line)
        






        t.lt(60)
        t.fd(line)







t = turtle.Turtle()
t.shape("turtle")
t.speed(100)
t.up()
t.goto(-500, 0)
t.down
snejinka_koha(t, 100)
t.rt(120)
snejinka_koha(t, 100)
t.rt(120)
snejinka_koha(t, 100)
turtle.mainloop()
