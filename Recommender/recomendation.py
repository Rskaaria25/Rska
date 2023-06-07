import pandas as pd
import numpy as np
import random
import tensorflow as tf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations_by_types(food_types, similarity_matrix, k=10):
    food_indices = []
    for food_type in food_types:
        indices = data[data['Tipe'].str.contains(food_type)].index
        food_indices.extend(indices)
    food_indices = list(set(food_indices))
    
    similarity_scores = list(enumerate(similarity_matrix[food_indices].sum(axis=0)))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    top_k_food_indices = [i for i, _ in similarity_scores[1:k+1]]
    top_k_food_names = data.loc[top_k_food_indices, 'Nama'].values
    return top_k_food_names