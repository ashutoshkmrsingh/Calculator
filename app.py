from flask import Flask

#intializing main app
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello World'

@app.route("/about/")
def hello_worl():
    return 'About'

if __name__ == '__main__':
    app.run(debug=True)