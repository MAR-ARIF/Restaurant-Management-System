from datetime import datetime
import hashlib
import os
import getpass
import json
try:
    with open("menu.json","r") as f:
        menu=json.load(f)
except FileNotFoundError:
    menu={}
try:
    with open("coupon_code.json","r") as f:
        coupon_code=json.load(f)
except FileNotFoundError:
    coupon_code={}
menu={
    "starters":{
        "Garlic Bread": 3.49,
    "Chicken Wings": 5.99,
    "Mozzarella Sticks": 4.99,
    },
    "mains":{
            "Cheeseburger": 6.99,
    "Veggie Burger": 6.49,
    "Margherita Pizza": 8.49,
    "Pepperoni Pizza": 9.49,
    "Grilled Chicken": 10.99,
    "Spaghetti Bolognese": 9.99,
    "Paneer Tikka": 8.99,
    },
    "sides":{
            "French Fries": 2.99,
    "Onion Rings": 3.49,
    "Coleslaw": 2.49,
    "Side Salad": 3.99,

    },
    "drinks":{
            "Coke": 1.99,
    "Lemonade": 2.49,
    "Iced Tea": 2.99,
    "Coffee": 2.49,
    "Water": 0.99,
    },
    "desserts":{
            "Chocolate Cake": 4.99,
    "Ice Cream Sundae": 3.99,
    "Brownie": 3.49,
    "Fruit Salad": 3.99

    }
    }

choice_map={
        "s":"starters",
        "m":"mains",
        "sd":"sides",
        "dr":"drinks",
        "ds":"desserts"
    }

coupon_code={
    'foodie25':0.25,
    'under18':0.18,
    'save10':0.10
}

tax=0.1 #10% tax

