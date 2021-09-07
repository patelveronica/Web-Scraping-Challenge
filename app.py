from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create an instance of Flask
app = Flask(__name__)

# use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/missionsttomars_db")

# Rout to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    destination_data = mongo.db.information.find_one()
    # return template and data
    return render_template("index.html",marsinfo = destination_data)

# Rout that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # run the scrape function
    mars_data = scrape_mars.scrape_info()

    # update the Mongo database using update and upsert=true
    mongo.db.information.update({}, mars_data, upsert=True)
    # redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
