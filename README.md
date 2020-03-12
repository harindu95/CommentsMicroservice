# Comments Microservice

I decide to use pipenv https://docs.python-guide.org/dev/virtualenvs/.

## Requirements
    1. Install python3
    2. Install pipenv   
        - pip3 install pipenv
    3. pipenv shell
    4. Install required dependencies
        pipenv install
    5. Start the server on localhost: 
        python3 microservice.py

## Setup database
    1. Install MySql
    2. Create database 'comments'
    3. Create user 'microservice'
    4. test database connection with:
        http://localhost:5000/database
    

### Initialize database
    export FLASK_APP=run.py
    flask init-db

### Test Coverage report
    coverage run -m pytest test
    coverage report --include="app/*"