def restaurant_order_system():
    #showing menu and taking order
    global menu,coupon_code
    all_order=[]
    total_price=0
    discount=0
    service_charge=0

    while True:
            menu_choice = input("\nPlease enter s to view starters,m to view mains,sd to view sides,dr to view drinks and ds to view desserts: ").strip().lower()
            category = choice_map.get(menu_choice)
            if category and category in menu:
                print(f"\n        ***{category.capitalize()} menu****      ")
                for i, (item, price) in enumerate(menu[category].items()):
                    print(f"--{i}.{item:<20}| price: £{price}")

                # taking order
                order_num = input("\nWhat would you like to order? Enter the number code of the order: ")
                while True:
                    if order_num.isdigit():
                        order_num = int(order_num)
                        for i, (item, price) in enumerate(menu[category].items()):
                            if order_num == i:
                                all_order.append((item,price))
                                total_price+=float(price)
                                for orders, price in all_order:
                                    print(f"you ordered {orders}")
                                break
                        else:
                            print("Invalid number code. Enter a valid number code.")
                            order_num = input("\nTry again. Enter the number code of the order: ")
                            continue
                        break
                    else:
                        print("Please enter a number.")
                        order_num = input("\nTry again. Enter the number code of the order: ")
                        continue
                
                reorder = input("\nDo you want to order anything else? y/n: ").lower()
                if reorder == 'y':
                    continue
                else:
                    break
            
            else:
                print("Invalid input. Please select a dish from the menu.")
                continue

    #discount
    while True:
        coupon_elig=input("\nDo you have any coupon code?(y/n): ").lower()
        if coupon_elig=='n':
            break
        elif coupon_elig=='y':
            code=input("Enter your coupon code for discount: ").lower()
            if code in coupon_code:
                discount+=float(coupon_code[code])
                print(f"You get {discount*100}% discount")
                break
                
            else:
                print("Wrong code.Try again.")
                continue
            
            
        else:
            print("Wrong input.Try again.")
            continue
        
    #service charge
    while True:
        scharge=input("\nDo you want to give any service charge?(y/n): ").lower()
        if scharge=='n':
            break
        elif scharge=='y':
            scharge_pr=input("How much percentage service charge you want to give?(10/15/20/or any random): ")
            service_charge+=float(float(scharge_pr)/100)
            break
        else:
            print("Wrong input.Try again")



    #now showing total order with price and taking payment
    input("\nPress enter to view your orders and total price.\n")
    print("----Order Summary----".center(60))
    for i,(item,price) in enumerate(all_order,1):
        print(f"{i}.{item:<20}|Price: £{price}".center(60))

    print(("-"*45).center(60))
    indent = " " * 15  # 20 spaces to shift everything right

    print(indent + f"{'Total':<20}- £{total_price:.2f}")
    print(indent + f"{'Tax':<20}- £{total_price*tax:.2f}(10%)")
    print(indent + f"{'Discount':<20}- £{discount*total_price:.2f}({discount*100}%)")
    print(indent + f"{'Service charge':<20}- £{service_charge*total_price:.2f}({service_charge*100}%)")
    print((f"-"*55).center(60))
    net_total=total_price+total_price*tax+service_charge*total_price-discount*total_price
    print(indent + f"{'NET TOTAL':<20}- {net_total:.2f}")

    while True:
        pay=input("\n Press C to pay: ").lower()
        if pay =='c':
            print("\n Payment successful. Thank you!")
            break
        else:
            print("Wrong input.Try again.")
            continue

    input("\nPress enter to view your recipt.")
    print("----Order Summary----".center(60))
    for i,(item,price) in enumerate(all_order,1):
        print(f"{i}.{item:<20}|Price: £{price}".center(60))

    print(("-"*45).center(60))
    indent = " " * 15  # 20 spaces to shift everything right

    print(indent + f"{'Total':<20}- £{total_price:.2f}")
    print(indent + f"{'Tax':<20}- £{total_price*tax:.2f}(10%)")
    print(indent + f"{'Discount':<20}- £{discount*total_price:.2f}({discount*100}%)")
    print(indent + f"{'Service charge':<20}- £{service_charge*total_price:.2f}({service_charge*100}%)")
    print((f"-"*55).center(60))
    net_total=total_price+total_price*tax+service_charge*total_price-discount*total_price
    print(indent + f"{'NET TOTAL':<20}- {net_total:.2f}")
    print(("✅PAID").center(60))
    print(f"Date: {datetime.now().strftime('%d/%m/%Y, time-%H:%M:%S')}".center(60))

#hashing function
def hashing_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
#function to save hashed password
def save_hpass(hvalue):
    with open("admin.txt","w") as f:
        f.write(hvalue)

#function to load saved password
def load_password():
    if os.path.exists('admin.txt'):
        with open("admin.txt","r") as f:
            return f.read().strip()
    else:
        return None
def admin_login():
    saved_pd=load_password()
    if saved_pd is None:
        print("No password set yet.Please create one.")
        pwd=input("Set your admin password: ")
        save_hpass(hashing_password(pwd)) # hashing_password(pwd) creates pass with hash in first function and the save it in 2nd one
        print("Password set successfully! You are now logged in.")
        return True
    else:
        entered=getpass.getpass("Enter password to log in as Admin: ")
        if hashing_password(entered)==saved_pd:
            print("✅ Access granted.")
            return True
        else:
            print("❌ Access denied.")
            return False
        
def change_password():
    saved_pwd=load_password()
    entered=getpass.getpass("Enter old password: ")
    if hashing_password(entered)==saved_pwd:
        new_pd=getpass.getpass("Enter new password: ")
        save_hpass(hashing_password(new_pd))
        print("New Password set successfully.")
    else:
        print("Incorrect password.")

