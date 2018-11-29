import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def homepage_function():
    raw_data = pd.read_csv("dataset.csv", index_col=1)
    list = raw_data.index
    return render_template("homepage.html", countries=list.astype(str).values.tolist())


@app.route("/data/<country>/")

def result(country):
    raw_data = pd.read_csv("dataset.csv", index_col=1)

    country_data = raw_data.loc[country.capitalize()]
    data_as_dict = country_data.T.to_dict()
    return render_template("info_page.html", country_info = data_as_dict)


app.run(debug=True)