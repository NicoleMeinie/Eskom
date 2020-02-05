def number_of_tweets_per_day(df):

  """This fuction calculates the number of tweets that were posted per day."""

  df['Date'] = [item[:10] for item in df['Date']]
  df['Tweets'] = [1 for item in df['Tweets']]

  return twitter_df.groupby('Date').sum()
