import sqlalchemy
import traceback

from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, inspect
from sqlalchemy.orm import Session, sessionmaker, mapper
from sqlalchemy.exc import IntegrityError

from sqlalchemy.sql import text


from sqlalchemy import create_engine

class DbManager:
    def __init__(self, config_manager=None, log_manager=None):
        self.config_manager = config_manager
        self.log_manager = log_manager
        self.session = None

        self.connect()

        if self.config_manager.app_config.debug:
            self.log_manager.debug("DbManager init")

    def connect(self):
        try:
            host = self.config_manager.app_config.db_host
            port = self.config_manager.app_config.db_port
            user = self.config_manager.app_config.db_user
            password = self.config_manager.app_config.db_pass
            database = self.config_manager.app_config.db_name

            engine = create_engine(
                f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}",
                isolation_level="READ COMMITTED"
            )

            self.session = Session(bind=engine)
            self.session.execute(text('SELECT * FROM test_school.test_table')).fetchall()

            self.log_manager.info('Connect to DB successfully done.')
        except Exception as e:
            print(e)
            self.log_manager.error('Connect to DB failed.')


# # тут использовать ConfigManager (все креды хранить в .env, читать менеджером
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:123@192.168.1.106:3306/test_school'
# db = SQLAlchemy(app)
#
# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=True)
#     password = db.Column(db.String(500), nullable=True)
#     first_name = db.Column(db.String(50), nullable=True)
#     last_name = db.Column(db.String(50), nullable=True)
#
# class Tests(db.Model):
#     test_id = db.Column(db.Integer, primary_key=True)
#     article = db.Column(db.String(50), nullable=True)
#     config = db.Column(db.String(50), nullable=True)
#     state = db.Column(db.Integer, nullable=True)
#
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
#
# class Transactions(db.Model):
#     transaction_id = db.Column(db.Integer, primary_key=True)
#     test_id = db.Column(db.Integer, db.ForeignKey('tests.test_id', ondelete='CASCADE'))
#
#
# class Tests_results(db.Model):
#     test_result = db.Column(db.Integer, primary_key=True)
#     test_answer = db.Column(db.String(50), nullable=True)
#     session_id = db.Column(db.Integer, nullable=False)
#     first_name = db.Column(db.String(50), nullable=True)
#     last_name = db.Column(db.String(50), nullable=True)
#     number_class = db.Column(db.String(50), nullable=True)
#
#     test_id = db.Column(db.Integer, db.ForeignKey('tests.test_id', ondelete='CASCADE'))
#     transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.transaction_id', ondelete='CASCADE'))