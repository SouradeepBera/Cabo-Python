import redis
import json

client_id = 0

r = redis.Redis(host="redis-19760.c212.ap-south-1-1.ec2.cloud.redislabs.com", port=19760,
                username="Sayani-Dutta", password="4@everSoura", decode_responses=True)

sub = r.pubsub(ignore_subscribe_messages=True)
sub.subscribe(("server-to-client" + str(client_id)))
sub.subscribe("server-to-all")

for message in sub.listen():
    data = json.loads(message['data'])
    print(data['body'])
    if data['response_req']:
        response = input()
        r.publish("client"+str(client_id)+"-to-server", response)
