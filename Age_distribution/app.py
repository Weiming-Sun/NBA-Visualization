
#dependecies
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func, desc
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
###
from sqlalchemy import Column, Float, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
import pandas as pd
import numpy as np
import os

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
#creating engine
engine = create_engine("sqlite:///nba.sqlite")
Base.metadata.create_all(engine)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Print all of the classes mapped to the Base
print(Base.classes.keys())

# Save reference to the table
nba = Base.classes.nba_table
# Create our session (link) from Python to the DB
session = Session(engine)

# Create the inspector and connect it to the engine
inspector = inspect(engine)

# Using the inspector to print the column names within the 'dow' table and its types
columns = inspector.get_columns('nba_table')
#print(columns)

#base template
@app.route("/")
def index():
    return render_template('index.html')

#collecting all years and types of games played in a year
@app.route('/yearandtype')
@app.route('/yearandtype/')
def yearandtype():
    year = 0
    typ = ""
    yearType = []
    #yearAndType = {}
    results = session.query(nba.Season, nba.Type).order_by(nba.Season.desc()).distinct()
    #print(len(results))
    for result in results:
        year = result[0]
        typ = result[1]
        yearType.append(str(year)+":"+typ)
    return jsonify(yearType)

#is there a relationship between age and average salary?
@app.route('/avgageandsalary')
def avgageandsalary():
    age = []
    avgSalary=[]
    avgAgeAndSalary = {}
    count = 0
    salary = 0
    results = session.query(nba.AGE, nba.SAL).order_by(nba.AGE.desc()).all()
    #print(len(results))
    for i in range (0, len(results)-1):   
        if(results[i][0] ==results[i+1][0]):
            count = count+1
            salary= salary+(results[i][1])
            #print(salary)
        else:
            count = count+1
            salary= salary+(results[i][1])
            avgSalary.append(round(salary/count, 2))
            age.append(results[i][0])
            count = 0
            salary = 0
    #print(avgSalary)
    count = count+1
    salary= salary+(results[i+1][1])
    avgSalary.append(round(salary/count, 2))
    age.append(results[i][0])
    avgAgeAndSalary =dict(zip(age, avgSalary))
    return jsonify(avgAgeAndSalary)

#age distribution of all players in a given year -- how many players are in each age year range
@app.route('/ageDistribution', defaults = {'year': 2017, 'typ': 'Regular'})
@app.route('/ageDistribution/', defaults = {'year': 2017, 'typ': 'Regular'})
@app.route('/ageDistribution/<year>/<typ>')
@app.route('/ageDistribution/<year>', defaults = {'typ': 'Regular'})
@app.route('/ageDistribution/<year>/', defaults = {'typ': 'Regular'})
def ageDistribution(year, typ):
    age =0
    names = []
    count =0
    ageDistribution = {}
    allAgeGroups = {}
    results = session.query(nba.AGE, nba.PLAYER).filter(nba.Season == year, nba.Type ==typ).order_by(nba.AGE.desc()).all()
    #print(len(results))
    #print(results[0])
    for i in range (0, len(results)-1):   
        if(results[i][0] ==results[i+1][0]):
            names.append(results[i][1])
            #count = count +1
            #print(names)
        else:
            names.append(results[i][1])
            age=results[i][0]
            count = len(names)
            #print(count)
            #ageDistribution ={age : [names, count]}
            allAgeGroups[age] = names 
            age =0
            count = 0
            names = []
    names.append(results[i+1][1])
    age=results[i][0]
    count = len(names)
    #ageDistribution ={age : [names, count]}
    #allAgeGroups.append(ageDistribution)
    allAgeGroups[age] = names
    return jsonify(allAgeGroups)
    

