from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
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
    conn = mysql.connect()
    return "Database connected"

if __name__ == "__main__":
    app.run()