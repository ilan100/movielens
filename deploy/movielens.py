import requests
import zipfile
import io
import os
import csv


URL = "https://files.grouplens.org/datasets/movielens/ml-100k.zip"

class MovieLens:
    def __init__(self):
        self.foldername = "ml-100k"
        self.data = []
        self.ratings = []
        self.movies = {}
        self.init = False

    def load_ratings(self):
        with open(self.foldername + "/u.data", "r") as f:
            reader = csv.reader(f, delimiter="\t")
            for row in reader:
                # Each row: user_id, item_id, rating, timestamp
                user_id = int(row[0])
                item_id = int(row[1])
                rating = int(row[2])
                # timestamp = row[3]  # optional
                self.ratings.append((user_id, item_id, rating))

    def load_movies(self):
        with open("ml-100k/u.item", "r", encoding="latin-1") as f:
            reader = csv.reader(f, delimiter="|")
            for row in reader:
                item_id = int(row[0])
                title = row[1]
                self.movies[item_id] = title

    def create_combined_ratings(self):
        for user_id, item_id, rating in self.ratings:
            title = self.movies.get(item_id, "Unknown")
            self.data.append((user_id, title, rating))
        self.init = True

    def print_data_records(self, num: int):
        if (num > len(self.data)):
            return False
        for entry in self.data[:num]:
            print(entry)
        return True

    def find_movie_by_name(self, movie_name: str):
        result = []
        for entry in self.data:
            user_id, title, rating = entry
            if movie_name.lower() in title.lower():  # case-insensitive match
                result.append(entry)
        return result

    def get_movie_average_rating(self, title: str):
        average = 0
        movie_data = self.find_movie_by_name(title)
        size = len(movie_data)
        if (size < 1):
            print("No movie found with tile:", title)
            return -1
        for movie in movie_data:
            average += movie[2]
        average /= size
        return average

    def load_and_prepare_data(self):
        download_movielens()
        self.load_ratings()
        self.load_movies()
        self.create_combined_ratings()


# Obtain the MovieLens 100K dataset (download it to computer)
def download_movielens(path="ml-100k"):
    if os.path.exists(path):
        #print("Dataset already exists.")
        return

    print("Downloading dataset...")
    response = requests.get(URL)

    if response.status_code != 200:
        raise Exception("Failed to download dataset")

    print("Extracting...")
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        z.extractall()

    print("Done!")



#------------------------------------------------------------------------------------

if __name__ == '__main__':
    res = True
    try:
        download_movielens()
    except Exception as e:
        print(e)
        res = False
    finally:
        pass

    ML = MovieLens()
    ML.load_ratings()
    ML.load_movies()
    ML.create_combined_ratings()
    ML.print_data_records(10)

    # Example usage:
    movie_entries = ML.find_movie_by_name("Toy Story")
    for e in movie_entries[:5]:  # print first 5 matches
        print(e)
    print(ML.get_movie_average_rating("Thoy Story"))