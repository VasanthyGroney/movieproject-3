import json

FILE_PATH = 'data.json'

def get_movies():
    """
    Retrieve all movies from the JSON file.

    Returns:
        dict: A dictionary containing movies data.
    """
    try:
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_movies(movies):
    """
    Save movies data to the JSON file.

    Args:
        movies (dict): A dictionary containing movies data.
    """
    with open(FILE_PATH, 'w') as file:
        json.dump(movies, file, indent=4)

def add_movie(title, year, rating):
    """
    Add a new movie to the JSON file.

    Args:
        title (str): The title of the movie.
        year (str): The release year of the movie.
        rating (float): The rating of the movie.
    """
    movies = get_movies()
    movies[title] = {"year": year, "rating": rating}
    save_movies(movies)

def delete_movie(title):
    """
    Delete a movie from the JSON file.

    Args:
        title (str): The title of the movie to delete.
    """
    movies = get_movies()
    del movies[title]
    save_movies(movies)

def update_movie(title, rating):
    """
    Update the rating of an existing movie in the JSON file.

    Args:
        title (str): The title of the movie to update.
        rating (float): The new rating for the movie.
    """
    movies = get_movies()
    movies[title]['rating'] = rating
    save_movies(movies)
