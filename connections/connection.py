from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def auto_migrate():
    
    from models.persons import Person
    from models.phone_nos import Phone_no
    from models.add import Address
        
    db.create_all()
    db.session.commit()
    
def seeder():
    
    from models.persons import Person
    from models.phone_nos import Phone_no
    from models.add import Address
    
    Person.seed()
    Phone_no.seed()
    Address.seed()

