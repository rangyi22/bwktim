import turtle as t

n = int(input())
t.shape('turtle')
for i in range(n):
    t.forward(100)
    t.right(360/n)
t.mainloop()