#age and 3pointers of all players in a given year 
@app.route('/ageAnd3Pts/<year>/<typ>')
@app.route('/ageAnd3Pts', defaults = {'year': 2017, 'typ': 'Regular'})
@app.route('/ageAnd3Pts/', defaults = {'year': 2017, 'typ': 'Regular'})
@app.route('/ageAnd3Pts/<year>', defaults = {'typ': 'Regular'})
@app.route('/ageAnd3Pts/<year>/', defaults = {'typ': 'Regular'})
def ageAnd3Pts(year, typ):
    age =0
    names = []
    THREEPM = []
    age3PMDistribution = {}
    allAge3PMGroups = []
    results = session.query(nba.AGE, nba.PLAYER, nba.THREEPM).filter(nba.Season == year, nba.Type ==typ).order_by(nba.AGE.desc()).all()
    #print(len(results))
    #print(results[0])
    for i in range (0, len(results)-1):   
        if(results[i][0] ==results[i+1][0]):
            names.append(results[i][1])
            THREEPM.append(results[i][2])
            #print(names)
        else:
            names.append(results[i][1])
            THREEPM.append(results[i][2])
            age=results[i][0]
            age3PMDistribution ={age : [names, THREEPM]}
            allAge3PMGroups.append(age3PMDistribution)
            age =0
            names = []
            THREEPM = []
    names.append(results[i+1][1])
    THREEPM.append(results[i+1][2])
    age=results[i][0]
    age3PMDistribution ={age : [names, THREEPM]}
    allAge3PMGroups.append(age3PMDistribution)
    return jsonify(allAge3PMGroups)

#age and 3pointers of all players in a given year 
@app.route('/ageAndTop3Pts/<year>/<typ>')
@app.route('/ageAndTop3Pts', defaults = {'year': 2017, 'typ': 'Regular'})
@app.route('/ageAndTop3Pts/', defaults = {'year': 2017, 'typ': 'Regular'})
@app.route('/ageAndTop3Pts/<year>', defaults = {'typ': 'Regular'})
@app.route('/ageAndTop3Pts/<year>/', defaults = {'typ': 'Regular'})
def ageAndTop3Pts(year, typ):
    age =[]
    TopTHREEPM = []
    THREEPM = []
    ageTop3PMDistribution = {}
    results = session.query(nba.AGE, nba.THREEPM).filter(nba.Season == year, nba.Type == typ).order_by(nba.AGE.desc()).all()
    for i in range (0, len(results)-1):   
        if(results[i][0] ==results[i+1][0]):
            THREEPM.append(results[i][1])
        else:
            THREEPM.append(results[i][1])
            age.append(results[i][0])
            TopTHREEPM.append(max(THREEPM))
            THREEPM = []
    THREEPM.append(results[i+1][1])
    TopTHREEPM.append(max(THREEPM))
    age.append(results[i][0])
    ageTop3PMDistribution = dict(zip(age, TopTHREEPM))
    return jsonify(ageTop3PMDistribution)

#age and FGM of all players in a given year 
@app.route('/ageAndFGM/<year>/<typ>')
@app.route('/ageAndFGM', defaults= {'year': 2017, 'typ': 'Regular'})
@app.route('/ageAndFGM/', defaults= {'year': 2017, 'typ': 'Regular'})
@app.route('/ageAndFGM/<year>', defaults= {'typ': 'Regular'})
@app.route('/ageAndFGM/<year>/', defaults= {'typ': 'Regular'})
def ageAndFGM(year, typ):
    age =0
    names = []
    FGM = []
    ageFGMDistribution = {}
    allAgeFGMGroups = []
    results = session.query(nba.AGE, nba.PLAYER, nba.FGM).filter(nba.Season == year, nba.Type ==typ).order_by(nba.AGE.desc()).all()
    #print(len(results))
    #print(results[0])
    for i in range (0, len(results)-1):   
        if(results[i][0] ==results[i+1][0]):
            names.append(results[i][1])
            FGM.append(results[i][2])
            #print(names)
        else:
            names.append(results[i][1])
            FGM.append(results[i][2])
            age=results[i][0]
            ageFGMDistribution ={age : [names, FGM]}
            allAgeFGMGroups.append(ageFGMDistribution)
            age =0
            names = []
            FGM = []
    names.append(results[i+1][1])
    FGM.append(results[i+1][2])
    age=results[i][0]
    ageFGMDistribution ={age : [names, FGM]}
    allAgeFGMGroups.append(ageFGMDistribution)
    #print(allAgeGroups)
    return jsonify(allAgeFGMGroups) 
    
