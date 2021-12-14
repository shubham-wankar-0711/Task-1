from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from connections.connection import db
# from models.phone_nos import Phone_no

class Person(db.Model):
    
    __table_args__ = {'schema':'task_db'}
    __table_name__ = 'person'
    
    person_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    phone_no = relationship('Phone_no',backref='owner', lazy='dynamic')
    address = relationship('Address',backref='owner1', lazy='dynamic')
    
    @staticmethod
    def seed():
        
        count = Person.query.count()
        if count == 0:
            
            per = [
                Person(name = 'Rohan', age = 26),
                Person(name = 'Rohit', age = 27),
                Person(name = 'Sai Madhur', age = 26),
                Person(name = 'Umamahesh', age = 23),
                Person(name = 'Bharathi', age = 25),
            ]
            
            try:
                db.session.add_all(per)
                db.session.commit()
            except Exception as e:
                print('Exception = {} '.format(e))
                
        else:
            print('Person Data is already seeded...!!!!')