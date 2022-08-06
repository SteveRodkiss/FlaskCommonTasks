from flask import Flask, render_template
import sqlite3   #for the database stuff

app = Flask(__name__)

#the path and filename for the database
DATABASE = "database.db"

#routes go here
@app.route('/')
def index():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM item"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()    
    return render_template('index.html',results=results)

#this bit of code runs the app that we just made with debug on
if __name__ == "__main__":
    app.run(debug=True)
