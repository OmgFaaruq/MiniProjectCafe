
# Function for 'create product and add to product list'

def create_product_and_add_to_product_list(product_name, product_price, product_list):
    product = {
        'product': product_name,
        'price': product_price
        }
    product_list.append(product)
    return product_list



# Function for 'updating existing product'

def updating_existing_product(product_to_update, updated_product_name, updated_product_price):
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
    return product_to_update



# Function for 'delete product from product list'

def delete_product_from_product_list(product_list, product_index):
    del product_list[product_index]
    return product_list



# Function for 'create courier and append to couriers list'

def create_courier_and_append_to_couriers_list(courier_name, courier_phone, couriers_list):
    new_courier = {
        'name': courier_name,
        'phone': courier_phone
        }
    couriers_list.append(new_courier)
    return couriers_list



# Function for 'updating exisiting courier'

def updating_exisiting_courier(courier_to_update, updated_courier_name, updated_courier_phone):
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
    return courier_to_update



# Function for 'delete courier'

def delete_courier_from_courier_list(couriers_list, courier_index_value):
    del couriers_list[courier_index_value]
    return couriers_list



# Function for 'create order and add to orders list'

def create_order_and_append_to_orders_list(customer_name, customer_address, customer_phone, customers_items, courier_index_value, order_status, orders_list):
    new_order = {
        'Customer Name': customer_name,
        'Customer Address': customer_address,
        'Customer Phone': customer_phone,
        'Courier': courier_index_value,
        'Order Status': order_status,
        'Items': customers_items
        }
    orders_list.append(new_order)
    return orders_list



# Function for 'updating exisiting order status'

def updating_exisiting_order_status(order_status_list, new_order_status_index, order_to_update):
    new_order_status = order_status_list[new_order_status_index]
    order_to_update['Order Status'] = new_order_status
    return order_to_update



# Function for 'updating exisiting order'

# Function for 'delete order'

def delete_order_from_orders_list(orders_list, orders_list_index_input):
    del orders_list[orders_list_index_input]
    return orders_list