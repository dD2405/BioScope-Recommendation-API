# BioScope-Recommendation-API

- API Link : https://bioscope-api.herokuapp.com/movie?title=Inception

An open movie recommendation API that has been built using Python and deployed on Heroku. 
This API is based on the Content-Based Filtering technique used in recommendation systems where we recommend items to a user based on the input item's attributes. 
We have more than 6000 movies present in our dataset and our recommendation algorithm works accordingly.

## Use the BioScope API whilst building your website or app and recommend movies to your users accordingly.

# File Description:- 
## recommendation.py
Here, we have our logic written for the recommendation algorithm. Consists a total of 5 functions

### get_data(): 
- get_data() is used to fetch the data about the movies and return the dataset with it's attributes as the result for further preprocessing.

### combine_data():-
- combine_data() drops the columns not required for feature extraction and then combines the cast and genres column,finally returning the combine column as the result of this function.
