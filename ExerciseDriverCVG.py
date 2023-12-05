from ClassModuleCVG import Price

def select_itemsCVG():
    product_list = []
    item = int(input("How many items will you order today? "))
    
    # Validation for item
    while not item > 0:
        print("Number of items must be at least 1.")
        item = int(input("How many items will you order today? "))
    
    # Loops according to number of item
    for num in range(item):
        print(f'Item #{num + 1}-')
        input_food = input("Enter food: ")
        input_amt = float(input("Enter amount of pounds: "))
        
        # Validation for input amount
        while not input_amt > 0:
            print("Amount of pounds must be greater than 0")
            input_amt = float(input("Enter amount of pounds: "))
        
        # Create and append object into list
        item = [input_food, input_amt]
        product_list.append(item)
    
    return product_list

def show_listCVG(product_list):
    print("Here's a summary of the items purchased:")
    print("----------------------------------------")
    # Putting the Price into a new variable and displaying
    for item in product_list:
        price_item = Price(name = item[0], amt = item[1])
        # Printing everything according to list
        print(f"Food Name: {price_item.get_food_nameCVG()}")
        print(f"Amount: {price_item.get_food_amtCVG()}")
        print(f"Standard Price: ${price_item.get_standard_priceCVG():,.2f}")
        print(f"Calculated Price: ${price_item.calculate_costCVG():,.2f} \n")

def calculated_final_costCVG(product_list):
    total = 0.00
    for item in product_list:
        each_price = Price(name = item[0], amt = item[1]).calculate_costCVG()
        total += each_price
    return total

def mainCVG():
    items_list = select_itemsCVG()
    show_listCVG(items_list)
    total_cost = calculated_final_costCVG(items_list)
    print(f"Total Cost of all items: ${total_cost:,.2f}")

if __name__ == "__main__":
    mainCVG()