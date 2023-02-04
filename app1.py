import streamlit as st
import os
import pandas as pd
import json
import pymongo as pym      # Interface with Python <--> MongoDB                  
import csv  
from google.colab import files               


# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd

def twit(query,limit):
    tweets_list1 = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i>limit:
            break
        tweets_list1.append([tweet.date, tweet.id,tweet.url, tweet.rawContent, tweet.user.username,tweet.retweetCount,tweet.lang,tweet.source,tweet.likeCount])
    # Creating a dataframe from the tweets list above
    tweets_df1 = pd.DataFrame(tweets_list1, columns=['Date', 'Id', 'Url','Tweet Content', 'User', 'retweet count','language', 'source', 'like count'])



    return tweets_df1

    input_form = st.form("input_form")
    input_form.write("Query inputs:")
    submit_button = input_form.form_submit_button("Submit")

    if submit_button is True:

        df = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

        st.dataframe(df)

        st.download_button(
            label="Download df",
            data=df.to_csv().encode("utf-8"),
            file_name="filename.csv",
            mime="text/csv"
        )
# customize form
def main():
    st.image('download1.png')
    st.header("Twitter Scraper")
    input_form = st.form("input_form")
    query = input_form.text_input('What do you want to search for?')
    limit = input_form.slider('How many tweets do you want to get?', 0, 500, step=10)
    selectbox = input_form.selectbox("Do you Want to Save as CSV file?",["Yes", "No"])
    submitted = input_form.form_submit_button("Search")
    submitted1 = input_form.form_submit_button("Save to Database")
    
    
        

    if submitted is True:
        
        result_df=twit(query,limit)
        dp = result_df
        
        st.dataframe(result_df)

        global csv
        
        csv=dp.to_csv(index=False).encode('utf-8')
        
        st.download_button(
          label="Press to Download",
          data=csv,
          file_name="file.csv",
          mime="text/csv",
          key='download-csv'
          )


    if submitted1 is True:
    # Making a Connection to MongoClient
        client = pym.MongoClient("mongodb+srv://Sree:Sree123@cluster0.j4yl447.mongodb.net/?retryWrites=true&w=majority")

     # CREATING A DATABASE:
        db = client["tweets"]

     # CREATING A COLLECTION (*AKA* TABLE):
        user_info_table= db["tweet"]
        result_df=twit(query,limit)
        result_df.reset_index(inplace=True)
        result_df_dict = result_df.to_dict('records')
        user_info_table.insert_many(result_df_dict)

if __name__ == "__main__":
    main()
