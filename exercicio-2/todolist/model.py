from sqlalchemy import Column, Integer, String, Boolean, ColumnDefault
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

Base = declarative_base()


db = SQLAlchemy(model_class=Base)

class TodoItem(db.Model):
    __tablename__ = 'todoitems'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    done = Column(Boolean, ColumnDefault(False))

    def as_dict(self):
        return {'id': self.id, 'text': self.text, 'done': self.done}