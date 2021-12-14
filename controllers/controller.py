from flask import current_app as app
from models.persons import Person
from models.phone_nos import Phone_no
from models.add import Address
from flask.json import jsonify
from flask import Flask,request,make_response
from connections.connection import db

# GET METHOD TO RETRIEVE DATA FROM DATABASE

@app.route('/person_details', methods=['GET'])
def person_detail():
    
    data = Person.query.all()    
    
    for person in data:
        # print('Person: ',person)
        print()
        print('Person {} Personal Details: - \n'.format(person.person_id))
        print('Person ID :- ',person.person_id)
        print('Person Name :- ',person.name)
        print('Person Age :- ',person.age)
        print()
        
        for phone in person.phone_no:
            # print('Phones: ',phone)
            print('Person {} Phone Details: - \n'.format(phone.id))
            print('Person ID :- ',phone.id)
            print('Person Number :- ',phone.number)
            print('Number belongs to which country :- ',phone.country)
            print()
            
            
            for address in person.address:
                # print('Address: ',address)
                print('Person {} Address Details: - \n'.format(address.id))
                print('Person ID :- ',address.id)
                print('Person Address :- ',address.addr)                
                print()
                
#  POST METHOD TO POST/ADD DATA IN DATABASE

@app.route('/create/<int:id>/<address>/<phone_no>', methods=['POST'])
def create(id,address,phone_no):
    
    data = request.get_json()
    # print(data)
    # print()
    # print(data['Address'])
    person_data = Person.query.filter_by(person_id = data['id']).first()
    print(person_data)
    phone = Phone_no(id=10, number=data['phone_no'],country='India',owner = person_data)
    addrs = Address(id=10, addr=data['Address'], owner1 = person_data)
    
    try:
        db.session.add(phone)
        db.session.add(addrs)
        db.session.commit()
    except Exception as e:
        print('Exception: {}'.format(e))    
     
    #    task = task_schema.load(data)
    #    result = task_schema.dump(task.create())
    #    return make_response(jsonify({"task": result}), 200)
    
    return jsonify({'status':'Success'})
    
    
# PUT METHOD TO UPDATE DATA IN DATABASE

@app.route('/update/<int:id>/<address>', methods=['PUT'])
def update(id,address):
    
    data = request.get_json()
    person_data = Person.query.all()
    
    # print(data)
    # print()
    # print(data['Address'])
    # person_data = Person.query.filter_by(person_id = data['id']).first()  
      
    for person in person_data:
        for address in person.address:
            if person.person_id == data['id'] :
                address.addr = data['Address']
    
    try:                
        db.session.commit()
    except Exception as e:
        print('Exception: {}'.format(e))
        
                        
    return jsonify({'status':'Success'})
        