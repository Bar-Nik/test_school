from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = 'users'
    _id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=True)
    password: Mapped[str] = mapped_column(String(500), nullable=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=True)

class Tests(Base):
    __tablename__ = 'tests'
    test_id: Mapped[int] = mapped_column(primary_key=True)
    article: Mapped[str] = mapped_column(String(50), nullable=True)
    config: Mapped[str] = mapped_column(String(50), nullable=True)
    state: Mapped[int] = mapped_column(nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))

class Transactions(Base):
    __tablename__ = 'transactions'
    transaction_id: Mapped[int] = mapped_column( primary_key=True)
    test_id: Mapped[int] = mapped_column(ForeignKey('tests.test_id', ondelete='CASCADE'))


class Tests_results(Base):
    __tablename__ = 'test_results'
    test_result: Mapped[int] = mapped_column(primary_key=True)
    test_answer: Mapped[str] = mapped_column(String(50), nullable=True)
    session_id: Mapped[int] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=True)
    number_class: Mapped[str] = mapped_column(String(50), nullable=True)

    test_id: Mapped[int] = mapped_column(ForeignKey('tests.test_id', ondelete='CASCADE'))
    transaction_id: Mapped[int] = mapped_column(ForeignKey('transactions.transaction_id', ondelete='CASCADE'))


# from run import db
#
# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def __repr__(self):
#         return '<User %r>' % self.username