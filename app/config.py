'''Application wide configurations'''

# MYSQL_DATABASE_USER = 'microservice'
# MYSQL_DATABASE_PASSWORD = ''
# MYSQL_DATABASE_DB = 'test_comments'
# MYSQL_DATABASE_HOST = 'localhost'

# dialect+driver://username:password@host:port/database
# SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:bienbien1!@nikelausm.caqihksh4b3a.ca-central-1.rds.amazonaws.com/Nozy'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://microservice:@localhost/test_comments'
SQLALCHEMY_TRACK_MODIFICATIONS = False