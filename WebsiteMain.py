from flask import Flask, render_template, url_for, request, redirect, jsonify

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    # I have a folder called GameArchive with a bunch of json files in it, I need to load all of the JSON files. Their names are the dates each game was published

    allGames = []
    for file in o



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)