import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

# Check the current working directory to debug file path
st.write("Current Working Directory:", os.getcwd())

# Load the dataset (fix any potential issues with the file name or path)
try:
    df = pd.read_csv("IMDB-Movie-Data.csv")
except FileNotFoundError:
    st.error("File not found. Please check if the file IMDB-Movie-Data.csv is in the correct directory.")
    st.stop()

# Display the first few rows of the dataframe
st.write("First few rows of the dataset:", df.head())

# Show basic information about the dataset
st.write("Dataset Information:")
st.write(df.info())

# Show missing values in the dataset
st.write("Missing Values:")
missing_values = df.isnull().sum()
st.write(missing_values)

# Show a heatmap of missing values
st.write("Heatmap of missing values:")
plt.figure(figsize=(10, 7))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Heatmap of Missing Values")
plt.tight_layout()
st.pyplot()

# Display the percentage of missing values
st.write("Percentage of Missing Values:")
per_missing = df.isnull().sum() * 100 / len(df)
st.write(per_missing)

# Handle missing data - Optional: Fill missing numeric values with the column mean
df_filled = df.fillna(df.mean(numeric_only=True))  # Fills missing numeric values with column mean
# For categorical columns, you can fill with the mode:
# df['column_name'] = df['column_name'].fillna(df['column_name'].mode()[0])

# Drop rows with missing values (Optional: You can choose to drop or fill missing values)
df_cleaned = df.dropna(axis=0)
st.write("Data after dropping missing values:", df_cleaned.shape)

# Check for duplicate data
dup_data = df.duplicated().any()
st.write(f"Any duplicate data present: {dup_data}")

# Show basic statistics about the dataframe
st.write("Statistical Summary of the Dataset:")
st.write(df.describe(include='all'))

# Display the titles of movies with runtime >= 180 minutes
st.write("Movies with runtime >= 180 minutes:")
long_movies = df[df['Runtime (Minutes)'] >= 180]['Title']
st.write(long_movies)

# Find the year with the highest average votes
st.write("Year with highest average votes:")
avg_votes_per_year = df.groupby('Year')['Votes'].mean().sort_values(ascending=False)
st.write(avg_votes_per_year.head())

# Plot average votes by year
st.write("Average Votes by Year:")
plt.figure(figsize=(10, 6))
sns.barplot(x='Year', y='Votes', data=df)
plt.title("Average votes by Year")
plt.tight_layout()
st.pyplot()

# Find the year with the highest average revenue
st.write("Year with highest average revenue:")
avg_revenue_per_year = df.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False)
st.write(avg_revenue_per_year.head())

# Plot average revenue by year
st.write("Average Revenue by Year:")
plt.figure(figsize=(10, 6))
sns.barplot(x='Year', y='Revenue (Millions)', data=df)
plt.title("Average Revenue by Year")
plt.tight_layout()
st.pyplot()

# Display top 10 directors with highest average ratings
st.write("Top Directors with Highest Average Ratings:")
top_directors = df.groupby('Director')['Rating'].mean().sort_values(ascending=False).head(10)
st.write(top_directors)

# Display the top 10 longest movies by runtime
st.write("Top 10 Longest Movies:")
top10 = df.nlargest(10, 'Runtime (Minutes)')[['Title', 'Runtime (Minutes)']].set_index('Title')
st.write(top10)

# Plot top 10 longest movies
st.write("Top 10 Longest Movies:")
plt.figure(figsize=(10, 6))
sns.barplot(x='Runtime (Minutes)', y=top10.index, data=top10)
plt.title("Top 10 Longest Movies")
plt.tight_layout()
st.pyplot()

# Display number of movies per year
st.write("Number of Movies per Year:")
movies_per_year = df['Year'].value_counts()
st.write(movies_per_year)

# Plot the number of movies per year
st.write("Number of Movies per Year (Countplot):")
plt.figure(figsize=(10, 6))
sns.countplot(x='Year', data=df)
plt.title("Number of Movies per Year")
plt.tight_layout()
st.pyplot()

# Display the title of the most popular movie (highest revenue)
st.write("Most Popular Movie (Highest Revenue):")
highest_revenue_movie = df[df['Revenue (Millions)'] == df['Revenue (Millions)'].max()]['Title']
st.write(highest_revenue_movie)
