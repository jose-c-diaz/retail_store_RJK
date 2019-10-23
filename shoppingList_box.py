def printTopBox(width: int):
    print(u'\u2554' + u'\u2550'* width + u'\u2557')

def printBottomBox(width: int):
    print(u'\u255a' + u'\u2550'* width + u'\u255d')

def printInBox(text: str, width: int):
    spaceToFill = width - len(text)
    print(u'\u2551' + text + " "*spaceToFill + u'\u2551')

def printShoppingCart():
    boxWidth = 100
    printTopBox(boxWidth)
    printInBox(f"---------- {len(shoppingArray)} Item/s in Your Shopping Cart ----------", boxWidth)
    totalPrice = 0
    for i in range(len(shoppingArray)):
        row = shoppingArray[i]
        printInBox(f"{i+1} - {row[3]}", boxWidth)
        printInBox(f"    {row[4]}", boxWidth)
        printInBox(f"    Price={row[5]}      X             Amount={row[6]}", boxWidth)
        totalPrice = totalPrice + (float(row[5]) * float(row[6]))
    printInBox("-----------------------------------------------------", boxWidth)
    printInBox(f"Your Total is: $ {totalPrice}", boxWidth)
    printBottomBox(boxWidth)
