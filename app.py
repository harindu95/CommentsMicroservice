from flask import Flask,jsonify
from flaskext.mysql import MySQL
from db import db
from init import create_app

app = create_app();
db.init_app(app)
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'microservice'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'comments'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/")
def main():
    return "Welcome!"

# Need to setup mysql beforehand
@app.route("/database")
def db_test():
    # conn = mysql.connect()
    # return "Database connected"
    d = db.get_db()
    return "Database connected .... " + repr(d)


@app.route("/api/comment/<id>/")
def comment(id):
    response = {}
    response['type'] = 'comment'
    response['id'] = id
    response['UserId'] = '213344'
    response['Desc'] = 'Comment description'
    return jsonify(response)



if __name__ == "__main__":
    app.run()