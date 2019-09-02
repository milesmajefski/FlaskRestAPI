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
from flask import Flask, Response, request, jsonify
from pymongo import MongoClient, errors
from bson import json_util


app = Flask(__name__)
db_user = os.getenv('DB_USER', 'nuthin')
db_password = os.getenv('DB_PASSWORD', '')
connect_str = 'mongodb+srv://{}:{}@cluster0-uh9qt.mongodb.net/test?retryWrites=true&w=majority'.format(db_user, db_password)


@app.route('/')
def index():
    try:
        client = MongoClient(connect_str)
    except errors.PyMongoError as e:
        return 'Fail! cuz db no worky! %s' % e

    db = client['python_class']
    if db:
        posts = db.microblog
        post = posts.find()
        return Response(json_util.dumps(post), mimetype='application/json')


@app.route('/posts', methods=['POST'])
def create_post():
    try:
        client = MongoClient(connect_str)
        # return request.form['title']
    except errors.PyMongoError as e:
        return 'Fail! cuz db no worky! %s' % e

    db = client['python_class']
    if db:
        posts = db.microblog
        post_data = {'title': request.form['title']}
        inserted = posts.insert_one(post_data)
        return Response(json_util.dumps(inserted.inserted_id), mimetype='application/json')


def connect():
    client = MongoClient(connect_str)
    db = client['python_class']
    if db:
        print('Connected to my db!')
        posts = db.microblog
        pprint.pprint(posts.find_one())

if __name__ == '__main__':
    #connect()
    #print(db_user)
    app.run(debug=False)