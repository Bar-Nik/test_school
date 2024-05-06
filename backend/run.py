from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test_api():
    # return "test get work"
    return "<h1>test get work</h1>"


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )
