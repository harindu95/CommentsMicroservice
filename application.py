'''Launch Flask Application'''

from app import microservice

application = microservice.app

if __name__ == '__main__':
    application.run()
