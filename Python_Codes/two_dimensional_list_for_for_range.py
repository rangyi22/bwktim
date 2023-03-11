a = [[10, 20], [30, 40], [50, 60]]

for i in range(len(a)):        # Size of Row
    for j in range(len(a[i])): # Size of Column
        print(a[i][j], end=' ')
    print()
