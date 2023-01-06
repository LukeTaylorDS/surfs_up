
# Import Dependencies 
from flask import Flask

# Create Flask Instance
app = Flask(__name__)

# Creating Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'