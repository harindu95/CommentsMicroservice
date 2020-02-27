from app import microservice

app = microservice.app

if __name__ == '__main__':
    app.run(debug=True)