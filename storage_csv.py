import csv
from istorage import IStorage

class StorageCsv(IStorage):
    def __init__(self, file_path):
        """
        Initializes the StorageCsv with a file path to the CSV file.
        """
        self.file_path = file_path

    def _load_data(self):
        """
        Loads data from the CSV file and returns it as a dictionary.
        """
        data = {}
        try:
            with open(self.file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row["title"]
                    data[title] = {
                        "year": int(row["year"]),
                        "rating": float(row["rating"]),
                        "poster": row["poster"]
                    }
        except FileNotFoundError:
            pass
        return data

    def _save_data(self, data):
        """
        Saves data to the CSV file.
        """
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["title", "year", "rating", "poster"])
            writer.writeheader()
            for title, details in data.items():
                writer.writerow({
                    "title": title,
                    "year": details["year"],
                    "rating": details["rating"],
                    "poster": details["poster"]
                })

    def list_movies(self):
        """
        Returns a dictionary of dictionaries containing the movies information in the database.
        """
        return self._load_data()

    def add_movie(self, title, year, rating, poster):
        """
        Adds a movie to the movies database.
        """
        data = self._load_data()
        data[title] = {"year": year, "rating": rating, "poster": poster}
        self._save_data(data)

    def delete_movie(self, title):
        """
        Deletes a movie from the movies database.
        """
        data = self._load_data()
        if title in data:
            del data[title]
            self._save_data(data)

    def update_movie(self, title, rating):
        """
        Updates a movie in the movies database.
        """
        data = self._load_data()
        if title in data:
            data[title]["rating"] = rating
            self._save_data(data)
