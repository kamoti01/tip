from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.script import Manager
#from flask.ext.migrate import Migrate

 
app = Flask(__name__)
 
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy()
db.app = app
db.init_app(app)
 
#migrate = Migrate(app,db)
#manager = Manager(app)
