"""
Microblog service as Restful API
- MongoDB for database

Post:
    - Text
    - Title

    Meta:
    - Author = id(username)
    - Date

User:
    - username


RESTful API:
CRUD
create, read, update, delete


POST
www.us.com/posts


GET
www.us.com/posts

GET
www.us.com/posts/1625375


PUT
www.us.com/posts/1625375

DELETE
www.us.com/posts/1625375

"""
import os
import pprint
from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)
db_user = os.getenv('DB_USER', 'nuthin')
db_password = os.getenv('DB_PASSWORD', '')

@app.route('/home')
@app.route('/')
def index():
    return "Hello, World!"

def connect():
    connect_str = 'mongodb+srv://{}:{}@cluster0-uh9qt.mongodb.net/test?retryWrites=true&w=majority'.format(db_user, db_password)

    client = MongoClient(connect_str)
    db = client['python_class']
    if db:
        print('Connected to my db!')
        posts = db.microblog
        pprint.pprint(posts.find_one())

if __name__ == '__main__':
    connect()
    print(db_user)
    app.run(debug=False)