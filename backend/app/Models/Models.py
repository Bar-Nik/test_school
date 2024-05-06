from typing import Annotated, Optional
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


intpk = Annotated[int, mapped_column(primary_key=True)]
str_50 = Annotated[str, '50']
str_100 = Annotated[str, '100']
str_500 = Annotated[str, '500']

class Base(DeclarativeBase):
    type_annotation_map = {
        str_50: String(50),
        str_100: String(100),
        str_500: String(500)
    }

class Users(Base):
    __tablename__ = 'users'

    _id: Mapped[intpk]
    email: Mapped[Optional[str_100]] = mapped_column(unique=True)
    password: Mapped[Optional[str_500]]
    first_name: Mapped[Optional[str_50]]
    last_name: Mapped[Optional[str_50]]

class Tests(Base):
    __tablename__ = 'tests'

    _id: Mapped[intpk]
    article: Mapped[Optional[str_50]]
    config: Mapped[Optional[str_50]]
    state: Mapped[Optional[int]]

    user_id: Mapped[int] = mapped_column(ForeignKey('users._id', ondelete='CASCADE'))

class Transactions(Base):
    __tablename__ = 'transactions'

    _id: Mapped[intpk]
    test_id: Mapped[int] = mapped_column(ForeignKey('tests._id', ondelete='CASCADE'))


class TestsResults(Base):
    __tablename__ = 'test_results'

    _id: Mapped[intpk]
    test_answer: Mapped[Optional[str_50]] = mapped_column(String(50))
    session_id: Mapped[Optional[int]]
    first_name: Mapped[Optional[str_50]]
    last_name: Mapped[Optional[str_50]]
    number_class: Mapped[Optional[str_50]]

    test_id: Mapped[int] = mapped_column(ForeignKey('tests._id', ondelete='CASCADE'))
    transaction_id: Mapped[int] = mapped_column(ForeignKey('transactions._id', ondelete='CASCADE'))
