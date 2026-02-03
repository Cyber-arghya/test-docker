from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='db', port=6379) # 'db' matches the service name in compose

@app.route('/')
def hello():
    count = redis.incr('hits')
    return f'Hello! This page has been viewed by aghya {count} times.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)