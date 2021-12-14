from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from connections.connection import db,auto_migrate,seeder
from models.persons import Person

class Phone_no(db.Model):    
        
    __table_args__ = {'schema': 'task_db'}
    __table_name__ = 'phone_no'
    
    id = Column(Integer, primary_key=True)
    number = Column(String, primary_key=True, nullable=False)
    country = Column(String,nullable=False)
    user_id = Column(Integer,ForeignKey('task_db.person.person_id'))
    
    @staticmethod
    def seed():
        
        count = Phone_no.query.count()
        if count == 0:
            
            data = db.session.query(Person).filter_by(name="Rohan").first()
            phone = Phone_no(id=1,number='9890733580',country='India',owner = data)
            
            data1 = db.session.query(Person).filter_by(name="Rohit").first()
            phone = Phone_no(id=2,number='7709390319',country='India',owner = data1)
            
            data2 = db.session.query(Person).filter_by(name="Sai Madhur").first()
            phone = Phone_no(id=3,number='9999999999',country='India',owner = data2)
            
            data3 = db.session.query(Person).filter_by(name="Umamahesh").first()
            phone = Phone_no(id=4,number='8888888888',country='India',owner = data3)
            
            data4 = db.session.query(Person).filter_by(name="Bharathi").first()
            phone = Phone_no(id=5,number='7777777777',country='India',owner = data4)
            
            try:
                db.session.add(phone)
                db.session.commit()
            except Exception as e:
                print('Exception: {}'.format(e))
                
        else:
            print('Phone Data Already Satisfied....!!!')
    