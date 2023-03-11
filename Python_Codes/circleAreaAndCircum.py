import math
def areaAndCircum(r):
    area = math.pi * r ** 2
    circum = 2 * math.pi * r
    res = area, circum
    return res

radius = 4
area, circum = areaAndCircum(radius)
#print('Radius', radius, 'and the area and circumference of a circle is :', areaAndCircum(radius))
print('Radius', radius, 'and the area and circumference of a circle is :', area, circum)