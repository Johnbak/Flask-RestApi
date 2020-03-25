#!flask/bin/python
from flask import Flask, jsonify ,request
import logging
import pymysql

app = Flask(__name__)
connection=pymysql.connect(host='mysql', database='testdb',user='root', password='root', port=3306) #mysql links in docker-compose
# ('localhost:3306','root','root','testdb')
# (host='localhost', database='testdb',user='root', password='root', port=3306

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Alcolhol,Beer,Cigar,Pipe', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    logging.warning('Watch out!')


    return jsonify({'tasks': tasks}),200

@app.route('/todo/api/v1.0/tasks/insert', methods=['POST'])
def insert_profile():
    if request.method == "POST":
        content = request.json
        logging.warning(content['name'])
        logging.warning(content['country'])
        logging.warning(content['gank'])


    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `bermingham` (`country`, `gank`, `name`) VALUES (%s, %s,%s)"
            cursor.execute(sql, (content['country'], content['gank'],content['name']))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

        # with connection.cursor() as cursor:
        #     # Read a single record
        #     sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        #     cursor.execute(sql, ('webmaster@python.org',))
        #     result = cursor.fetchone()
        #     print(result)
    finally:
        connection.close()



        return jsonify({'tasks': tasks}),200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)