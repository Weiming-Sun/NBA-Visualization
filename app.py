import pandas as pd
from flask import Flask, render_template, jsonify

df = pd.read_csv('NBA.csv')

app = Flask(__name__)

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

@app.route("/nbasalary/<year>")
def nbasalary(year):

    tempdf = df[df['Season']==int(year)]

    x = tempdf['SAL'].values.tolist()
    y = tempdf['+/-'].values.tolist()
    text = tempdf['PLAYER'].values.tolist()    
    size = (tempdf['PTS']/35).values.tolist()

    bubbledata = {"x": x, "y": y, "hovertext": text, "mode": "markers", "marker": {"color": "rgb(255, 0, 0)", "size": size}}

    return jsonify(bubbledata)

if __name__ == '__main__':
    app.run(debug=True)