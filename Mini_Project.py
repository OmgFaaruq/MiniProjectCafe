product_list = []
couriers_list = []
orders_list = []
 

import csv

# function to load lists from .csv files

def read_file(filename, loading_list):
    with open(f'{filename}', 'r') as file:
        reader = csv.DictReader(file, delimiter= ',')
        for row in reader:
            loading_list.append(row)    
    return

read_file('products.csv', product_list)
read_file('couriers.csv', couriers_list)
read_file('orders.csv', orders_list)


# function to save lists to .csv files

def write_file(filename, loading_list):
    with open(f'{filename}', mode='w') as file:
        keys = loading_list[0].keys()
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(loading_list)
    return



order_status_list = ['PREPARED', 'OUT FOR DELIVERY', 'DELIVERED']



# START OF OUTER LOOP <--------- Beginning of UI
while True:
    start = int(input("\nWelcome to Julio's Cafe \n\
    Here are our Main Menu Options: \n\
    0. Exit \n\
    1. Products Menu \n\
    2. Couriers Menu \n\
    3. Orders Menu \n\
    >> "))
    
    if start == 0: # start(0) == 0 => TRUE, start(1) == 0 => FALSE
        
        # Savings lists to .csv
        write_file('products.csv', product_list)
        write_file('couriers.csv', couriers_list)
        write_file('orders.csv', orders_list)
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
                
            # Printing product list
            elif product_menu_option == 1:
                print("\nProduct list: ", product_list)
                print()
                product_menu_option = int(input("Please select one of the following options: \n\
        0. Return to Main Menu \n\
        1. View the product list \n\
        2. Add a new product to the list \n\
        3. Update an exisiting product \n\
        4. Delete a product \n\
        >> "))
            
            # Adding item to product list
            elif product_menu_option == 2:
                print()
                product_name = input('What is the new product you would like to add? ')
                product_price = float(input(f'What is the price of {product_name}? '))
                product = {
                    'product': product_name,
                    'price': product_price
                    }
                product_list.append(product)
                print("\nProduct list: ", product_list)
                print()
                product_menu_option = int(input('Please select one of the following options: \n\
        0. Return to Main Menu \n\
        1. View the product list \n\
        2. Add a new product to the list \n\
        3. Update an exisiting product \n\
        4. Delete a product \n\
        >> '))            
            
            # update exisiting product
            elif product_menu_option == 3:
                print()
                print('Products:')
                for (count, item) in enumerate(product_list):
                    print(count, item, sep = " ")
                print()

                while True:
                    try:
                        product_index = int(input("Product Index: "))
                        product_to_update = product_list[product_index]
                        print()
                    except Exception:
                        print()
                        print('Product index is invalid. Please try again')
                        print()
                    else:
                        print(f'You have selected {product_to_update} to update')
                        print()
                        updated_product_name = input('Please input updated product name, otherwise click Enter: ')
                        updated_product_price = input('Please input updated product price, otherwise click Enter: ')
                        for key, value in product_to_update.items():
                            if key == 'product':
                                if not updated_product_name:
                                    continue
                                else:
                                    product_to_update[key] = updated_product_name
                            if key == 'price':
                                if not updated_product_price:
                                    continue
                                else:
                                    product_to_update[key] = updated_product_price
                        print('Updated product: ', product_to_update)
                        print()
                        product_menu_option = int(input("Please select one of the following options: \n\
        0. Return to Main Menu \n\
        1. View the product list \n\
        2. Add a new product to the list \n\
        3. Update an exisiting product \n\
        4. Delete a product \n\
        >> "))
                        break

            # Delete product
            elif product_menu_option == 4:
                print()
                print('Products:')
                for (count, item) in enumerate(product_list):
                    print(count, item, sep = " ")

                while True:
                    try:
                        print()
                        product_index = int(input("Please input the index of the product you would like to delete: "))
                        del product_list[product_index]
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
                    break

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

            # Return to Main Menu
            if courier_menu_option == 0:
                print()
                break 

            # Print couriers list
            elif courier_menu_option == 1:
                print('\nCouriers List: ', couriers_list)
                print()
                courier_menu_option = int(input("Please select one of the following options: \n\
        0. Return to main menu \n\
        1. View couriers list \n\
        2. Create new courier \n\
        3. Update existing courier \n\
        4. Delete courier \n\
        >> "))

            # Create new courier
            elif courier_menu_option == 2:
                print()
                courier_name = input('Please input courier name: ')
                courier_phone = int(input('Please input courier\'s phone number: '))
                new_courier = {
                    'name': courier_name,
                    'phone': courier_phone
                }
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

            # Update exisiting courier
            elif courier_menu_option ==3:
                print()
                print('Couriers:')
                for (count, item) in enumerate(couriers_list):
                    print(count, item, sep = " ")
                print()

                while True:
                    try:
                        courier_index_value = int(input('Please input the index of the exisiting courier you would like to UPDATE: '))
                        courier_to_update = couriers_list[courier_index_value]
                        print()
                    except Exception:
                        print()
                        print('Courier Index is invalid. Please try again.')
                        print()
                    else:
                        print(f"You have selected '{courier_to_update}' to update")
                        print()
                        updated_courier_name = input('Please input updated courier\'s name, otherwise click Enter: ')
                        updated_courier_phone = input('Please input updated courier\'s phone numbers, otherwise click Enter: ')
                        for key, value in courier_to_update.items():
                            if key == 'name':
                                if not updated_courier_name:
                                    continue
                                else:
                                    courier_to_update[key] = updated_courier_name
                            if key == 'phone':
                                if not updated_courier_phone:
                                    continue
                                else:
                                    courier_to_update[key] = updated_courier_phone
                        print()
                        print('Couriers:')
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
                    break

            # Delete courier
            elif courier_menu_option == 4:
                print()
                print('Courtiers:')
                for (count, item) in enumerate(couriers_list):
                    print(count, item, sep = " ")
                print()

                while True:
                    try:
                        courier_index_value = int(input('Please input the index of the exisiting courier you would like to DELETE: '))
                        del couriers_list[courier_index_value]
                    except Exception:
                        print()
                        print('Courier Index is invalid. Please try again.')
                        print()
                    else:
                        print('\nCouriers List: ', couriers_list)
                        print()
                        courier_menu_option = int(input("Please select one of the following options: \n\
        0. Return to main menu \n\
        1. View couriers list \n\
        2. Create new courier \n\
        3. Update existing courier \n\
        4. Delete courier \n\
        >> "))
                break
        
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

            # Print orders list
            elif orders_menu_section == 1:
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

            # Create an order
            elif orders_menu_section == 2:
                print()
                customer_name = input('Input Name: ')
                customer_address = input('Input Address: ')
                customer_phone = input('Input number: ')
                print()
                print('Products:')
                print()
                for (count, item) in enumerate(product_list):
                    print(count, item, sep = " ")
                print()
                product_list_choice = input("Please input the indices of the product you would like to add to your order and separate them by a comma: ")
                print()
                print('Couriers:')
                print()
                for (count, item) in enumerate(couriers_list):
                    print(count, item, sep = " ")
                print()
                courier_index_value = int(input('Please input the index of a courier from above: '))
                print()
                print('Product:')
                order_status = 'PREPARING'
                new_order = {
                    'Customer Name': customer_name,
                    'Customer Address': customer_address,
                    'Customer Phone': customer_phone,
                    'Courier': courier_index_value,
                    'Order Status': order_status,
                    'Items': product_list_choice,
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

            # Update exisiting order status
            elif orders_menu_section == 3:
                for (count, item) in enumerate(orders_list):
                    print(count, item, sep = ' ')
                print()

                while True:
                    try:
                        orders_list_index_input = int((input("Please enter the order index value: ")))
                        order_to_update = orders_list[orders_list_index_input]
                    except Exception:
                        print()
                        print('Order Index is invalid. Please try again.')
                        print()
                    else:
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
                        break
                
            # Update existiting order:
            elif orders_menu_section == 4:
                print()
                for (count, item) in enumerate(orders_list):
                    print(count, item, sep = ' ')
                print()
                
                while True:
                    try:
                        orders_list_index_input = int((input("Please enter the order index value: ")))
                        order_to_update = orders_list[orders_list_index_input]
                        print()
                    except Exception:
                        print()
                        print('Order Index is invalid. Please try again.')
                        print()
                    else:
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
                    break

            # Delete order 
            elif orders_menu_section == 5:
                for (count, item) in enumerate(orders_list):
                    print(count, item, sep = " ")
                print()

                while True:
                    try:
                        orders_list_index_input = int((input("Please enter the order index value: ")))
                        del orders_list[orders_list_index_input]
                    except Exception:
                        print()
                        print('Order Index is invalid. Please try again.')
                        print()
                    else:
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
                    break
        #END of ORDER MENU INNER loop <---------


    

