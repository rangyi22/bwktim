import turtle as t

t.shape("turtle")
t.bgcolor("black")
t.color("green")
t.speed(0)  # draw a picture with the max speed

n = 20
for _ in range(n+1):
    t.circle(80)
    t.left(360.0/n)

t.done()