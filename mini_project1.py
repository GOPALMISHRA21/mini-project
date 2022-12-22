import numpy as np
import pandas as pd
import plotly.express as px 
import matplotlib.pyplot as plt
import plotly.graph_objects as go 
import streamlit as st
import missingno as msno
import seaborn as sns

st.set_page_config(layout='wide')

def clean_duration_count(value):
    if isinstance(value,float):
        return value
    value_parts = value.split()
    duration_time = value_parts[0].replace(',','')
    return duration_time

def clean_dataset(df):
    df['duration'] = df['duration'].apply(clean_duration_count).astype(float)
    return df

def load_dataset():
    df = pd.read_csv('data/netflix.csv')
    df = clean_dataset(df)
    return df

st.title("Netflix data shown in visuals format")
with st.spinner("loading dataset"):                        
    print("D")
    df=load_dataset()
    

movie = df[df['type'] == 'Movie']
tv_show = df[df['type'] == 'TV Show']

view_options = ["Dont Show",'Show All','Only Movies','Only Shows']
view_choice = st.sidebar.radio("Select View", view_options)
if view_choice == view_options[0]:
    st.info("View Dataset on the sidebar")
elif view_choice == view_options[1]:
    st.write(df)
elif view_choice == view_options[2]:
    st.write(movie)
elif view_choice == view_options[3]:
    st.write(tv_show)

st.header("Yearly release")
all_year_count=df["release_year"].value_counts().reset_index()
fig = px.bar(all_year_count, 'index', 'release_year', title="No of releases respect to years")
movie_year_count=movie["release_year"].value_counts().reset_index()
st.write(movie_year_count)
fig2 = px.bar(movie_year_count, 'index', 'release_year', title="No of Movies releasae respect to years", log_y=True)
show_year_count=tv_show["release_year"].value_counts().reset_index()
fig3 = px.bar(show_year_count, 'index', 'release_year', title="No of shows releasae respect to years",log_y=True)
st.plotly_chart(fig, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig3, use_container_width=True)

fig=plt.figure(figsize=(2,4))
sns.countplot(data=df ,x='type')

st.plotly_chart(fig)

director_name=df['director'].value_counts().reset_index()
fig=px.area(director_name,'index','director',title="NO of production count respect to director",color='director')
st.plotly_chart(fig, use_container_width=True)

df_countries = df['country'].value_counts().reset_index()
fig=px.funnel_area(df_countries.head(n=10),'index','country',title="Top 10 countries have production with count")
st.plotly_chart(fig, use_container_width=True)

movie.sort_values('duration',inplace=True, ascending=False)
fig = px.bar(movie, 'title', 'duration', title="Duration of movies", color='release_year')
st.plotly_chart(fig, use_container_width=True)

cast_count=df['cast'].value_counts().head(10)
fig=px.bar(cast_count,title='Top 10 most castings')
st.plotly_chart(fig, use_container_width=True)

release=df['release_year'].value_counts().head(10)
fig=px.bar(release,title='Top 10 years have more production')
st.plotly_chart(fig, use_container_width=True)

tv_show.value_counts()
fig=px.line(tv_show.head(10),'title','duration',title='Top 10 TV shows  have maximum length')
st.plotly_chart(fig, use_container_width=True,)

movie.value_counts()
fig=px.line(movie.head(10),'title','duration',title='10 Movies have maximum length')
st.plotly_chart(fig, use_container_width=True)

india_df = df[df['country'] =='India'].copy()
fig=px.scatter(india_df.head(n=50),'title', 'director', title='Top 50 Movies released in India  per year 1900-2022',color_discrete_sequence=["red", "green", "blue", "goldenrod", "magenta"],)
st.plotly_chart(fig, use_container_width=True)

rating_counts=df["rating"].value_counts().reset_index()
fig=px.bar(rating_counts, 'index', 'rating', title="Ratings counts in netflix",)
st.plotly_chart(fig, use_container_width=True)

listed_count=df['listed_in'].value_counts()
fig=px.funnel(listed_count.head(n=10),title='Top 10  category listed' )
st.plotly_chart(fig, use_container_width=True)

