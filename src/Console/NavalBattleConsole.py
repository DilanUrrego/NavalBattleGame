import sys
sys.path.append("src")

from Program.NavalBattle import NavalBattle



if __name__ == "__main__":
    navalBattle = NavalBattle()
    print("Enter the size of the board you want to play on: ")
    print("(min:5, max:9)")

    w = int(input("Columns: "))
    h = int(input("Rows: "))
    navalBattle.generateBoard(w,h)
    
    
    if w == h:
        print(f"Máximo {w-1} barcos")
        num_ships = int(input("Ingrese el número de barcos: "))
        navalBattle.addShips(num_ships, w)
    
    elif w>h:
        print(f"Máximo {h-1} barcos")
        num_ships = int(input("Ingrese el número de barcos: "))
        navalBattle.addShips(num_ships, h)
    
    elif w<h:
        print(f"Máximo {w-1} barcos")
        num_ships = int(input("Ingrese el número de barcos: "))
        navalBattle.addShips(num_ships,w)
    
    print("Enter the coordinate you want to atack in the format: C2")
    print("Where 'C' is the column and '2' the row")
    navalBattle.showInfo()
    navalBattle.showPlayerBoard()
    while True:
        
        coordenada = input(f"Coordinate: ")
        if navalBattle.shoot(coordenada):
            navalBattle.downedShip()
    
        if navalBattle.ships_quantity==0:
            navalBattle.showPlayerBoard()
            print("YOU WON!!")
            break
        navalBattle.showPlayerBoard()

