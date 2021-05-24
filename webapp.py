from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json 

app = Flask(__name__)

@app.route('/')
def render_about():
    return render_template('about.html')


@app.route('/databycountry')
def render_databycountry():
    country = request.args['country']
    return render_template('databycountrydisplay.html', options = get_country_options(), TotalDeaths = fact_by_country(country))
    
def get_country_options():
    listOfCountries = []
    with open('aids.json') as demographics_data:
        years = jsson.load(demographics_data)
    for year in years:
        if not(year["Country"] in listOfCountries):
            listOfCountries.append(year["Country"])
    options = ""
    for c in listOfCountries:
        options = options + Markup("<option value=\"" + c + "\">" + c + "</option>")
    return options 

def fun_fact_by_country(country):
    with open('aids.json') as demographics_data:
        year = json.load(demographics_data)
    highest = 0
    lowest = 15000
    
    for x in years:
        if x["Country"] == country:
            totaldeaths = x["AIDS-Related Deaths"]["All Ages"] 
            if totaldeaths > highest:
                highest = totaldeaths
                highYear = x["Year"]
            elif totaldeaths == 0:
    	        lowest = lowest
            elif totaldeaths < lowest:
                lowest = totaldeaths
                lowYear = x["Year"]
        highest = round(highest, 2)
        lowest = round(lowest, 2)

    return "The year with the highest deaths in " + country + " is " + highYear + " (" + str(highest) + "%)" + " and the year with the lowest deaths in " + country + " is " + lowYears + " (" + str(lowest) + "%)"




if __name__=="__main__":
    app.run(debug=True)
