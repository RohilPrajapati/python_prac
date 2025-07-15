import psycopg2
import redis
from flask import Flask, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

app = Flask(__name__)

pg_conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
pg_cursor = pg_conn.cursor()

r = redis.Redis(host='localhost',port=6379,db=0)

# 1. cache aside (Lazy Loading)
"""
Concept :
- Check Redis First
- if not in cache, fetch from Postgres and store in Redis
"""

@app.route('/user/<int:user_id>/')
def get_user(user_id):
    key = f"user:{user_id}"
    if r.exists(key):
        user_data = r.hgetall(key)
        return jsonify(
            {
                "source":"cache",
                "user":{k.decode(): v.decode() for k,v in user_data.items()}
            }
        )
    # fallback to Postgres

    pg_cursor.execute("select id, name, email from users where id = %s",(user_id,))
    row = pg_cursor.fetchone()
    if not row:
        return jsonify({"error":"User not found"}),404
    
    user = {"id":row[0],"name":row[1], "email":row[2]}
    r.hset(key,mapping=user)
    r.expire(key,60) 

    return jsonify({
        "source":"db",
        "user":user
    })

if __name__ == '__main__':
    app.run(debug=True)