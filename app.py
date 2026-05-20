from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__) #Creates the Flask Web App

#Loading Dataset
df = pd.read_csv("movies.csv")

#Converting Genre text into numbers
cv = CountVectorizer()
matrix = cv.fit_transform(df["genre"])

#Finding similarity between all movies
similarity = cosine_similarity(matrix)

#Function to recommend movies
def recommend(movie_name):

    movie_name = movie_name.lower() #Converts input into lowercase

    matching = df[df["title"].str.lower() == movie_name] #Finding entered movie in dataset

    if matching.empty:
        return ["Movie Not Found"]

    movie_index = matching.index[0] #Getting movie row index

    distances = similarity[movie_index] #Getting similarity scores of that movie with all other movies

    movie_list = list(enumerate(distances)) #Creating list of movie index and similarity score

    sorted_movies = sorted(movie_list, key=lambda x: x[1], reverse=True) #Sorting from highest similarity to lowest

    recommendations = []

    for i in sorted_movies[1:6]: #Taking top 5 recommended movies
        movie = df.iloc[i[0]]
        recommendations.append(
            f"{movie['title']} ({movie['year']}) ⭐ {movie['rating']}"
        )

    return recommendations

#Homepage Route
@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = [] #Empty list for storing recommendations

    if request.method == "POST": #Runs when user clicks Recommend button
        movie_name = request.form["movie"] #Getting movie name from input box
        recommendations = recommend(movie_name) #Calling recommendation function

    return render_template("index.html", recommendations=recommendations) #Sending result to webpage

#Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)