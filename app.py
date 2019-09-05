import os
import socket

from flask import Flask
from redis import Redis, RedisError


# Redis Connection Variable
redis_host = os.getenv("REDIS_HOST", "127.0.0.1")
redis_port = os.getenv("REDIS_PORT", 6379)
redis_pass = os.getenv("REDIS_PASSWORD", None)


# Library Variable
app = Flask(__name__)
redis = Redis(host=redis_host, port=redis_port, password=redis_pass,
              db=0, socket_connect_timeout=2, socket_timeout=2)


# Main Application
@app.route("/")
def index():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>Cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    
    return html.format(name=os.getenv("NAME", "World"), hostname=socket.gethostname(), visits=visits)


# Run Application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)