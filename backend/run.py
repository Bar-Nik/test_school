from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:123@192.168.1.106:3306/test_school'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(500), nullable=True)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)

class Tests(db.Model):
    test_id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.String(50), nullable=True)
    config = db.Column(db.String(50), nullable=True)
    state = db.Column(db.Integer, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))

class Transactions(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('tests.test_id', ondelete='CASCADE'))


class Tests_results(db.Model):
    test_result = db.Column(db.Integer, primary_key=True)
    test_answer = db.Column(db.String(50), nullable=True)
    session_id = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    number_class = db.Column(db.String(50), nullable=True)

    test_id = db.Column(db.Integer, db.ForeignKey('tests.test_id', ondelete='CASCADE'))
    transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.transaction_id', ondelete='CASCADE'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            hash = generate_password_hash(request.form['password'])
            user = Users(email=request.form['email'], password=hash, first_name=request.form['first_name'], last_name=request.form['last_name'])
            db.session.add(user)
            db.session.commit()
        except:
            db.session.rollback()
            print("Ошибка добавления в БД")


    return render_template('register.html', title='Регистрация')

if __name__ == "__main__":
    app.run(debug=True)
# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#         app.run(debug=True)