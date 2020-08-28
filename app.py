from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
#What do I put after localhost?
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    mars_dataDB = mongo.db.mars_data_collected.find_one()

    #Return the tempalte and dadata

    return render_template("index.html", planet = mars_dataDB)

@app.route("/scrape_all")
def scrape():

    mars_dataDB = mongo.db.mars_data_collected

    mars_data = scrape_mars.scrape_all()

    #Update the mongo datase using update and upsert=True

    mars_dataDB.update({}, mars_data, upsert=True)

    # Redirect back to home page

    return redirect("/", code = 302)

if __name__ == "__main__":
    app.run(debug=True, port = 5020)


