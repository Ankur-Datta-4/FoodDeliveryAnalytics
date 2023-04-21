"""
    Order:{
        orderId,
        userId,
        items:[
            {
                itemId,
                priceItem,
                categoryName,
                itemName,
                quantity
            }
        ],
        netPrice,
        discountPrice,
        hotelName,
        hotelId,
        createdAt,
        status: 'order-confirm' | 'cooking' | "waiting-for-delivery" | "out-for-delivery" | "delivered" | "cancelled" | "refund",
        payment: 'cod' | 'online' | 'wallet', 
    }
    
    orderUpdate:{
        orderId,
        status,
        deliveryBoyName,
        deliveryBoyPhone
    } 
    
"""
# generate data for schema above
import random
import uuid
import time
from datetime import datetime, timedelta

# Define possible values for status and payment
STATUS_OPTIONS = ['order-confirm', 'cooking', 'waiting-for-delivery', 'out-for-delivery', 'delivered', 'cancelled', 'refund']
PAYMENT_OPTIONS = ['cod', 'online', 'wallet']

# Function to generate a random order
def generate_order():
    # Generate random orderId and userId
    order_id = str(uuid.uuid4())
    user_id = random.randint(1, 1000)
    
    # Generate a random number of items
    num_items = random.randint(1, 10)
    
    # Generate a list of items with random values
    items = []
    for i in range(num_items):
        item_id = random.randint(1, 100)
        price_item = round(random.uniform(1, 100), 2)
        category_name = f"Category {random.randint(1, 10)}"
        item_name = f"Item {random.randint(1, 100)}"
        quantity = random.randint(1, 5)
        items.append({
            "itemId": item_id,
            "priceItem": price_item,
            "categoryName": category_name,
            "itemName": item_name,
            "quantity": quantity
        })
    
    # Calculate netPrice and discountPrice based on items
    net_price = sum(item['priceItem'] * item['quantity'] for item in items)
    discount_price = round(random.uniform(0, net_price), 2)
    
    # Generate random hotelName and hotelId
    hotel_name = f"Hotel {random.randint(1, 50)}"
    hotel_id = random.randint(1, 100)
    
    # Generate a random createdAt datetime between 1 week ago and now
    created_at = datetime.now() - timedelta(weeks=1) + timedelta(days=random.randint(1, 7), hours=random.randint(1, 24))
    
    # Choose a random status and payment method
    status = random.choice(STATUS_OPTIONS)
    payment = random.choice(PAYMENT_OPTIONS)
    
    # Return the order as a dictionary
    return {
        "orderId": order_id,
        "userId": user_id,
        "items": items,
        "netPrice": net_price,
        "discountPrice": discount_price,
        "hotelName": hotel_name,
        "hotelId": hotel_id,
        "createdAt": created_at,
        "status": status,
        "payment": payment
    }

# Function to generate a random order update
def generate_order_update(order_id):
    # Choose a random status and generate a delivery boy name and phone number
    status = random.choice(STATUS_OPTIONS)
    delivery_boy_name = f"Delivery Boy {random.randint(1, 10)}"
    delivery_boy_phone = f"+91{random.randint(1000000000, 9999999999)}"
    
    # Return the order update as a dictionary
    return {
        "orderId": order_id,
        "status": status,
        "deliveryBoyName": delivery_boy_name,
        "deliveryBoyPhone": delivery_boy_phone
    }

# Generate orders and order updates at the specified rates
while True:
    # Generate 4 orders per second
    for i in range(4):
        order = generate_order()
        print(order)
    # Generate 1 order update per second
    order_update = generate_order_update('abc123')
    print(order_update)
    # Wait for 1 second before generating
    time.sleep(1)
