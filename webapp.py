from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json 

app = Flask(__name__)

@app.route('/')
def render_about():
    return render_template('about.html')

@app.route('/databycountry')
def render_databycountry():
    return render_template('databycountry.html', options = get_country_options())
    
@app.route('/data')
def render_data():
    country = request.args['country']
    return render_template('databycountrydisplay.html', options = get_country_options(), countryFact = fact_by_country(country))
    

def get_country_options():
    listOfCountries = []
    with open('aids.json') as demographics_data:
        years = json.load(demographics_data)
    for year in years:
        if not(year["Country"] in listOfCountries):
            listOfCountries.append(year["Country"])
    options = ""
    for c in listOfCountries:
        options = options + Markup("<option value=\"" + c + "\">" + c + "</option>")
    return options 



def fact_by_country(country):
    with open('aids.json') as demographics_data:
        years = json.load(demographics_data)
    highest = 0
    lowest = 15000
    
    highYear= 1990
    lowYear= 2015
       
    for x in years:
        if x["Country"] == country:
            totaldeaths = x["Data"]["AIDS-Related Deaths"]["All Ages"] 
            if totaldeaths > highest:
                highest = totaldeaths
                highYear = x["Year"]
            elif totaldeaths == 0:
    	        lowest = lowest
            if totaldeaths < lowest:
                lowest = totaldeaths
                lowYear = x["Year"]
        highest = round(highest, 2)
        lowest = round(lowest, 2)

    return "The year with the highest deaths in " + country + " is " +  str(highYear) + " (" + str(highest) + ")" + " and the year with the lowest deaths in " + country + " is " + str(lowYear) + " (" + str(lowest) + ")"




if __name__=="__main__":
    app.run(debug=True)
