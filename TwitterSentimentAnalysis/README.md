# Twitter Sentiment Analysis

The following project uses python 3 to download the tweets, store them in mongoDB database and finally perform sentiment analysis on them.

### The Approach
The tasks performed in this project are as following:

    Download the tweets.
    Save the downloaded(raw) tweets in a csv file.
    Import the csv file as a dataframe and clean the tweets column and other columns as well.
    Save the dataframe with clean columns as another csv file. This serves as a backup copy.
    Import the data from cleaned csv file, convert it into json format and save it mongoDB database.
    Import the tweets from mongodb database, perform sentiment analysis(classify them as positive, negative or neutral) and update the database with same information(as a new field).
