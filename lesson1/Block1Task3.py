shipsCount = int (input())
if shipsCount % 20 <= 19 and shipsCount % 20 >= 5 or shipsCount % 20 == 0:
    print("Кораблей")
elif shipsCount % 10 == 1:
    print("Корабль")
else: print("Корабля")