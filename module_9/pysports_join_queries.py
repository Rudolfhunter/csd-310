import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
db = mysql.connector.connect(**config)

cursor = db.cursor()
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player LEFT OUTER JOIN team ON player.team_id = team.team_id")
players = cursor.fetchall()

print("-- DISPLAYING PLAYER RECORDS --")

for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}".format(player[3]))
    print()

input("Press any key to continue...")