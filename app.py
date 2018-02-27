import os
import socket

from flask import Flask
from redis import Redis, RedisError


# Declare Library
app = Flask(__name__)
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)


# Main Application
@app.route("/")
def home():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>Cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    
    return html.format(name=os.getenv("NAME", "World"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)