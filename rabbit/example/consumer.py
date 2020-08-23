import rabbitpy

# Set up connection to RabbitMQ.
url = 'amqp://guest:guest@localhost:5672/%2F'
connection = rabbitpy.Connection(url)

# Create a channel to talk on.
channel = connection.channel()

# Connect to queue.
queue = rabbitpy.Queue(channel, 'example-queue')

while len(queue) > 0:
    message = queue.get()
    print('Message:')
    print('    ID: %s' % message.properties['message_id'])
    print('  Time: %s' % message.properties['timestamp'].isoformat())
    print('  Body: %s' % message.body)
    print('')
    message.ack()

# Close connection.
connection.close()
