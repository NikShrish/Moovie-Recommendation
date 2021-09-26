from flask import Flask,jsonify,request
import csv

all_movies=[]

with open('movies.csv',encoding="utf-8")as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]


liked_movies=[]
unliked_movies=[]
did_not_watch=[]

app=Flask(__name__)

@app.route('/get_movie')
def get_movie():
    return jsonify({
        "data":all_movies[0],
        "status":"success"
    })

@app.route('/liked_movie',methods=["POST"])
def liked_movie():
    global all_movies
    movie=all_movies[0]
    liked_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201


@app.route('/unlike_movie',methods=["POST"])
def unliked_movie():
    global all_movies
    all_movies=all_movies[1:]
    unliked_movies.append(all_movies)
    return jsonify({
        "status":"success"
    }),201










if __name__ =="__main__":
    app.run(debug=True)
