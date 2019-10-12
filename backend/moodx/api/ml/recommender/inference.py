import argparse
import random
from CFModel import CFModel
from recommender import *

# Use the pre-trained model
trained_model = CFModel(max_userid, max_movieid, K_FACTORS)

# Load weights
trained_model.load_weights('weights.h5')

parser = argparse.ArgumentParser()
parser.add_argument('--user_id', type=int)
parser.add_argument('--emo', type=int)
args = vars(parser.parse_args())

# Pick a random test user
# A random test user (user_id = 2000)  # TODO: Test user for debugging
TEST_USER = 2000
emo = args["emo"]

# users[users['user_id'] == args["user_id"]]  # user specified
users[users['user_id'] == random.randint(1, 2000)]  # random


# Function to predict the ratings given User ID and Movie ID
def predict_rating(user_id, movie_id):
    return trained_model.rate(user_id - 1, movie_id - 1)


user_ratings = ratings[ratings['user_id'] == TEST_USER][['user_id',
                                                         'movie_id',
                                                         'rating']]

user_ratings['prediction'] = user_ratings\
    .apply(lambda x: predict_rating(TEST_USER, x['movie_id']), axis=1)

recommendations = ratings[ratings['movie_id'].isin(user_ratings['movie_id']) == False][['movie_id']]\
    .drop_duplicates()

recommendations['prediction'] = recommendations\
    .apply(lambda x: predict_rating(TEST_USER, x['movie_id']), axis=1)

# negative is 0 and positive is 1
emo_map = {1: ["Comedy", "Drama", "Fantasy", "Action", "Adventure", "Animation", "Children's", "Crime", "Documentary",
               "Horror", "Mystery", "Sci-Fi"], 0: ["Comedy", "Fantasy", "Thriller", "War", "Western", "Action",
                                                   "Adventure", "Film-Noir", "Musical", "Romance"]}
sorted_recs = recommendations.\
    sort_values(by='prediction', ascending=False).\
    merge(movies,
          on='movie_id',
          how='inner',
          suffixes=['_u', '_m']).\
    head(5)

# print(type(sorted_recs))
# print(sorted_recs)

recommended = set()
for genre in sorted_recs["genres"]:
    gen = genre.split("|")
    for g in gen:
        if g in emo_map[emo]:
            movie = sorted_recs[sorted_recs["genres"] == genre]["title"]
            # print(list(movie))
            for x in list(movie):
                recommended.add(x[: x.index(" (")])

print(recommended)
