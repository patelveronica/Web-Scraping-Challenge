from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pandas as pd
import time

# create an instance of Flask
app = Flask(__name__)

# use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/MissionToMars_db")

# Rout to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_information = mongo.db.marsdata.find_one()
    # return template and data
    return render_template("index.html", mars_information=mars_information)

# Rout that will trigger the scrape function
@app.route("/scrape")
def scrape():
    # run the scrape function
    mars_information = mongo.db.marsdata
    mars_datainfo = scrape_mars.scrape()
    # update the Mongo database using update and upsert=true
    mars_information.update({}, mars_datainfo, upsert=True)
    mars_information = mongo.db.marsdata.find_one()
    # redirect back to home page
    url = 'https://galaxyfacts-mars.com/'
    # browser.visit(url)
    tables= pd.read_html(url) 

    table_df = tables[1] 
    table_df.columns = ['Description', 'Value']
    print(tables)
    marsfacts = table_df.to_html()
    print(marsfacts)
    return render_template("index.html", marsfacts=marsfacts, mars_information=mars_information)

# Redirect back to home page
    # return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)
