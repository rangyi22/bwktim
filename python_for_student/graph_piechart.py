#graph_piechart.py
import matplotlib.pyplot as plt

pets = ['Dog','Cat','Rodent','Reptile','Fish']
numbers = [1110, 987, 312, 97, 398] # Population 
cols = ['c','m','r','y','g']
plt.pie(numbers, labels=pets, colors=cols, startangle=90,
        explode=(0,0,0.1,0.05,0),  autopct='%1.1f%%')
plt.show()
