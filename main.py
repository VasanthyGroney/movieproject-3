from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv


def main():
    """
    Main function to run the MovieApp.
    """
    storage_type = input("Choose storage type (json/csv): ").strip().lower()
    if storage_type == 'json':
        storage = StorageJson('movies.json')
    elif storage_type == 'csv':
        storage = StorageCsv('movies.csv')
    else:
        print("Invalid storage type. Please choose either 'json' or 'csv'.")
        return

    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()
