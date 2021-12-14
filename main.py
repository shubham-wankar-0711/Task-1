from flask import Flask
from connections.connection import db,auto_migrate,seeder
import os
from models.persons import Person

app = Flask(__name__)
app.config.from_pyfile(os.path.join(os.getcwd(), 'configs', 'conf.py'))
db.init_app(app)

with app.app_context():
    auto_migrate()
    seeder()
    
    from controllers import controller

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8999,debug=True)