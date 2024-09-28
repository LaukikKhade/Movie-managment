from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def load_movies_from_csv(file_path):
    """Load movies from a CSV file."""
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

# Load the movie data from the CSV file
movies = load_movies_from_csv('movies.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    filtered_movies = movies
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        # Filter movies based on the search query
        filtered_movies = [movie for movie in movies if search_query.lower() in movie['title'].lower()]
        return render_template('index.html', movies=filtered_movies)

    return render_template('index.html', movies=filtered_movies)

@app.route('/filter', methods=['POST'])
def filter_movies():
    genre = request.form.get('genre')
    if genre and genre != 'All':
        filtered_movies = [movie for movie in movies if movie['Genre'] == genre]
    else:
        filtered_movies = movies
    return render_template('index.html', movies=filtered_movies)

if __name__ == '__main__':
    app.run(debug=True)
