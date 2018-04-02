import pandas as pd
from flask import Flask, render_template, jsonify

df = pd.read_csv('NBA.csv')

colorlist = []
for team in df["TEAM"]:
    if team == "GSW":
        colorlist.append("rgb(0, 107, 182)")
    else:
        colorlist.append("rgb(255, 0, 0)")
df['COLOR'] = colorlist

df["hovertext"] = df["PLAYER"] + " (" + df["TEAM"] + ")"

app = Flask(__name__)

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

@app.route("/nbasalary/<year>/<gtype>")
def nbasalary(year, gtype):

    tempdf = df[(df['Season']==int(year)) & (df['Type']==gtype)]
    tempdf = tempdf.reset_index(drop=True)
    tempdf.to_csv('result.csv')

    x = tempdf['SAL'].values.tolist()
    y = tempdf['+/-'].values.tolist()
    hovertext = tempdf['hovertext'].values.tolist()    
    color = tempdf['COLOR'].values.tolist()   
    if gtype == 'Regular':
        size = (tempdf['PTS']/20).values.tolist()
    else:
        size = (tempdf['PTS']/5).values.tolist()

    data = {"x": x, "y": y, "hovertext": hovertext, "mode": "markers", "marker": {"color": color, "size": size}}

    tempdf = df.iloc[0:0]
    x = []
    y = []
    hovertext = []
    color = []
    size = []

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)