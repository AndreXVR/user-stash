from user_stash.extensions import db
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid4()))
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.TEXT(), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<User {self.first_name}, {self.last_name}, {self.email}>"

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def create(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def read_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def update(self, first_name=None, last_name=None, email=None, password=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        if password:
            self.hash_password(password)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
