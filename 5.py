x= int(input("Enter any Number:"))

match x:
    case 0:
        print("x is zero")
    case 1:
        print('x is one')
    case 2:
        print('x is two')
    case 3:
        print('x is three')
    case 4:
        print('x is four')
    case 5:
        print('x is five')
    case 6:
        print('x is six')
    case _ if x > 6 and x < 15:
        print('x is bigger than 6')
    case _:
        print("invalid number")
    