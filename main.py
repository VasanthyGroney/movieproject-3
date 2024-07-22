class MovieApp:
    def __init__(self, storage):
        """
        Initializes the MovieApp with a storage object.
        """
        self._storage = storage

    def _command_list_movies(self):
        """
        Lists all movies in the storage.
        """
        movies = self._storage.list_movies()
        for title, details in movies.items():
            print(f"Title: {title}, Year: {details['year']}, Rating: {details['rating']}, Poster: {details['poster']}")

    def _command_movie_stats(self):
        """
        Prints statistics about the movies in the storage.
        """
        movies = self._storage.list_movies()
        if not movies:
            print("No movies available.")
            return

        total_movies = len(movies)
        average_rating = sum(movie['rating'] for movie in movies.values()) / total_movies
        print(f"Total movies: {total_movies}")
        print(f"Average rating: {average_rating:.2f}")

    def _command_add_movie(self):
        """
        Adds a new movie to the storage.
        """
        title = input("Enter the movie title: ")
        year = int(input("Enter the movie year: "))
        rating = float(input("Enter the movie rating: "))
        poster = input("Enter the path to the movie poster: ")
        self._storage.add_movie(title, year, rating, poster)
        print("Movie added successfully.")

    def _command_delete_movie(self):
        """
        Deletes a movie from the storage.
        """
        title = input("Enter the movie title to delete: ")
        self._storage.delete_movie(title)
        print("Movie deleted successfully.")

    def _command_update_movie(self):
        """
        Updates the rating of a movie in the storage.
        """
        title = input("Enter the movie title to update: ")
        rating = float(input("Enter the new rating: "))
        self._storage.update_movie(title, rating)
        print("Movie rating updated successfully.")

    def _generate_website(self):
        """
        Generates a website with the list of movies.
        """
        movies = self._storage.list_movies()
        with open('movies.html', 'w') as file:
            file.write("<html><body><h1>Movie List</h1><ul>")
            for title, details in movies.items():
                file.write(
                    f"<li>{title} ({details['year']}): {details['rating']} <img src='{details['poster']}' alt='{title} poster' /></li>")
            file.write("</ul></body></html>")
        print("Website generated successfully.")

    def run(self):
        """
        Runs the movie app, providing a menu for the user to interact with.
        """
        while True:
            print("\nMenu:")
            print("1. List movies")
            print("2. Movie stats")
            print("3. Add movie")
            print("4. Delete movie")
            print("5. Update movie")
            print("6. Generate website")
            print("7. Quit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self._command_list_movies()
            elif choice == "2":
                self._command_movie_stats()
            elif choice == "3":
                self._command_add_movie()
            elif choice == "4":
                self._command_delete_movie()
            elif choice == "5":
                self._command_update_movie()
            elif choice == "6":
                self._generate_website()
            elif choice == "7":
                break
            else:
                print("Invalid choice. Please try again.")
