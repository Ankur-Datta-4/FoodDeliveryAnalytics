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
        status,
        payment: 'cod' | 'online' | 'wallet', 
    }
    
    orderUpdate:{
        orderId,
        status,
        deliveryBoyName,
        deliveryBoyPhone
    }
   
   
    
    
"""



import json
import time
from random import randint
# from kafka import KafkaProducer
from faker import Faker
import math

fake = Faker()

# Kafka configuration
KAFKA_BROKER = 'localhost:9092'
ORDER_TOPIC = 'orders'
ORDER_UPDATE_TOPIC = 'order_updates'
COORDINATES_TOPIC = 'coordinates'

# producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def generate_items(category):
    items = {
        'Pizza': ['Margherita', 'Pepperoni', 'BBQ Chicken', 'Veggie', 'Hawaiian'],
        'Burger': ['Cheeseburger', 'Veggie Burger', 'Grilled Chicken Burger', 'Bacon Burger', 'Portobello Mushroom Burger'],
        'Sushi': ['California Roll', 'Spicy Tuna Roll', 'Philadelphia Roll', 'Dragon Roll', 'Rainbow Roll'],
        'Indian': ['Butter Chicken', 'Paneer Tikka', 'Chana Masala', 'Chicken Biryani', 'Palak Paneer'],
        'Chinese': ['Kung Pao Chicken', 'Fried Rice', 'Chow Mein', 'Sweet and Sour Pork', 'Mapo Tofu']
    }
    return [fake.random_element(items[category]) for _ in range(randint(1, 4))]

def generate_order():
    category = fake.random_element(elements=('Pizza', 'Burger', 'Sushi', 'Indian', 'Chinese'))
    items = generate_items(category)
    order = {
        "order_id": fake.uuid4(),
        "customer_id": fake.uuid4(),
        "hotel_id": fake.uuid4(),
        "category": category,
        "items": [{"name": item, "price": round(fake.random_number(digits=3, fix_len=True), 2)} for item in items],
        "timestamp": int(time.time())
    }
    return order


def generate_order_update(order_id):
    update = {
        "order_id": order_id,
        "status": fake.random_element(elements=('order-confirm', 'cooking', 'waiting for captain', 'order-cancelled', 'shipped', 'delivered')),
        "timestamp": int(time.time())
    }
    return update

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in kilometers

    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)

    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(lat1) * math.cos(lat2) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c

    return distance
def generate_coordinates(customer_latitude, customer_longitude, prev_latitude=None, prev_longitude=None):
    if prev_latitude is None or prev_longitude is None:
        # If this is the first coordinate, generate a random starting point
        latitude = fake.latitude()
        longitude = fake.longitude()
    else:
        # Otherwise, generate a coordinate that gradually gets nearer to the customer
        latitude = prev_latitude + (customer_latitude - prev_latitude) / 10
        longitude = prev_longitude + (customer_longitude - prev_longitude) / 10

    distance = haversine(customer_latitude, customer_longitude, latitude, longitude)

    coordinates = {
        "delivery_person_id": fake.uuid4(),
        "latitude": latitude,
        "longitude": longitude,
        "customer_latitude": customer_latitude,
        "customer_longitude": customer_longitude,
        "distance": distance,
        "timestamp": int(time.time())
    }
    return coordinates, latitude, longitude

# Generate a random starting point
prev_latitude = fake.latitude()
prev_longitude = fake.longitude()

while True:
    # Produce messages to Kafka topics
    order = generate_order()
    print ("order" , order)

    order_update = generate_order_update(order['order_id'])
    print("ORDER_UPDATE_TOPIC", order_update)

    customer_latitude = fake.latitude()
    customer_longitude = fake.longitude()

    # Generate the next coordinate and update the previous coordinates
    coordinates, prev_latitude, prev_longitude = generate_coordinates(customer_latitude, customer_longitude, prev_latitude, prev_longitude)
    print("COORDINATES_TOPIC", coordinates)

    # Sleep for a few seconds
    time.sleep(randint(1, 5))

