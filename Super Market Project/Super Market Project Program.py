print()
print(" ================== WELCOME TO SUPER MARKET FUTURE =============== ")
print()
customer_name = input("Please Enter your Name: ")
print()
dict_menu = {"RICE":10,"SUGAR":20,"SALT":30,"TISSUE":40,"PERFUME":50,"LEMONS":25,"TURMERIC":25}
price = 0
pricelist = []
print(" ============================ MENU =============================== ")
print()
print(" ================== List of Products Available  ================== ")
for keys, values in dict_menu.items():
    print(f'''
{keys:<15} : {values}''')
print()

while True:
    user_input = input('''
Please Make a selection: \nPRESS [1]. For Shopping: \nPRESS [2]. For Billing Section: \nPRESS[3]. To Exit''')
    if user_input == '1':
        while True:

            user_choice = input("Please Select your Item [or] Simply type 'DONE' when Finished: ").upper().strip()
            
            if user_choice in dict_menu:
                quantity = int(input("Enter quantity: "))
                total_price = quantity * dict_menu[user_choice]
                price += total_price 
                pricelist.append([user_choice, quantity, dict_menu[user_choice], total_price])

                print(f"{user_choice} ---> {quantity} = {quantity} x {dict_menu[user_choice]} = {total_price}")
            
            elif user_choice == 'DONE':
                print("Ok. Lets move to billing.")
                break
            
            else:
                print(f"{user_choice} is not available. Sorry, Try Again!")
    
    elif user_input == '2':
        if not pricelist:
            print("\nCart is empty. Please add items first.")
            continue
        else:
            print("\n====================== FINAL BILL ===============================")
            print(f"Customer   : {customer_name}")
            print("-----------------------------------------------------------------")
            print(f"{'S.No':<15}{'Item':<10}{'Qty':<15}{'Rate':<10}{'Total':<15}")
            print("-----------------------------------------------------------------")
    
        serial_no = 1
        for entry in pricelist:
            item, qty, rate, item_total = entry
            print(f"{serial_no:<15}{item:<10}{qty:<15}{rate:<10}{item_total:<15}")
            serial_no += 1

        print("-----------------------------------------------------------------")
        subtotal = price
        tax = subtotal * 0.10
        grand_total = subtotal + tax
        print(f"{'Subtotal':<50}: {subtotal:<50}")
        print(f"{'Tax (10%)':<50}: {tax:<50}")
        print(f"{'Grand Total':<50}: {grand_total:<50}")
        print("=================================================================\n")
        print()
        card = int(input("Please Enter your Last 4 digit Card Number: "))
        cvv = int(input("Enter your 3 Digit CVV: "))
        Expiry_date = int(input("Enter Expiry Year: "))
        print("Payment Approved!")
    
    
        print("Thank you, please visit us again.")
        break

    elif user_input == '3':
        print(f"Thankyou {customer_name} Please visit us again")
        break
    else:
        print(f"Opps it's an Invalid Option {customer_name}! Please Try again.")
            
