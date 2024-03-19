import requests
from bs4 import BeautifulSoup
import time

def twitter_scraper(accounts, ticker, time_interval):
    while True:
        for account in accounts:
            url = f"{account}?lang=en"
            response = requests.get(url)
            if response.status_code == 200:
                scrape = BeautifulSoup(response.content, 'html.parser')
                tweets = scrape.find_all('div', {'data-testid': 'tweet'})
                count = 0
                for tweet in tweets:
                    tweet_text = tweet.find('div', {'lang': 'en'})
                    if tweet_text:
                        if f"${ticker.upper()}" in tweet_text.text:
                            count += 1
                print(f"{ticker.upper()} was mentioned {count} times in the last {time_interval} minutes on {account}.")
            else:
                print(f"Failed to scrape {account}")
        
        time.sleep(time_interval * 60)

if __name__ == "__main__":
    accounts = [
        "https://twitter.com/Mr_Derivatives",
        "https://twitter.com/warrior_0719",
        "https://twitter.com/ChartingProdigy",
        "https://twitter.com/allstarcharts",
        "https://twitter.com/yuriymatso",
        "https://twitter.com/TriggerTrades",
        "https://twitter.com/AdamMancini4",
        "https://twitter.com/CordovaTrades",
        "https://twitter.com/Barchart",
        "https://twitter.com/RoyLMattox"
    ]
    
    ticker = input("Enter the ticker symbol to search for: ")
    time_interval = input("Enter the time interval for scraping: ")
    
    twitter_scraper(accounts, ticker, time_interval)

