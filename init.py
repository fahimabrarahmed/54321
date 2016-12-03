from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index0.html')

@app.route("/bend0.html")
def bend():
    return render_template('bend0.html')


@app.route("/fend0.html")
def fend():
    return render_template('fend0.html')

@app.route("/myMR0.html")
def myMR():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * from Customer")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('myMR0.html', users=users)

@app.route("/myMR0.html/<type>")
def myMRR(type=None):
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    statement = ("SELECT movieName, Rating FROM Movie, Customer, Showing WHERE idMovie=Movie_idMovie AND idShowing=Showing_idShowing AND Customer_idCustomer=%s")
    cursor.execute(statement, type)
    data=cursor.fetchall()
    cnx.close()
    return render_template('myMR02.html', data=data, type=type)

@app.route("/1")
def test():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    statement = ("SELECT DISTINCT movieName, Rating FROM Movie, Customer, Showing, Attend WHERE idMovie=Movie_idMovie AND idShowing=Showing_idShowing AND Customer_idCustomer=1")
    cursor.execute(statement, type)
    data=cursor.fetchall()
    cnx.close()
    return render_template('myMR02.html', data = data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)