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
        payment: 'cod' | 'online' | 'wallet'

        orderUpdate:{
        orderId,
        status : 'order-confirm' | 'cooking' | "waiting-for-delivery" | "out-for-delivery" | "delivered" | "cancelled" | "refund",
        deliveryBoyName,
        deliveryBoyPhone
        }
    }
    
    
"""

import random
import datetime
import time

payment = ["cod", "online", "wallet"]
status = ["order-confirm", "cooking", "waiting-for-delivery",
          "out-for-delivery", "delivered", "cancelled", "refund"]


def generateOrders():

    data = []
    # generate 1000 orders
    for i in range(1000):
        order = {}
        order["orderId"] = i
        order["userId"] = random.randint(1, 100)
        order["items"] = []
        for j in range(random.randint(1, 5)):
            item = {}
            item["itemId"] = random.randint(1, 100)
            item["priceItem"] = random.randint(1, 100)
            item["categoryName"] = "categoryName"
            item["itemName"] = "itemName"
            item["quantity"] = random.randint(1, 5)
            order["items"].append(item)
        order["netPrice"] = random.randint(1, 100)
        order["discountPrice"] = random.randint(1, 100)
        order["hotelName"] = "hotelName"
        order["hotelId"] = random.randint(1, 100)
        order["createdAt"] = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S")

        # randomise status
        order["status"] = status[random.randint(0, 6)]
        order["payment"] = payment[random.randint(0, 2)]

        # randomise orderUpdate
        order["orderUpdate"] = {}
        order["orderUpdate"]["orderId"] = i
        order["orderUpdate"]["status"] = status[random.randint(0, 6)]
        # generate random names
        order["orderUpdate"]["deliveryBoyName"] = "DeliveryBoyName " + \
            str(random.randint(1, 100))

        # generate 10 digit random phone numebr
        order["orderUpdate"]["deliveryBoyPhone"] = random.randint(
            1000000000, 9999999999)

        data.append(order)

    return data


data = generateOrders()
print(data)
