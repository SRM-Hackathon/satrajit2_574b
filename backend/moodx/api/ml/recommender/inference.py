from django.conf import settings

import os
import argparse
import random

from api.ml.recommender.CFModel import CFModel
from api.ml.recommender.recommender import *

WEIGHTS_PATH = os.path.join(settings.MEDIA_ROOT, 'weights.h5')

# Use the pre-trained model
trained_model = CFModel(max_userid, max_movieid, K_FACTORS)


# Load weights
trained_model.load_weights(WEIGHTS_PATH)

users[users['user_id'] == random.randint(1, 2000)]  # random

# Function to predict the ratings given User ID and Movie ID
def predict_rating(user_id, movie_id):
    return trained_model.rate(user_id - 1, movie_id - 1)


user_ratings = ratings[ratings['user_id'] ==
                       TEST_USER][['user_id', 'movie_id', 'rating']]

user_ratings['prediction'] = user_ratings.apply(lambda x: predict_rating(TEST_USER, x['movie_id']), axis=1)


def predict_movie(emo, gender="M", zipcode=55117, age_desc="56+", occ_desc="self-employed"):
    users = pd.read_csv('users.csv', sep='\t', encoding='latin-1',
                        usecols=['user_id', 'gender', 'zipcode', 'age_desc', 'occ_desc'])
    TEST_USER = users[users["gender"] == gender]
    TEST_USER = users[users["zipcode"] == gender]
    TEST_USER = users[users["zipcode"] == zipcode]
    TEST_USER = users[users["age_desc"] == age_desc]
    TEST_USER = int(list(users[users["occ_desc"] == occ_desc]["user_id"])[0])
    recommendations = ratings[ratings['movie_id'].isin(user_ratings['movie_id']) == False][
        ['movie_id']].drop_duplicates()
    recommendations['prediction'] = recommendations.apply(
        lambda x: predict_rating(TEST_USER, x['movie_id']), axis=1)

    # negative is 0 and positive is 1
    emo_map = {
        1: ["Comedy", "Drama", "Fantasy", "Action", "Adventure", "Animation", "Children's", "Crime", "Documentary",
            "Horror", "Mystery", "Sci-Fi"], 0: ["Comedy", "Fantasy", "Thriller", "War", "Western", "Action",
                                                "Adventure", "Film-Noir", "Musical", "Romance"]}
    sorted_recs = recommendations.sort_values(by='prediction',
                                              ascending=False).merge(movies,
                                                                     on='movie_id',
                                                                     how='inner',
                                                                     suffixes=['_u', '_m']).head(5)

    # print(type(sorted_recs))
    # print(sorted_recs)

    recommended = list()
    for genre in sorted_recs["genres"]:
        gen = genre.split("|")
        for g in gen:
            if g in emo_map[emo]:
                movie = sorted_recs[sorted_recs["genres"] == genre]["title"]
                # print(list(movie))
                for x in list(movie):
                    if x[: x.index(" (")] not in recommended:
                        recommended.append(x[: x.index(" (")])
    print(recommended)
    return recommended
    
