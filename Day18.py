# ==========================================
# MOVIE DATASET ANALYSIS - DAY 18
# ==========================================

# Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------
# STEP 1: CREATE MOVIE DATASET
# ------------------------------------------

data = {
    'Movie_Name': [
        'Inception',
        'Avengers',
        'Titanic',
        'Joker',
        'Interstellar',
        'Bahubali',
        'KGF',
        'Pushpa',
        'Dangal',
        '3 Idiots'
    ],
    
    'Rating': [8.8, 8.5, 7.9, 8.4, 8.7, 8.2, 8.1, 7.8, 8.4, 8.5],
    
    'Genre': [
        'Sci-Fi',
        'Action',
        'Romance',
        'Drama',
        'Sci-Fi',
        'Action',
        'Action',
        'Action',
        'Sports',
        'Comedy'
    ],
    
    'Revenue': [
        829,
        2798,
        2187,
        1074,
        701,
        650,
        250,
        350,
        310,
        400
    ]
}

df = pd.DataFrame(data)

print("========== MOVIE DATASET ==========")
print(df)

# ------------------------------------------
# STEP 2: HIGHEST RATED MOVIES
# ------------------------------------------

highest_rated = df.sort_values(by='Rating', ascending=False)

print("\n========== HIGHEST RATED MOVIES ==========")
print(highest_rated[['Movie_Name', 'Rating']])

# ------------------------------------------
# STEP 3: MOST PROFITABLE GENRES
# ------------------------------------------

genre_revenue = df.groupby('Genre')['Revenue'].sum()

print("\n========== MOST PROFITABLE GENRES ==========")
print(genre_revenue)

# ------------------------------------------
# STEP 4: GENRE VS REVENUE GRAPH
# ------------------------------------------

plt.figure(figsize=(8,5))

genre_revenue.plot(kind='bar')

plt.title("Genre vs Revenue")
plt.xlabel("Genre")
plt.ylabel("Revenue")

plt.show()

# ------------------------------------------
# STEP 5: RATING DISTRIBUTION GRAPH
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.hist(df['Rating'], bins=5)

plt.title("Rating Distribution")
plt.xlabel("Ratings")
plt.ylabel("Number of Movies")

plt.show()

# ------------------------------------------
# STEP 6: CORRELATION BETWEEN
# RATING AND REVENUE
# ------------------------------------------

correlation = df['Rating'].corr(df['Revenue'])

print("\n========== CORRELATION ==========")
print("Correlation between Rating and Revenue:", correlation)

# ------------------------------------------
# STEP 7: TOP 5 MOVIES
# ------------------------------------------

top5 = df.sort_values(by='Revenue', ascending=False).head(5)

print("\n========== TOP 5 MOVIES ==========")
print(top5[['Movie_Name', 'Revenue']])

# ------------------------------------------
# STEP 8: SCATTER PLOT
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.scatter(df['Rating'], df['Revenue'])

plt.title("Rating vs Revenue")
plt.xlabel("Rating")
plt.ylabel("Revenue")

plt.show()

# ------------------------------------------
# STEP 9: PROJECT SUMMARY
# ------------------------------------------

print("\n========== PROJECT SUMMARY ==========")

print("""
1. Analyzed movie dataset
2. Found highest rated movies
3. Identified profitable genres
4. Visualized genre vs revenue
5. Visualized rating distribution
6. Calculated correlation between rating and revenue
7. Displayed top 5 movies
""")

# ==========================================
# END OF PROJECT
# ==========================================