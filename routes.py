from flask import Flask
from flask.ext.wtf import Form
from flask import render_template, redirect, flash
from flask import request 
from formS import TipForm
from datetime import datetime
import re
from flask import Flask, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap 
app= Flask(__name__)
app.secret_key = 'luther college'
app.config.from_pyfile('app.cfg')
db = SQLAlchemy(app) 
Bootstrap(app)

class Tips(db.Model):
  # Setting the table name and
  # creating columns for various fields
  __tablename__ = 'tips' 
  id = db.Column('tip_id', db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  tip = db.Column(db.String(200))
  pub_date = db.Column(db.DateTime)
  
  def __init__(self, name, tip):
      # Initializes the fields with entered data
      # and sets the published date to the current time
      self.name = name
      self.tip = tip
      self.pub_date = datetime.now()
db.drop_all
db.create_all()

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/signup')
def signup():
  return render_template('signup.html')

@app.route('/tips')
def tips():
	return "Hello World!"

@app.route('/index')
def index():
  return render_template('show_all.html')

@app.route('/h')
def show_all():
  return render_template('show_all.html', tips=Tips.query.order_by(Tips.pub_date.desc()).all()  )


# This view method responds to the URL /new for the methods GET and POST
@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        # Check if all the fields are entered. If not, raise an error
        if not request.form['name'] or not request.form['tip']: 
            flash('Please enter all the fields', 'error')
        
        else:
            # The data is valid. So create a new 'Tips' object
            # to save to the database
            tip = Tips(request.form['name'],
                               #request.form['email'],
                               request.form['tip'])
    
            # Add it to the SQLAlchemy session and commit it to
            # save it to the database
            db.session.add(tip)
            db.session.commit()
            
            # Flash a success message
            flash('Tip was successfully posted')
            
            # Redirect to the view showing all the comments
            return redirect(url_for('show_all'))
    
    # Render the form template if the request is a GET request or
    # the form validation failed
    return render_template('new.html')
 
if __name__ == '__main__':
  app.run(debug=True)
