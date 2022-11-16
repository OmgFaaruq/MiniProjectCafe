product_list = []

couriers_list = []

orders_list = []

order_status_list = ['PREPARED', 'OUT FOR DELIVERY', 'DELIVERED']


# load product list from products.txt
products_file = open("products.txt", 'r')

lines = products_file.readlines() 
for line in lines:
    product = line.strip()    
    product_list.append(product)


# load couriers list from couriers.txt
couriers_file = open('couriers.txt', 'r')

lines1 = couriers_file.readlines()
for line in lines1:
    couriers = line.strip()
    couriers_list.append(couriers)



# START OF OUTER LOOP <---------
while True:
    start = int(input("\nWelcome to Julio's Cafe \n\
    Here are our Main Menu Options: \n\
    0. Exit \n\
    1. Products Menu \n\
    2. Couriers Menu \n\
    3. Orders Menu \n\
    >> "))
    
    if start == 0: # start(0) == 0 => TRUE, start(1) == 0 => FALSE

        # save product list to products.txt 
        with open("products.txt", 'w') as f:
            for product in product_list:
                f.write(product + '\n')

        # save couriers list to couriers.txt
        with open("couriers.txt", 'w') as f:
            for courier in couriers_list:
                f.write(courier + '\n')
        break

    elif start == 1:
        print()
        print("Product Menu Options")
        print()
        product_menu_option = int(input("Please select one of the following options: \n\
        0. Return to Main Menu \n\
        1. View the product list \n\
        2. Add a new product to the list \n\
        3. Update an exisiting product \n\
        4. Delete a product \n\
        >> "))

        # START of Prodcut Menu Option INNER LOOP <---------
        while True: 
            
            # Return to Main Menu
            if product_menu_option == 0:
                print()
                break 
                
        # product list
            if product_menu_option == 1:
                print("\nProduct list: ", product_list)
                print()
                product_menu_option = int(input("Please select one of the following options: \n\
        0. Return to Main Menu \n\
        1. View the product list \n\
        2. Add a new product to the list \n\
        3. Update an exisiting product \n\
        4. Delete a product \n\
        >> "))
            
            # adding item to product list
            elif product_menu_option == 2:
                print()
                product_name = input("What is the new product you would like to add? ")
                product_list.append(product_name)
                print("\nProduct list: ", product_list)
                print()
                product_menu_option = int(input("Please select one of the following options: \n\
        0. Return to Main Menu \n\
        1. View the product list \n\
        2. Add a new product to the list \n\
        3. Update an exisiting product \n\
        4. Delete a product \n\
        >> "))            
            
            # update exisiting product
            elif product_menu_option == 3:
                print()
                print(list(enumerate(product_list)))
                print()

                while True:
                    try:
                        product_index = int(input("Product Index: "))
                        if product_index > len(product_list)-1:
                            raise Exception
                    except Exception:
                        print()
                        print('Product index is invalid. Please try again')
                        print()
                    else:
                        product_name = input("Product Name: ")
                        product_list[product_index] = product_name
                        print("\nProduct list: ", product_list)
                        print()
                        product_menu_option = int(input("Please select one of the following options: \n\
        0. Return to Main Menu \n\
        1. View the product list \n\
        2. Add a new product to the list \n\
        3. Update an exisiting product \n\
        4. Delete a product \n\
        >> "))

            # delete product
            elif product_menu_option == 4:
                print()
                print(list(enumerate(product_list)))

                while True:
                    try:
                        print()
                        product_index = int(input("Product Index: "))
                        del product_list[product_index]
                        if product_index > len(product_list)-1:
                            raise Exception
                    except Exception:
                        print()
                        print('Product index is invalid. Please try again')
                        print()
                    else:
                        print("\nProduct list: ", product_list)
                        print()
                        product_menu_option = int(input("Please select one of the following options: \n\
        0. Return to Main Menu \n\
        1. View the product list \n\
        2. Add a new product to the list \n\
        3. Update an exisiting product \n\
        4. Delete a product \n\
        >> "))

        # END of Prodcut Menu Option INNER LOOP <---------


    elif start == 2:
        print()
        print('Couriers Menu Options')
        print()
        courier_menu_option = int(input("Please select one of the following options: \n\
        0. Return to Main Menu \n\
        1. View couriers list \n\
        2. Create new courier \n\
        3. Update existing courier \n\
        4. Delete courier \n\
        >> "))

        #START of COURIER INNER LOOP
        while True:

            #return to Main Menu
            if courier_menu_option == 0:
                print()
                break 

            # print couriers list
            if courier_menu_option == 1:
                print('\nCouriers List: ', couriers_list)
                print()
                courier_menu_option = int(input("Please select one of the following options: \n\
        0. Return to main menu \n\
        1. View couriers list \n\
        2. Create new courier \n\
        3. Update existing courier \n\
        4. Delete courier \n\
        >> "))

            # create new courier
            elif courier_menu_option == 2:
                print()
                new_courier = input('Please input courier name: ')
                print()
                couriers_list.append(new_courier)
                print('\nCouriers List: ', couriers_list)
                print()
                courier_menu_option = int(input("Please select one of the following options: \n\
        0. Return to main menu \n\
        1. View couriers list \n\
        2. Create new courier \n\
        3. Update existing courier \n\
        4. Delete courier \n\
        >> "))

            # update exisiting courier #ASK PATRICK
            elif courier_menu_option ==3:
                print()
                for (count, item) in enumerate(couriers_list):
                    print(count, item, sep = " ")
                print()
                courier_index_value = int(input('Please input the index of the exisiting courier you would like to UPDATE: '))
                courier_to_update = couriers_list[courier_index_value]
                print()
                print(f"You have selected '{courier_to_update}' to update")
                print()
                new_courier_name = input('Please type out the new courier\'s name: ')
                couriers_list[courier_index_value] = new_courier_name
                print()
                for (count, item) in enumerate(couriers_list):
                    print(count, item, sep = " ")
                print()
                courier_menu_option = int(input("Please select one of the following options: \n\
        0. Return to main menu \n\
        1. View couriers list \n\
        2. Create new courier \n\
        3. Update existing courier \n\
        4. Delete courier \n\
        >> "))

            # delete courier
            elif courier_menu_option == 4:
                print()
                for (count, item) in enumerate(couriers_list):
                    print(count, item, sep = " ")
                print()
                courier_index_value = int(input('Please input the index of the exisiting courier you would like to DELETE: '))
                del couriers_list[courier_index_value]
                print('\nCouriers List: ', couriers_list)
                print()
                courier_menu_option = int(input("Please select one of the following options: \n\
        0. Return to main menu \n\
        1. View couriers list \n\
        2. Create new courier \n\
        3. Update existing courier \n\
        4. Delete courier \n\
        >> "))
        
        # END of INNER COURIER LOOP


    elif start == 3:
        print()
        print('Orders Menu')
        print()
        orders_menu_section = int(input("Please select one of the following options: \n\
        0. Return to main menu \n\
        1. View the orders dictionary \n\
        2. Create a new order \n\
        3. Update existing order status \n\
        4. Update exisiting order \n\
        5. Delete order \n\
        >> "))

        #START of ORDER MENU INNER loop <---------
        while True:

            # Return to Main Menu
            if orders_menu_section == 0:
                print()
                break

            # print orders list
            if orders_menu_section == 1:
                print('\nOrders: ', orders_list)
                print()
                orders_menu_section = int(input("Please select one of the following options: \n\
        0. Return to main menu \n\
        1. View the orders dictionary \n\
        2. Create a new order \n\
        3. Update existing order status \n\
        4. Update exisiting order \n\
        5. Delete order \n\
        >> "))

            # create an order
            elif orders_menu_section == 2:
                print()
                customer_name = input('Input Name: ')
                customer_address = input('Input Address: ')
                customer_phone = input('Input number: ')
                print()
                for (count, item) in enumerate(couriers_list):
                    print(count, item, sep = " ")
                print()
                courier_index_value = int(input('Please select courier: '))
                courier_selected = couriers_list[courier_index_value]
                order_status = 'PREPARING'
                new_order = {
                    'Customer Name': customer_name,
                    'Customer Address': customer_address,
                    'Customer Phone': customer_phone,
                    'Courier': courier_selected,
                    'Order Status': order_status
                }
                orders_list.append(new_order)
                print()
                print(new_order)
                print()
                orders_menu_section = int(input("Please select one of the following options: \n\
        0. Return to main menu \n\
        1. View the orders dictionary \n\
        2. Create a new order \n\
        3. Update existing order status \n\
        4. Update exisiting order \n\
        5. Delete order press \n\
        >> "))

            # update exisiting order status
            elif orders_menu_section == 3:
                for (count, item) in enumerate(orders_list):
                    print(count, item, sep = ' ')
                print()
                orders_list_index_input = int((input("Please enter the order index value: ")))
                order_to_update = orders_list[orders_list_index_input]
                print()
                print(f"You have selected {order_to_update} to update")
                print()
                for (count, item) in enumerate(order_status_list):
                    print(count, item, sep = ' ')
                print()
                new_order_status_index = int(input('Please select an index from the Order Status List: '))
                new_order_status = order_status_list[new_order_status_index]
                order_to_update['Order Status'] = new_order_status
                print('\nUpdated Order: ', order_to_update)
                print()
                orders_menu_section = int(input("Please select one of the following options: \n\
        0. Return to main menu \n\
        1. View the orders dictionary \n\
        2. Create a new order \n\
        3. Update existing order status \n\
        4. Update exisiting order \n\
        5. Delete order \n\
        >> "))
                
            # update existiting order:
            elif orders_menu_section == 4:
                for (count, item) in enumerate(orders_list):
                    print(count, item, sep = ' ')
                print()
                orders_list_index_input = int((input("Please enter the order index value: ")))
                order_to_update = orders_list[orders_list_index_input]
                print()
                print(f'You have selected {order_to_update} to update')
                print()
                updated_customer_name = input('Please input updated customer name, otherwise click Enter: ')
                print()
                updated_customer_address = input('Please input updated customer address, otherwise click Enter: ')
                print()
                updated_customer_phone = input('Please input updated customer phone, otherwise click Enter: ')
                for key, value in order_to_update.items():
                    if key == 'Customer Name':
                        if not updated_customer_name:
                            continue
                        else:
                            order_to_update[key] = updated_customer_name
                    if key == 'Customer Address':
                        if not updated_customer_address:
                            continue
                        else:
                            order_to_update[key] = updated_customer_address
                    if key == 'Customer Phone':
                        if not updated_customer_phone:
                            continue
                        else:
                            order_to_update[key] = updated_customer_phone
                print(order_to_update)
                print()
                orders_menu_section = int(input("Please select one of the following options: \n\
        0. Return to main menu \n\
        1. View the orders dictionary \n\
        2. Create a new order \n\
        3. Update existing order status \n\
        4. Update exisiting order \n\
        5. Delete order \n\
        >> ")) 

            # delete order 
            elif orders_menu_section == 5:
                for (count, item) in enumerate(orders_list):
                    print(count, item, sep = " ")
                print()
                orders_list_index_input = int((input("Please enter the order index value: ")))
                del orders_list[orders_list_index_input]
                print()
                print('Orders: ', orders_list)
                print()
                orders_menu_section = int(input("Please select one of the following options: \n\
        0. Return to main menu \n\
        1. View the orders dictionary \n\
        2. Create a new order \n\
        3. Update existing order status \n\
        4. Update exisiting order \n\
        5. Delete order \n\
        >> "))

        #END of ORDER MENU INNER loop <---------


    

