from newsapi import NewsApiClient
import pandas as pd
import time

# Initialize the NewsApiClient with your API key
newsapi = NewsApiClient(api_key='57629d630a0745f1b9f8c18b970447fe')

# Create an empty DataFrame to store the data
df = pd.DataFrame(columns=["Title", "Description", "Content"])

# Main loop to fetch and store news data iteratively
while True:
    # Fetch news articles using the News API
    all_articles = newsapi.get_everything(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          language='en',
                                          sort_by='relevancy',
                                          page=1)  # You can adjust the page number as needed
    
    if 'articles' in all_articles:
        for article in all_articles['articles']:
            title = article.get('title', 'N/A')
            description = article.get('description', 'N/A')
            content = article.get('content', 'N/A')
            df = df.append({"Title": title, "Description": description, "Content": content}, ignore_index=True)
    
    # Save DataFrame to the same CSV file as before
    print('uploading...')
    df.to_csv("scraped_news_data.csv", index=False)
    
    # Sleep for 5 seconds
    time.sleep(5)

