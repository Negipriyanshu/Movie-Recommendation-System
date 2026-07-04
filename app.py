import streamlit as st
import nltk
import sklearn
import pandas as pd
import numpy
import pickle
import joblib


st.title("Movie Recommendation System")

with open('movie.pickle','rb') as m:
    movies = pickle.load(m)
    
similarity = joblib.load('similarity.pkl')

movie_names=movies['title'].values

def recommend(name_movie):
    movie_index=movies[movies['title']==name_movie].index[0]
    
    recommendation = similarity[movie_index]
    
    movie_list = sorted(enumerate(recommendation),reverse=True,key=lambda x: x[1])[1:6]
    recommended_movies=[]
    
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies   
        

name_movie = st.selectbox("Enter the Movie Name",movie_names)

if st.button("Recommend"):
    
    recomendation =recommend(name_movie)
    
    st.write("The Recommend Movies are : ")
    for i in recomendation:
        st.write(i)
