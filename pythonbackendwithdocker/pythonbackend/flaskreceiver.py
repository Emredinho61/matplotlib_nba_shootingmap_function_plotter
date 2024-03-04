import json

from flask import Flask, make_response, request, send_file
from flask_cors import CORS
from plotter import SimplePlot, BarPlot, PiePlot, TrigPlot, NbaShootingMapPlotter
import sqlite3

app = Flask(__name__)

DATABASE = "pythonbackend/data/NBA_2004_2023_Shots.db"
CORS(app, supports_credentials=True, resources={r'/*': {'origins': '*'}})


def connect_db():
    return sqlite3.connect(DATABASE)


def getDataNBAPlayers(season):
    conn = connect_db()
    cur = conn.cursor()
    # extract the Team and players to display them as options in frontend
    cur.execute(
        f"SELECT TEAM_NAME, PLAYER_NAME FROM nbashotsperplayer as NBA where NBA.SEASON_1 == {season}")
    data = cur.fetchall()
    conn.close()
    return data


def getMadeShotPos(player, season):
    conn = connect_db()
    cur = conn.cursor()
    # query to get the location of made shots of every player
    cur.execute(
        f"SELECT LOC_X, LOC_Y FROM nbashotsperplayer as NBA where NBA.PLAYER_NAME == '{player}' AND SHOT_MADE == 'TRUE' AND NBA.SEASON_1 == {season}")
    data = cur.fetchall()
    conn.close()
    return data


def getMissedShotsPos(player, season):
    conn = connect_db()
    cur = conn.cursor()
    # query to get the location of made shots of every player
    cur.execute(
        f"SELECT LOC_X, LOC_Y FROM nbashotsperplayer as NBA where NBA.PLAYER_NAME == '{player}' AND SHOT_MADE == 'FALSE' AND NBA.SEASON_1 == {season}")
    data = cur.fetchall()
    conn.close()
    return data


def parseToCascadeFormat(data):
    """
    in order to be useful in the frontend I want a format like:
    - {'tname': 'Houston Rockets', [{'players': 'Alperen Sengun'}, ...]}
    without duplicates, thus a set
    """

    result = []
    teams = set(team[0] for team in data)
    for team in teams:
        players_set = set()
        players = []
        for player in data:
            if player[0] == team and player[1] not in players_set:
                players_set.add(player[1])
                players.append({'pname': player[1]})  # Use 'name' key for player name
        team_info = {'tname': team, 'players': players}
        result.append(team_info)
    return result


@app.route("/postPlotNBA", methods=["POST", "GET"])
def respondToPlotRequest():
    # extract the data of post request
    try:
        player = request.get_json().get("selectedPlayer").get("pname")
        missed = request.get_json().get("missed")
        season = request.get_json().get("season")
        heatmap = request.get_json().get("heatmap")
        if missed == "False":
            loc_x_y = getMadeShotPos(player, season)
        else:
            loc_x_y = getMissedShotsPos(player, season)
        loc_x = []
        loc_y = []

        # use the nba plotting class of plotter.py
        for oneData in loc_x_y:
            loc_x.append(float(oneData[0]))
            loc_y.append(float(oneData[1]))
        nbaPlotter = NbaShootingMapPlotter(loc_x, loc_y, missed, player, season, heatmap)
        nbaPlotter.drawPointsOnCourt()
        # send image as response to post request
        return send_file("plots/nbaPlot.png", mimetype="image/png")
    except AttributeError:
        return make_response("Choose a player", 400)


@app.route("/postNBA", methods=["POST", "GET"])
def respondToNBA():
    # extract the data of post request
    season = request.get_json().get("selectedSeason").get('code')
    dataPerSeason = parseToCascadeFormat(getDataNBAPlayers(season))
    # respond with every teams player (Structured)
    return make_response(dataPerSeason, 200)


@app.route("/postTrig", methods=["POST", "GET"])
def respondToValuesTrig():
    # extract the data of post request
    resp = request.get_json()
    start = resp.get("start")
    stop = resp.get("stop")
    mode = resp.get("mode")
    numOfSamples = resp.get("numOfSamples")
    a = resp.get("a")
    b = resp.get("b")
    c = resp.get("c")
    d = resp.get("d")
    title = resp.get("title")

    # use the trigonometric plotting class
    trigPlotter = TrigPlot(
        mode=mode,
        start=start,
        stop=stop,
        numOfSamples=numOfSamples,
        a=a,
        b=b,
        c=c,
        d=d,
        title=title,
    )
    trigPlotter.plotTrigPlot()
    # respond to request with plot as image
    return send_file("plots/trigPlot.png", mimetype="image/png")


@app.route("/postSimplePlot", methods=["POST", "GET"])
def respondToValuesSimp():
    # extract the data of post request
    resp = request.get_json()
    start = resp.get("start")
    stop = resp.get("stop")
    fun = resp.get("fun")
    xlabel = resp.get("xlabel")
    ylabel = resp.get("ylabel")
    title = resp.get("title")

    simplePlotter = SimplePlot(
        fun=fun, start=start, stop=stop, xlabel=xlabel, ylabel=ylabel, title=title
    )
    simplePlotter.plotSimplePlot()

    # respond to request with plot as image
    return send_file("plots/simplePlot.png", mimetype="image/png")


@app.route("/postBar", methods=["POST", "GET"])
def respontToBar():
    # extract the data of post request
    resp = request.get_json()
    xlabel = resp.get("xlabel")
    ylabel = resp.get("ylabel")
    title = resp.get("title")
    values = resp.get("values")

    names = []
    vals = []
    colors = []

    # for the colors we need it in hex notation, so we append it
    for oneDict in values:
        names.append(str(oneDict.get("name")))
        vals.append(oneDict.get("val"))
        colors.append("#" + oneDict.get("color"))
    barPlotter = BarPlot(
        names=names, vals=vals, colors=colors, xlabel=xlabel, ylabel=ylabel, title=title
    )
    barPlotter.plotBarPlot()

    # respond to request with plot as image
    return send_file("plots/barPlot.png", mimetype="image/png")


@app.route("/postPie", methods=["POST", "GET"])
def respontToPie():
    # extract the data of post request
    resp = request.get_json()
    values = resp.get("values")
    title = resp.get("title")
    names = []
    vals = []
    colors = []

    # for the colors we need it in hex notation, so we append it
    for oneDict in values:
        names.append(str(oneDict.get("name")))
        vals.append(oneDict.get("val"))
        colors.append("#" + oneDict.get("color"))
    piePlotter = PiePlot(names=names, vals=vals, colors=colors, title=title)
    piePlotter.plotPieChart()

    # respond to post request with image as plot
    return send_file("plots/piePlot.png", mimetype="image/png")


if __name__ == "__main__":
    # run the app on port 5000
    app.run(debug=True, port=5000, host="0.0.0.0")
