import pandas as pd


wiki = pd.read_csv(r'LessonsExcervises/WikiMoviePandaExercise/wiki_movie_plots_deduped.csv')

#1 of records
# len(wiki)

#2 what columns?
print(wiki.columns)

#3 number of columns
# print(len(wiki.columns))

#4 how many non-null observations are there in each column?
# wiki.info()

#5 What are the last 8 records of the dataset? Use indexing.
# print(wiki.iloc[-8:])

#6 What are the last 8 records of the dataset? Use a function.
# wiki.tail(8)

#7 What are the first 5 records of the dataset? Use indexing.
# print(wiki.iloc[:5])

#8 What are the first 5 records of the dataset? Use a function.
# wiki.head(5)

#9 What are the top 5 listed genres?
# print(wiki.Genre.value_counts().head(5))

#10  Who are the top 5 directors?
# print(wiki.Director.value_counts().head(5))

#11 What are the counts for origin/ethnicity?

# print(wiki['Origin/Ethnicity'].value_counts().head(5))

#12 Are there any titles that are duplicated?
# x=wiki['Title'].value_counts()
# print(x[x>1])

#13 What is the most popular year?
# print(wiki['Release Year'].value_counts().head(5))