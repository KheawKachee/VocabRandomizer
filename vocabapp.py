from flask import Flask, render_template, url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd
import sqlite3
from sqlalchemy.sql.expression import func
import os

# Define file paths
def csvreplacedb(csv_file,db_file):
    df = pd.read_csv(csv_file)# Load CSV into a DataFrame
    conn = sqlite3.connect(db_file)# Connect to SQLite database (or create it if it doesn't exist)
    df.to_sql("vocab", conn, if_exists="replace", index=True)# Write the DataFrame to the database which drop table before inserting new db
    conn.close()# Close the connection
    print(f"CSV data successfully imported into {db_file}")#just print with f function where can directly insert variable

csvreplacedb("Dict.csv","database.db") #use def

app = Flask(__name__) # Initialize the Flask application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/kheaw/Task-Master/database.db' # Set the database URI to use SQLite.
db = SQLAlchemy(app) # Create an SQLAlchemy instance for interacting with the database


class vocab(db.Model): #define class called vocab
    index = db.Column(db.Integer, primary_key=True)   # Define the 'index' column as an integer and the primary key for the table.
    English = db.Column(db.String(200),nullable=False) #define english and thai column contain string up to 200 & cant be null
    Thai = db.Column(db.String(200),nullable=False)

    def __repr__(self):   # Define the string representation of an instance of this class for debugging or logging.
        return '<vocab id %r>' % self.id


@app.route('/',methods = ['POST', 'GET']) # Define the route for the root URL ('/') with both POST and GET methods allowed.
def index():
    if request.method =='POST':
        return redirect('/') #req is post -> redirect itself
    else:
        term = vocab.query.order_by(func.random()).first() #random 1 vocab in db
        return render_template('index.html', term= term) #render in html with variable 'term'

@app.route('/list/',methods = ['POST', 'GET']) # Define the route for slash list slash w\ post n get
def list():
    if request.method =='POST':
        newcsv = request.files['table'] # let newcsv be the request files from action namend table (enctype="multipart/form-data" for transmitting binary data (like files) to the server)
        csvreplacedb(newcsv,"test.db") #turn csv to db which Drop the table before inserting new values.
        terms = vocab.query.order_by(vocab.English).all() #order it by A to Z
        return redirect('/') # to root
    else:
        terms = vocab.query.order_by(vocab.English).all() #order it by A to Z
        return render_template('list.html', terms= terms) #render /list with terms var
    
@app.route('/edit/<int:index>',methods = ['POST', 'GET']) #route for editing vocab table in database.db
def update(index):
    term = vocab.query.get_or_404(index) #get vocab.index or print error404
    if request.method=='POST':
        term.Engish =request.form['English']
        term.Thai =request.form['Thai']  #assign new Eng and Thai for editing variable
        try: 
            db.session.commit() #commit it to database
            return redirect('/list/') #back to list page
        except:
            return 'cant edit' #return error msg
    else: 
        return render_template('edit.html',term=term) #render edit when no method with var called term (editing term)

with app.app_context():
    db.create_all() 
#Flask requires an "application context" to execute certain operations that interact with the app's configuration or current state.
# When you call db.create_all(), it needs access to the Flask app's context (like configuration variables and database URI) to know how to initialize the database.
# app.app_context() temporarily pushes the application context, allowing the code inside the with block to interact with the Flask app.


if __name__ == "__main__":
    app.run(debug=True)

#This checks if the script is being run as the main program (as opposed to being imported as a module into another script).
# When you run a Python file, Python sets a special variable __name__. If the file is run directly (not imported), __name__ will be set to "__main__".