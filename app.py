from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        db = mysql.connector.connect(
            host="mysql",
            user="root",
            password="root",
            database="devops"
        )
        return "<h1>Success! Flask successfully connected to MySQL container.</h1>"
    except Exception as e:
        return f"<h1>Connection Failed! Error: {e}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
