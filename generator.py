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