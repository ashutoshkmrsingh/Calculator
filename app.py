from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from Response.parse_input import ParseInput

# intializing main app
app = Flask(__name__)

# initializing input parser
p = ParseInput()

# adding CORS to all origin
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api", methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def api():
    if request.method == 'POST':
        try:
            text = request.get_json()['text']
            return jsonify({
                'text': p.parse(text)
            })
        except KeyError:
            return jsonify({
                'text': '',
                'message': 'Invalid Key - Key not found'
            })
    else:
        return jsonify({
            'text': '',
            'message': 'request method not supported try using POST'
        })


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run()
