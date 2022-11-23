
from product import create_product_and_add_to_product_list

def test_create_product_and_add_to_product_list():

    # Assemble
    product_name = "Pepsi"
    product_price = 0.59
    product_list = []

    # Action 
    product_list = create_product_and_add_to_product_list(product_name, product_price, product_list)

    # Assert
    assert product_list == [{'product': 'Pepsi', 'price': 0.59}]



from product import updating_existing_product


def test_updating_existing_product():
    
    # Assemble
    product_to_update = {'product': 'Chicken', 'price': 9.00}
    updated_product_name = 'Noodles & Chicken'
    updated_product_price = ''

    # Action 
    product_to_update = updating_existing_product(product_to_update, updated_product_name, updated_product_price)

    # Assert     
    assert product_to_update == {'product': 'Noodles & Chicken', 'price': 9.00}



from product import delete_product_from_product_list

def test_delete_product_from_product_list():

    # Assemble
    product_list = [{'product': 'Pepsi', 'price': 0.59}, {'product': 'Chicken', 'price': 9.00}]
    product_index = 1

    # Action
    product_list = delete_product_from_product_list(product_list, product_index)

    # Assert 
    assert product_list == [{'product': 'Pepsi', 'price': 0.59}]



from product import create_courier_and_append_to_couriers_list

def test_create_courier_and_append_to_couriers_list():

    # Assemble
    courier_name = 'Joshua'
    courier_phone = 1234567
    couriers_list = []

    # Action
    courier_list = create_courier_and_append_to_couriers_list(courier_name, courier_phone, couriers_list)

    # Assert
    assert courier_list == [{'name': 'Joshua', 'phone': 1234567}]



from product import updating_exisiting_courier

def test_updating_exisiting_courier():

    # Assemble
    courier_to_update = {'name': 'Louise', 'phone': 986712442}
    updated_courier_name = ''
    updated_courier_phone = 56786563

    # Action
    courier_to_update = updating_exisiting_courier(courier_to_update, updated_courier_name, updated_courier_phone)

    # Assert
    assert courier_to_update == {'name': 'Louise', 'phone': 56786563}



from product import delete_courier_from_courier_list

def test_delete_courier_from_courier_list():

    # Assemble
    couriers_list = [{'name': 'Louise', 'phone': 986712442}, {'name': 'Joshua', 'phone': 1234567}]
    courier_index_value = 1

    # Action 
    couriers_list = delete_courier_from_courier_list(couriers_list, courier_index_value)

    # Assert
    couriers_list = [{'name': 'Louise', 'phone': 986712442}]



from product import create_order_and_append_to_orders_list

def test_create_order_and_append_to_orders_list():

    # Assemble
    customer_name = 'Mick'
    customer_address = 'Queen Victoria, Walford, EastEnd'
    customer_phone = 8833558866
    customers_items = ['1,2']
    courier_index_value = 0
    order_status = 'PREPARING'
    orders_list = []

    # Action
    orders_list = create_order_and_append_to_orders_list(customer_name, customer_address, customer_phone, customers_items, courier_index_value, order_status, orders_list)

    # Assert
    assert orders_list == [{
        'Customer Name': 'Mick',
        'Customer Address': 'Queen Victoria, Walford, EastEnd',
        'Customer Phone': 8833558866,
        'Courier': 0,
        'Order Status': 'PREPARING',
        'Items': ['1,2']
        }]



from product import updating_exisiting_order_status

def test_updating_exisiting_order_status():

    # Assemble 
    order_to_update = {
        'Customer Name': 'Mick',
        'Customer Address': 'Queen Victoria, Walford, EastEnd',
        'Customer Phone': 8833558866,
        'Courier': 0,
        'Order Status': 'PREPARING',
        'Items': 1
        }
    order_status_list = ['PREPARED', 'OUT FOR DELIVERY', 'DELIVERED']
    new_order_status_index = 1

    # Action 
    order_to_update = updating_exisiting_order_status(order_status_list, new_order_status_index, order_to_update)

    # Assert
    assert order_to_update == {
        'Customer Name': 'Mick',
        'Customer Address': 'Queen Victoria, Walford, EastEnd',
        'Customer Phone': 8833558866,
        'Courier': 0,
        'Order Status': 'OUT FOR DELIVERY',
        'Items': 1
        }



from product import delete_order_from_orders_list

def test_delete_order_from_orders_list():

    # Assemble
    orders_list_index_input = 0
    orders_list = [{
        'Customer Name': 'Mick',
        'Customer Address': 'Queen Victoria, Walford, EastEnd',
        'Customer Phone': 8833558866,
        'Courier': 0,
        'Order Status': 'PREPARING',
        'Items': ['1,2']
        }]

    # Action
    orders_list = delete_order_from_orders_list(orders_list, orders_list_index_input)

    # Assert
    assert orders_list == []