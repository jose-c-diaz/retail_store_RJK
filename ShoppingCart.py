import numpy
shoppingArray = list()
ordersArray = list()


def addProductToShppingCart(row, amount):
    a = len(shoppingArray)

    ordersArray = row
    ordersArray = ordersArray + (amount, )
    shoppingArray.insert(a+1, ordersArray)


def printShoppingCart():
    print(
        f"---------- {len(shoppingArray)} Item/s in Your Shopping Cart ----------")
    totalPrice = 0
    for i in range(len(shoppingArray)):
        row = shoppingArray[i]
        print(f"\n{i+1} - {row[3]}")
        print(f"    {row[4]}")
        print(f"    Price={row[5]}      X             Amount={row[6]}")
        totalPrice = totalPrice + (float(row[5]) * float(row[6]))
    print("-----------------------------------------------------")
    print(f"Your Total is: $ {totalPrice}")
