
 _cwd = dirname(abspath(__file__))

SECRET_KEY = 'luthercollege'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'flask-tracking.db')
SQLALCHEMY_ECHO = True
WTF_CSRF_SECRET_KEY = 'luthercollegeagain'

app = Flask(__name__)
app.config.from_object(__name__)

db = SQLAlchemy(app)