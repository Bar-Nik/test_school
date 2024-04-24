

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