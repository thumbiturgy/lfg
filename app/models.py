from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from secrets import token_urlsafe

from app import db, login

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    token = db.Column(db.String(250), unique=True)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'User: {self.username}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def hash_password(self,password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def add_token(self):
        setattr(self,'token',token_urlsafe(32))
    
    def get_id(self):
        return str(self.user_id)
    
class Post(db.Model):
    id=  db.Column(db.Integer, primary_key = True)
    body= db.Column(db.String(250))
    timestamp= db.Column(db.DateTime, default=datetime.utcnow)
    user_id= db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    character_id= db.Column(db.Integer, db.ForeignKey('character.character_id'), nullable=False)

    def __repr__(self):
        return f'<Post: {self.body}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

class Character(db.Model):
    character_id= db.Column(db.Integer, primary_key = True)
    name= db.Column(db.String(100))
    hero_class= db.Column(db.String(30))
    species= db.Column(db.String(50))
    party_role= db.Column(db.String(50))
    saves= db.Column(db.String(30))
    personality_type= db.Column(db.String(200))
    portrait= db.Column(db.String(100))
    model= db.Column(db.String(100))
    user_id= db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

class Party(db.Model):
    party_id= db.Column(db.Integer, primary_key = True)
    party_name= db.Column(db.String(50))
    member1= db.Column(db.Integer, db.ForeignKey('character.character_id'))
    member2= db.Column(db.Integer, db.ForeignKey('character.character_id'))
    member3= db.Column(db.Integer, db.ForeignKey('character.character_id'))
    member4= db.Column(db.Integer, db.ForeignKey('character.character_id'))
    member5= db.Column(db.Integer, db.ForeignKey('character.character_id'))
    member6= db.Column(db.Integer, db.ForeignKey('character.character_id'))
    member7= db.Column(db.Integer, db.ForeignKey('character.character_id'))
    member8= db.Column(db.Integer, db.ForeignKey('character.character_id'))
    user_id= db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)



