# Requirements of Shopping Website

1. Users should be able to search for products
2. Sellers should be able to update/add/delete/view the catalog. 
3. Users should be able to do some funnel events like: 
    - Viewing a product page
    - Adding product to the cart
    - Placing an order 
    - Removing from the cart
    - Making payment 
    - Login
    - Register
    - Review for a product
    - Apply coupon 
    - Subscribe for a product
    - Check order status
    - Cancel an order
    - Add to an order
4. Users should be able to search products based on name or category
5. Customer should get notification about order status

# Use Case Diagram

## Actors

1. Guest: Can search, browse and add items to cart. Can become a registered member. 
2. Registered Member: Can perform all activities like guest. Can also place an order. Can check status of orders, get notified. Can also sell products
3. Admin: Maintaining categories & accounts. 
4. System: Sending notification about order & shipping status

## Use cases 

1. Updating the catalog (add/remove/modify)
2. Search the catalog (by name/category)
3. Adding to cart (remove/add/modify)
4. Check out to place an order
5. Make payment to place an order 
6. Cancel or track the order status
7. Get notifcation (on status change)
8. Admin: Add a new product category

## Class Diagram 

1. Account: Customer, Guest, Admin
2. Guest
3. Customer
4. Admin
5. Catalog
6. Category
7. Product 
7. Item (like SKU)
8. Product Review
9. ShoppingCart
9. Order
10. OrderStatus (enum): Cancel, Pending, Completed, Unshipped
11. ShippmentStatus: Shipped, Delivered, Pending
12. Payment
13. PaymentStatus
