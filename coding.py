import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def homepage_function():
    #raw_data = pd.read_csv("dataset.csv", index_col=1)
    #list = raw_data.index
    # country_list: convert list to list of strings
    return render_template("homepage.html", countries = "country_list")


@app.route("/<country>/")

def info_page_function(country):
    return render_template("info_page.html", country_info = country)
    # raw_data = pd.read_csv("dataset.csv", index_col=1)
    # full_data = raw_data.T.to_dict().values()
    # country_data: dictionary with info about 1 country
    # return render_template("info_page.html", country_info = country_data)


app.run(debug=True)



#Note: return str(full_data) prints all the data to localhost