## Initial starting list
stocks = ["Apple", "Google", "Tesla", "Microsoft"]

print("These are current stocks in the portfolio:", stocks)

## User prompting for adding or removing
action = input("Would you like to add or remove stocks? (Add/Remove/Neither)")

## Actual adding and removing function
def add_stock():
    stocks.append(input("What stock would you like to add"))
    print("This is the new portfolio", stocks)
    if input("Would you like to add more?") == "Yes":
        add_stock()
    else:
        print("Have a nice day!")
def remove_stock():
    stocks.remove(input("What stock would you like to remove?"))
    print("This is the new portfolio", stocks)
    if input("Would you like to remove more?") == "Yes":
        remove_stock()
    else: 
        print("Have a nice day!")

if action == "Add":
    add_stock()
elif action == "Remove":
    remove_stock()
else:
    print("Have a nice day!")





    






