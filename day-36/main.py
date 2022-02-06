from email import message
from http import client
import requests
from twilio.rest import Client
import os
STOCK = "HP"
COMPANY_NAME = "Helmerich & Payne Inc."
STOCK_URL = 'https://www.alphavantage.co/query'
NEWS_URL = "https://newsapi.org/v2/everything"


client = Client(ACCOUNT_SID, AUTH_TOKEN)
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
news_params = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "pageSize": 3
}
response = requests.get(STOCK_URL, stock_params)
data = response.json()["Time Series (Daily)"]

data_list =[value for (key, value) in data.items()]
yesterday = float(data_list[0]["4. close"])
day_before_yesterday = float(data_list[1]["4. close"])
# print(yesterday)
# print(day_before_yesterday)
diff = yesterday-day_before_yesterday
percentage = "{:.2f}".format(diff/day_before_yesterday)
if abs(float(percentage))>0.05:
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    response = requests.get(NEWS_URL, params=news_params)
    data = response.json()
    articles = data["articles"]
    title=[]
    description=[]
    url=[]
    for i in range(3):
        title.append(articles[i]["title"])
        description.append(articles[i]["description"])
        url.append(articles[i]["url"])
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    message = client.messages.create(
        body = f'HP:{percentage}\n{title[0]}\n{description[0]}\n{url[0]}\n{title[1]}\n{description[1]}\n{url[1]}\n{title[2]}\n{description[2]}\n{url[2]}',
        from_='+19036238540',
        to='+16824080758'
    )

    print(message.sid)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

