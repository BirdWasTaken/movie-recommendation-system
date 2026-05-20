# Movie Recommendation System

This project is a web-based movie recommendation system built using Python and Flask. It recommends similar movies based on genre using cosine similarity.

## Features

* Search movies by title
* Recommends 5 similar movies
* Shows release year and rating
* Handles case-insensitive input
* Web interface using Flask

## Technologies Used

* Python
* Pandas
* Flask
* Scikit-learn
* HTML
* CSS

## Machine Learning Concepts Used

* CountVectorizer
* Cosine Similarity
* Content-Based Recommendation System

## Project Structure

* app.py → main Flask backend
* movies.csv → movie dataset
* templates/index.html → webpage
* static/style.css → styling

## How to Run

1. Install libraries
   pip install pandas flask scikit-learn

2. Run application
   python app.py

3. Open in browser
   http://127.0.0.1:5000

## Future Improvements

* Larger movie dataset
* Movie posters
* Search suggestions
* SQL database integration