#age and FGM of all players in a given year 
@app.route('/ageAndTopFGM/<year>/<typ>')
@app.route('/ageAndTopFGM', defaults= {'year': 2017, 'typ': 'Regular'})
@app.route('/ageAndTopFGM/', defaults= {'year': 2017, 'typ': 'Regular'})
@app.route('/ageAndTopFGM/<year>', defaults= {'typ': 'Regular'})
@app.route('/ageAndTopFGM/<year>/', defaults= {'typ': 'Regular'})
def ageAndTopFGM(year, typ):
    age =[]
    TopFGM = []
    FGM = []
    ageTopFGMDistribution = {}
    results = session.query(nba.AGE, nba.FGM).filter(nba.Season == year, nba.Type ==typ).order_by(nba.AGE.desc()).all()
    for i in range (0, len(results)-1):   
        if(results[i][0] == results[i+1][0]):
            FGM.append(results[i][1])
        else:
            FGM.append(results[i][1])
            age.append(results[i][0])
            TopFGM.append(max(FGM))
            FGM = []
    FGM.append(results[i+1][1])
    TopFGM.append(max(FGM))
    age.append(results[i][0])
    ageTopFGMDistribution = dict(zip(age, TopFGM))
    return jsonify(ageTopFGMDistribution)


#age and %Winning of all players in a given year 
@app.route('/ageAndPWin/<year>/<typ>')
@app.route('/ageAndPWin', defaults = {'year': 2017, 'typ':'Regular'})
@app.route('/ageAndPWin/', defaults = {'year': 2017, 'typ':'Regular'})
@app.route('/ageAndPWin/<year>', defaults = {'typ': 'Regular'})
@app.route('/ageAndPWin/<year>/', defaults = {'typ': 'Regular'})
def ageAndPWin(year, typ):
    age =0
    names = []
    win = 0
    #totalGames = 0
    PWin = []
    agePWinDistribution = {}
    allAgePWinGroups = []
    results = session.query(nba.AGE, nba.PLAYER, nba.W, nba.GP).filter(nba.Season == year, nba.Type ==typ).order_by(nba.AGE.desc()).all()
    #print(len(results))
    #print(results[0])
    for i in range (0, len(results)-1):   
        if(results[i][0] ==results[i+1][0]):
            names.append(results[i][1])
            win = round(100*(results[i][2]/results[i][3]),2)
            PWin.append(win)
            #print(names)
        else:
            names.append(results[i][1])
            win = round(100*(results[i][2]/results[i][3]),2)
            PWin.append(win)
            age=results[i][0]
            agePWinDistribution ={age : [names, PWin]}
            allAgePWinGroups.append(agePWinDistribution)
            age = 0
            win = 0
            names = []
            PWin = []
    names.append(results[i+1][1])
    win = round(100*(results[i+1][2]/results[i+1][3]), 2)
    PWin.append(win)
    age=results[i][0]
    agePWinDistribution ={age : [names, PWin]}
    allAgePWinGroups.append(agePWinDistribution)
    #print(allAgeGroups)
    return jsonify(allAgePWinGroups)

#age and % top Winning of all players in a given year 
@app.route('/ageAndTopPWin/<year>/<typ>')
@app.route('/ageAndTopPWin', defaults = {'year': 2017, 'typ':'Regular'})
@app.route('/ageAndTopPWin/', defaults = {'year': 2017, 'typ':'Regular'})
@app.route('/ageAndTopPWin/<year>', defaults = {'typ': 'Regular'})
@app.route('/ageAndTopPWin/<year>/', defaults = {'typ': 'Regular'})
def ageAndTopPWin(year, typ):
    age = []
    win = 0
    TopPwin = []
    PWin = []
    ageTopPwinDistribution = {}
    results = session.query(nba.AGE, nba.W, nba.GP).filter(nba.Season == year, nba.Type ==typ)\
                .order_by(nba.AGE.desc()).all()
    for i in range (0, len(results)-1):   
        if(results[i][0] == results[i+1][0]):
            win = round(100*(results[i][1]/results[i][2]),2)
            PWin.append(win)
        else:
            win = round(100*(results[i][1]/results[i][2]),2)
            PWin.append(win)
            age.append(results[i][0])
            TopPwin.append(max(PWin))
            win = 0
            PWin = []
    win = round(100*(results[i+1][1]/results[i+1][2]),2)
    PWin.append(win)
    TopPwin.append(max(PWin))
    age.append(results[i][0])
    ageTopPwinDistribution = dict(zip(age, TopPwin))
    return jsonify(ageTopPwinDistribution)

if __name__ == "__main__":
    app.run(debug=True)