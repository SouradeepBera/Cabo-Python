import redis

client_id = 1

r = redis.Redis(host="redis-19760.c212.ap-south-1-1.ec2.cloud.redislabs.com", port=19760,
                username="Souradeep-Bera", password="amaN*1712", decode_responses=True)

sub = r.pubsub(ignore_subscribe_messages=True)
sub.subscribe(("server-to-client" + str(client_id)))
sub.subscribe("server-to-all")

for message in sub.listen():
    print(message['data'])
    response = input()
    r.publish("client"+str(client_id)+"-to-server", response)

