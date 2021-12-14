from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from connections.connection import db,auto_migrate,seeder
from models.persons import Person

class Address(db.Model):    
        
    __table_args__ = {'schema': 'task_db'}
    __table_name__ = 'address'
    
    id = Column(Integer, primary_key=True)
    addr = Column(String, nullable=False)   
    user_id = Column(Integer,ForeignKey('task_db.person.person_id'))
    
    @staticmethod
    def seed():
        
        count = Address.query.count()
        if count == 0:
            
            data = db.session.query(Person).filter_by(name="Rohan").first()
            addrs = Address(id=1,addr='Nagpur, Maharashtra', owner1 = data)
            
            data = db.session.query(Person).filter_by(name="Rohit").first()
            addrs = Address(id=2,addr='Pune, Maharashtra', owner1 = data)
            
            data = db.session.query(Person).filter_by(name="Sai Madhur").first()
            addrs = Address(id=3,addr='Hyderabad, Telangana', owner1 = data)
            
            data = db.session.query(Person).filter_by(name="Umamahesh").first()
            addrs = Address(id=4,addr='Vijayawada, Andhara Pradesh', owner1 = data)
            
            data = db.session.query(Person).filter_by(name="Bharathi").first()
            addrs = Address(id=5,addr='Mumbai, Maharashtra', owner1 = data)
            
            try:
                db.session.add(addrs)
                db.session.commit()
            except Exception as e:
                print('Exception: {}'.format(e))
                
        else:
            print('Phone Data Already Satisfied....!!!')
    