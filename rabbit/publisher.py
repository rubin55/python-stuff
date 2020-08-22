import rabbitpy

# Set up connection to RabbitMQ.
url = 'amqp://guest:guest@localhost:5672/%2F'
connection = rabbitpy.Connection(url)

# Create a channel to talk on.
channel = connection.channel()

# Set up an exchange.
exchange = rabbitpy.Exchange(channel, 'example-exchange')
exchange.declare()

# Set up a queue and bind to exchange.
queue = rabbitpy.Queue(channel, 'example-queue')
queue.declare()
queue.bind(exchange, 'example-routing-key')

# Let's do some test messages.
for message_number in range(0, 100):
    message = rabbitpy.Message(
        channel,
        'Test message #%i' % message_number,
        {'content_type': 'text/plain'},
        opinionated=True
    )
    print('Publishing message #%i' % message_number)
    message.publish(exchange, 'example-routing-key')

# Close connection.
connection.close()
