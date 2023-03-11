while True:
    print("[Enter the menu.]")
    select = int(input("1. Game Begins 2. See the Ranking 3. Game Over >>> "))
    
    if select == 1:
        print("-> Game begins")
    elif select == 2:
        print("-> See the Ranking")
    elif select == 3:
        print("-> Game Over")
        break
    else:
        print("Enter the number again!")