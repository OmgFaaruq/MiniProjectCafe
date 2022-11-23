# MiniProjectCafe

## Project Background:

Our client has launched a pop-up café in a busy business district. They are offering home-made lunches and refreshments to the surrounding offices. As such, they require a software application which helps them to log and track orders.

### Client Requirements:

- Maintain a collection of products and couriers.
- When a customer makes a new order, create this on the system.
- Update the status of an order i.e: preparing, out-for-delivery, delivered.
- When I exit my app, all data needs to be persisted and not lost.
- When I start my app, all persisted data needs to be loaded onto the system.
- Ensure my app has been tested and proven to work well.


### How did your design go about meeting the project's requirements?

My main thoughts regarding the design of this software was functionality and how easy it was to use. During the development, the user was at the forefront of my mind.
As each week was released I implemented the new requirements in chronological order.

### Overview

Welcome to Julio's Cafe:

    Here are our Main Menu Options:
    0. Exit
    1. Products Menu
    2. Couriers Menu
    3. Orders Menu
    >>
    
    Product Menu Options

    Please select one of the following options: 
        0. Return to Main Menu 
        1. View the product list 
        2. Add a new product to the list    
        3. Update an exisiting product      
        4. Delete a product 
        >> 

    Couriers Menu Options

    Please select one of the following options: 
        0. Return to Main Menu
        1. View couriers list
        2. Create new courier
        3. Update existing courier
        4. Delete courier
        >>
        
     Orders Menu Options

     Please select one of the following options: 
        0. Return to main menu 
        1. View the orders dictionary       
        2. Create a new order 
        3. Update existing order status     
        4. Update exisiting order 
        5. Delete order 
        >> 

### How did you guarantee the project's requirements?

Unit Testing was the way in which I ensured requirements were met. This included quite a bit of refractoring as well as being selective in what needed to be tested. I have written tests for all core functions in the test.py file above. 


### If you had more time, how you would improve upon?

Implement week 5 and 6 of the clients specification as well as input try-except blocks at every point of user input.


### What did you most enjoy implementing?

Whilst each week had it's challenges, implementing try-except blocks which stopped my code from breaking because of an incorrect input and instead raised an error message and allowed the user to input something else has been extremely useful especially when someone else use's the app.
