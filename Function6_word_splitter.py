def word_splitter(df):
 """Write a function which splits a sentence into a list of the separate words"""

 df['split tweets'] = [string.lower().split() for string in df['Tweets']]
  
 return df
