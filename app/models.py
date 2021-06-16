from . import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True,index=True)
    bio = db.Column(db.String(255))
    image_path = db.Column(db.String(255))
    pass_secure  = db.Column(db.String(255))
    tasks = db.relationship("Task",backref="user",lazy="dynamic")

    def save_user(self):
        db.session.add(self)
        db.session.commit()
    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
      return f'User: {self.username}'



class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer,primary_key=True)
    task = db.Column(db.String(255))
    time = db.Column(db.Column(db.Integer))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    
    def save_task(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
      return f'task: {self.task}'
