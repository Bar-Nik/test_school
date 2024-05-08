from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Простая запись CORS(app) делает ваше приложение доступным для всех источников (*).
# Это удобно при разработке, однако для рабочего окружения необходимо ограничить доступ.
# https://sky.pro/wiki/python/razreshenie-cors-vo-flask-dlya-zaprosov-cherez-j-query/
CORS(app)

@app.route('/api', methods=['GET'])
def test_api():
    # return "test get work"
    return "<h1>test get work</h1>"


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=8000,
        debug=True
    )
