#tac = input("Enter cells: ")
tac = "_________"
def print_out(tac):
    print("-"*9)
    print("| "+arr[0]+" "+arr[1]+" "+arr[2]+" |")
    print("| "+arr[3]+" "+arr[4]+" "+arr[5]+" |")
    print("| "+arr[6]+" "+arr[7]+" "+arr[8]+" |")
    print("-"*9)
def result(tac):
    arr = list(tac)
    x_count = 0
    o_count = 0
    nocount = 0
    count = 0
    R1X = R2X = R3X = C1X = C2X = C3X = D1X = D2X = 0
    R1O = R2O = R3O = C1O = C2O = C3O = D1O = D2O = 0
    for i in arr:
        if i == "X":
            x_count += 1
        elif i == "O":
            o_count += 1
        else:
            nocount += 1
    if abs(x_count - o_count) > 1:
        #print("Impossible")
        return("Impossible")
    else:
        if (arr[0] == arr[1] == arr[2] == "X"):
            R1X = 1
        elif (arr[3] == arr[4] == arr[5] == "X"):
            R2X = 1
        elif (arr[6] == arr[7] == arr[8] == "X"):
            R3X = 1
        elif (arr[0] == arr[3] == arr[6] == "X"):
            C1X = 1
        elif (arr[1] == arr[4] == arr[7] == "X"):
            C2X = 1
        elif (arr[2] == arr[5] == arr[8] == "X"):
            C3X = 1
        elif (arr[0] == arr[4] == arr[8] == "X"):
            D1X = 1
        elif (arr[2] == arr[4] == arr[6] == "X"):
            D2X = 1
        if (arr[0] == arr[1] == arr[2] == "O"):
            R1O = 1
        elif (arr[3] == arr[4] == arr[5] == "O"):
            R2O = 1
        elif (arr[6] == arr[7] == arr[8] == "O"):
            R3O = 1
        elif (arr[0] == arr[3] == arr[6] == "O"):
            C1O = 1
        elif (arr[1] == arr[4] == arr[7] == "O"):
            C2O = 1
        elif (arr[2] == arr[5] == arr[8] == "O"):
            C3O = 1
        elif (arr[0] == arr[4] == arr[8] == "O"):
            D1O = 1
        elif (arr[2] == arr[4] == arr[6] == "O"):
            D2O = 1
        if ((R1X + R2X + R3X + C1X + C2X + C3X + D1X + D2X) > 0 and
            (R1O + R2O + R3O + C1O + C2O + C3O + D1O + D2O) > 0):
            #print("Impossible")
            return("Impossible")
        elif ((R1X + R2X + R3X + C1X + C2X + C3X + D1X + D2X) == 0 and
              (R1O + R2O + R3O + C1O + C2O + C3O + D1O + D2O) == 0 and nocount > 0):
            #print("Game not finished")
            return("Game not finished")
        elif ((R1X + R2X + R3X + C1X + C2X + C3X + D1X + D2X) == 0 and
              (R1O + R2O + R3O + C1O + C2O + C3O + D1O + D2O) == 0 and nocount == 0):
            #print("Draw")
            return("Draw")
        elif R1X + R2X + R3X + C1X + C2X + C3X + D1X + D2X > 0:
            #print("X wins")
            return("X wins")
        elif R1O + R2O + R3O + C1O + C2O + C3O + D1O + D2O > 0:
            #print("O wins")
            return("O wins")

def is_full(x, y, tac):
    cell_return = '_'
    if (x,y) == (1,1):
        cell_return = tac[6]
    elif (x,y) == (1,2):
        cell_return = tac[3]    
    elif (x,y) == (1,3):
        cell_return = tac[0]
    elif (x,y) == (2,1):
        cell_return = tac[7]
    elif (x,y) == (2,2):
        cell_return = tac[4]
    elif (x,y) == (2,3):
        cell_return = tac[1]
    elif (x,y) == (3,1):
        cell_return = tac[8]
    elif (x,y) == (3,2):
        cell_return = tac[5]
    elif (x,y) == (3,3):
        cell_return = tac[2]
    return cell_return

def cell_value(x, y):
    if (x,y) == (1,1):
        return 6
    elif (x,y) == (1,2):
        return 3   
    elif (x,y) == (1,3):
        return 0
    elif (x,y) == (2,1):
        return 7
    elif (x,y) == (2,2):
        return 4
    elif (x,y) == (2,3):
        return 1
    elif (x,y) == (3,1):
        return 8
    elif (x,y) == (3,2):
        return 5
    elif (x,y) == (3,3):
        return 2
    return tac

def swapping(var):
    if var == "X":
        return("O")
    else:
        return("X")
    
arr = list(tac)
print_out(arr)
z = 0
r = ""
swap = "O"
while z < 1:
    coord = input("Enter the coordinates: ")
    if " " in coord:
        x, y = coord.split()
    else:
        x = coord
        y = ""
    if not(x.isdigit()) or not(y.isdigit()):
        print("You should enter numbers!")
    elif int(x) > 3 or int(y) > 3:
        print("Coordinates should be from 1 to 3!")
    elif is_full(int(x), int(y), arr) in ('X', 'O'):
        print("This cell is occupied! Choose another one!")
    else:
        x = int(x)
        y = int(y)    
        i = cell_value(x, y)
        swap = swapping(swap)
        arr[i] = swap
        print_out(arr)
        r = result(arr)
        if r in ("Draw", "X wins", "O wins"):
            print(r)
            z = 1
