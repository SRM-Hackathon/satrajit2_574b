from django.conf import settings

import os
import math
import numpy as np
import pandas as pd
from api.ml.recommender.CFModel import CFModel
import matplotlib.pyplot as plt
from keras.callbacks import Callback, EarlyStopping, ModelCheckpoint

RATINGS_PATH = os.path.join(settings.MEDIA_ROOT, 'ratings.csv')
USERS_PATH = os.path.join(settings.MEDIA_ROOT, 'users.csv')
MOVIES_PATH = os.path.join(settings.MEDIA_ROOT, 'movies.csv')

# Reading ratings file
ratings = pd.read_csv(RATINGS_PATH,
                      sep='\t',
                      encoding='latin-1',
                      usecols=['user_id', 'movie_id', 'user_emb_id', 'movie_emb_id', 'rating'])
max_userid = ratings['user_id'].drop_duplicates().max()
max_movieid = ratings['movie_id'].drop_duplicates().max()

# Reading users file
users = pd.read_csv(USERS_PATH,
                    sep='\t',
                    encoding='latin-1',
                    usecols=['user_id', 'gender', 'zipcode', 'age_desc', 'occ_desc'])

# Reading movies file
movies = pd.read_csv(MOVIES_PATH,
                     sep='\t',
                     encoding='latin-1',
                     usecols=['movie_id', 'title', 'genres'])

# Create training set
shuffled_ratings = ratings.sample(frac=1., random_state=1)

# Shuffling users
Users = shuffled_ratings['user_emb_id'].values
print('Users:', Users, ', shape =', Users.shape)

# Shuffling movies
Movies = shuffled_ratings['movie_emb_id'].values
print('Movies:', Movies, ', shape =', Movies.shape)

# Shuffling ratings
Ratings = shuffled_ratings['rating'].values
print('Ratings:', Ratings, ', shape =', Ratings.shape)

# Define constants
K_FACTORS = 100  # The number of dimensional embeddings for movies and users
# A random test user (user_id = 2000)  # TODO: Test user for debugging
TEST_USER = 2000
