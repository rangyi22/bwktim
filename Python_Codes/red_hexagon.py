import turtle as t

n = 6 # Hexagon
t.shape('turtle')
t.color('#FF69B4') # Hot Pink
#t.color('red')
t.begin_fill()
for i in range(n):
    t.forward(100)
    t.right(360/n)
t.end_fill()
t.mainloop()