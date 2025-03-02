from payment_method import coins
from Coffee_Items import Menu

Machine_Ingredients={
    'water':500,
    'milk':1000,
    'coffee':500,
    'Money':0.0
}
def Check_Ingredients(coffee_type):
    if(Machine_Ingredients["water"]>Menu[coffee_type]["Ingredients"]["water"]):
        print("ingridents are suffcient to make a coffee")
        return True
    else:
        return False
def Get_Price(Coffee_type):
    return Machine_Ingredients["water"]>Menu[Coffee_type]["cost"]
def Get_Coins(coffee_cost):
    print(f" Plesae insert coins ")
    quarter = int(input("How many quarter:"))
    if ( quarter > 0):
        dimmes = int( input("How many Dimmes:"))
        if ( dimmes > 0):
            nickles =int( input("How many nickles"))
            if (nickles > 0):
                pennies = int(input("How many pennies"))
                if (pennies > 0):
                  return  calculate_amount(quarter,dimmes,nickles,pennies,coffee_cost)

    else:
        print("Please Insert correct amount")
        Get_Coins(coffee_cost)


def calculate_amount(quarter, dimmes,nickles,pennies,coffee_cost):
    total_amount_inserted= (coins["Quarter"] * quarter)+ (coins["Dimmes"]*dimmes)+ (coins["Nickles"]*nickles)+ (coins["Pennies"]*pennies)
    return calculate_change(total_amount_inserted, coffee_cost)
def calculate_change(inserted, cost):

    if(inserted-cost>0):
        print(f"here is your change: $ {round((inserted-cost),2)}")
        Add_Profit(round((inserted-cost),2))
        return True
    else:
        print("Insufficient coins inserted")
        return False
def Add_Profit(profit):
    Machine_Ingredients["Money"] += profit
def Make_Coffee(coffee_type):
    Machine_Ingredients["water"] -=Menu[coffee_type]["Ingredients"]["water"]
    Machine_Ingredients["coffee"] -= Menu[coffee_type]["Ingredients"]["coffee"]
    if(coffee_type!="espresso"):
        Machine_Ingredients["milk"] -= Menu[coffee_type]["Ingredients"]["milk"]
    return True

def print_report():
    print(f"""here are remaining item
    Water: {Machine_Ingredients["water"]} ml
    Milk: {Machine_Ingredients["milk"]} ml
    Coffee: {Machine_Ingredients["coffee"]} g
    Money: $ {Machine_Ingredients["Money"]}  """)
print("Welcome to Cofee machine ☕")
Coffee_price=0
Is_off=False

while(Is_off==False):
    take_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if (take_order == "off"):
        print("off")
        Is_off=True
        # turn of the machine from here
    elif (take_order == "report"):
       print_report()
        # print a report here and show amount of materials in machine
    elif (take_order == "espresso" or take_order == "lattee" or take_order == "cappuccino"):
        isSufficient = Check_Ingredients(take_order)
        if (isSufficient):
            Coffee_price = Get_Price(take_order)
            IsAmount_deducted = Get_Coins(Coffee_price)
            if (IsAmount_deducted):
                if ( Make_Coffee(take_order)):
                    print(f"Here is your {take_order}. Enjoy!")

        else:
            print("Machine has not enough ingridients come back later")





    #customer want espresson here we check if there are enough material or not
    #then we take amount from customer


