### Hey there

#### Here's DBT project, which illustrats contrast between stream and batch processing

Data generation:

Operations:
Batch:

- Number of total orders per day
- Total value of order
- Max revenue value(in INR) in 1 day
- Most sold category per day
- Segmentation of users

Streaming:

- Coordinate tracking
- Order received event:(for hotel)
- Order update event(order-confirm, cooking, waiting for captain, order-cancelled, shipped, delivered)
- Track number of pending orders(for hotel)
- Top-selling today (for customer)

I am building a python streaming server, which streams data to external sources about food-delivery app like doordash. I need to be able to do feasible batch and streaming application. Following are the operations Batch:

- Number of total orders per day
- Total value of order
- Max revenue value(in INR) in 1 day
- Most sold category per day

Streaming:

- Coordinate tracking
- Order received event:(for hotel)
- Order update event(order-confirm, cooking, waiting for captain, order-cancelled, shipped, delivered)
- Track number of pending orders(for hotel)
- Top-selling today (for customer)
