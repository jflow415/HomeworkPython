#!usr/bin/env python3
import pandas as pd 
import matplotlib.pyplot as plt

#creatting data frame
df = pd.read_csv("anime.csv")
print(df)

#create column of how many years it was broadcated 
df['yearslive'] = df['finishYr'] - df['startYr'] 
print(df.head())

#drop two columns 
dropped=df.drop(columns=["ongoing","dropped"])
print(dropped)

#create csv file with the columns missing 
dropped.to_csv("dropped_columns.csv")

#create a writer
writer = pd.ExcelWriter('anime.xlsx')

#make the dataframe an xlsx so that I can convert to excel
df.to_excel(writer, index = False)
writer.save()

#writer for dropped columns
droppedWriter = pd.ExcelWriter('dropped_columns.xlsx')

#use dataframe from earlier with updated columns
dropped.to_excel(droppedWriter, index =False)
droppedWriter.save()

#plot columns mediaType, ratings, and votes
#Compare the ratings from movies and TVs
#make tvs with different plotting theme 
movie = df[df.mediaType == 'Movie']
tv = df[df.mediaType == 'TV']
plt.plot (movie.rating, movie.votes)
plt.plot(tv.rating, tv.votes, 'o')
plt.show()

