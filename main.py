from flask import Flask,jsonify,request
import csv

all_movies = []

with open('data1.csv', encoding = 'utf-8') as f:
    reader =csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
disliked_movies = []
did_not_watch = []

app = Flask(__name__)

@app.route("/get_movies")
def get_moives():
    return jsonify({
        "data" : all_movies[0],
        "status": "success"
    })

@app.route("/liked_movies", methods =["POST"])
def liked_moives():
    movies = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movies)

    return jsonify({
        "status": "success"
    }) , 201

@app.route("/disliked_movies" , methods =["POST"])
def disliked_movies():
    movies = all_movies[0]
    all_movies = all_movies[1:]
    disliked_movies.append(movies)

    return jsonify({
        "status": "success"
    }) , 201

@app.route("/not_watched" , methods =["POST"])
def not_watched():
    movies = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch.append(movies)

    return jsonify({
        "status": "success"
    }) , 201



if __name__ == "__main__":
    app.run()