import pandas as pd
import scipy.sparse as sp
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_data():
        movie_data = pd.read_csv('dataset/movie_data.csv.zip')
        movie_data['original_title'] = movie_data['original_title'].str.lower()
        return movie_data

def combine_data(data):
        data_recommend = data.drop(columns=['movie_id', 'original_title','plot'])
        data_recommend['combine'] = data_recommend[data_recommend.columns[0:2]].apply(
                                                                        lambda x: ','.join(x.dropna().astype(str)),axis=1)
        
        data_recommend = data_recommend.drop(columns=[ 'cast','genres'])
        return data_recommend
        
def transform_data(data_combine, data_plot):
        count = CountVectorizer(stop_words='english')
        count_matrix = count.fit_transform(data_combine['combine'])

        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(data_plot['plot'])

        combine_sparse = sp.hstack([count_matrix, tfidf_matrix], format='csr')
        cosine_sim = cosine_similarity(combine_sparse, combine_sparse)
        
        return cosine_sim


def recommend_movies(title):
        title = title.lower()

        data = get_data()
        combine = combine_data(data)
        transform = transform_data(combine,data)

        indices = pd.Series(data.index, index = data['original_title'])
        index = indices[title]

        sim_scores = list(enumerate(transform[index]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:21]

        movie_indices = [i[0] for i in sim_scores]
        
        movie_id = data['movie_id'].iloc[movie_indices]
        movie_title = data['original_title'].iloc[movie_indices]
        movie_genres = data['genres'].iloc[movie_indices]

        recommendation_data = pd.DataFrame(columns=['Movie_Id','Name'])

        recommendation_data['Movie_Id'] = movie_id

        recommendation_data['Name'] = movie_title
        recommendation_data['genre'] = movie_genres

        return recommendation_data

def results(movie_name):
        find_movie = get_data()
        
        if movie_name not in find_movie['original_title'].unique():
                return 'Movie not in Database'
    
        else:
                recommendations = recommend_movies(movie_name)
                return recommendations.to_dict('records')

