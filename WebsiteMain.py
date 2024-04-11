from flask import Flask, render_template, url_for, request, redirect, jsonify
import json
import os

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    # I have a folder called GameArchive with a bunch of json files in it, I need to load all of the JSON files. Their names are the dates each game was published

    allGames = []
    for file in os.listdir('GameArchive'):
        if file.endswith('.json'):
            with open(f'GameArchive/{file}') as f:
                allGames.append(json.load(f))
                
    return render_template('index.html', allGames=allGames)

@app.route('/game/<gameDate>', methods=['GET', 'POST'])
def game(gameDate):
    with open(f'GameArchive/{gameDate}.json') as f:
        gameData = json.load(f)
    return render_template('game.html', game=gameData)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)