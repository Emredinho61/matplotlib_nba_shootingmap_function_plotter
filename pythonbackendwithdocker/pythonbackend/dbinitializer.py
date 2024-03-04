import csv
import sqlite3

"""
dbinitializer.py: Used for creating a database and extracting the content of a csv file full of data.
"""

# create connection to the database
con = sqlite3.connect(
    "pythonbackend/data/NBA_2004_2023_Shots.db")

# return a cursor for maneuvering through the db
cur = con.cursor()

# sql: CREATE TABLE querry used
cur.execute(
    "CREATE TABLE nbashotsperplayer (SEASON_1 int, TEAM_ID int, TEAM_NAME text, PLAYER_ID int, PLAYER_NAME text, EVENT_TYPE text, SHOT_MADE text, LOC_X double, LOC_Y double);")

# in the csv from stats.nba.com we have information we do not need, so I only use the columns that are interesing for me
# open and read csv file, extracting the needed columns
with open('pythonbackend/data/NBA_2004_2023_Shots.csv',
          'r') as fin:  # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    # comma used as a default delimitter
    dr = csv.DictReader(fin)
    to_db = [(i['SEASON_1'], i['TEAM_ID'], i['TEAM_NAME'], i['PLAYER_ID'], i['PLAYER_NAME'], i['EVENT_TYPE'],
              i['SHOT_MADE'], i['LOC_X'], i['LOC_Y']) for i in dr]

# insert the data extracted out of the csv into the db
cur.executemany(
    "INSERT INTO nbashotsperplayer (SEASON_1, TEAM_ID, TEAM_NAME, PLAYER_ID, PLAYER_NAME, EVENT_TYPE, SHOT_MADE, LOC_X, LOC_Y) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);",
    to_db)
con.commit()
con.close()
