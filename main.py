from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route and a function to handle the route
@app.route('/')
def hello_world():
    return 'Hello, World!'

