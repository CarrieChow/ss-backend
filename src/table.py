import os
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


engine = sa.create_engine(
    os.environ["DATABASE_URL"],
    **{"encoding": 'utf-8'}
)
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "user"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), default="", nullable=False)


class Score(Base):
    __tablename__ = "score"
    id = sa.Column(sa.Integer, primary_key=True)
    score = sa.Column(sa.Integer, nullable=False)
    subject = sa.Column(sa.String(255), nullable=False)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'), nullable=False)


class Contact(Base):
    __tablename__ = "contact"
    __table_args__ = (sa.PrimaryKeyConstraint('user_id', 'other_id'), )
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'), nullable=False)
    other_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'), nullable=False)


class Account(Base):
    __tablename__ = "account"
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'), nullable=False, primary_key=True)
    balance = sa.Column(sa.Integer, nullable=False)