def admin_interface():
    global menu,coupon_code, tax
    print("\nWelcome to McGILL RESTAURENT admin panel.\n")
    while True:
        option=input("Please choose an option(1-7): 1. view menu\n" \
        "                              2. Add item in menu\n" \
        "                              3. Update item's price\n" \
        "                              4. Update Tax rate\n" \
        "                              5. Coupon code setting\n" \
        "                              6. Change Password\n" \
        "                              7.Exit\n")
        if option=="1":
            for category,details in menu.items():
                print("\n" + category.upper().center(60) + "\n")
                for dish,price in details.items():
                    print((f"{dish}|£{price}").center(60))
            input("\nPress enter to go back to main menu")
        elif option=="2":
            add_item=input("Enter the item name you want to add in menu: ")
            item_price=input("Enter the price of this item: ")
            while True:
                 item_category=input("Enter the category name you want to add this item in(starters/mains/sides/desserts/drinks): ")
                 if item_category not in menu:
                     print("Category doesn't exist in your menu. Try again.")
                     continue
                 else:
                     menu[item_category][add_item]=float(item_price)
                     print("\nItem added successfully in your menu.")
                     break
            with open("menu.json","w") as f:
                json.dump(menu,f)
            input("\nPress enter to go back to main menu.")

        elif option=="3":
                itemP=input("Enter the item's name you want to update price: ").lower()
                found= False
                for category,item in menu.items():
                    for dish in item:
                        if itemP == dish.lower():
                            price=input(f"Enter the updated price of {dish}: £")
                            try:
                                price=float(price)
                                if price>=0:
                                    print("Price updated successfully!!!")
                                    menu[category][dish]=price
                            except ValueError:
                                print("Price must be non-negative.")
                            found= True
                            break
                    if found:
                        break
                if not found:
                    print("Dish not found in menu")
                with open("menu.json","w") as f:
                    json.dump(menu,f)
                input("\nPress enter to go back to main menu.")
                            
       
        elif option=="4":
            updated_Tax=input("Enter the updated tax rate: ")
            if updated_Tax.isdigit() and int(updated_Tax)>0:
                tax=float(updated_Tax)/100
                print("Tax rate updated successfully!!!")
            else:
                print("Invalid tax rate.")
            input("\nPress enter to go back to main menu.")
        
        elif option=="5":
            opt=input("Choose an option: 1. View Coupon codes.\n2.Add coupon\n3.Remove coupon.")
            if opt=="1":
                print("\n")
                print(("----Coupon Code----").center(60))
                print("\n")
                for codes,prt in coupon_code.items():
                    print((f"-{codes}|percentage-{prt*100}\n").center(60))
            elif opt=="2":
                add_c=input("Enter the coupon code you want to add: ")
                prct=input("Enter the discount percentage for this coupon code: ")
                if prct.isdigit and int(prct)>=0:
                    coupon_code[add_c]=float(prct)/100
                    print("Coupon code added successfully")
                   
                else:
                    print("Invalid percentage.")
            
            elif opt=="3":
                rm_c=input("Enter the coupon code you want to remove: ")
                if rm_c in coupon_code:
                    del coupon_code[rm_c]
                    print("Coupon code removed successfully!!!")
                else:
                    print("Coupon code not found.")
                input("\nPress enter to go back to main menu.")
            else:
                print("Invalid choice.")
            with open("coupon_code.json","w") as f:
                        json.dump(coupon_code,f)
           
            input("\nPress enter to go back to main menu.")
        elif option=="6":
            change_password()
            input("\nPress enter to go back to main menu.")
        
        elif option=="7":
            print("Exiting admin interface....")
            print("\nBYE!!!")
            break
        else:
            print("Wrong choice. Try again.")
            continue                



                 
#main 
print("\n")
print(("----WELCOME TO McGILL RESTAURENT----\n").center(100))

while True:
    print("\n")
    option=input("Choose an option: 1. Customer interface.\n" \
"                  2. Admin login.\n"
"                  3.Exit\n")
    if option=="1":
            
            restaurant_order_system()
            input("\nPress enter to go back to main menu.")

    elif option=="2":
            if admin_login():
                admin_interface()
            
    
            
            input("\nPress enter to go back to main menu.")
    elif option=="3":
        print("Exiting program.BYE!!!")
        break
    else:
         print("Wrong input.Try again!")
   
    


 






    

