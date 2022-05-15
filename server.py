import redis

def construct_msg():
    pass

r = redis.Redis(host="redis-19760.c212.ap-south-1-1.ec2.cloud.redislabs.com", port=19760,
                username="Server", password="Server@123", decode_responses=True)

sub = r.pubsub(ignore_subscribe_messages=True)

n_players = 2
for i in range(n_players):
    sub.subscribe("client"+str(i)+"-to-server")

is_kaboo = -1
swap = -1
first_player = -1
for i in range(n_players):
    r.publish("server-to-client" + str(i), "Kaboo? 1 or 0")
    for message in sub.listen():
        data = message['data']
        channel = message['channel']
        if channel == "client"+str(i)+"-to-server":
            is_kaboo = data
            break
    
    if is_kaboo == 1:
        break

    r.publish("server-to-client" + str(i), "Swap? 1 or 0")
    for message in sub.listen():
        data = message['data']
        channel = message['channel']
        if channel == "client"+str(i)+"-to-server":
            swap = data
            break
    
    r.publish("server-to-all", "show player's current card")
    for message in sub.listen():
        data = message['data']
        channel = message['channel']
        # first_player = data['player_id']
        # card = data['card']
        if channel:
            break
        
print("is_kaboo", is_kaboo)
print("swap", swap)
print("first_player", first_player)


