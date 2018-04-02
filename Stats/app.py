from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd


# Database setup
engine = create_engine("sqlite:///nba2.db")

# reflecting an existing database.
Base = automap_base()

# reflecting the tables
Base.prepare(engine, reflect=True)

# Assigning the nba class to a variable called `Data`
Data = Base.classes.nba

# Creating session from python to DB
session = Session(engine)

# Flask set up
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("indexb.html")

@app.route("/stats")
def stats_chart():
    
     # query for the top 10 players data
    results = session.query(Data.PLAYER, Data.PTS, Data.AST).\
        order_by(Data.PTS.desc()).\
        limit(10).all()

    # Extract the players data from our results
    PLAYER = [row[0] for row in results]
    PTS = [int(row[1]) for row in results]

    # Generate the plot trace
    plot_trace = {"x": PLAYER, "y": PTS, "type": "bar"}
    return jsonify(plot_trace)

if __name__ == "__main__":
    app.run(debug=True)

