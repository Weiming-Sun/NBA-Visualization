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

df["text"] = df["PLAYER"] + " (" + df["TEAM"] + ")"

app = Flask(__name__)

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

@app.route("/nbasalary/<year>")
def nbasalary(year):

    tempdf = df[df['Season']==int(year)]
    tempdf = tempdf.reset_index(drop=True)
    '''tempdf.to_csv('result.csv')'''

    x = tempdf['SAL'].values.tolist()
    y = tempdf['+/-'].values.tolist()
    text = tempdf['text'].values.tolist()    
    color = tempdf['COLOR'].values.tolist()   
    size = (tempdf['PTS']/35).values.tolist()

    data = {"x": x, "y": y, "hovertext": text, "mode": "markers", "marker": {"color": color, "size": size}}

    tempdf = df.iloc[0:0]
    x = []
    y = []
    text = []
    color = []
    size = []

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)